#NIM        :   13519199
#Kelas      :   04
#Nama file  :   tucil2_13519199.py
#Deskripsi  :   Tugas Kecil 2 Strategi Algortima IF2211 - Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)

#Kamus
from collections import defaultdict

#Deskripsi
matkul= defaultdict()
listkata = [] 
prereq = [] 
output = [] 
bool = defaultdict()
utama1 = []
i = 1
j = 0

#Membaca File Luar
f = open("namafile.txt", "r") #file yang akan dibaca
f1 = f.readlines()


#Algorritma
for word in f1:
    listkata.append(word.strip().replace(".", "").replace(" ", "").split(",")) #urut
    utama = listkata[0] #paling depan
    prereq = listkata[1:] #prereq 
    
for words in f1:
    listkata1 = words.strip().replace(".", "").replace(" ", "").split(",") #pecah list
    utama1.append(listkata1[0]) #dijadikan urut
    utama2 = listkata1[0] #dipecah satu-per-satu
    bool[utama2] = False

for vertex in listkata : 
    matkul[vertex[0]] = [] #jika tidak ditunujuk
        
for j in range(len(listkata)) : #jika menunjuk
    if(len(listkata[j]) > 1) : #mulai dari list[1]
        for i in range(1,len(listkata[j])): #cari matkul yang mengandung C1
            matkul[listkata[j][i]].append(listkata[j][0]) #j adalah baris, append dgn selain list[0]

def topology_sort(graph): #topografi
    if not bool[graph]: 
        bool[graph] = True
        for graph2 in matkul[graph]:
            topology_sort(graph2)
        output.insert(0, graph)        

for graph in bool: #mencari semua hasil
    topology_sort(graph)

for k in range(len(matkul)):
    print("Semester {} : {}".format(k+1, output[k]))
