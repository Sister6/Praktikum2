import Pyro4
import urllib2
from xml.etree import ElementTree as ET

class ParserServer:
    def __init__(self):
        print "Listening...."
        
    def getData(self):
        pilihan = raw_input('Pilih XML yang akan di parse : ')
        data = []
        f = []
        if(pilihan == 1):
            f = urllib2.urlopen('http://data.bmkg.go.id/alamatstasiun.xml')
        elif(pilihan == 2):
            f = urllib2.urlopen('http://data.bmkg.go.id/aviation_id.xml')
        elif(pilihan == 3):
            f = urllib2.urlopen('http://data.bmkg.go.id/cuaca_wisata.xml')
        elif(pilihan == 4):
            f = urllib2.urlopen('http://data.bmkg.go.id/daerah_gelombang_tinggi.xml')
        elif(pilihan == 5):
            f = urllib2.urlopen('http://data.bmkg.go.id/gempaterkini.xml')
        xml = ET.fromstring(f.read())
        root = xml.getroot()
        for node in root:
            data.append(node.tag, node.text)
        return data  

url = ParserServer()    
daemon = Pyro4.Daemon()
nameserver = Pyro4.locateNS()
uri = daemon.register(url)
nameserver.register("rmi",uri)
print "Ready for Remote Object."
daemon.requestLoop()