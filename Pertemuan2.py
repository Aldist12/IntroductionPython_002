#Input string
name = input("Masukkan nama lengkap Anda: ")

#Input Integer
age = int(input("Masukkan umur Anda: "))

#Input float
height = float(input("Masukkan tinggi Anda (dalam cm): "))

#Input boolean
bool_python_input = input("Apakah anda suka Python? (iya/tidak): ")
bool_python = bool_python_input.lower() == "iya"

answer = [name, age, height, bool_python]
labels = ["Nama", "Umur", "Tinggi", "Suka Python"]

#Tampilkan hasil tanpa menggunakan perulangan
#print("\n==== Outout Data ====")
#for i in range(len(answer)):
#    print(f"{labels[i]}: {answer[i]}")

#Tampilkan tipe data dari setiap jawaban
#print("\nTipe data dari setiap jawaban:")
#for i in range(len(answer)):
#    print(f"{labels[i]}: {type(answer[i])}")

#Tampilkan hasil tanpa menggunakan perulangan
print("\n==== Outout Data ====")
print(f"{labels[0]} : {answer[0]}")
print(f"{labels[1]} : {answer[1]}")
print(f"{labels[2]} : {answer[2]}")
print(f"{labels[3]} : {answer[3]}")

#Tampilkan tipe data dari setiap jawaban
print("\nTipe data dari setiap jawaban:")
print(f"{labels[0]} : {type(answer[0])}")
print(f"{labels[1]} : {type(answer[1])}")
print(f"{labels[2]} : {type(answer[2])}")
print(f"{labels[3]} : {type(answer[3])}")

