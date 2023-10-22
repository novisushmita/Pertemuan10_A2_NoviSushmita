# membuat matriks menggunakan perulangan sesuai inputan
m = int(input("masukkan jumlah kolom : "))
n = int(input("masukkan jumlah baris : "))
x = [0]*m 
for i in range(m): 
    x[i] = [1]*n
    print(x)