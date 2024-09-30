def kemungkinan_minimum(nominal: list[int], nilai: int) -> list[int]:
    total_nilai = nilai
    hasil = []

    for denom in reversed(nominal):
        while total_nilai >= denom:
            total_nilai -= denom
            hasil.append(denom)

    return hasil

nominal = [1, 2, 5, 10]
print("Nominal mata uang yang tersedia: ", nominal)

nilai = input("Masukkan jumlah angka yang ingin ditukar: ").strip()

try:
    nilai = int(nilai)

    if nilai <= 0:
        print("Nilai tidak bleh nol atau negatif.")
    else:
        hasil = kemungkinan_minimum(nominal, nilai)
        print("Jumlah koin minimal yang dikeluarkan adalah", len(hasil))  # Fixed here
        print(" ".join(map(str, hasil)))

except ValueError:
    print("Input harus berupa angka valid.")
