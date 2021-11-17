import numpy as np
import matplotlib.pyplot as plt
import csv
from script import Opening, Menu, About, Closing, Lastword
from gauss import gauss_1, gauss_2, gauss_3

def regresi() :
    print(' ')
    print('MAIN MENU > METODE REGRESI')
    print('===============================================')

    def f(a, b, x):
        return a + b * x

    def rumus_regresi():
        print(' ')
        print('Berikut adalah metode input yang dapat dipilih')
        print('1. Secara manual')
        print('2. Input melalui file')
        print('3. Kembali ke main menu')
        print('4. Closing')
        tanya_input = input('Masukkan pilihan metode input : ')
        if tanya_input == "1" :
            print(' ')
            N = int(input('Masukkan Batas Jumlah Data : '))
            x = []
            y = []
            for _ in range(N):
                x.append(float(input('Masukkan nilai x (berurutan) : ')))
            for _ in range(N):
                y.append(float(input('Masukkan nilai y (berurutan) : ')))
            n = len(x)
            x_total = 0
            y_total = 0
            x_sq_total = 0
            xy_total = 0
            for i in range(n):
                x_total = x_total + x[i]
                y_total = y_total + y[i]
                x_sq_total = x_sq_total + x[i] * x[i]
                xy_total = xy_total + x[i] * y[i]

            b = (n * xy_total - x_total * y_total) / (n * x_sq_total - (x_total) * x_total)
            a = y_total / n - b * x_total / n

        elif tanya_input == "2" :
            x = []
            y = []

            with open("Data_Input_Regresi.txt", "r") as csvfile:
                next(csvfile)
                regresi = csv.reader(csvfile, delimiter="\t")
                for row in regresi:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
            n = len(x)
            x_total = 0
            y_total = 0
            x_sq_total = 0
            xy_total = 0
            for i in range(n):
                x_total = x_total + x[i]
                y_total = y_total + y[i]
                x_sq_total = x_sq_total + x[i] * x[i]
                xy_total = xy_total + x[i] * y[i]

            b = (n * xy_total - x_total * y_total) / (n * x_sq_total - (x_total) * x_total)
            a = y_total / n - b * x_total / n

            print('\nInputan data melalui file telah berhasil terbaca')

        elif tanya_input == "3" :
            Menu()

        elif tanya_input == "4":
            Closing()
        else:
            print(' ')
            print("Mohon maaf tolong isi pilihan dengan benar!")
            rumus_regresi()

        def perintah_1():
            print(' ')
            print('Berikut adalah beberapa command selanjutnya : ')
            print('1. Tampilkan solusi')
            print('2. Simpan solusi dalam file')
            tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
            if tanya_solusi == "1":
                print(' ')
                print('fungsi hasil regresi : y = ', a, '+', b, 'x')

            elif tanya_solusi == "2":
                f = open("Solusi_Regresi.txt", "w+")
                f.write("Solusi fungsi regresi : ")
                f.write("\n")
                f.write('y = ')
                f.write(str(a))
                f.write(' + ')
                f.write(str(b))
                f.write('x')
                f.close()

            else:
                print(' ')
                print("Mohon maaf tolong isi pilihan dengan benar!")
                perintah_1()

        perintah_1()
        def perintah_2():
            print(' ')
            print('Berikut adalah beberapa command selanjutnya : ')
            print('1. Hitung nilai taksiran')
            print('2. Tidak perlu')
            print('3. Kembali ke menu sebelumnya')
            tanya_taksiran = input('Bagaimana pilihan command anda ? ')
            if tanya_taksiran == "1":
                print(' ')
                x_soal = float(input("Masukkan nilai x: "))
                y_jawab = f(a, b, x_soal)
                print("Nilai perkiraan y untuk x = ", x_soal, " adalah : ", y_jawab)
                def perintah_3() :
                    print('')
                    print('Berikut adalah beberapa command dengan plot yang dihasilkan : ')
                    print('1. Tampilkan plot')
                    print('2. Simpan gambar dalam file')
                    print('3. Tidak perlu')
                    tanya_plot = input('Bagaimana pilihan command anda tekait hasil interpolasi ? ')
                    if tanya_plot == "1":
                        print(' ')
                        N = 100
                        x_plot = [0 for i in range(N)]
                        y_plot = [0 for i in range(N)]
                        for i in range(N):
                            x_plot[i] = (1.5 / 100.0) * i
                            y_plot[i] = f(a, b, x_plot[i])
                        fig, ax = plt.subplots()
                        ax.plot(x, y, 'ro', label='data')
                        ax.plot(x_soal, y_jawab, 'bs', label='titik yang diestimasi')
                        ax.plot(x_plot, y_plot, 'g', label='garis regresi')
                        ax.legend()
                        plt.suptitle('Grafik Regresi')
                        plt.xlabel("x")
                        plt.ylabel("f(x) = y")
                        plt.show()
                        Closing()

                    elif tanya_plot == "2":
                        print(' ')
                        N = 100
                        x_plot = [0 for i in range(N)]
                        y_plot = [0 for i in range(N)]
                        for i in range(N):
                            x_plot[i] = (1.5 / 100.0) * i
                            y_plot[i] = f(a, b, x_plot[i])
                        fig, ax = plt.subplots()
                        ax.plot(x, y, 'ro', label='data')
                        ax.plot(x_soal, y_jawab, 'bs', label='titik yang diestimasi')
                        ax.plot(x_plot, y_plot, 'g', label='garis regresi')
                        ax.legend()
                        plt.suptitle('Grafik Regresi')
                        plt.xlabel("x")
                        plt.ylabel("f(x) = y")
                        plt.savefig('Grafik_Regresi.pdf')
                        Closing()

                    elif tanya_plot == "3":
                        Closing()
                    else :
                        perintah_3()

                perintah_3()

            if tanya_taksiran == "2":
                def perintah_3() :
                    print(' ')
                    print('Berikut adalah beberapa command dengan plot yang dihasilkan : ')
                    print('1. Tampilkan plot')
                    print('2. Simpan gambar dalam file')
                    print('3. Tidak perlu')
                    print(' ')
                    tanya_plot = input('Bagaimana pilihan command anda tekait hasil interpolasi ? ')
                    print('(Masukkan dengan angka 1,2 atau 3 saja)')
                    if tanya_plot == "1":
                        print(' ')
                        N = 100
                        x_plot = [0 for i in range(N)]
                        y_plot = [0 for i in range(N)]
                        for i in range(N):
                            x_plot[i] = (1.5 / 100.0) * i
                            y_plot[i] = f(a, b, x_plot[i])
                        fig, ax = plt.subplots()
                        ax.plot(x, y, 'ro', label='data')
                        ax.plot(x_plot, y_plot, 'g', label='garis regresi')
                        ax.legend()
                        plt.xlabel("x")
                        plt.ylabel("f(x) = y")
                        plt.show()
                    elif tanya_plot == "2":
                        print(' ')
                        N = 100
                        x_plot = [0 for i in range(N)]
                        y_plot = [0 for i in range(N)]
                        for i in range(N):
                            x_plot[i] = (1.5 / 100.0) * i
                            y_plot[i] = f(a, b, x_plot[i])
                        fig, ax = plt.subplots()
                        ax.plot(x, y, 'ro', label='data')
                        ax.plot(x_plot, y_plot, 'g', label='garis regresi')
                        ax.legend()
                        plt.xlabel("x")
                        plt.ylabel("f(x) = y")
                        plt.savefig('Grafik_Regresi.pdf')
                    elif tanya_plot == "3":
                        Closing()
                    else:
                        print(' ')
                        print("Mohon maaf tolong isi pilihan dengan benar!")
                        perintah_3()

                perintah_3()

            elif tanya_taksiran == "3" :
                perintah_1()

            else:
                print(' ')
                print("Mohon maaf tolong isi pilihan dengan benar!")
                perintah_2()

        perintah_2()

    rumus_regresi()