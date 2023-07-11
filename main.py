# Membuat bentuk Persegi
print("Membuat bentuk Persegi")
for i in range(5):
    print("*"*5)

# Membuat segitiga
print("Membuat segitiga")
for i in range(5):
    print("*" * i)

# Membuat segitiga sama kaki
print("Membuat segitiga sama kaki")
baris = 5
for i in range(1, baris):
    print(" " * (baris - 1) + "*" * i + "*" * (i - 1))
    baris -= 1