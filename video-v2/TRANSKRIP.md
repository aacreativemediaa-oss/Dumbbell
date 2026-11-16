# Transkrip & Log Suntingan v2: "3 Senaman Trim Gelebeh"

Brief: **Hook** "3 senaman untuk trim gelebeh lengan & peha" · **USP** "Ada banyak pilihan berat.
Bentuk bersegi senang pegang & tak mudah bergolek" · **CTA** "Nak trim gelebeh, start sekarang!" ·
**Muzik** Motivation.

## 1. Transkrip audio asal (12 klip)

Semua klip ditranskrip dengan Whisper `large-v3` (Bahasa Melayu, VAD). **Tiada percakapan dalam
mana-mana klip.** Audio asal hanya ambien, bunyi tapak kaki atau muzik latar eksport CapCut.
Video ini disunting tanpa suara: mesej disampaikan melalui teks on-screen, muzik dan SFX.

| Fail | Tempoh | Kandungan | Digunakan? |
|---|---|---|---|
| `lv_0_20260110144309.mp4` | 50.1s | Dumbbell **biru 1KG**: unboxing, close-up, senaman (baju kelabu) | Ya: USP |
| `lv_0_20260110232408.mp4` | 46.2s | Dumbbell **pink 2KG**: unboxing, close-up, lunge/squat (baju ungu) | Ya: USP, Senaman 2, CTA |
| `IMG_1163.MOV` | 20.0s | Squat + front raise, hijau (luar, baju merah) | Ya: Senaman 1 |
| `IMG_1164.MOV` | 14.5s | Squat jump, hijau (luar, baju merah) | Ya: Senaman 3 |
| `IMG_1208.MOV` | 16.1s | Squat + front raise (luar) | Tidak (pendua) |
| `IMG_1209.MOV` | 11.1s | Squat jump (luar, baju biru/merah) | Ya: hook, Senaman 3 |
| `IMG_1989.MOV` | 9.6s | Squat + front raise (luar, baju biru) | Tidak (pendua) |
| `IMG_1990.MOV` | 12.2s | Squat ke lantai (luar, baju biru) | Tidak (bukan 3 senaman) |
| `IMG_1991.MOV` | 11.2s | Squat deadlift (luar, baju biru) | Tidak (bukan 3 senaman) |
| `IMG_2533.MOV` | 12.7s | Squat + front raise (dalam rumah) | Ya: hook, USP, Senaman 1 |
| `IMG_2534.MOV` (×2) | 16.9s / 18.9s | Squat deadlift (dalam rumah) | Tidak (bukan 3 senaman) |

## 2. Skrip teks on-screen (31.8s, 9:16, 100 BPM; setiap potongan jatuh pada beat)

| Masa | Shot | Teks on-screen | SFX |
|---|---|---|---|
| 0.0–1.2 | Squat jump (IMG_1209) | **HOOK:** "**3** CUMA SENAMAN · TRIM **GELEBEH** (bergoyang) · LENGAN & PEHA" + bulatan ①②③ (① menyala) | Boom, pop |
| 1.2–2.4 | Reverse lunge pink (lv_0 B) | ② menyala | Whoosh, klik |
| 2.4–3.6 | Squat + raise dalam rumah (IMG_2533) | ③ menyala, muzik build-up (tom + snare roll) | Whoosh, klik |
| 3.6–7.2 | 3 kad video: biru / pink / hijau | **USP 1:** "ADA BANYAK PILIHAN BERAT", label **1KG · 2KG · + LAGI** | Drop muzik, swoosh, pop×3, ding |
| 7.2–8.4 | Muka segi lapan pink (close-up) | **USP 2:** "BENTUK BERSEGI", garis segi lapan dilukis | Whoosh, riser |
| 8.4–9.6 | Tangan genggam dumbbell pink | ✓ "SENANG PEGANG" | Ding |
| 9.6–12.0 | Muka segi lapan biru | Demo: bola bulat bergolek pergi ✗ vs segi lapan kekal stabil ✓ · ✓ "TAK MUDAH BERGOLEK" | Swoosh, whoosh, pop, ding |
| 12.0–17.4 | Squat + front raise (IMG_1163 → IMG_2533) | **SENAMAN 1/3 · SQUAT + FRONT RAISE** · Lengan + peha · 12 ulangan × 3 set | Boom, klik |
| 17.4–22.8 | Reverse lunge, pink 2KG (lv_0 B) | **SENAMAN 2/3 · REVERSE LUNGE** · Peha + punggung · 10 setiap kaki × 3 set | Whoosh, klik |
| 22.8–28.2 | Squat jump (IMG_1164 → IMG_1209) | **SENAMAN 3/3 · SQUAT JUMP** · Peha + bakar kalori · 10 ulangan × 3 set | Whoosh, klik |
| 28.2–31.8 | Sepasang pink 2KG | **CTA:** "NAK TRIM GELEBEH, **START SEKARANG!**" + butang "TEKAN BEG KUNING" | Boom, pop×2, ding |

Sepanjang video: bar progres atas (pink → emas), punch-zoom setiap potongan, flash pada potongan.

## 3. Bahagian yang dibuang (~4 min rakaman → 31.8s)

- Kedua-dua `lv_0`: babak model berdiri statik di awal, buka pita/kotak/plastik, close-up berulang,
  dan senaman pendua di hujung.
- `IMG_1208`, `IMG_1989`: squat + front raise pendua.
- `IMG_1990`, `IMG_1991`, `IMG_2534` ×2: squat deadlift (bukan sebahagian daripada 3 senaman).
- Semua klip senaman: bahagian bersedia/berdiri dan ulangan berlebihan (setiap gerakan dipendekkan jadi 2–3 rep).

## 4. Audio

- Muzik "Motivation" dijana sendiri (`tools/gen_motivation.py`): 100 BPM, progresi I–V–vi–IV (C–G–Am–F),
  build-up tom + snare roll dalam hook, kemudian drop pada 3.6s dengan kick four-on-the-floor, power chord dan string.
- SFX juga dijana sendiri. Semua audio bebas hak cipta.
