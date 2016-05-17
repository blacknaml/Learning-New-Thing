#!/usr/bin/python

from __future__ import print_function

def main():
    # membuat prompt untuk tipe data string
    s = raw_input('Masukan bilangan bulat: ')

    # melakukan konversi dari tipe string ke integer
    bilbulat = int(s)

    # menggunakan variabel untuk melakukan perhitungan
    hasil = bilbulat + 1

    # menampilkan nilai variabel
    print("Bilangan yang dimasukan adalah %d" % bilbulat)
    print("%d + 1 = %d" % (bilbulat, hasil))

if __name__ == "__main__":
    main()
