uihaidug = input ("Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma): ").split()

def henm ():
    shuiii=int(input("Berapa harga barang H&M ?: "))
    if shuiii >= 10000000:
        shuiii*10/100
    elif shuiii >= 25000000:
        shuiii*25/100
    print ("Harga H&M       Rp.     ",shuiii,"  Diskon Rp.", shuiii)

henm()
