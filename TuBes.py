import numpy as np
import matplotlib.pyplot as plt
import csv

def opening():
    print('\n\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  SOFTWARE PENGHITUNG METODE NUMERIK KOMPUTASI')
    print('-------------------------------------------------')
    print('Programmer : 1. Lalu Iqbal T (12316025)')
    print('             2. Muhammad Aldi F (12316049)')
    print('             3. Adur (12317045)')
    print('-------------------------------------------------')
    print(' Last Updated: 25 November 2019')
    print(' Contact : aldimfirdaus2@gmail.com')
    print('           lal25uiqbal@gmail.com')
    print('           adurputra@gmail.com')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def main_menu():
    print(' \n\n')
    print('MAIN MENU')
    print('===============================================')
    print('1. Metode Gauss')
    print('2. Metode Trapezoidal')
    print('3. Metode Regresi Kuadrat Terkecil')
    print('4. Metode Interpolasi Polinom Newton')
    print('5. About')
    print('0. Exit')
    print('-----------------------------------------------')
    pilihan_main_menu = input('Masukkan Angka Menu : ')
    if pilihan_main_menu == "1":
        gauss()
    elif pilihan_main_menu == "2" :
        trapezoidal()
    elif pilihan_main_menu == "3" :
        regresi()
    elif pilihan_main_menu == "4" :
        interpolasi()
    elif pilihan_main_menu == "5" :
        about()
    elif pilihan_main_menu == "0" :
        keluar()
    else :
        print('\n')
        print("Mohon maaf tolong isi pilihan dengan benar!")
        main_menu()

def gauss():
    print('\n\n')
    print('MAIN MENU > METODE GAUSS')
    print('===============================================')
    print('1. Sistem Persamaan Linier (SPL) 3 Variabel')
    print('2. SPL 4 Variabel')
    print('3. SPL 5 Variabel')
    print('4. Main Menu')
    print('0. Exit')
    print('-----------------------------------------------')
    pilihan_gauss = input('Masukkan Angka Menu : ')
    if pilihan_gauss == "1":
        gauss_1()
    elif pilihan_gauss == "2" :
        gauss_2()
    elif pilihan_gauss == "3" :
        gauss_3()
    elif pilihan_gauss == "4":
        main_menu()
    elif pilihan_gauss == "0" :
        keluar()
    else:
        print('\n\n')
        print("Mohon maaf tolong isi pilihan dengan benar!")
        gauss()

def gauss_1() :
    print('\n\n')
    print('MAIN MENU > METODE GAUSS > SPL 3 Variabel')
    print('-------------------------------------------')
    print('Berikut adalah metode input yang dapat dipilih')
    print('1. Secara manual')
    print('2. Input melalui file')
    print('3. Kembali ke main menu')
    print('4. Keluar')
    tanya_input = input('Masukkan pilihan metode input : ')
    if tanya_input == "1" :
        a = np.zeros((3, 3))
        b = np.zeros(3)
        print('\nMasukkan koefisien dari persamaan 1, 2, dan 3 secara berurutan ! ')
        for e in range(0, 3):
            for f in range(0, 3):
                a[e][f] = input()
        print('\nMasukkan hasil dari persamaan 1,2, dan 3 ! ')
        for h in range(0, 3):
            b[h] = input()

        [m, n] = a.shape
        a1 = np.zeros((m, n))
        b1 = np.zeros(m)
        for i in range(0, m):
            for j in range(0, n):
                a1[i, j] = a[i, j] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
            b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
        for i in range(1, m):
            for j in range(0, n):
                a1[i, j] = a1[i, j] - a1[0, j]
            b1[i] = b1[i] - b1[0]
        a2 = np.zeros((m, n))
        b2 = np.zeros(m)
        for i in range(0, m):
            for j in range(0, n):
                a2[i, j] = a1[i, j]
            b2[i] = b1[i]
        for i in range(1, m):
            for j in range(0, n):
                a2[i, j] = a1[i, j] * a1[1, 1] * a1[2, 1] / a1[i, 1]
            b2[i] = b1[i] * a1[1, 1] * a1[2, 1] / a1[i, 1]
        for i in range(2, m):
            for j in range(0, n):
                a2[i, j] = a2[i, j] - a2[1, j]
            b2[i] = b2[i] - b2[1]

        print('\nBerikut adalah beberapa command selanjutnya : ')
        print('1. Tampilkan solusi')
        print('2. Simpan solusi dalam file')
        tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
        if tanya_solusi == "1":
            x = np.zeros(m)
            x[2] = b2[2] / a2[2, 2]
            x[1] = [b2[1] - a2[1, 2] * x[2]] / a2[1, 1]
            x[0] = [b2[0] - a2[0, 2] * x[2] - a2[0, 1] * x[1]] / a2[0, 0]

            print('\nSolusi Metode Gauss untuk SPL 3 Variabel sebagai berikut : ')
            print(x)

        elif tanya_solusi == "2":
            x = np.zeros(m)
            x[2] = b2[2] / a2[2, 2]
            x[1] = [b2[1] - a2[1, 2] * x[2]] / a2[1, 1]
            x[0] = [b2[0] - a2[0, 2] * x[2] - a2[0, 1] * x[1]] / a2[0, 0]

            f=open("Solusi_Gauss_SPL3.txt","w+")
            f.write("Solusi Metode Gauss untuk SPL 3 Variabel sebagai berikut : ")
            f.write(str(x))
            f.close()

    elif tanya_input == "2":
        a = np.loadtxt(fname= 'input_koef_3_var.txt')
        b = np.loadtxt(fname= 'input_hasil_3_var.txt')
        [m, n] = a.shape
        a1 = np.zeros((m, n))
        b1 = np.zeros(m)
        for i in range(0, m):
            for j in range(0, n):
                a1[i, j] = a[i, j] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
            b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
        for i in range(1, m):
            for j in range(0, n):
                a1[i, j] = a1[i, j] - a1[0, j]
            b1[i] = b1[i] - b1[0]
        a2 = np.zeros((m, n))
        b2 = np.zeros(m)
        for i in range(0, m):
            for j in range(0, n):
                a2[i, j] = a1[i, j]
            b2[i] = b1[i]
        for i in range(1, m):
            for j in range(0, n):
                a2[i, j] = a1[i, j] * a1[1, 1] * a1[2, 1] / a1[i, 1]
            b2[i] = b1[i] * a1[1, 1] * a1[2, 1] / a1[i, 1]
        for i in range(2, m):
            for j in range(0, n):
                a2[i, j] = a2[i, j] - a2[1, j]
            b2[i] = b2[i] - b2[1]
        print('\nBerikut adalah beberapa command selanjutnya : ')
        print('1. Tampilkan solusi')
        print('2. Simpan solusi dalam file')
        tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
        if tanya_solusi == "1":
            x = np.zeros(m)
            x[2] = b2[2] / a2[2, 2]
            x[1] = [b2[1] - a2[1, 2] * x[2]] / a2[1, 1]
            x[0] = [b2[0] - a2[0, 2] * x[2] - a2[0, 1] * x[1]] / a2[0, 0]

            print('\nSolusi Metode Gauss untuk SPL 3 Variabel sebagai berikut : ')
            print(x)
        elif tanya_solusi == "2":
            x = np.zeros(m)
            x[2] = b2[2] / a2[2, 2]
            x[1] = [b2[1] - a2[1, 2] * x[2]] / a2[1, 1]
            x[0] = [b2[0] - a2[0, 2] * x[2] - a2[0, 1] * x[1]] / a2[0, 0]

            f = open("Solusi_Gauss_SPL3.txt", "w+")
            f.write("Solusi Metode Gauss untuk SPL 3 Variabel sebagai berikut : ")
            f.write(str(x))
            f.close()

    elif tanya_input == "3":
        main_menu()

    elif tanya_input == "4":
        keluar()
    else :
        print(' ')
        print("Mohon maaf tolong isi pilihan dengan benar!")
        gauss_1()

def gauss_2 ():
    print('\n\n')
    print('MAIN MENU > METODE GAUSS > SPL 4 Variabel')
    print('-------------------------------------------')
    print('Berikut adalah metode input yang dapat dipilih')
    print('1. Secara manual')
    print('2. Input melalui file')
    print('3. Kembali ke main menu')
    print('4. Keluar')
    tanya_input = input('Masukkan pilihan metode input : ')
    if tanya_input == "1" :
        m = np.zeros((4, 4))
        n = np.zeros(4)
        print(' ')
        print('Masukkan koefisien dari persamaan 1, 2, 3, dan 4 secara berurutan ! ')
        for e in range(0, 4):
            for f in range(0, 4):
                m[e][f] = input()
        print('Masukkan hasil dari persamaan 1, 2, 3, dan 4 ! ')
        for h in range(0, 4):
            n[h] = input()

        [x, y] = m.shape
        m1 = np.ones((x, y))
        n1 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m1[i, j] = m[i, j] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] / m[i, 0]
            n1[i] = n[i] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] / m[i, 0]
        for i in range(1, x):
            for j in range(0, y):
                m1[i, j] = m1[i, j] - m1[0, j]
            n1[i] = n1[i] - n1[0]

        m2 = np.ones((x, y))
        n2 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j]
            n2[i] = n1[i]
        for i in range(1, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j] * m1[1, 1] * m1[2, 1] * m1[3, 1] / m1[i, 1]
            n2[i] = n1[i] * m1[1, 1] * m1[2, 1] * m1[3, 1] / m1[i, 1]
        for i in range(2, x):
            for j in range(0, y):
                m2[i, j] = m2[i, j] - m2[1, j]
            n2[i] = n2[i] - n2[1]
        m3 = np.ones((x, y))
        n3 = np.ones(x)

        for i in range(0, x):
            for j in range(0, y):
                m3[i, j] = m2[i, j]
            n3[i] = n2[i]
        for i in range(2, x):
            for j in range(0, y):
                m3[i, j] = m2[i, j] * m2[1, 2] * m2[2, 2] * m2[3, 2] / m2[i, 2]
            n3[i] = n2[i] * m2[1, 2] * m2[2, 2] * m2[3, 2] / m2[i, 2]

        for i in range(3, x):
            for j in range(0, y):
                m3[i, j] = m3[i, j] - m3[2, j]
            n3[i] = n3[i] - n3[2]

        print(' ')
        print('Berikut adalah beberapa command selanjutnya : ')
        print('1. Tampilkan solusi')
        print('2. Simpan solusi dalam file')
        tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
        if tanya_solusi == "1":
            sol = np.ones(x)

            sol[3] = n3[3] / m3[3, 3]
            sol[2] = [n3[2] - m3[2, 3] * sol[3]] / m3[2, 2]
            sol[1] = [n3[1] - m3[1, 3] * sol[3] - m3[1, 2] * sol[2]] / m3[1, 1]
            sol[0] = [n3[0] - m3[0, 3] * sol[3] - m3[0, 2] * sol[2] - m3[0, 1] * sol[1]] / m3[0, 0]

            print("Solusi Metode Gauss untuk SPL 4 Variabel sebagai berikut : ")
            print(sol)

        elif tanya_solusi == "2":
            sol = np.ones(x)

            sol[3] = n3[3] / m3[3, 3]
            sol[2] = [n3[2] - m3[2, 3] * sol[3]] / m3[2, 2]
            sol[1] = [n3[1] - m3[1, 3] * sol[3] - m3[1, 2] * sol[2]] / m3[1, 1]
            sol[0] = [n3[0] - m3[0, 3] * sol[3] - m3[0, 2] * sol[2] - m3[0, 1] * sol[1]] / m3[0, 0]

            f = open("Solusi_Gauss_SPL4.txt", "w+")
            f.write("Solusi Metode Gauss untuk SPL 3 Variabel sebagai berikut : ")
            f.write(sol)
            f.close()

    elif tanya_input == "2":
        m = np.loadtxt(fname= 'input_koef_4_var.txt')
        n = np.loadtxt(fname= 'input_hasil_4_var.txt')
        [x, y] = m.shape
        m1 = np.ones((x, y))
        n1 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m1[i, j] = m[i, j] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] / m[i, 0]
            n1[i] = n[i] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] / m[i, 0]
        for i in range(1, x):
            for j in range(0, y):
                m1[i, j] = m1[i, j] - m1[0, j]
            n1[i] = n1[i] - n1[0]

        m2 = np.ones((x, y))
        n2 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j]
            n2[i] = n1[i]
        for i in range(1, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j] * m1[1, 1] * m1[2, 1] * m1[3, 1] / m1[i, 1]
            n2[i] = n1[i] * m1[1, 1] * m1[2, 1] * m1[3, 1] / m1[i, 1]
        for i in range(2, x):
            for j in range(0, y):
                m2[i, j] = m2[i, j] - m2[1, j]
            n2[i] = n2[i] - n2[1]
        m3 = np.ones((x, y))
        n3 = np.ones(x)

        for i in range(0, x):
            for j in range(0, y):
                m3[i, j] = m2[i, j]
            n3[i] = n2[i]
        for i in range(2, x):
            for j in range(0, y):
                m3[i, j] = m2[i, j] * m2[1, 2] * m2[2, 2] * m2[3, 2] / m2[i, 2]
            n3[i] = n2[i] * m2[1, 2] * m2[2, 2] * m2[3, 2] / m2[i, 2]

        for i in range(3, x):
            for j in range(0, y):
                m3[i, j] = m3[i, j] - m3[2, j]
            n3[i] = n3[i] - n3[2]

        print(' ')
        print('Berikut adalah beberapa command selanjutnya : ')
        print('1. Tampilkan solusi')
        print('2. Simpan solusi dalam file')
        tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
        if tanya_solusi == "1":
            sol = np.ones(x)

            sol[3] = n3[3] / m3[3, 3]
            sol[2] = [n3[2] - m3[2, 3] * sol[3]] / m3[2, 2]
            sol[1] = [n3[1] - m3[1, 3] * sol[3] - m3[1, 2] * sol[2]] / m3[1, 1]
            sol[0] = [n3[0] - m3[0, 3] * sol[3] - m3[0, 2] * sol[2] - m3[0, 1] * sol[1]] / m3[0, 0]

            print("Solusi Metode Gauss untuk SPL 4 Variabel sebagai berikut : ")
            print(sol)

        elif tanya_solusi == "2":
            sol = np.ones(x)

            sol[3] = n3[3] / m3[3, 3]
            sol[2] = [n3[2] - m3[2, 3] * sol[3]] / m3[2, 2]
            sol[1] = [n3[1] - m3[1, 3] * sol[3] - m3[1, 2] * sol[2]] / m3[1, 1]
            sol[0] = [n3[0] - m3[0, 3] * sol[3] - m3[0, 2] * sol[2] - m3[0, 1] * sol[1]] / m3[0, 0]

            f = open("Solusi_Gauss_SPL4.txt", "w+")
            f.write("Solusi Metode Gauss untuk SPL 3 Variabel sebagai berikut : ")
            f.write(sol)
            f.close()

    elif tanya_input == "3":
        main_menu()

    elif tanya_input == "2":
        keluar()
    else :
        print(' ')
        print("Mohon maaf tolong isi pilihan dengan benar!")
        gauss_2()

def gauss_3() :
    print('\n\n')
    print('MAIN MENU > METODE GAUSS > SPL 5 Variabel')
    print('-----------------------------------------')
    print('Berikut adalah metode input yang dapat dipilih')
    print('1. Secara manual')
    print('2. Input melalui file')
    print('3. Kembali ke main menu')
    print('4. Keluar')
    tanya_input = input('Masukkan pilihan metode input : ')
    if tanya_input == "1":
        print(' ')
        m = np.zeros((5, 5))
        n = np.ones(5)
        print('Masukkan koefisien dari persamaan 1, 2, 3, 4, dan 5 secara berurutan ! ')
        for e in range(0, 5):
            for f in range(0, 5):
                m[e][f] = input()
        print('\nMasukkan hasil dari persamaan 1, 2, 3, 4, dan 5 ! ')
        for h in range(0, 5):
            n[h] = input()
        # langkah 1
        [x, y] = m.shape
        m1 = np.ones((x, y))
        n1 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m1[i, j] = m[i, j] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] * m[4, 0] / m[i, 0]
            n1[i] = n[i] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] * m[4, 0] / m[i, 0]

        for i in range(1, x):
            for j in range(0, y):
                m1[i, j] = m1[i, j] - m1[0, j]
            n1[i] = n1[i] - n1[0]

        # langkah 2
        m2 = np.ones((x, y))
        n2 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j]
            n2[i] = n1[i]

        for i in range(1, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j] * m1[1, 1] * m1[2, 1] * m1[3, 1] * m1[4, 1] / m1[i, 1]
            n2[i] = n1[i] * m1[1, 1] * m1[2, 1] * m1[3, 1] * m1[4, 1] / m1[i, 1]

        for i in range(2, x):
            for j in range(0, y):
                m2[i, j] = m2[i, j] - m2[1, j]
            n2[i] = n2[i] - n2[1]

        # langkah 3
        m3 = np.ones((x, y))
        n3 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m3[i, j] = m2[i, j]
            n3[i] = n2[i]

        for i in range(2, x):  # idem langkah 1 untuk menghilangkan satu nilai terakhir dari kolom ketiga
            for j in range(0, y):
                m3[i, j] = m2[i, j] * m2[1, 2] * m2[2, 2] * m2[3, 2] * m2[4, 2] / m2[i, 2]
            n3[i] = n2[i] * m2[1, 2] * m2[2, 2] * m2[3, 2] * m2[4, 2] / m2[i, 2]

        for i in range(3, x):
            for j in range(0, y):
                m3[i, j] = m3[i, j] - m3[2, j]
            n3[i] = n3[i] - n3[2]

        # langkah 4
        m4 = np.ones((x, y))
        n4 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m4[i, j] = m3[i, j]
            n4[i] = n3[i]

        for i in range(3, x):
            for j in range(0, y):
                m4[i, j] = m3[i, j] * m3[1, 3] * m3[2, 3] * m3[3, 3] * m3[4, 3] / m3[i, 3]
            n4[i] = n3[i] * m3[1, 3] * m3[2, 3] * m3[3, 3] * m3[4, 3] / m3[i, 3]

        for i in range(4, x):
            for j in range(0, y):
                m4[i, j] = m4[i, j] - m4[3, j]
            n4[i] = n4[i] - n4[3]

        print(' ')
        print('Berikut adalah beberapa command selanjutnya : ')
        print('1. Tampilkan solusi')
        print('2. Simpan solusi dalam file')
        tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
        if tanya_solusi == "1":
            sol = np.ones(x)

            sol[4] = n4[4] / m4[4, 4]
            sol[3] = (n4[3] - m4[3, 4] * sol[4]) / m4[3, 3]
            sol[2] = (n4[2] - m4[2, 4] * sol[4] - m4[2, 3] * sol[3]) / m4[2, 2]
            sol[1] = (n4[1] - m4[1, 4] * sol[4] - m4[1, 3] * sol[3] - m4[1, 2] * sol[2]) / m4[1, 1]
            sol[0] = (n4[0] - m4[0, 4] * sol[4] - m4[0, 3] * sol[3] - m4[0, 2] * sol[2] - m4[0, 1] * sol[1]) / m4[0, 0]

            print(" ")
            print('Solusi Metode Gauss untuk SPL 5 Variabel sebagai berikut : ')
            print(sol)

        elif tanya_solusi == "2":
            sol = np.ones(x)

            sol[4] = n4[4] / m4[4, 4]
            sol[3] = (n4[3] - m4[3, 4] * sol[4]) / m4[3, 3]
            sol[2] = (n4[2] - m4[2, 4] * sol[4] - m4[2, 3] * sol[3]) / m4[2, 2]
            sol[1] = (n4[1] - m4[1, 4] * sol[4] - m4[1, 3] * sol[3] - m4[1, 2] * sol[2]) / m4[1, 1]
            sol[0] = (n4[0] - m4[0, 4] * sol[4] - m4[0, 3] * sol[3] - m4[0, 2] * sol[2] - m4[0, 1] * sol[1]) / m4[0, 0]

            f = open("Solusi_Gauss_SPL5.txt", "w+")
            f.write("Solusi Metode Gauss untuk SPL 5 Variabel sebagai berikut : ")
            f.write("\n")
            f.write(str(sol))
            f.close()

    elif tanya_input == "2" :
        m = np.loadtxt(fname='input_koef_5_var.txt')
        n = np.loadtxt(fname='input_hasil_5_var.txt')
        [x, y] = m.shape
        [x, y] = m.shape
        m1 = np.ones((x, y))
        n1 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m1[i, j] = m[i, j] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] * m[4, 0] / m[i, 0]
            n1[i] = n[i] * m[0, 0] * m[1, 0] * m[2, 0] * m[3, 0] * m[4, 0] / m[i, 0]

        for i in range(1, x):
            for j in range(0, y):
                m1[i, j] = m1[i, j] - m1[0, j]
            n1[i] = n1[i] - n1[0]

        # langkah 2
        m2 = np.ones((x, y))
        n2 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j]
            n2[i] = n1[i]

        for i in range(1, x):
            for j in range(0, y):
                m2[i, j] = m1[i, j] * m1[1, 1] * m1[2, 1] * m1[3, 1] * m1[4, 1] / m1[i, 1]
            n2[i] = n1[i] * m1[1, 1] * m1[2, 1] * m1[3, 1] * m1[4, 1] / m1[i, 1]

        for i in range(2, x):
            for j in range(0, y):
                m2[i, j] = m2[i, j] - m2[1, j]
            n2[i] = n2[i] - n2[1]

        # langkah 3
        m3 = np.ones((x, y))
        n3 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m3[i, j] = m2[i, j]
            n3[i] = n2[i]

        for i in range(2, x):  # idem langkah 1 untuk menghilangkan satu nilai terakhir dari kolom ketiga
            for j in range(0, y):
                m3[i, j] = m2[i, j] * m2[1, 2] * m2[2, 2] * m2[3, 2] * m2[4, 2] / m2[i, 2]
            n3[i] = n2[i] * m2[1, 2] * m2[2, 2] * m2[3, 2] * m2[4, 2] / m2[i, 2]

        for i in range(3, x):
            for j in range(0, y):
                m3[i, j] = m3[i, j] - m3[2, j]
            n3[i] = n3[i] - n3[2]

        # langkah 4
        m4 = np.ones((x, y))
        n4 = np.ones(x)
        for i in range(0, x):
            for j in range(0, y):
                m4[i, j] = m3[i, j]
            n4[i] = n3[i]

        for i in range(3, x):
            for j in range(0, y):
                m4[i, j] = m3[i, j] * m3[1, 3] * m3[2, 3] * m3[3, 3] * m3[4, 3] / m3[i, 3]
            n4[i] = n3[i] * m3[1, 3] * m3[2, 3] * m3[3, 3] * m3[4, 3] / m3[i, 3]

        for i in range(4, x):
            for j in range(0, y):
                m4[i, j] = m4[i, j] - m4[3, j]
            n4[i] = n4[i] - n4[3]

        print(' ')
        print('Berikut adalah beberapa command selanjutnya : ')
        print('1. Tampilkan solusi')
        print('2. Simpan solusi dalam file')
        tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
        if tanya_solusi == "1":
            sol = np.ones(5)

            sol[4] = n4[4] / m4[4, 4]
            sol[3] = (n4[3] - m4[3, 4] * sol[4]) / m4[3, 3]
            sol[2] = (n4[2] - m4[2, 4] * sol[4] - m4[2, 3] * sol[3]) / m4[2, 2]
            sol[1] = (n4[1] - m4[1, 4] * sol[4] - m4[1, 3] * sol[3] - m4[1, 2] * sol[2]) / m4[1, 1]
            sol[0] = (n4[0] - m4[0, 4] * sol[4] - m4[0, 3] * sol[3] - m4[0, 2] * sol[2] - m4[0, 1] * sol[1]) / m4[0, 0]

            print(" ")
            print('Solusi Metode Gauss untuk SPL 5 Variabel sebagai berikut : ')
            print(sol)

        elif tanya_solusi == "2":
            sol = np.ones(x)

            sol[4] = n4[4] / m4[4, 4]
            sol[3] = (n4[3] - m4[3, 4] * sol[4]) / m4[3, 3]
            sol[2] = (n4[2] - m4[2, 4] * sol[4] - m4[2, 3] * sol[3]) / m4[2, 2]
            sol[1] = (n4[1] - m4[1, 4] * sol[4] - m4[1, 3] * sol[3] - m4[1, 2] * sol[2]) / m4[1, 1]
            sol[0] = (n4[0] - m4[0, 4] * sol[4] - m4[0, 3] * sol[3] - m4[0, 2] * sol[2] - m4[0, 1] * sol[1]) / m4[0, 0]

            f = open("Solusi_Gauss_SPL5.txt", "w+")
            f.write("Solusi Metode Gauss untuk SPL 5 Variabel sebagai berikut : ")
            f.write("\n")
            f.write(str(sol))
            f.close()

    elif tanya_input == "3":
        main_menu()

    elif tanya_input == "4":
        keluar()
    else :
        print(' ')
        print("Mohon maaf tolong isi pilihan dengan benar!")
        gauss_3()

def trapezoidal() :
    print(' ')
    print('MAIN MENU > METODE TRAPEZOIDAL')
    print('===============================================')
    print('Berikut adalah metode input yang dapat dipilih')
    print('1. Secara manual')
    print('2. Input melalui file')
    print('3. Kembali ke main menu')
    print('4. Keluar')
    tanya_input = input('Masukkan pilihan metode input : ')
    if tanya_input == "1":
        ll = input('Masukkan batas bawah : ')
        eval_ll = eval(ll)
        ul = input('Masukkan batas atas : ')
        eval_ul = eval(ul)
        N = int(input('Masukkan Jumlah sub-interval : '))

        def rumus_trapezoidal(a, b, N):
            print(' ')
            print('PERHATIAN! Untuk memasukkan fungsi haruslah berurutan')
            print('           Untuk persamaan fungsi numpy gunakan gunakan np.')
            f = lambda x: eval(input('Masukkan persamaan fungsi : '))
            h = np.linspace(a, b, N + 1)
            y = f(h)
            y_right = y[1:]
            y_left = y[:-1]
            dx = (b - a) / N
            T = (dx / 2) * np.sum(y_right + y_left)
            def perintah__1() :
                print(' ')
                print('Berikut adalah beberapa command selanjutnya : ')
                print('1. Tampilkan solusi')
                print('2. Simpan solusi dalam file')
                print('3. Kembali ke menu sebelumnya')
                tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
                if tanya_solusi == "1":
                    print(' ')
                    print('Solusi perhitungan Integral dengan metode trapezoidal dari fungsi diatas : ', T)

                elif tanya_solusi == "2":
                    f = open("Solusi_Trapezoidal.txt", "w+")
                    f.write("Solusi perhitungan Integral dengan metode trapezoidal dari fungsi diatas : ")
                    f.write(str(T))
                    f.close()

                elif tanya_solusi == "3" :
                    trapezoidal()

                else:
                    print(' ')
                    print("Mohon maaf tolong isi pilihan dengan benar!")
                    perintah__1()

            perintah__1()

        rumus_trapezoidal(eval_ll, eval_ul, N)

    elif tanya_input == "2":
        f = lambda x: eval(input('Masukkan persamaan fungsi : '))
        ll = np.loadtxt(fname= 'input_ll.txt')
        ul = np.loadtxt(fname= 'input_ul.txt')
        N = np.loadtxt(fname= 'input_N.txt')

        def rumus_trapezoidal(a, b, N):
            print(' ')
            print('PERHATIAN! Untuk memasukkan fungsi haruslah berurutan')
            print('           Untuk persamaan fungsi numpy gunakan gunakan np.')
            f = lambda x: eval(input('Masukkan persamaan fungsi : '))
            h = np.linspace(a, b, N + 1)
            y = f(h)
            y_right = y[1:]
            y_left = y[:-1]
            dx = (b - a) / N
            T = (dx / 2) * np.sum(y_right + y_left)
            def perintah__1() :
                print(' ')
                print('Berikut adalah beberapa command selanjutnya : ')
                print('1. Tampilkan solusi')
                print('2. Simpan solusi dalam file')
                print('3. Kembali ke menu sebelumnya')
                tanya_solusi = input('Bagaimana command selanjutnya untuk solusi ?')
                if tanya_solusi == "1":
                    print(' ')
                    print('Solusi perhitungan Integral dengan metode trapezoidal dari fungsi diatas : ', T)

                elif tanya_solusi == "2":
                    f = open("Solusi_Trapezoidal.txt", "w+")
                    f.write("Solusi perhitungan Integral dengan metode trapezoidal dari fungsi diatas : ")
                    f.write(str(T))
                    f.close()

                elif tanya_solusi == "3" :
                    trapezoidal()

                else:
                    print(' ')
                    print("Mohon maaf tolong isi pilihan dengan benar!")
                    perintah__1()

            perintah__1()

        rumus_trapezoidal(ll, ul, N)


    else :
        print("Maaf masukkan pilihan dengan benar !")
        trapezoidal()

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
        print('4. Keluar')
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
            main_menu()

        elif tanya_input == "4":
            keluar()
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
                        akhiran()

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
                        akhiran()

                    elif tanya_plot == "3":
                        keluar()
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
                        keluar()
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
    print('4. Keluar')
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
        main_menu()
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



def about() :
    print('')
    print('===============================================================================================================')
    print('                 Program ini disusun oleh tiga pemuda dari komponen kecil penyatu bangsa.')
    print('        Komponen-komponen kecil itu berasal dari ayam jago dari timur, kota beribu candi, dan kota hujan')
    print("            Program ini dibuat untuk menghitung penyelesaian masalah matematis dengan metode numerik")
    print('                         Kita paham bahwa program ini masih memiliki kekurangan')
    print('Semoga dengan bantuan user, program ini dapat ditemukan dan diperbaiki agar lebih akurat dan efisien kedepannya')
    print('                     Semoga program ini dapat bermanfaat untuk user yang membutuhkannya')
    print('===============================================================================================================')

def akhiran() :
    print('\n\nProgram telah selesai!!')
    print('Dan anda telah mendapatkan solusinya')
    print('Apakah anda ingin keluar porgram ?')
    print('1. Ya')
    print('2. Tidak')
    print('(Masukkan dengan angka 1 atau 2 saja)')
    pilihan_akhir = input()
    if pilihan_akhir == "1" :
        keluar()
    if pilihan_akhir == "2" :
        print('Menuju ke menu utama...')
        main_menu()
    else :
        print('Maaf pilihan anda sepertinya salah')
        print('Silahkan coba kembali!!')
        akhiran()

def keluar():
    print(' ')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')
    print("  Terimakasih semoga dapat membantu... :)")
    print(' ')
    print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    quit()

#Program utama
opening()
main_menu()
akhiran()