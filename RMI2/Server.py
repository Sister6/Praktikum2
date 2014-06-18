import rpyc
import urllib
from elementtree.ElementTree import parse


class infoCuaca(rpyc.Service):
    def exposed_getRSS(self, url):
        message =''
        
        # get data from XML
        rss = parse(urllib.urlopen(url)).getroot()
        for data in rss.findall('gempa'):
            magnitude = data.find('Magnitude').text
            jumlah = data.find('Jumlah').text
            message = message + 'Magnitude\t: '+magnitude+ ' Jumlah\t: '+jumlah+'\n'
            print'\n---------------'
        return message;
        
# connecting to client
# send class to client
# load client from connecting function
from rpyc.utils.server import ThreadedServer
temp = ThreadedServer(infoCuaca, port = 5000)
temp.start()

