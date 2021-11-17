from gauss import gauss_menu
from trapezoidal import trapezoidal
from regresi import regresi
from interpolasi import interpolasi

def Opening():
    print('\n\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
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
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def Menu():
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
    pilihan = int(input('Masukkan Angka Menu : '))
    iteration = True
    while iteration :        
        if pilihan == 1:
            gauss_menu()
            iteration = False
        elif pilihan == 2 :
            trapezoidal()
            iteration = False
        elif pilihan== 3 :
            regresi()
            iteration = False
        elif pilihan== 4 :
            interpolasi()
            iteration = False
        elif pilihan== 5 :
            About()
            iteration = False
        elif pilihan == 0 :
            Closing()
            iteration = False
        else :
            print('\n')
            print("Mohon maaf tolong isi pilihan dengan benar!")

def About() :
    print('')
    print('===============================================================================================================')
    print('                 Program ini disusun oleh tiga pemuda dari komponen kecil penyatu bangsa.')
    print('        Komponen-komponen kecil itu berasal dari ayam jago dari timur, kota beribu candi, dan kota hujan')
    print("            Program ini dibuat untuk menghitung penyelesaian masalah matematis dengan metode numerik")
    print('                         Kita paham bahwa program ini masih memiliki kekurangan')
    print('Semoga dengan bantuan user, program ini dapat ditemukan dan diperbaiki agar lebih akurat dan efisien kedepannya')
    print('                     Semoga program ini dapat bermanfaat untuk user yang membutuhkannya')
    print('===============================================================================================================')
    input('\n\nKlik enter untuk kembali ke main menu!!')
    Menu()
    
    
def Lastword():
    print(' ')
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')
    print("  Terimakasih semoga dapat membantu... :)")
    print(' ')
    print('  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def Closing() :
    print('\n\nProgram telah selesai!!')
    print('Dan anda telah mendapatkan solusinya')
    print('Apakah anda ingin keluar porgram ?')
    print('1. Ya')
    print('2. Tidak')
    print('(Masukkan dengan angka 1 atau 2 saja)')
    pilihan_akhir = int(input())
    if pilihan_akhir == 1 :
        Lastword()
    elif pilihan_akhir == 2 :
        print('Menuju ke menu utama...')
        Menu()
    else :
        print('Maaf pilihan anda sepertinya salah')
        print('Silahkan coba kembali!!')
        Closing()