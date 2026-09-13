Ringkasan Hari 28

1.PostgreSQL adalah database server (berjalan terus di latar belakang), beda dengan SQLite yang cuma satu file.
2.Instalasi PostgreSQL di Windows lewat installer EDB, sudah termasuk PostgreSQL Server, pgAdmin 4, Stack Builder, dan Command Line Tools.
3.psycopg2-binary adalah package Python untuk koneksi ke PostgreSQL (pip install psycopg2-binary).
4.psycopg2.connect(host, database, user, password) dipakai untuk koneksi, butuh info lebih banyak dibanding sqlite3.connect() karena ada sistem keamanan (login).
5.SERIAL PRIMARY KEY di PostgreSQL setara dengan INTEGER PRIMARY KEY di SQLite — sama-sama nomor urut otomatis.
6.Semua perintah SQL dasar (SELECT, INSERT, UPDATE, DELETE, WHERE, ORDER BY, dll) sama persis antara SQLite dan PostgreSQL.
7.pgAdmin adalah GUI bawaan untuk melihat/mengelola database secara visual — klik kanan tabel → "View/Edit Data" → "All Rows" untuk melihat isi data.
8.DBeaver adalah alternatif GUI yang lebih ringan dan modern dibanding pgAdmin.
9.Stack Builder itu opsional — boleh dibatalkan (Cancel) kalau tidak butuh tools tambahan.
10.localhost berarti "server ada di komputer ini sendiri" — nanti bisa diganti alamat server lain kalau database-nya online.