# jlpt-kotoba

Daftar kosakata default untuk aplikasi [flashcard-jlpt](https://github.com/retry19/flashcard-jlpt), dipisahkan berdasarkan level JLPT.

## Struktur data

### Kotoba

Setiap level tersedia di `N{level}/kotoba.csv` dengan urutan kolom tetap:

```csv
Kana,Kanji,Tipe,Definisi,Notes
```

Kolom `Notes` berisi catatan tambahan seperti batasan penggunaan, nuansa makna, atau konteks. Kolom ini boleh dikosongkan jika tidak ada catatan.

Contoh:

```csv
ちいさい,小さい,adj-i,kecil,untuk barang/manusia
```

URL data mentah mengikuti pola:

```text
https://raw.githubusercontent.com/retry19/jlpt-kotoba/main/N5/kotoba.csv
```

### Kanji

Data kanji pada setiap level disimpan dalam dua file: `kanji.csv` dan
`kanji_vocabulary.csv`.

#### `kanji.csv`

Berisi daftar kanji beserta pengucapan dan artinya, dengan urutan kolom tetap:

```csv
id,kanji,onyomi,kunyomi,meaning
```

Kolom `id` adalah pengenal kanji yang menjadi key relasi dengan
`kanji_vocabulary.csv`. Jangan mengubah atau menggeser `id` yang sudah ada agar
relasi tetap benar. Kolom `kanji` berisi karakter yang dipelajari dan dapat
menyertakan okurigana, misalnya `出る`. Kolom `onyomi` atau `kunyomi` boleh
kosong jika kanji tersebut tidak memiliki bacaan yang dicantumkan. Gunakan
tanda kurung Jepang `（ ）` untuk menandai bagian okurigana dalam bacaan.

Contoh:

```csv
1,一,イチ,ひと（つ）,satu
2,二,ニ/ジ,ふた（つ）,dua
3,三,サン,みっ（つ）,tiga
```

URL data mentah mengikuti pola:

```text
https://raw.githubusercontent.com/retry19/jlpt-kotoba/main/N5/kanji.csv
```

#### `kanji_vocabulary.csv`

Berisi daftar kosakata yang berhubungan dengan kanji melalui `kanji_id`, dengan
urutan kolom tetap. Satu kanji dapat memiliki nol atau lebih entri kosakata.

```csv
kanji_id,word,reading,meaning,type
```

Kolom `kanji_id` harus merujuk ke `id` yang tersedia dalam `kanji.csv`. Kolom
`type` berisi `example` untuk contoh penggunaan reguler atau `exception` untuk
kata dengan bacaan atau penggunaan khusus. Kolom `meaning` boleh kosong jika
arti belum dicantumkan.

Contoh:

```csv
15,先生,せんせい,guru,example
15,先月,せんげつ,bulan lalu,example
```

URL data mentah mengikuti pola:

```text
https://raw.githubusercontent.com/retry19/jlpt-kotoba/main/N5/kanji_vocabulary.csv
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
6. Nilai Kana, Kanji, Tipe, atau Notes boleh kosong; jangan menukar posisi kolom.

Sebelum commit, pastikan setiap baris mempunyai tepat lima kolom dan tidak ada kosakata yang hilang atau terduplikasi tanpa sengaja.
