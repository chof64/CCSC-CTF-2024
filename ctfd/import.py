#!/usr/bin/env python3
"""Push all CCSC challenges into CTFd. Zero-edit spin-up: secrets are hardcoded (temporary event, NOT secret).

Server (Windows):
  docker compose up -d --build
  python3 ctfd/import.py --url http://<HOST-IP>:51024 --host <HOST-IP>

The script waits for CTFd to boot, completes the /setup wizard itself
(users mode, open registration, no email verification) and imports all
38 challenges via the pre-shared admin token from docker-compose.yml.
No browser clicks needed.

Idempotent: existing challenges (matched by name) are updated, not duplicated.
Attachments: each challenge's `public/` dir is zipped in-memory and uploaded.
"""
import argparse
import io
import os
import re
import sys
import time
import zipfile
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("need `requests`: pip install requests")

# TEMPORARY, NOT SECRET - keep PRESET_ADMIN_TOKEN in sync with docker-compose.yml
PRESET_ADMIN_NAME = "admin"
PRESET_ADMIN_EMAIL = "admin@ccsc.local"
PRESET_ADMIN_PASSWORD = "ccsc-kingston-temp-admin!"
PRESET_TOKEN = "ccsc-kingston-temp-token-2024"

ROOT = Path(__file__).resolve().parent.parent

# dir: repo dir holding public/. conn: None | ("nc", port) | ("http", port) | ("tcp", port)
CHALLENGES = [
    # crypto
    dict(dir="crypto/andromeda-cloud-storage", name="Andromeda Cloud Storage", cat="crypto", val=200,
         conn=("nc", 51001), flag="ccsc{congrats.here.is.a.s1d3.ch4nNel?!}",
         desc="Andromeda's \"unbreakable\" cloud is open for signups. Compressor is very naive - ever heard of CRIME?"),
    dict(dir="crypto/andromeda-cloud-storage-v2", name="Andromeda Cloud Storage v2", cat="crypto", val=200,
         conn=("nc", 51002), flag="CCSC{p4dd1ng_oracl3_att4ck_due_to_flawed_implem3ntati0n_of_decryption!9f03268fc9363db00c7a43}",
         desc="We fixed v1. Now with real AES, real MAC. Decryption still tells you a little too much..."),
    dict(dir="crypto/inverted-oracle", name="Inverted Oracle", cat="crypto", val=50,
         conn=("nc", 51003), flag="CCSC{fL1p1Ty_Fl1P!!}",
         desc="Orion's terminal says yes or no. That's all it says. That's all you need. Flip it."),
    dict(dir="crypto/identity-thief", name="Identity Thief", cat="crypto", val=100,
         conn=None, flag="CCSC{Y0u_g0tt4_b3_c4r3fu11_wh3n_us1n9_f13ld_m4th3m4tics}",
         desc="He stole our keys using fancy field math. Notebook (public/main.sage) and scratch paper (public/output.txt) attached. Do the math back."),
    # misc
    dict(dir="misc/armored-up", name="Armored Up", cat="misc", val=100,
         conn=("nc", 51004), flag="CCSC{pr0ject_3cho_let_th3ir_gu4rd_d0wn_ag4in}",
         desc="One PyArmor'd file. One forgotten password. Python 3.11.2 on Debian 12. Guards get lazy - go ask it nicely."),
    dict(dir="misc/metadata-matters", name="Metadata Matters", cat="misc", val=50,
         conn=None, flag="CCSC{M4sk}",
         desc="Root hash in hand: `$6$yWctB8cp...` 10 chars, upper + lower + digit + symbol. Unless the password was never in the hash... check the file's baggage."),
    dict(dir="misc/password-keep", name="Password Keep", cat="misc", val=50,
         conn=None, flag="CCSC{history_may_not_repeat_or_rhyme_but_it_is_always_useful}",
         desc="One cold vault. One chall.7z attached. No password. But history repeats itself - shell history, git history... you get it."),
    dict(dir="misc/superguesser", name="Superguesser Part 1", cat="misc", val=50,
         conn=("nc", 51005), flag="CCSC{part1_sec0nds_and_s33ds_d0nt_m1x_t0gether}",
         desc="I'm thinking of a number. You have seconds. And I suck at randomness."),
    dict(dir="misc/superguesser_2", name="Superguesser Part 2", cat="misc", val=100,
         conn=("nc", 51006), flag="CCSC{part2_m1lli5_n33d_som3_brains_and_s0me_luck}",
         desc="You beat seconds. Cute. Now I'm thinking in millis and I brought a brain."),
    dict(dir="misc/superguesser_3", name="Superguesser Part 3", cat="misc", val=200,
         conn=("nc", 51007), flag="CCSC{part3_nan0s_d0nt_c4re_bis3ct_is_1n_the_a1r}",
         desc="Nanos now. No more guessing seeds, kid. Bisect the air itself."),
    dict(dir="misc/welcome_to_ccsc24", name="Welcome", cat="misc", val=50,
         conn=None, flag="CCSC{rul3s_ar3_n0t_m3ant_t0_b3_br0k3n!}",
         desc="Free points. Just prove you can read. Start at #rules."),
    # pwn
    dict(dir="pwn/GOT-Override", name="GOT Override", cat="pwn", val=50,
         conn=("nc", 51008), flag="CCSC{if_Th1s_is_Your_First_Pwn_Feel_Pr0ud_otherwise_K33p_going}",
         desc="New to pwn? Perfect. There's a table of addresses just begging to be overwritten."),
    dict(dir="pwn/hijack", name="hijack", cat="pwn", val=200,
         conn=("nc", 51009), flag="CCSC{if_y0u_Used-FSOP_which_technique?}",
         desc="The hooks are all but gone. Find another way."),
    dict(dir="pwn/infiltration", name="Infiltration", cat="pwn", val=100,
         conn=("nc", 51010), flag="CCSC{c0r3dumps_4r3_us3ful_4_d3bugg1ng_4nd_stuff}",
         desc="The secret is locked in memory and the binary won't talk. Unless it crashes... crashes leave cores. Cores talk."),
    dict(dir="pwn/model-scan", name="Model Scan", cat="pwn", val=50,
         conn=("nc", 51011), flag="CCSC{why_4r3_w3_st1ll_us1ng_p1kl3?!?}",
         desc="Totally safe AI scanner. Scans every model. Definitely can't be tricked by a pickle."),
    dict(dir="pwn/spilled", name="Spilled", cat="pwn", val=50,
         conn=("nc", 51012), flag="CCSC{00ps_1_sp1ll3d_4_f3w_byt3s}",
         desc="Our AI junior learned C yesterday. It spills a few bytes... everywhere."),
    # reverse
    dict(dir="reverse/TLV", name="TLV", cat="reverse", val=200,
         conn=("tcp", 51013), flag="CCSC{Fr3aking_H4te_Revers1ng_W1thout_Symb0ls}",
         desc="Old protocol. No symbols. No mercy. Speak in Type-Length-Value or don't speak at all. Raw TCP, bring Scapy (not HTTP)."),
    dict(dir="reverse/ancient-vm", name="Ancient VM", cat="reverse", val=100,
         conn=None, flag="CCSC{r3v_s0m3_rust_4nd_s0lv3_s0m3_c0nstra1nt5}",
         desc="Rusty VM. Lost source. We have the program, we have the output. All that's missing is the input - just solve 1000 constraints before lunch."),
    dict(dir="reverse/drone-army", name="Drone Army", cat="reverse", val=100,
         conn=None, flag="CCSC{4rMy_0f_X0rs_R3v3r5eD!!}",
         desc="One drone_army.s controls the whole swarm. It's just XORs all the way down. How hard can it be?"),
    dict(dir="reverse/license-ops", name="Licensed Ops", cat="reverse", val=50,
         conn=("nc", 51014), flag="CCSC{Y0ur_Rev3rsing_Journey_Just_st4rted}",
         desc="Enter license key to continue. No key? No problem. The check is right there if you look."),
    # web
    dict(dir="web/arcane-runes", name="Arcane Runes", cat="web", val=100,
         conn=("http", 51015), flag="CCSC{myst1cal_cosplAI_0r_wAIst3_of_tAIm3}",
         desc="The machines chant in runes and waste your time. Or do they? Persevere. The prompt is the puzzle."),
    dict(dir="web/cross-checked-report", name="Cross Checked Report", cat="web", val=50,
         conn=("http", 51016), flag="CCSC{1f_1t_acc3pt5_1NpuT_1t_W!LL_b3_XSSed}",
         desc="See something, say something. File a guard report. Our bot reads everything you submit, faithfully rendering every tag and script."),
    dict(dir="web/microbuns", name="Microbuns", cat="web", val=100,
         conn=("http", 51017), flag="CCSC{CybeR_r3alms_and_Anc1ent_v0w5}",
         desc="A silicon poet who loves buns and verses. He'll recite anything. Feed him well."),
    dict(dir="web/portal", name="Portal", cat="web", val=200,
         conn=("http", 51018), flag="CCSC{s1d3_t0_s1d3_4ND_fr0n7_tO_b4ck}",
         desc="Admin portal found. Login works. Totally secure. We even left you a snippet to prove it."),
    dict(dir="web/shodanql", name="ShodanQL", cat="web", val=50,
         conn=("http", 51019), flag="CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998}",
         desc="Search OrionTech's machines by IP. The search box talks straight to the database, like it's 1998."),
    dict(dir="web/shodanql_revenge", name="ShodanQL - Revenge", cat="web", val=50,
         conn=("http", 51020), flag="CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998_for_real_this_time}",
         desc="We patched ShodanQL. For real this time. No more `' OR 1=1 --`. Probably."),
    dict(dir="web/underground_watch_part_1", name="Underground Watch - Part 1", cat="web", val=50,
         conn=("http", 51021), flag="CCSC{f1l3_upl04d_47t4ck5_mu5t_b3_570pp3d}",
         desc="Somebody uploaded a shell and left a note in `/`. Find how they got in. The uploader trusts you. Too much."),
    dict(dir="web/warriors_tech_shop", name="Warriors Tech Shop", cat="web", val=200,
         conn=("http", 51023), flag="CCSC{w3_f0rg3_4nd_r3b1nd_0ur_0wn_t00ls}",
         desc="Hacker gear, legit prices, checkout with JWT. Our key server is very helpful - just ask it where the keys are. And is that shop inside our own network?"),
    # forensics
    dict(dir="forensics/HIDden-1", name="HIDden-1", cat="forensics", val=100,
         conn=None, flag="CCSC{Dis4bling_USBs_D03s_n0t_Dis4ble_HID}",
         desc="Somebody plugged something into that workstation. USBs are disabled, but HID? Nobody disables keyboards. Find the keystrokes."),
    dict(dir="forensics/HIDden-2", name="HIDden-2", cat="forensics", val=100,
         conn=None, flag="CCSC{part2-N1ce_One-Decrypting_Th3_C0mms}",
         desc="Nice typing. Now what did the implant phone home? The comms look like noise. Noise decrypts."),
    dict(dir="forensics/HIDden-3", name="HIDden-3", cat="forensics", val=100,
         conn=None, flag="CCSC{It-C4nn0t_Be_Helpd_Push_On}",
         desc="It cannot be helped. Push on. Last stage. The implant's final words are in there."),
    dict(dir="forensics/asteroid_wars", name="Asteroid Wars", cat="forensics", val=50,
         conn=None, flag="CCSC{1f_th3_4ud10_d035n7_h3lp_ch3ck_m3t4d473!!!TINKGI!}",
         desc="3 minutes of boring meeting audio. The real message isn't audible - it's about the file. TINKGI!"),
    dict(dir="forensics/attachment", name="Attachment", cat="forensics", val=50,
         conn=None, flag="CCSC{Wh4t_1s_4_f1L3,_r341ly?}",
         desc="Don't open the MalDoc. Seriously. But tell us: what is a file, really? Bytes lie. Headers lie. Unzip the truth."),
    dict(dir="forensics/forensic_trace_process", name="Forensic Trace Process", cat="forensics", val=50,
         conn=None, flag="CCSC{4n4lyz1ng_F0r_P4ssw0rds_4nd_th3n_f0r_f1l3s}",
         desc="One pcap attached. Passwords first, files second. Follow the stream, carve the goods."),
    dict(dir="forensics/galactic-connection", name="Galactic Connection", cat="forensics", val=50,
         conn=None, flag="CCSC{wpa2_passwords_are_not_secure}",
         desc="Sniffed WPA2 at an Echo facility. Get on their network, see where the agents phone home. Submit the domain minus `.com`."),
    dict(dir="forensics/hidden-horizons", name="Hidden Horizons", cat="forensics", val=100,
         conn=None, flag="CCSC{N3ver_ev3r_G1ve_Up}",
         desc="One flag.bmp attached. A vast flat field of pixels. Stare past it. Never give up."),
    dict(dir="forensics/orion-lsassault", name="Orion Lsassault", cat="forensics", val=50,
         conn=None, flag="CCSC{P455w0rds_4r3_n0t_s4F3_fr0m_duMp5!!!}",
         desc="Lead engineer's PC got dumped. LSASS went with it. His password is still in there, fleeting but not gone."),
    dict(dir="forensics/underground_watch_part_2", name="Underground Watch - Part 2", cat="forensics", val=100,
         conn=("http", 51022), flag="CCSC{tuNn3L1n9_w17H_iMP3rf3c7_f0rw4rd_53cr3Cy}",
         desc="They got in via webshell (Part 1), then tunneled out. HTTP, then HTTPS that isn't. What tunnel did they build? Requires Part 1."),
]


def render_conn(conn, host):
    if not conn:
        return "", ""
    kind, port = conn
    if kind == "nc":
        return f"nc {host} {port}", f"Connect: `nc {host} {port}`"
    if kind == "tcp":
        return f"{host}:{port} (raw TCP)", f"Connect (raw TCP, not HTTP): `nc {host} {port}`"
    return f"http://{host}:{port}", f"Service: `http://{host}:{port}`"


def zip_public(chal_dir):
    pub = ROOT / chal_dir / "public"
    if not pub.is_dir() or not any(pub.iterdir()):
        return None, None
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(pub.rglob("*")):
            if f.is_file() and f.name != ".gitkeep":
                z.write(f, f.relative_to(pub))
    if not buf.getbuffer().nbytes or len(zipfile.ZipFile(io.BytesIO(buf.getvalue())).namelist()) == 0:
        return None, None
    name = Path(chal_dir).name + "-public.zip"
    return name, buf.getvalue()


def wait_for_ctfd(url, timeout=180):
    """Block until CTFd answers HTTP (container still booting/migrating)."""
    deadline = time.time() + timeout
    while True:
        try:
            r = requests.get(f"{url}/setup", timeout=5)
            if r.status_code < 500:
                return
        except requests.ConnectionError:
            pass
        if time.time() > deadline:
            sys.exit(f"CTFd at {url} did not come up within {timeout}s")
        time.sleep(5)


def needs_setup(url, s):
    r = s.get(f"{url}/api/v1/challenges")
    r.raise_for_status()
    return r.url.rstrip("/").endswith("/setup")


def run_setup(url, s):
    """Complete CTFd's /setup wizard programmatically (fresh DB only)."""
    page = s.get(f"{url}/setup")
    page.raise_for_status()
    m = re.search(r'name="nonce"[^>]*?value="([^"]+)"', page.text)
    form = dict(ctf_name="CCSC 2024 - Kingston",
                ctf_description="Cyprus Cyber Security Challenge CTF 2024 (temporary instance)",
                user_mode="users",
                name=PRESET_ADMIN_NAME, email=PRESET_ADMIN_EMAIL,
                password=PRESET_ADMIN_PASSWORD,
                challenge_visibility="private", account_visibility="public",
                score_visibility="public", registration_visibility="public",
                verify_emails="false", start="", end="")
    if m:
        form["nonce"] = m.group(1)
    r = s.post(f"{url}/setup", data=form)
    r.raise_for_status()
    if needs_setup(url, s):
        sys.exit("CTFd setup did not complete - finish /setup in the browser, then re-run")
    print("CTFd setup completed (users mode, open registration)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=os.environ.get("CTFD_URL", "http://localhost:51024"))
    ap.add_argument("--token", default=os.environ.get("CTFD_TOKEN", PRESET_TOKEN))
    ap.add_argument("--host", default=os.environ.get("CTFD_HOST", "localhost"))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    url = a.url.rstrip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {a.token}"})

    existing = {}
    if not a.dry_run:
        wait_for_ctfd(url)
        if needs_setup(url, s):
            run_setup(url, s)
        # Content-Type: json required so CTFd honors the token on GET
        r = s.get(f"{url}/api/v1/challenges?view=admin",
                  headers={"Content-Type": "application/json"})
        r.raise_for_status()
        existing = {c["name"]: c for c in r.json()["data"]}

    for c in CHALLENGES:
        conn_short, conn_line = render_conn(c["conn"], a.host)
        body = c["desc"] + (f"\n\n{conn_line}" if conn_line else "")
        zip_name, zip_bytes = zip_public(c["dir"])
        if zip_name:
            body += f"\n\nAttachment: `{zip_name}`"
        payload = dict(name=c["name"], category=c["cat"], description=body,
                       value=c["val"], type="standard", state="visible",
                       connection_info=conn_short)
        if a.dry_run:
            print(f"DRY {c['name']} [{c['cat']} {c['val']}] conn={conn_short or '-'} files={zip_name or '-'}")
            continue
        if c["name"] in existing:
            cid = existing[c["name"]]["id"]
            s.patch(f"{url}/api/v1/challenges/{cid}", json=payload).raise_for_status()
            print(f"updated {c['name']} (id={cid})")
        else:
            r = s.post(f"{url}/api/v1/challenges", json=payload)
            r.raise_for_status()
            cid = r.json()["data"]["id"]
            print(f"created {c['name']} (id={cid})")
            # flag only on create; updates keep existing flags
            r = s.post(f"{url}/api/v1/flags",
                       json=dict(challenge_id=cid, content=c["flag"], type="static", data=""))
            r.raise_for_status()
        if zip_bytes:
            files = {"file": (zip_name, zip_bytes, "application/zip")}
            r = s.post(f"{url}/api/v1/files", files=files,
                       data={"challenge": str(cid), "type": "challenge"})
            r.raise_for_status()
            print(f"  + attached {zip_name} ({len(zip_bytes)//1024} KB)")


if __name__ == "__main__":
    main()
