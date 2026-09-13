Ringkasan Hari 23

1.Package adalah kode buatan orang lain yang bisa dipasang dan langsung dipakai, tanpa perlu menulis ulang dari nol.
2.pip adalah tool bawaan Python untuk mengelola package.
3.pip install nama_package untuk menginstall package baru.
4.pip uninstall nama_package untuk menghapus package.
5.pip list untuk melihat daftar package yang sudah terinstall.
6.pip freeze > requirements.txt menyimpan daftar package + versinya ke sebuah file.
7.pip install -r requirements.txt menginstall semua package yang tercatat di file itu sekaligus.
8.Sebaiknya package diinstall setelah virtual environment diaktifkan, supaya tidak masuk ke Python global.
9.Setelah pip install, package tetap perlu import di kode Python sebelum bisa dipakai.
10.requirements.txt penting untuk kerja tim — memastikan semua orang pakai versi package yang sama persis.