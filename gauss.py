import numpy as np
from script import Menu, Closing

def gauss_menu():
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
    iteration = True
    while iteration:
        if pilihan_gauss == "1":
            gauss_1()
            iteration = False
        elif pilihan_gauss == "2" :
            gauss_2()
            iteration = False
        elif pilihan_gauss == "3" :
            gauss_3()
            iteration = False
        elif pilihan_gauss == "4":
            Menu()
            iteration = False
        elif pilihan_gauss == "0" :
            Closing()
            iteration = False
        else:
            print('\n\n')
            print("Mohon maaf tolong isi pilihan dengan benar!")

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
        Menu()

    elif tanya_input == "4":
        Closing()
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
        Menu()

    elif tanya_input == "2":
        Closing()
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
        Menu()

    elif tanya_input == "4":
        Closing()
    else :
        print(' ')
        print("Mohon maaf tolong isi pilihan dengan benar!")
        gauss_3()