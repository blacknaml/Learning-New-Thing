#!/usr/bin/python

from __future__ import print_function

def main():
    # membuat prompt untuk tipe integer
    bilbulat = int(raw_input("Masukan bilangan bulat: "))

    # menggunakan variabel untuk melakukan perhitungan
    hasil = bilbulat + 1

    # menampilkan nilai variabel
    print("Bilangan yang dimasukkan adalah %d" % bilbulat)
    print("%d + 1 = %d" %(bilbulat, hasil))

if __name__ == "__main__":
    main()
