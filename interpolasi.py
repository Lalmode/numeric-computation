import numpy as np
import matplotlib.pyplot as plt
import csv
from script import Opening, Menu, About, Closing, Lastword
from gauss import gauss_1, gauss_2, gauss_3

def interpolasi() :
    print(' ')
    print('MAIN MENU > METODE INTERPOLASI METODE POLINOM NEWTON')
    print('======================================================')
    n_polinom = int(input('Masukkan nilai derajat interpolasi: '))
    print(' ')
    print('Berikut adalah metode input yang dapat dipilih')
    print('1. Secara manual')
    print('2. Input melalui file')
    print('3. Kembali ke main menu')
    print('4. Closing')
    tanya_input = input('Masukkan pilihan metode input : ')
    if tanya_input == "1":
        print(' ')
        N = int(input('Masukkan Nilai N: '))
        x = []
        y = []
        for _ in range(N):
            x.append(float(input('Masukkan Nilai x (berurutan): ')))
        print(' ')
        for _ in range(N):
            y.append(float(input('Masukkan Nilai y (berurutan): ')))
        n_polinom = n_polinom + 1
        ST = [[0 for j in range(n_polinom)] for i in range(N)]
        for i in range(N):
            ST[i][0] = y[i]
        for j in range(1, n_polinom):
            for i in range(N - j):
                ST[i][j] = (ST[i + 1][j - 1] - ST[i][j - 1]) / (x[i + j] - x[i])
    elif tanya_input == "2":
        x = []
        y = []

        with open("Data_Input_Interpolasi_Polinom.txt", "r") as csvfile:
            next(csvfile)
            inter_pol = csv.reader(csvfile, delimiter="\t")
            for row in inter_pol:
                x.append(float(row[0]))
                y.append(float(row[1]))

        n_polinom = n_polinom + 1
        ST = [[0 for j in range(n_polinom)] for i in range(len(x))]
        for i in range(len(x)):
            ST[i][0] = y[i]
        for j in range(1, n_polinom):
            for i in range(len(x) - j):
                ST[i][j] = (ST[i + 1][j - 1] - ST[i][j - 1]) / (x[i + j] - x[i])

    elif tanya_input == "3":
        Menu()
    elif tanya_input == "4":
        quit()
    else:
        print(' ')
        print("Mohon maaf tolong isi pilihan dengan benar!")
        interpolasi()

    print(' ')
    print('Berikut adalah beberapa command selanjutnya : ')
    print('1. Hitung nilai taksiran')
    print('2. Tidak perlu')
    tanya_taksiran = input('Bagaimana pilihan command anda ? ')
    if tanya_taksiran == "1":
        print(' ')
        x_soal = float(input('Masukkan nilai x yang ingin ditaksir f(x)-nya: '))
        jumlah = ST[0][0]
        for i in range(1, n_polinom):
            suku = ST[0][i]
            for j in range(i):
                suku = suku * (x_soal - x[j])
            jumlah = jumlah + suku
        y_jawab = jumlah
        print(' ')
        print('Berikut adalah beberapa command selanjutnya : ')
        print('1. Tampilkan solusi')
        print('2. Simpan solusi dalam file')
        tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
        if tanya_solusi == "1":
            print('Nilai Taksiran f(x)-nya adalah : ', y_jawab)

        elif tanya_solusi == "2":
            f = open("Solusi_Interpolasi_Polinom.txt", "w+")
            f.write("Solusi interpolasi polinom : ")
            f.write(str(y_jawab))
            f.close()

        print(' ')
        print('Berikut adalah beberapa command dengan plot yang dihasilkan : ')
        print('1. Tampilkan plot')
        print('2. Simpan gambar dalam file')
        print('3. Tidak perlu')
        tanya_plot = input('Bagaimana pilihan command anda tekait hasil interpolasi ? ')
        if tanya_plot == "1":
            print(' ')
            N = 100
            x_min = float(input('Masukkan nilai batas x minimum : '))
            x_max = float(input('Masukkan nilai batas x maksimum : '))
            y_min = float(input('Masukkan nilai batas y minimum : '))
            y_max = float(input('Masukkan nilai batas y maksimum : '))
            x_plot = [0 for i in range(N)]
            y_plot = [0 for i in range(N)]
            for ii in range(N):
                x_plot[ii] = ((x_max - x_min) / N) * ii + x_min
                jumlah = ST[0][0]
                for i in range(1, n_polinom):
                    suku = ST[0][i]
                    for j in range(i):
                        suku = suku * (x_plot[ii] - x[j])
                    jumlah = jumlah + suku
                y_plot[ii] = jumlah
            fig, ax = plt.subplots()
            plt.suptitle('Grafik Interpolasi Polinom Newton')
            ax.plot(x, y, 'ro', label='data')
            ax.plot(x_soal, y_jawab, 'bs', label='titik estimasi')
            ax.plot(x_plot, y_plot, "g", label='garis interpolasi ')
            ax.legend()
            plt.xlabel("x")
            plt.ylabel("f(x) = y")
            plt.axis([x_min, x_max, y_min, y_max])
            plt.show()

        if tanya_plot == "2":
            print(' ')
            N = 100
            x_min = float(input('Masukkan nilai batas x minimum : '))
            x_max = float(input('Masukkan nilai batas x maksimum : '))
            y_min = float(input('Masukkan nilai batas y minimum : '))
            y_max = float(input('Masukkan nilai batas y maksimum : '))
            x_plot = [0 for i in range(N)]
            y_plot = [0 for i in range(N)]
            for ii in range(N):
                x_plot[ii] = ((x_max - x_min) / N) * ii + x_min
                jumlah = ST[0][0]
                for i in range(1, n_polinom):
                    suku = ST[0][i]
                    for j in range(i):
                        suku = suku * (x_plot[ii] - x[j])
                    jumlah = jumlah + suku
                y_plot[ii] = jumlah
            fig, ax = plt.subplots()
            plt.suptitle('Grafik Interpolasi Polinom Newton')
            ax.plot(x, y, 'bo', label='data')
            ax.plot(x_soal, y_jawab, 'ys', label='titik estimasi')
            ax.plot(x_plot, y_plot, "r", label='garis interpolasi')
            ax.legend()
            plt.xlabel("x")
            plt.ylabel("f(x) = y")
            plt.axis([x_min, x_max, y_min, y_max])
            plt.savefig('Grafik_Interpolasi.pdf')

    if tanya_taksiran == "2":
        print(' ')
        print('Berikut adalah beberapa command dengan plot yang dihasilkan : ')
        print('1. Tampilkan plot')
        print('2. Simpan gambar dalam file')
        print('3. Tidak perlu')
        tanya_plot = input('Bagaimana pilihan command anda tekait hasil interpolasi ? ')
        if tanya_plot == "1":
            print(' ')
            N = 100
            x_min = float(input('Masukkan nilai batas x minimum : '))
            x_max = float(input('Masukkan nilai batas x maksimum : '))
            y_min = float(input('Masukkan nilai batas y minimum : '))
            y_max = float(input('Masukkan nilai batas y maksimum : '))
            x_plot = [0 for i in range(N)]
            y_plot = [0 for i in range(N)]
            for ii in range(N):
                x_plot[ii] = ((x_max - x_min) / N) * ii + x_min
                jumlah = ST[0][0]
                for i in range(1, n_polinom):
                    suku = ST[0][i]
                    for j in range(i):
                        suku = suku * (x_plot[ii] - x[j])
                    jumlah = jumlah + suku
                y_plot[ii] = jumlah
            fig, ax = plt.subplots()
            plt.suptitle('Grafik Interpolasi Polinom Newton')
            ax.plot(x, y, 'bo', label='data')
            ax.plot(x_plot, y_plot, "r", label='garis interpolasi')
            ax.legend()
            plt.xlabel("x")
            plt.ylabel("f(x) = y")
            plt.axis([x_min, x_max, y_min, y_max])
            plt.show()

        if tanya_plot == "2":
            print(' ')
            N = 100
            x_min = float(input('Masukkan nilai batas x minimum : '))
            x_max = float(input('Masukkan nilai batas x maksimum : '))
            y_min = float(input('Masukkan nilai batas y minimum : '))
            y_max = float(input('Masukkan nilai batas y maksimum : '))
            x_plot = [0 for i in range(N)]
            y_plot = [0 for i in range(N)]
            for ii in range(N):
                x_plot[ii] = ((x_max - x_min) / N) * ii + x_min
                jumlah = ST[0][0]
                for i in range(1, n_polinom):
                    suku = ST[0][i]
                    for j in range(i):
                        suku = suku * (x_plot[ii] - x[j])
                    jumlah = jumlah + suku
                y_plot[ii] = jumlah
            fig, ax = plt.subplots()
            plt.suptitle('Grafik Interpolasi Polinom Newton')
            ax.plot(x, y, 'bo', label='data')
            ax.plot(x_plot, y_plot, "r", label='garis interpolasi')
            ax.legend()
            plt.xlabel("x")
            plt.ylabel("f(x) = y")
            plt.axis([x_min, x_max, y_min, y_max])
            plt.savefig('Grafik_Interpolasi.pdf')