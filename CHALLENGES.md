# CCSC 2024 — Challenges

Scoring is fixed by difficulty: **easy 50 · medium 100 · hard 200** (from `challenge.yml` tags).

> Replace `0.0.0.0` with the event IP when deploying. `Find me at` uses the **host** port.

## Crypto — breaking ciphers, oracles and math

| Challenge | Points | Flag | Port |
|---|---|---|---|
| Andromeda Cloud Storage | 200 | `ccsc{congrats.here.is.a.s1d3.ch4nNel?!}` | 1337 |
| Andromeda Cloud Storage v2 | 200 | `CCSC{p4dd1ng_oracl3_att4ck_due_to_flawed_implem3ntati0n_of_decryption!9f03268fc9363db00c7a43}` | 1338 |
| Inverted Oracle | 50 | `CCSC{fL1p1Ty_Fl1P!!}` | 13373 |
| Identity Thief | 100 | `CCSC{Y0u_g0tt4_b3_c4r3fu11_wh3n_us1n9_f13ld_m4th3m4tics}` | static files |

## Misc — grab-bag: guessing games, password cracking, sanity checks

| Challenge | Points | Flag | Port |
|---|---|---|---|
| Armored Up | 100 | `CCSC{pr0ject_3cho_let_th3ir_gu4rd_d0wn_ag4in}` | 1339 |
| Metadata Matters | 50 | `CCSC{M4sk}` | static |
| Password Keep | 50 | `CCSC{history_may_not_repeat_or_rhyme_but_it_is_always_useful}` | static (`public/chall.7z`) |
| Superguesser Part 1 | 50 | `CCSC{part1_sec0nds_and_s33ds_d0nt_m1x_t0gether}` | 9745 |
| Superguesser Part 2 | 100 | `CCSC{part2_m1lli5_n33d_som3_brains_and_s0me_luck}` | 9746 |
| Superguesser Part 3 | 200 | `CCSC{part3_nan0s_d0nt_c4re_bis3ct_is_1n_the_a1r}` | 9747 |
| Welcome | 50 | `CCSC{rul3s_ar3_n0t_m3ant_t0_b3_br0k3n!}` | static (read #rules) |

## Pwn — binary exploitation, overflow the buffers

| Challenge | Points | Flag | Port |
|---|---|---|---|
| GOT Override | 50 | `CCSC{if_Th1s_is_Your_First_Pwn_Feel_Pr0ud_otherwise_K33p_going}` | 1340 |
| hijack | 200 | `CCSC{if_y0u_Used-FSOP_which_technique?}` | 1341 |
| Infiltration | 100 | `CCSC{c0r3dumps_4r3_us3ful_4_d3bugg1ng_4nd_stuff}` | 1342 |
| Model Scan | 50 | `CCSC{why_4r3_w3_st1ll_us1ng_p1kl3?!?}` | 1343 |
| Spilled | 50 | `CCSC{00ps_1_sp1ll3d_4_f3w_byt3s}` | 1344 |

## Reverse — reverse-engineer binaries, VMs and protocols

| Challenge | Points | Flag | Port |
|---|---|---|---|
| TLV | 200 | `CCSC{Fr3aking_H4te_Revers1ng_W1thout_Symb0ls}` | 8080 (raw TCP, not HTTP) |
| Ancient VM | 100 | `CCSC{r3v_s0m3_rust_4nd_s0lv3_s0m3_c0nstra1nt5}` | static (`public/vm`, `program.txt`, `output.txt`) |
| Drone Army | 100 | `CCSC{4rMy_0f_X0rs_R3v3r5eD!!}` | static (`public/drone_army.s`) |
| Licensed Ops | 50 | `CCSC{Y0ur_Rev3rsing_Journey_Just_st4rted}` | 1345 |

## Web — hack the web apps (SQLi, XSS, uploads, JWT, SSRF)

| Challenge | Points | Flag | Port |
|---|---|---|---|
| Arcane Runes | 100 | `CCSC{myst1cal_cosplAI_0r_wAIst3_of_tAIm3}` | 3000 |
| Cross Checked Report | 50 | `CCSC{1f_1t_acc3pt5_1NpuT_1t_W!LL_b3_XSSed}` | 5001 (container :5000; remapped off macOS AirPlay port 5000) |
| Microbuns | 100 | `CCSC{CybeR_r3alms_and_Anc1ent_v0w5}` | 8083 |
| Portal | 200 | `CCSC{s1d3_t0_s1d3_4ND_fr0n7_tO_b4ck}` | 3004 |
| ShodanQL | 50 | `CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998}` | 3003 |
| ShodanQL - Revenge | 50 | `CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998_for_real_this_time}` | 3006 |
| Underground Watch - Part 1 | 50 | `CCSC{f1l3_upl04d_47t4ck5_mu5t_b3_570pp3d}` | 3001 |
| Warriors Tech Shop | 200 | `CCSC{w3_f0rg3_4nd_r3b1nd_0ur_0wn_t00ls}` | 3005 |

## Forensics — pcaps, dumps, stego and metadata

| Challenge | Points | Flag | Port |
|---|---|---|---|
| HIDden-1 | 100 | `CCSC{Dis4bling_USBs_D03s_n0t_Dis4ble_HID}` | static (`inject.bin`, `traffic.pcapng`) |
| HIDden-2 | 100 | `CCSC{part2-N1ce_One-Decrypting_Th3_C0mms}` | static (`inject.bin`, `traffic.pcapng`) |
| HIDden-3 | 100 | `CCSC{It-C4nn0t_Be_Helpd_Push_On}` | static (`inject.bin`, `traffic.pcapng`) |
| Asteroid Wars | 50 | `CCSC{1f_th3_4ud10_d035n7_h3lp_ch3ck_m3t4d473!!!TINKGI!}` | static (`internal_communication.mp3`) |
| Attachment | 50 | `CCSC{Wh4t_1s_4_f1L3,_r341ly?}` | static (`MalDoc.xlsx`) |
| Forensic Trace Process | 50 | `CCSC{4n4lyz1ng_F0r_P4ssw0rds_4nd_th3n_f0r_f1l3s}` | static (`forensic_trace_process.pcapng`) |
| Galactic Connection | 50 | `CCSC{wpa2_passwords_are_not_secure}` | static (`galactic_connection.pcapng`) |
| Hidden Horizons | 100 | `CCSC{N3ver_ev3r_G1ve_Up}` | static (`flag.bmp`) |
| Orion Lsassault | 50 | `CCSC{P455w0rds_4r3_n0t_s4F3_fr0m_duMp5!!!}` | static (`lsassault.zip`) |
| Underground Watch - Part 2 | 100 | `CCSC{tuNn3L1n9_w17H_iMP3rf3c7_f0rw4rd_53cr3Cy}` | 3002 + static pcap |

---

## Crypto

### Andromeda Cloud Storage

Category Name: crypto
Category Description: Breaking ciphers, padding oracles and crypto math.

Points: 200
Flag: `ccsc{congrats.here.is.a.s1d3.ch4nNel?!}`

Description: The Andromeda Cloud Storage v1.1.1 is a highly secure encrypted storage. Register an account to store data securely in an intergalactic way. After registration you will "soon" receive your personal symmetric key to read the secret flag. Hint: the `Encoder` is a custom naive compression function for ASCII — read up on classic compression algorithms.

Find me at: `0.0.0.0:1337`

### Andromeda Cloud Storage v2

Category Name: crypto
Category Description: Breaking ciphers, padding oracles and crypto math.

Points: 200
Flag: `CCSC{p4dd1ng_oracl3_att4ck_due_to_flawed_implem3ntati0n_of_decryption!9f03268fc9363db00c7a43}`

Description: v2.0.0 of the Andromeda Cloud Storage with personal AES and MAC keys. New feature: now supports the full range of bytes!

Find me at: `0.0.0.0:1338`

### Inverted Oracle

Category Name: crypto
Category Description: Breaking ciphers, padding oracles and crypto math.

Points: 50
Flag: `CCSC{fL1p1Ty_Fl1P!!}`

Description: Infiltrating the Orion Secure Terminal is the only path forward in uncovering the secrets of Project Echo. This high-security terminal uses advanced cryptography — can you invert its security mechanisms?

Find me at: `0.0.0.0:13373`

### Identity Thief

Category Name: crypto
Category Description: Breaking ciphers, padding oracles and crypto math.

Points: 100
Flag: `CCSC{Y0u_g0tt4_b3_c4r3fu11_wh3n_us1n9_f13ld_m4th3m4tics}`

Description: Someone stole our identity and every secret we had! Luckily we retrieved some of the thief's code and output (`public/main.sage`, `public/output.txt`).

## Misc

### Armored Up

Category Name: misc
Category Description: Grab-bag — anything that doesn't fit elsewhere.

Points: 100
Flag: `CCSC{pr0ject_3cho_let_th3ir_gu4rd_d0wn_ag4in}`

Description: You exfiltrated a super secret Project Echo file protected with PyArmor. Figure out the correct password (Python 3.11.2, Debian 12, `public/armored_up.tar.gz`).

Find me at: `0.0.0.0:1339`

### Metadata Matters

Category Name: misc
Category Description: Grab-bag — anything that doesn't fit elsewhere.

Points: 50
Flag: `CCSC{M4sk}`

Description: An agent has a foothold on an isolated workstation and needs root. We extracted the root hash (`$6$yWctB8cp...`). Password policy: 10 chars with capitals, numbers, lowercase and symbols. Cracking seems impossible... unless you know something we don't?

### Password Keep

Category Name: misc
Category Description: Grab-bag — anything that doesn't fit elsewhere.

Points: 50
Flag: `CCSC{history_may_not_repeat_or_rhyme_but_it_is_always_useful}`

Description: Agents broke into a cold storage vault belonging to OrionTech and found a single file (`public/chall.7z`). Can you help them?

### Superguesser Part 1

Category Name: misc
Category Description: Grab-bag — anything that doesn't fit elsewhere.

Points: 50
Flag: `CCSC{part1_sec0nds_and_s33ds_d0nt_m1x_t0gether}`

Description: The machines live and breathe in binary. Search for ways to use that against them and capture the flag (`public/superguesser.zip`).

Find me at: `0.0.0.0:9745`

### Superguesser Part 2

Category Name: misc
Category Description: Grab-bag — anything that doesn't fit elsewhere.

Points: 100
Flag: `CCSC{part2_m1lli5_n33d_som3_brains_and_s0me_luck}`

Description: The machines live and breathe in binary. Search for ways to use that against them and capture the flag.

Find me at: `0.0.0.0:9746`

### Superguesser Part 3

Category Name: misc
Category Description: Grab-bag — anything that doesn't fit elsewhere.

Points: 200
Flag: `CCSC{part3_nan0s_d0nt_c4re_bis3ct_is_1n_the_a1r}`

Description: The machines live and breathe in binary. Search for ways to use that against them and capture the flag.

Find me at: `0.0.0.0:9747`

### Welcome

Category Name: misc
Category Description: Grab-bag — anything that doesn't fit elsewhere.

Points: 50
Flag: `CCSC{rul3s_ar3_n0t_m3ant_t0_b3_br0k3n!}`

Description: Welcome to the CCSC 2024, I hope you read the #rules!

## Pwn

### GOT Override

Category Name: pwn
Category Description: Binary exploitation — smash stacks, overwrite GOT, hijack control flow.

Points: 50
Flag: `CCSC{if_Th1s_is_Your_First_Pwn_Feel_Pr0ud_otherwise_K33p_going}`

Description: You have been recruited by the Andromeda Initiative to foil OrionTech's Project Echo. Exploit a critical vulnerability exposing the Global Offset Table (GOT) to dismantle their scheme.

Find me at: `0.0.0.0:1340`

### hijack

Category Name: pwn
Category Description: Binary exploitation — smash stacks, overwrite GOT, hijack control flow.

Points: 200
Flag: `CCSC{if_y0u_Used-FSOP_which_technique?}`

Description: The hooks are all but gone. Find another way.

Find me at: `0.0.0.0:1341`

### Infiltration

Category Name: pwn
Category Description: Binary exploitation — smash stacks, overwrite GOT, hijack control flow.

Points: 100
Flag: `CCSC{c0r3dumps_4r3_us3ful_4_d3bugg1ng_4nd_stuff}`

Description: You infiltrated Project Echo's systems but the secret is well guarded. If only there was a way to dump the secret...

Find me at: `0.0.0.0:1342`

### Model Scan

Category Name: pwn
Category Description: Binary exploitation — smash stacks, overwrite GOT, hijack control flow.

Points: 50
Flag: `CCSC{why_4r3_w3_st1ll_us1ng_p1kl3?!?}`

Description: Project Echo agents are testing cutting-edge AI models. They scan them so Andromeda hackers don't try anything tricky!

Find me at: `0.0.0.0:1343`

### Spilled

Category Name: pwn
Category Description: Binary exploitation — smash stacks, overwrite GOT, hijack control flow.

Points: 50
Flag: `CCSC{00ps_1_sp1ll3d_4_f3w_byt3s}`

Description: Project Echo is training a new AI model to be the best C developer. It's still learning input handling and spilling it all over the buffers...

Find me at: `0.0.0.0:1344`

## Reverse

### TLV

Category Name: reverse
Category Description: Reverse-engineering binaries, VMs and custom protocols.

Points: 200
Flag: `CCSC{Fr3aking_H4te_Revers1ng_W1thout_Symb0ls}`

Description: Decipher "Technological Labyrinth Vanguard", a forgotten network protocol in Project Echo's systems. Reverse TLV, find its weaknesses, and exploit them for the Andromeda Initiative.

Find me at: `0.0.0.0:8080` (raw TCP — speak TLV packets, not HTTP)

### Ancient VM

Category Name: reverse
Category Description: Reverse-engineering binaries, VMs and custom protocols.

Points: 100
Flag: `CCSC{r3v_s0m3_rust_4nd_s0lv3_s0m3_c0nstra1nt5}`

Description: An Andromeda hacker extracted an ancient, rusty VM belonging to Project Echo but couldn't get the secret file. Recover it (`public/vm`, `program.txt`, `output.txt`).

### Drone Army

Category Name: reverse
Category Description: Reverse-engineering binaries, VMs and custom protocols.

Points: 100
Flag: `CCSC{4rMy_0f_X0rs_R3v3r5eD!!}`

Description: OrionTech's drones are controlled by a highly encrypted program managing surveillance. Reverse it to hijack the fleet (`public/drone_army.s`).

### Licensed Ops

Category Name: reverse
Category Description: Reverse-engineering binaries, VMs and custom protocols.

Points: 50
Flag: `CCSC{Y0ur_Rev3rsing_Journey_Just_st4rted}`

Description: Navigate encrypted networks, dissect obscure digital artifacts and crack the licensing check to safeguard the digital frontier.

Find me at: `0.0.0.0:1345`

## Web

### Arcane Runes

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 100
Flag: `CCSC{myst1cal_cosplAI_0r_wAIst3_of_tAIm3}`

Description: We believe the machines are trying to waste our time. Nevertheless, persevere; retrieve the flag!

Find me at: `0.0.0.0:3000`

### Cross Checked Report

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 50
Flag: `CCSC{1f_1t_acc3pt5_1NpuT_1t_W!LL_b3_XSSed}`

Description: OrionTech monitors the area around their base with a guard reporting system. Have a look — maybe *you* could spot something instead? XSS the report and the bot will visit it.

Find me at: `0.0.0.0:5001`

### Microbuns

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 100
Flag: `CCSC{CybeR_r3alms_and_Anc1ent_v0w5}`

Description: I may be silicon but I can still stuff my RAM with buns and appreciate poetry. (`public/microbuns.zip`)

Find me at: `0.0.0.0:8083`

### Portal

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 200
Flag: `CCSC{s1d3_t0_s1d3_4ND_fr0n7_tO_b4ck}`

Description: We found an admin portal. Do we really need to say more? (`public/login_snippet.txt`)

Find me at: `0.0.0.0:3004`

### ShodanQL

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 50
Flag: `CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998}`

Description: A website listing all systems OrionTech owns. Access the admin page and take the site down for good. (IP search field is injectable.)

Find me at: `0.0.0.0:3003`

### ShodanQL - Revenge

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 50
Flag: `CCSC{pwn1nG_w1th_SQL1_1nj3ct10n_s1nc3_1998_for_real_this_time}`

Description: Same listing site, hardened — for real this time.

Find me at: `0.0.0.0:3006`

### Underground Watch - Part 1

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 50
Flag: `CCSC{f1l3_upl04d_47t4ck5_mu5t_b3_570pp3d}`

Description: The Andromeda surveillance app was hacked via file upload; the attacker left a note in `/`. Find the vulnerability and report how they got in.

Find me at: `0.0.0.0:3001`

### Warriors Tech Shop

Category Name: web
Category Description: Web exploitation — SQLi, XSS, uploads, JWT, SSRF.

Points: 200
Flag: `CCSC{w3_f0rg3_4nd_r3b1nd_0ur_0wn_t00ls}`

Description: Your one-stop shop for hacker essentials against Project Echo. You might also be able to purchase some secrets. (JWT JKU injection + DNS rebinding.)

Find me at: `0.0.0.0:3005`

## Forensics

### HIDden-1

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 100
Flag: `CCSC{Dis4bling_USBs_D03s_n0t_Dis4ble_HID}`

Description: Dissect the USB HID injection artifacts (`public/inject.bin`, `public/traffic.pcapng`).

### HIDden-2

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 100
Flag: `CCSC{part2-N1ce_One-Decrypting_Th3_C0mms}`

Description: Continue through the covert comms in the same capture set.

### HIDden-3

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 100
Flag: `CCSC{It-C4nn0t_Be_Helpd_Push_On}`

Description: Final stage of the HID injection trail.

### Asteroid Wars

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 50
Flag: `CCSC{1f_th3_4ud10_d035n7_h3lp_ch3ck_m3t4d473!!!TINKGI!}`

Description: We recorded OrionTech's secret meeting. The audio file holds something more meta than what's audible (`public/internal_communication.mp3`).

### Attachment

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 50
Flag: `CCSC{Wh4t_1s_4_f1L3,_r341ly?}`

Description: An agent received a suspicious attachment (`public/MalDoc.xlsx`). We stopped them before they opened it — tell us what's inside.

### Forensic Trace Process

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 50
Flag: `CCSC{4n4lyz1ng_F0r_P4ssw0rds_4nd_th3n_f0r_f1l3s}`

Description: Analyze the OrionTech internal pcap (`public/forensic_trace_process.pcapng`) and report any sensitive information.

### Galactic Connection

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 50
Flag: `CCSC{wpa2_passwords_are_not_secure}`

Description: An undercover hacker sniffed packets at a Project Echo facility. Get access to their galactic network (`public/galactic_connection.pcapng`). The flag is the domain agents access — submit minus `.com`, wrapped in `CCSC{}`.

### Hidden Horizons

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 100
Flag: `CCSC{N3ver_ev3r_G1ve_Up}`

Description: A digital odyssey through concealed secrets and obscurity (`public/flag.bmp`). Uncover the hidden horizons.

### Orion Lsassault

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 50
Flag: `CCSC{P455w0rds_4r3_n0t_s4F3_fr0m_duMp5!!!}`

Description: A process dump from a Project Echo lead engineer's PC holds fleeting authentication tokens. Find their machine password (`public/lsassault.zip`).

### Underground Watch - Part 2

Category Name: forensics
Category Description: Forensics — pcaps, dumps, disk images and stego.

Points: 100
Flag: `CCSC{tuNn3L1n9_w17H_iMP3rf3c7_f0rw4rd_53cr3Cy}`

Description: The attacker got in (see Part 1), then vanished like through an underground tunnel. The packet capture shows HTTP then HTTPS — work out the tunnel they built with their webshell (`public/underground_watch_part_2.pcapng`). Requires the Part 1 solution.

Find me at: `0.0.0.0:3002`
