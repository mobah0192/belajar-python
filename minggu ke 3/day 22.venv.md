Ringkasan Hari 22


1.Virtual environment mengisolasi library setiap proyek, supaya tidak saling bentrok versi.
2.python -m venv venv membuat virtual environment baru (folder venv).
3.venv\Scripts\activate (di Windows) mengaktifkan virtual environment.
4.Tanda virtual environment aktif: muncul (venv) di depan baris terminal.
5.deactivate untuk keluar dari virtual environment.
6.Virtual environment cukup dibuat sekali, setelah itu tinggal diaktifkan lagi setiap mau kerja di proyek itu.
7.Lupa mengaktifkan virtual environment sebelum install library akan membuat library masuk ke instalasi Python global/utama.
8.Folder venv biasanya tidak perlu ikut dibagikan/diunggah ke orang lain (akan dibahas lebih lanjut di materi Git).
9. virtual environment: seperti kamar kos terpisah untuk setiap penghuni (proyek).
10.Perintah virtual environment dijalankan lewat terminal, bukan ditulis di dalam file .py.