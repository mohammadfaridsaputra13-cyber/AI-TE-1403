def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

data = list(map(int, input(
    "Masukkan data (pisahkan dengan spasi): "
).split()))

target = int(input("Masukkan target yang dicari: "))

hasil = linear_search(data, target)

print("\n===== HASIL LINEAR SEARCH =====")
print("Data   :", data)
print("Target :", target)

if hasil != -1:
    print("Hasil  : Ditemukan pada index", hasil)
else:
    print("Hasil  : Data tidak ditemukan")
