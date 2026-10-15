# CCSC 2024 — Challenges

Scoring is fixed by difficulty: **easy 50 · medium 100 · hard 200** (from `challenge.yml` tags).

> Replace `0.0.0.0` with the event IP when deploying. Port is in the description and uses the **host** port.

## Crypto — breaking ciphers, oracles and math

| Challenge | Points | Description | Flag |
|---|---|---|---|
| Andromeda Cloud Storage | 200 | Andromeda's "unbreakable" cloud is open for signups. Store your secrets, get your personal key... eventually. Our compressor is *very* naive — ever heard of CRIME? Find it at `0.0.0.0:51001`. | `ccsc{congrats.here.is.a.s1d3.ch4nNel?!}` |
| Andromeda Cloud Storage v2 | 200 | We fixed v1. Now with real AES, real MAC, full bytes. What could possibly go wrong? Decryption still tells you a *little* too much... Find it at `0.0.0.0:51002`. | `CCSC{p4dd1ng_oracl3_att4ck_due_to_flawed_implem3ntati0n_of_decryption!9f03268fc9363db00c7a43}` |
| Inverted Oracle | 50 | Orion's terminal says yes or no. That's all it says. That's all you need. Flip it. Find it at `0.0.0.0:51003`. | `CCSC{fL1p1Ty_Fl1P!!}` |
| Identity Thief | 100 | He stole our keys using fancy field math. We got his notebook (`public/main.sage`) and his scratch paper (`public/output.txt`). Do the math back. | `CCSC{Y0u_g0tt4_b3_c4r3fu11_wh3n_us1n9_f13ld_m4th3m4tics}` |

## Misc — grab-bag: guessing games, password cracking, sanity checks

| Challenge | Points | Description | Flag |
|---|---|---|---|
| Armored Up | 100 | One PyArmor'd file. One forgotten password. Python 3.11.2 on Debian 12 (`public/armored_up.tar.gz`). Guards get lazy — go ask it nicely. Find it at `0.0.0.0:51004`. | `CCSC{pr0ject_3cho_let_th3ir_gu4rd_d0wn_ag4in}` |
| Metadata Matters | 50 | Root hash in hand: `$6$yWctB8cp...` 10 chars, upper + lower + digit + symbol. Uncrackable. Unless the password was never *in* the hash... check the file's baggage. | `CCSC{M4sk}` |
| Password Keep | 50 | One cold vault. One `public/chall.7z`. No password. But history repeats itself — shell history, git history... you get it. | `CCSC{history_may_not_repeat_or_rhyme_but_it_is_always_useful}` |
| Superguesser Part 1 | 50 | I'm thinking of a number. You have seconds. And I suck at randomness (`public/superguesser.zip`). Find it at `0.0.0.0:51005`. | `CCSC{part1_sec0nds_and_s33ds_d0nt_m1x_t0gether}` |
| Superguesser Part 2 | 100 | You beat seconds. Cute. Now I'm thinking in millis and I brought a brain. Bring luck, bring math. Find it at `0.0.0.0:51006`. | `CCSC{part2_m1lli5_n33d_som3_brains_and_s0me_luck}` |
| Superguesser Part 3 | 200 | Nanos now. No more guessing seeds, kid. Bisect the air itself. Find it at `0.0.0.0:51007`. | `CCSC{part3_nan0s_d0nt_c4re_bis3ct_is_1n_the_a1r}` |
| Welcome | 50 | Free points. Just prove you can read. Start at #rules. | `CCSC{rul3s_ar3_n0t_m3ant_t0_b3_br0k3n!}` |

## Pwn — binary exploitation, overflow the buffers

| Challenge | Points | Description | Flag |
|---|---|---|---|
| GOT Override | 50 | New to pwn? Perfect. There's a table of addresses just *begging* to be overwritten. Your first GOT, you'll never forget her. Find it at `0.0.0.0:51008`. | `CCSC{if_Th1s_is_Your_First_Pwn_Feel_Pr0ud_otherwise_K33p_going}` |
| hijack | 200 | The hooks are all but gone. Find another way. Find it at `0.0.0.0:51009`. | `CCSC{if_y0u_Used-FSOP_which_technique?}` |
| Infiltration | 100 | The secret is locked in memory and the binary won't talk. Unless it crashes... crashes leave cores. Cores talk. Find it at `0.0.0.0:51010`. | `CCSC{c0r3dumps_4r3_us3ful_4_d3bugg1ng_4nd_stuff}` |
| Model Scan | 50 | Totally safe AI scanner. Scans every model. Definitely can't be tricked by a pickle. Pickles are innocent. Find it at `0.0.0.0:51011`. | `CCSC{why_4r3_w3_st1ll_us1ng_p1kl3?!?}` |
| Spilled | 50 | Our AI junior learned C yesterday. It spills a few bytes... everywhere. Just ask it how it's feeling. Find it at `0.0.0.0:51012`. | `CCSC{00ps_1_sp1ll3d_4_f3w_byt3s}` |

## Reverse — reverse-engineer binaries, VMs and custom protocols

| Challenge | Points | Description | Flag |
|---|---|---|---|
| TLV | 200 | Old protocol. No symbols. No mercy. Speak in Type-Length-Value or don't speak at all. Raw TCP, bring Scapy. Find it at `0.0.0.0:51013` (raw TCP — speak TLV packets, not HTTP). | `CCSC{Fr3aking_H4te_Revers1ng_W1thout_Symb0ls}` |
| Ancient VM | 100 | Rusty VM. Lost source. We have the program, we have the output. All that's missing is the input — just solve 1000 constraints before lunch (`public/vm`, `program.txt`, `output.txt`). | `CCSC{r3v_s0m3_rust_4nd_s0lv3_s0m3_c0nstra1nt5}` |
| Drone Army | 100 | One `public/drone_army.s` controls the whole swarm. It's just XORs all the way down. How hard can it be? | `CCSC{4rMy_0f_X0rs_R3v3r5eD!!}` |
| Licensed Ops | 50 | Enter license key to continue. No key? No problem. The check is right there if you look. Find it at `0.0.0.0:51014`. | `CCSC{Y0ur_Rev3rsing_Journey_Just_st4rted}` |

## Web — hack the web apps (SQLi, XSS, uploads, JWT, SSRF)

| Challenge | Points | Description | Flag |
|---|---|---|---|
| Arcane Runes | 100 | The machines chant in runes and waste your time. Or do they? Persevere. The prompt is the puzzle. Find it at `0.0.0.0:51015`. | `CCSC{myst1cal_cosplAI_0r_wAIst3_of_tAIm3}` |
| Cross Checked Report | 50 | See something, say something. File a guard report. Our bot reads *everything* you submit, faithfully rendering every tag and script. Find it at `0.0.0.0:51016`. | `CCSC{1f_1t_acc3pt5_1NpuT_1t_W!LL_b3_XSSed}` |
| Microbuns | 100 | A silicon poet who loves buns and verses. He'll recite anything. Feed him well (`public/microbuns.zip`). Find it at `0.0.0.0:51017`. | `CCSC{CybeR_r3alms_and_Anc1ent_v0w5}` |
| Portal | 200 | Admin portal found. Login works. Totally secure. We even left you a snippet to prove it (`public/login_snippet.txt`). Find it at `0.0.0.0:51018`. | `CCSC{s1d3_t0_s1d3_4ND_fr0n7_tO_b4ck}` |
| ShodanQL | 50 | Search OrionTech's machines by IP. The search box talks straight to the database, like it's 1998. Find it at `0.0.0.0:51019`. | `CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998}` |
| ShodanQL - Revenge | 50 | We patched ShodanQL. For real this time. No more `' OR 1=1 --`. Probably. Find it at `0.0.0.0:51020`. | `CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998_for_real_this_time}` |
| Underground Watch - Part 1 | 50 | Somebody uploaded a shell and left a note in `/`. Find how they got in. The uploader trusts you. Too much. Find it at `0.0.0.0:51021`. | `CCSC{f1l3_upl04d_47t4ck5_mu5t_b3_570pp3d}` |
| Warriors Tech Shop | 200 | Hacker gear, legit prices, checkout with JWT. Our key server is *very* helpful — just ask it where the keys are. And is that shop inside our own network? Find it at `0.0.0.0:51023`. | `CCSC{w3_f0rg3_4nd_r3b1nd_0ur_0wn_t00ls}` |

## Forensics — pcaps, dumps, stego and metadata

| Challenge | Points | Description | Flag |
|---|---|---|---|
| HIDden-1 | 100 | Somebody plugged *something* into that workstation. USBs are disabled, but HID? Nobody disables keyboards. Find the keystrokes (`public/inject.bin`, `public/traffic.pcapng`). | `CCSC{Dis4bling_USBs_D03s_n0t_Dis4ble_HID}` |
| HIDden-2 | 100 | Nice typing. Now what did the implant phone home? The comms look like noise. Noise decrypts. | `CCSC{part2-N1ce_One-Decrypting_Th3_C0mms}` |
| HIDden-3 | 100 | It cannot be helped. Push on. Last stage. The implant's final words are in there. | `CCSC{It-C4nn0t_Be_Helpd_Push_On}` |
| Asteroid Wars | 50 | 3 minutes of boring meeting audio. The real message isn't audible — it's *about* the file (`public/internal_communication.mp3`). TINKGI! | `CCSC{1f_th3_4ud10_d035n7_h3lp_ch3ck_m3t4d473!!!TINKGI!}` |
| Attachment | 50 | Don't open `public/MalDoc.xlsx`. Seriously. But tell us: what *is* a file, really? Bytes lie. Headers lie. Unzip the truth. | `CCSC{Wh4t_1s_4_f1L3,_r341ly?}` |
| Forensic Trace Process | 50 | One pcap (`public/forensic_trace_process.pcapng`). Passwords first, files second. Follow the stream, carve the goods. | `CCSC{4n4lyz1ng_F0r_P4ssw0rds_4nd_th3n_f0r_f1l3s}` |
| Galactic Connection | 50 | Sniffed WPA2 at an Echo facility. Get on their network (`public/galactic_connection.pcapng`), see where the agents phone home. Submit the domain minus `.com`. | `CCSC{wpa2_passwords_are_not_secure}` |
| Hidden Horizons | 100 | One `public/flag.bmp`. A vast flat field of pixels. Stare past it. Never give up. | `CCSC{N3ver_ev3r_G1ve_Up}` |
| Orion Lsassault | 50 | Lead engineer's PC got dumped. LSASS went with it. His password is still in there, fleeting but not gone (`public/lsassault.zip`). | `CCSC{P455w0rds_4r3_n0t_s4F3_fr0m_duMp5!!!}` |
| Underground Watch - Part 2 | 100 | They got in via webshell (Part 1), then tunneled out. HTTP, then HTTPS that isn't. What tunnel did they build (`public/underground_watch_part_2.pcapng`)? Requires Part 1. Find it at `0.0.0.0:51022`. | `CCSC{tuNn3L1n9_w17H_iMP3rf3c7_f0rw4rd_53cr3Cy}` |
