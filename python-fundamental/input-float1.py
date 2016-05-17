#!/usr/bin/python

from __future__ import print_function

def main():
    # membuat prompt untuk tipe data float
    bilriil = int(raw_input("Masukkan bilangan riil: "))

    # menggunakan variabel untuk melakukan perhitungan
    hasil = bilriil * 2

    # menampilkan nilai variabel
    print("Bilangan yang dimasukkan %.2f" % bilriil)
    print("%f x 2 = %f" % (bilriil, hasil))

if __name__ == "__main__":
    main()
