import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")

print "Pilih data yang ingin dilihat "
print "1. Cuaca Dunia"
print "2. Cuaca Indonesia"
print "3. Cuaca Jabodetabek"
print "4. Cuaca Sulselbar"
print "5. Cuaca Maritim Penyebrangan"
print ""
x = input('Pilih Nomor : ')
data = proxy.get_data(x)
y=0
while y<len(data):
    print data[y]
    y=y+1

