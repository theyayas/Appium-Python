import csv

with open('email-password-recovery-code.csv') as fileKita:
    reader = csv.reader(fileKita, delimiter = ';')  #csv.DictReader = membuat baris pertama pada file menjadi keyword setiap data (nama, alamat, dsb)
    for baris in reader:
        #print(baris)
        print(baris[5])