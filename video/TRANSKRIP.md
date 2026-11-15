# Transkrip & Log Suntingan — Dumbbell 1KG (Raya)

## 1. Transkrip audio asal

Kelima-lima klip ditranskrip dengan Whisper `large-v3` (Bahasa Melayu, timestamp setiap perkataan, VAD).
**Tiada percakapan dikesan dalam mana-mana klip.** Whisper hanya menghasilkan frasa "halusinasi"
biasa ("Terima kasih kerana menonton!"), dan VAD tidak menjumpai suara manusia.

| Fail | Tempoh | Audio asal | Kandungan visual |
|---|---|---|---|
| `lv_0_20260110144309.mp4` | 50.1s | Muzik/ambien, tiada suara | Model pegang dumbbell → unboxing kotak 1KG → close-up produk → reverse lunge, squat + raise, squat deadlift |
| `IMG_1164.MOV` | 14.5s | Ambien (tapak kaki) | Squat jump dengan dumbbell (baju merah) |
| `IMG_1208.MOV` | 16.1s | Hampir senyap | Squat + front raise (baju biru/merah) |
| `IMG_1209.MOV` | 11.1s | Ambien | Squat jump (baju biru/merah) — **tidak digunakan** (sama dengan IMG_1164) |
| `IMG_1989.MOV` | 9.6s | Hampir senyap | Squat + front raise (baju biru) |

Oleh itu video ini disunting sebagai **video tanpa suara (text-led)**: semua mesej disampaikan melalui
motion graphics on-screen, muzik latar dan SFX. Audio asal dimatikan.

## 2. Skrip teks on-screen (hasil akhir, 30s, 9:16)

| Masa | Shot (sumber) | Teks on-screen | SFX |
|---|---|---|---|
| 0.0–1.0 | Squat jump (IMG_1164 5.0s) | **HOOK:** "DAH NAK RAYA…" / "TRIM **GELEBEH**" (perkataan bergoyang) | Boom + gegaran |
| 1.0–2.0 | Squat + raise (IMG_1208 0.5s) | "LENGAN & PEHA" + pill "SEBELUM RAYA!" (ketupat) | Whoosh, pop |
| 2.0–4.0 | Model pegang dumbbell (lv_0 0.0s) | "Cuma guna dumbbell 1KG di rumah" | Whoosh, pop |
| 4.0–5.5 | Kotak 1KG (lv_0 4.5s) | UNBOXING — "Parcel dah sampai!" | Swoosh, pop |
| 5.5–7.0 | Buka kotak (lv_0 11.0s) | DALAM KOTAK — "Dapat sepasang" | Swoosh, pop |
| 7.0–8.5 | Keluar dari plastik (lv_0 16.0s) | SESUAI PEMULA — "Ringan & mudah guna" | Swoosh, pop |
| 8.5–10.0 | Close-up logo 1KG (lv_0 21.0s) | Cop "1KG — SETIAP SATU" | Whoosh, ding |
| 10.0–11.5 | Sepasang (lv_0 28.6s) | COMPACT — "Senang simpan & bawa" | Swoosh, riser |
| 11.5–12.7 | (Squat + raise) | Kad hijau "3 GERAKAN WAJIB — LENGAN & PEHA" | Boom |
| 11.5–16.5 | Squat + front raise (IMG_1989 0.0s) | **1. SQUAT + FRONT RAISE** · Peha + lengan · 12 ulangan × 3 set | Whoosh, klik |
| 16.5–21.5 | Reverse lunge (lv_0 34.0s) | **2. REVERSE LUNGE** · Peha + punggung · 10 setiap kaki × 3 set | Whoosh, klik |
| 21.5–26.5 | Squat jump (IMG_1164 2.5s) | **3. SQUAT JUMP** · Peha + bakar lemak · 10 ulangan × 3 set | Whoosh, klik |
| 26.5–30.0 | Sepasang dumbbell (lv_0 30.1s) | **CTA:** "JOM TRIM SEBELUM RAYA!" · butang "TEKAN BEG KUNING" · ketupat jatuh | Boom, pop, ding |

Elemen sepanjang video: bar progres atas (hijau → emas), punch-zoom setiap potongan, flash putih pada potongan hook.

## 3. Bahagian yang dibuang (50s + 51s B-roll → 30s)

- lv_0 0:02–0:04 — model berdiri statik (lebih 2s).
- lv_0 0:06–0:11 — buka pita kotak (lambat, berulang).
- lv_0 0:12–0:16, 0:17–0:21, 0:22–0:29 — pusing-pusing plastik/dumbbell, close-up berulang.
- lv_0 0:39–0:50 — squat + raise & squat deadlift (pendua; versi IMG_1989 lebih jelas).
- IMG_1164 0:00–0:02 dan 0:08–0:14 — berdiri/bersedia, ulangan berlebihan.
- IMG_1208 kecuali 1s untuk hook — gerakan sama dengan IMG_1989.
- IMG_1209 — keseluruhan (pendua squat jump).
- IMG_1989 0:05–0:09 — ulangan berlebihan.

## 4. Audio

- Muzik latar 120 BPM dan semua SFX dijana secara prosedural (`tools/gen_audio.py`) — bebas hak cipta.
- Hook (0–4s) muzik lebih ringan, "drop" penuh selepas itu; fade-out 1.2s di hujung.
