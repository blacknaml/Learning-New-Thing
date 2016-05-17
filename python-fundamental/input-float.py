#!/usr/bin/python

from __future__ import print_function

def main():
    # membuat prompt untuk tipe data float
    bilriil = float(raw_input("Masukan bilangan riil: "))

    # menggunakan variabel untuk melakukan perhitungan
    hasil = bilriil * 2

    # menampilkan nilai variabel
    print("Bilangan yang dimasukan adalah %f" % bilriil)
    print("%.2f x 2 = %.2f" % (bilriil, hasil))

if __name__ == "__main__":
    main()
