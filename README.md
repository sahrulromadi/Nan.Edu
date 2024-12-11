# Nan.Edu

## Deskripsi

Nan.Edu adalah platform e-learning yang berfokus pada pengembangan pengetahuan dan keterampilan di bidang keuangan. Platform ini dirancang untuk memberikan akses pendidikan yang mudah diakses dan interaktif bagi para penggunanya.

## Fitur

1. Course -> Menyediakan berbagai kursus yang dirancang untuk membantu pengguna memahami konsep-konsep dasar hingga tingkat lanjut dalam bidang keuangan.
2. Quiz -> Fitur ujian interaktif yang memungkinkan pengguna menguji pemahaman mereka tentang materi yang telah dipelajari.
3. Video -> Menyediakan video tutorial dan materi pembelajaran visual yang memudahkan pengguna dalam memahami topik-topik yang dibahas.
4. News -> Menyediakan pembaruan terkini terkait dunia keuangan, termasuk artikel, tips, dan perkembangan terbaru di industri.

## Anggota Kelompok

1. 11054585 PUTRI PUSPITASARI
2. 10747647 SAID ALI M
3. 10190820 BAYU DWI PRASETYO
4. 9964277 RIZKA DIANRANI
5. 11726588 SYIFA SALSABILA
6. 10295760 BENAYA TITUS NATANAEL
7. 10849590 SAHRUL ROMADI
8. 11627401 PUTRI NADILLA MAHARANI

## Langkah-langkah Instalasi

### 1. Clone GitHub

```
git clone https://github.com/sahrulromadi/Nan.Edu.git
cd Nan.Edu
```

### 2. Membuat dan Mengaktifkan Virtual Environment (Disarankan)

```
python -m venv env
env\Scripts\activate
```

### 3. Menginstal Dependensi

```
pip install -r requirements.txt
```

### 4. Konfigurasi

Sebelum menjalankan proyek, Anda perlu menyiapkan pengaturan Anda sendiri. Ubah file `settings.txt` menjadi `settings.py` dan ubah pengaturan yang diperlukan seperti `SECRET_KEY`, `EMAIL_HOST_USER`, dan `EMAIL_HOST_PASSWORD` sesuai dengan informasi Anda.

- Anda dapat mengikuti tutorial berikut untuk menyiapkan email dan mendapatkan kredensial SMTP:
  [Tutorial Setup Email SMTP](https://youtu.be/Mezha1p_dTE?si=6QRiAUFm8K-XDZ5A)

- Anda dapat membuat SECRET_KEY baru menggunakan cara yang dijelaskan di tutorial ini:
  [Tutorial Generate Django Secret Key](https://youtu.be/ZTZvqVJ8RGc?si=ujNe77qiQDo8wnIN)

### 5. Menyiapkan Database

Proyek ini menggunakan SQLite sebagai database default. Untuk mengonfigurasi dan membuat database, jalankan perintah migrasi:

```
python manage.py makemigrations
python manage.py migrate
```

### 6. Konfigurasi Admin dan Django Allauth

- Membuat User Admin: Anda perlu membuat pengguna admin untuk dapat mengakses admin panel Django. Gunakan perintah berikut untuk membuat pengguna admin:

```
python manage.py createsuperuser
```

- Anda harus memasukkan "social application" di Django Admin untuk memungkinkan login menggunakan akun sosial media (Google). Anda bisa menonton tutorial berikut:
  [Tutorial Setup Social Application](https://youtu.be/RyB_wdEZhOwsi=2zDpeoSlsBJuMIe4)

### 7. Menjalankan Server

Setelah semua konfigurasi selesai, Anda dapat menjalankan server lokal untuk mengakses proyek:

```
python manage.py runserver
```
