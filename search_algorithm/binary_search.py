def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

data = list(map(int, input(
    "Masukkan data (pisahkan dengan spasi): "
).split()))

data.sort()

target = int(input("Masukkan target yang dicari: "))

hasil = binary_search(data, target)

print("\n===== HASIL BINARY SEARCH =====")
print("Data   :", data)
print("Target :", target)

if hasil != -1:
    print("Hasil  : Ditemukan pada index", hasil)
else:
    print("Hasil  : Data tidak ditemukan")
