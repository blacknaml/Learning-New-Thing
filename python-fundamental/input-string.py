#!/usr/bin/python

from __future__ import print_function

def main():
    # membuat promp untuk tipe data string
    nama = raw_input("Masukkan nama Anda: ")

    # membuat prompt untuk tipe data karakter
    karakter = raw_input("Masukkan sebuah karakter: ")

    # menampilkan nilai variabel
    print("Halo", nama, ", apa kabar?")
    print("Halo %s, apa kabar?" % nama)

    print("Karakter yang dimasukkan: '", karakter, "'")
    print("Karakter yang dimasukkan: '%c'" % karakter)

if __name__ =="__main__":
    main()
