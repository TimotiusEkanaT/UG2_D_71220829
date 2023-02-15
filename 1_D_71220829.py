print ("=============== MAKANAN ===============")
print ("1. Telur Bakar          : Rp 7.000")
print ("2. Lele Terbang Mas Bhe : Rp 10.000")
print ("3. Es Coklat Lempu      : Rp 5.000")
print ("4. Es Doger Langensari  : Rp 13.000")

print ("\n==================== PESANAN ====================")
tbdxi = int(input("Telur Bakar                : "))
ltdxi = int(input("Lele Terbang               : "))
ecdxi = int(input("Es Coklat                  : "))
eddxi = int(input("Es Doger                   : "))

print ("\n==================== TOTAL ====================")
print ("TOTAL TELUT BAKAR x ",tbdxi,"            : ","Rp ",tbdxi*7000)
print ("TOTAL LELE TERBANG x ",ltdxi,"           : ","Rp ",ltdxi*10000)
print ("TOTAL ES COKELAT x ",ecdxi,"             : ","Rp ",ecdxi*5000)
print ("TOTAL ES DOGER x ",eddxi,"               : ","Rp ",eddxi*13000)

tbbudd=tbdxi*7000
ltbudd=ltdxi*10000
ecbudd=ecdxi*5000
edbudd=eddxi*13000
shesssss= tbbudd+ltbudd+ecbudd+edbudd
print ("Jumlah total biaya yang harus dibayar adalah Rp ",shesssss)