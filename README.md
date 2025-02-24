Assignment 2 - Samsung Innovation Campus Batch 6

Kode Kelompok: UNI174

Nama Kelompok: RPP

Di dalam proyek ini kami membuat 2 program dengan script micropython dan python yang telah disambungkan ke rangkaian IoT yang telah kami buat, 2 sensor yang kami pakai adalah sensor PIR (Motion Sensor) dan DHT11 (Sensor Temperatur dan Kelembapan). Script micropython tersebut mengirimkan data sensor kepada platform ubidots yang memiliki suatu dashboard yang menampilkan data yang telah dikirim. Script python satunya berfungsi untuk mengirim data tersebut melewati API service yang dihubungkan dengan database mongoDB.

File:
1. ASS2.py
   -  File python tersebut merupakan script micropython yang berfungsi untuk mengambil dari ESP32, sensor PIR serta DHT11 dan mengirimkan data tersebut ke Ubidots untuk divisualisasikan serta Flask API untuk menghubungkan ke database.
  
2. DATABASE.py
   -  File python tersebut berfungsi untuk menerima data yang telah dikirim ke Flask API oleh main.py dan menyimpan data tersebut pada database MongoDB.
  
Link Video:
https://youtu.be/JphvP_Ej5-8

Link Foto:
https://drive.google.com/drive/folders/1P0QLlErj2-NH8KF38XqOW3Jh79qKgXc_?usp=sharing
