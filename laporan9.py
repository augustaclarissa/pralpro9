#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Dictionary

'''Seorang guru TK ingin mengajari murid-muridnya macam macam warna pada buah, maka dari itu Ia membuat kamus
hanya dengan memasukkan kata kunci buah dan warnanya, dengan format (nama buah : warna)'''

#input : nama buah : warna
#proses : membuat dictionary kosong, membuat perulangan untuk output
#output : nama buah berwarna x

kamus = dict()
kamus = {'manggis' : 'ungu', 'durian' : 'hijau', 'strawberry' : 'merah'}
for key in kamus:
    print("buah", key, "berwarna", kamus[key])