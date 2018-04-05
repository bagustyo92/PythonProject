import sys

def menu1():
	parameter = 1
	while (parameter == 1) :
		print "\n+++++++++++++++++++++++++++++"
		print "MAU ITUNG ITUNG APA ENTE GAN?"
		print "++++++++++++++++++++++++++++++"
		print "1. Penjumlahan"
		print "2. Pengurangan"
		print "3. Perkalian"
		print "4. Pembagian"
		print "5. Back to main"
		print "++++++++++++++++++++++++++++++\n"
		
		pilih = input ("Silahkan dipilih gan ")
		if pilih == 1 :
			x = input ("Angka Pertama	")
			y = input ("Angka Kedua	")
			z = x + y
			print "Hasilnya adalah ", float(z)
		if pilih == 2 :
			x = input ("Angka Pertama	")
			y = input ("Angka Kedua	")
			z = x - y
			print "Hasilnya adalah ", float(z)
		if pilih == 3 :
			x = input ("Angka Pertama	")
			y = input ("Angka Kedua	")
			z = x * y
			print "Hasilnya adalah ", float(z)
		if pilih == 4 :
			x = input ("Angka Pertama	")
			y = input ("Angka Kedua	")
			z = x / y
			print "Hasilnya adalah ", float(z)
		if pilih == 5 :
			parameter = 0
		else :
			pilihan = raw_input ("\nApakah ingin kembali menghitung? [y/n] = ")
			if (pilihan == "y") :
				parameter = 1
			elif (pilihan == "n") :
				parameter = 0
	main()

def menu2():
	pilihan = 1
	nama = []
	while pilihan == 1 :
		isi = raw_input ("Masukan nama yang ingin disimpan ")
		nama.append(isi)

		print "\nApakah ingin menambah nama? [y/n]"
		pilih = sys.stdin.readline()
		if pilih.strip() == "y" :
			pilihan = 1
		elif pilih.strip() == "n" :
			pilihan = 0
			print "\nData anda telah disimpan kedalam List Python"

	pilihan = 1
	while pilihan == 1 :
		print "\n++++++++++++++++++++++++++"
		print "DATABASE NAMA pake LIST"
		print "++++++++++++++++++++++++++"
		print "1. Tampilkan seluruh nama"
		print "2. KAPITAL"
		print "3. Membuat alamat email"
		print "4. Simpan ke dalam .txt"
		print "5. Buka database"
		print "6. Kembali ke menu"
		print "++++++++++++++++++++++++++"

		menu = input ("\nSilahkan dipilih gan ")
		if menu == 1 :
			print "\nHASIL :"
			print "\n".join(nama)
			raw_input("\nPencet dimana ajalah ")
		if menu == 2 :
			print "\nHASIL :"
			for i in range(len(nama)):
				print nama[i].upper()
			raw_input("\nPencet dimana ajalah ")
		if menu == 3 :
			print "\nHASIL :"
			for i in range(len(nama)):
				print "%s@ub.ac.id"%nama[i]
			raw_input("\nPencet dimana ajalah ")
		if menu == 4 :
			simpan = open("Database.txt","w")
			simpan.write("Nama yang disimpan :\n")
			for i in range(len(nama)):
				simpan.write(nama[i].upper())
				simpan.write("\n")
			simpan.write("\nAlamat email yang digunakan :\n")
			for i in range(len(nama)):
				simpan.write("%s@ub.ac.id\n"%nama[i])
			simpan.close()
			print"\nSELAMAT CUY data berhasil disimpan"
		if menu == 5 :
			simpan = open("Database.txt", "r")
			print simpan.read()
			raw_input("")
		else :
			pilihan = 0

	main()

def main():
	parameter = 1
	while (parameter == 1) :
		print "\n++++++++++++++++++++++++++"
		print "APLIKASI TUGAS SISTER NIH"
		print "++++++++++++++++++++++++++"
		print "1. Itung-itunganih gan"
		print "2. Database with LIST"
		print "3. Contoh Aplikasi ..."
		print "4. Exit"
		print "++++++++++++++++++++++++++\n"
		pilih = input ("Silahkan dipilih gan ")

		if pilih == 1 :
			menu1()
		if pilih == 2 :
			menu2()
		else :
			parameter = 0

	print "Terima Kasih Telah Gunain Aplikasi Tugas Ane Gan"

if __name__ == "__main__":main()