# Belajar Repository GIT
## Instalasi
Untuk melakukan proyek sederhana ini, perlu memiliki Git yang diinstal di komputer. Jika belum, dapat mengunduhnya dari [situs resmi Git](https://git-scm.com/downloads). Selain itu, perlu juga memiliki akun github dimana merupakan versi GIT yang berbasis online untuk lebih jelasnya bisa mengunjungi (https://github.com/). Pada proyek ini, karena memerlukan bahasa pemograman python, saya mencoba memanfaatkan Miniconda yang merupakan versi mini dari Anaconda sebagai salah paket environtment yang membantu dalam pengembangan yang berbasis python. 
## Buat Repository di GitHub
1. Buka browser dan kunjugi GitHub.
2. Login ke akun GitHub .
3. Klik tombol "+" di pojok kanan atas, kemudian pilih "New repository".
4. Beri nama repository "dibimbing-belajar-github".
5. Klik tombol "Create repository".

Buat repository GitHub "dibimbing-belajar-github".saya akan menunjukkan langkah-langkah singkat untuk melakukan kloning repository yang telah saya buat di akun GitHub.


## Clone Repository
Untuk melakukan clone repository, jalankan perintah berikut di terminal:

```bash
git clone https://github.com/ridhohrnf/dibimbing-belajar-github.git
```

## Buat file Python
1. Masuk ke direktori repository yang sudah di-clone.
2. Download username.csv yang akan digunakan sebagai data.
3. Buat file python untuk read file csv


## Commit Pertama
1. Melakukan commit untuk pertama kali sebagai main/master ke github
```bash
  git add read_file.py
  git add username.csv
  git commit -m "add feature"
  git push origin master
  ```
2. Melakukan pemeriksaan untuk menampilkan branch main/master

## Buat Branch Baru
1. Di terminal, masuk ke direktori repository.
2. Ketik perintah berikut untuk membuat branch baru dengan feature:
```bash
  git branch feature
  ```

3. Buat file Python baru (misalnya, filter_file.py) dan tambahkan function untuk filter file CSV.

4. Aktifkan branch baru dengan perintah berikut:
```bash
  git checkout feature
  ```

## Commit dan Push
1. Tambahkan file yang sudah dibuat ke staging area dengan perintah:
```bash
  git add filter_file.py
  ```

2. Lakukan commit dengan perintah:
```bash
  git commit -m "add feature read file"
  ```

4. Lakukan push ke repository dengan perintah:
```bash
  git push origin feature
  ```

## Buat Pull Request di GitHub
1. Buka browser dan pergi ke repository GitHub.
2. Pilih tab "Compare and Pull requests".
3. Tampilan akan sebagai berikut:
5. Feature terbaru untuk membaca file csv sudah ditambahkan
6. Dokumentasi dari latihan ini menggunakan README dimana file dibuat pada github. Agar file tersebut juga tersipan pada local komputer perlu melakukan metode pull request. Pertama aktifkan brach utama dengan perintah berikut:
 ```bash
  git checkout main
  ```
7. Setelah brach main aktif, lakukan perintah berikut pada terminal lokal
 ```bash
  git pull
  ```

## Kesimpulan
Dalam latihan ini, kita belajar tentang dasar-dasar penggunaan Git dan GitHub. Langkah-langkahnya mencakup membuat repository di GitHub, mengunduhnya ke komputer lokal, membuat perubahan pada file Python, membuat cabang baru, melakukan commit dan push, membuka pull request di GitHub, dan menggabungkan perubahan dari cabang fitur ke cabang master/main. Ini adalah langkah-langkah dasar yang dapat membantu kita memahami cara menggunakan Git dan GitHub untuk mengelola proyek perangkat lunak secara efisien.
