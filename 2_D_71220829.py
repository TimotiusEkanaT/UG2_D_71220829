piipa = (input('Masukkan Nomor Telepon : '))

if piipa[0:4] == ("0816") :
    print ("\nAnda menggunakan Indosat")
elif piipa[0:4] == ("0814") :
    print ("\nAnda menggunakan Telkomsel")
else :
    print ("\nOperator anda tidak diketahui")

akhu = int(piipa)
if akhu %2 == 0:
    print ("Nomor anda berakhiran genap")
else :
    print ("Nomor anda berakhiran ganjil")
