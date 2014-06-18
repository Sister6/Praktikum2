import rpyc

class client():
    def start(self):
        self.connecting()
    
    # function connecting
    # connect to server
    # load function from connection to getData
    def connecting(self):
        client.server = rpyc.connect('localhost',5000, config = {'allow_public_attrs':True})
        self.getData()
        

    def getData(self):
        print "Informasi Gempa Indonesia tahun 2012"
        print "Pilih bulan gempa (0-4)"
        print "0 untuk semua"
        var = input("Input : ")
        print "Harap Tunggu.... "
        if var == 0:
            url = 'http://data.bmkg.go.id/statistiksrgempa2012.xml'
        elif var == 1:
            url = 'http://data.bmkg.go.id/statistiksrgempa2012-01.xml'
        elif var == 2:
            url = 'http://data.bmkg.go.id/statistiksrgempa2012-02.xml'
        elif var == 3:
            url = 'http://data.bmkg.go.id/statistiksrgempa2012-03.xml'
        elif var == 4:
            url = 'http://data.bmkg.go.id/statistiksrgempa2012-04.xml'
        
        # call function in server
        informasiCuaca = client.server.root.getRSS(url)
        info = informasiCuaca
        print info
        
# start client program
temp = client()
temp.start()