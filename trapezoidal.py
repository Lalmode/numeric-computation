import numpy as np


def trapezoidal() :
    print(' ')
    print('MAIN MENU > METODE TRAPEZOIDAL')
    print('===============================================')
    print('Berikut adalah metode input yang dapat dipilih')
    print('1. Secara manual')
    print('2. Input melalui file')
    print('3. Kembali ke main menu')
    print('4. Closing')
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