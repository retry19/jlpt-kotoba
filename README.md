# jlpt-kotoba

Daftar kosakata default untuk aplikasi [flashcard-jlpt](https://github.com/retry19/flashcard-jlpt), dipisahkan berdasarkan level JLPT.

## Struktur data

Setiap level tersedia di `N{level}/kotoba.csv` dengan urutan kolom tetap:

```csv
Kana,Kanji,Tipe,Definisi
```

URL data mentah mengikuti pola:

```text
https://raw.githubusercontent.com/retry19/jlpt-kotoba/main/N5/kotoba.csv
```

## Konstanta `Tipe`

| Konstanta | Arti | Istilah Jepang | Contoh |
| --- | --- | --- | --- |
| `n` | Kata benda | 名詞 (`めいし`) | `がくせい,学生,n,siswa` |
| `adj-i` | Kata sifat-i | い形容詞 (`いけいようし`) | `せまい,狭い,adj-i,sempit` |
| `adj-na` | Kata sifat-na | な形容詞 (`なけいようし`) | `にがて,苦手,adj-na,payah/kurang suka` |

Data lama pada beberapa level masih menggunakan nama tipe berbahasa Indonesia. Saat data diperbarui, gunakan kode pendek yang terdokumentasi agar format antartingkat menjadi konsisten.

## Aturan perubahan

1. Pertahankan nama, urutan, dan jumlah kolom CSV.
2. Gunakan konstanta `Tipe` yang sudah terdokumentasi jika kategorinya sesuai.
3. Jangan membuat variasi penulisan untuk tipe yang sama.
4. Dokumentasikan konstanta baru sebelum menggunakannya.
5. Gunakan tanda kutip CSV jika nilai mengandung koma.
6. Nilai Kana, Kanji, atau Tipe boleh kosong; jangan menukar posisi kolom.

Sebelum commit, pastikan setiap baris mempunyai tepat empat kolom dan tidak ada kosakata yang hilang atau terduplikasi tanpa sengaja.
