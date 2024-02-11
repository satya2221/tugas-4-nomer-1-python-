uang_masuk=[]
uang_keluar=[]
def sum(arr) :
    total = 0
    for uang in arr : 
        total += uang
    return total

while True :
    print()
    print("Pilih Menu")
    print("1.Masukkan Uang")
    print("2.Keluarkan Uang")
    print("3.Jumlah Uang Masuk") 
    print("4.Jumlah Uang Keluar")
    print("5.Sisa Saldo ")
    print("6.Exit")
    
    pilmenu = input ("pilih Menu:\t")
    
    if pilmenu == "1" :
        uang_masuk_sekarang = int(input("1.Masukan Uang:\t"))
        uang_masuk.append (uang_masuk_sekarang)
        print(f"list uang masuk: {uang_masuk}")
        
    
    elif pilmenu == "2" :
        uang_keluar_sekarang = int(input("2.Keluarkan Uang:\t"))
        uang_keluar.append (uang_keluar_sekarang)
        print(f"list uang keluar: {uang_keluar}")
        
    elif pilmenu == "3" :
        print(f"jumlah uang masuk anda: {sum(uang_masuk)}")
        
    elif pilmenu == "4" :
        print(f"jumlah uang keluar anda: {sum(uang_keluar)}")
        
    elif pilmenu == "5" :
        saldo = sum(uang_masuk) - sum(uang_keluar)
        print(f"Sisa saldo anda: {saldo}")
        
    elif pilmenu == "6" :
        break
    
    else : 
        print ("pilihan tidak tersedia")