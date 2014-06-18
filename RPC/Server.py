import urllib
import xml.etree.ElementTree as ET
from SimpleXMLRPCServer import SimpleXMLRPCServer

global doc
global root
data = []

def get_data(i):
    if i==1:
        url = "http://data.bmkg.go.id/cuaca_dunia_1.xml"
        doc = ET.parse(urllib.urlopen(url))
        root = doc.getroot()
        tanggal = root.find('Tanggal').text
        data.append("Tanggal : " + tanggal)
        data.append("")
        for Row in root.findall('Isi/Row'):
            kota = Row.find('Kota').text
            cuaca = Row.find('Cuaca').text
            suhumin = Row.find('SuhuMin').text
            suhumax = Row.find('SuhuMax').text
            data.append("Kota : " + kota)
            data.append("Cuaca : " + cuaca)
            data.append("Suhu : " + suhumin + " - " + suhumax)
            data.append("")

    elif i==2:
        url = "http://data.bmkg.go.id/cuaca_indo_1.xml"
        doc = ET.parse(urllib.urlopen(url))
        root = doc.getroot()
        for Tanggal in root.findall('Tanggal'):
            mulai = Tanggal.find('Mulai').text
            sampai = Tanggal.find('Sampai').text
            data.append("Tanggal : " + mulai + " - " + sampai)
            data.append("")
        for Row in root.findall('Isi/Row'):
            kota = Row.find('Kota').text
            cuaca = Row.find('Cuaca').text
            suhumin = Row.find('SuhuMin').text
            suhumax = Row.find('SuhuMax').text
            kelembapanmin = Row.find('KelembapanMin').text
            kelembapanmax = Row.find('KelembapanMax').text
            data.append("Kota : " + kota)
            data.append("Cuaca : " + cuaca)
            data.append("Suhu : " + suhumin + " - " + suhumax)
            data.append("Kelembapan : " + kelembapanmin + " - " + kelembapanmax)
            data.append("")

    elif i==3:
        url = "http://data.bmkg.go.id/cuaca_jabodetabek_1.xml"
        doc = ET.parse(urllib.urlopen(url))
        root = doc.getroot()
        tanggal = root.find('Tanggal').text
        data.append("Tanggal : " + tanggal)
        data.append("")
        for Row in root.findall('Isi/Row'):
            daerah = Row.find('Daerah').text
            pagi = Row.find('Pagi').text
            siang = Row.find('Siang').text
            malam = Row.find('Malam').text
            data.append("Daerah : " + daerah)
            data.append("Pagi, Siang, Malam : " + pagi + " , " + siang + " , " + malam)
            data.append("")
            
    elif i==4:
        url = "http://data.bmkg.go.id/cuaca_sulselbar.xml"
        doc = ET.parse(urllib.urlopen(url))
        root = doc.getroot()
        for Tanggal in root.findall('Tanggal'):
            mulai = Tanggal.find('Mulai').text
            sampai = Tanggal.find('Sampai').text
            data.append("Tanggal : " + mulai + " - " + sampai)
            data.append("")
        for Row in root.findall('Isi/Row'):
            kota = Row.find('Kota').text
            cuaca = Row.find('Cuaca').text
            suhumin = Row.find('SuhuMin').text
            suhumax = Row.find('SuhuMax').text
            kelembapanmin = Row.find('KelembapanMin').text
            kelembapanmax = Row.find('KelembapanMax').text
            data.append("Kota : " + kota)
            data.append("Cuaca : " + cuaca)
            data.append("Suhu : " + suhumin)
            data.append("Kelembapan : " + kelembapanmin + " - " + kelembapanmax)
            data.append("")
   
    elif i==5:
        url = "http://data.bmkg.go.id/Maritim_Cuaca_Jalur_Penyebrangan.xml"
        doc = ET.parse(urllib.urlopen(url))
        root = doc.getroot()
        pubdate = root.find('pubDate').text
        data.append("Tanggal Publish : " + pubdate)
        data.append("")
        for Row in root.findall('Isi/Row'):
            fromdate = Row.find('fromDate').text
            todate = Row.find('toDate').text
            wilayah = Row.find('Wilayah').text
            arahangin = Row.find('Arah_Angin').text
            cuaca = Row.find('Cuaca').text
            kecangin = Row.find('Kec_Angin').text
            anginknot = Row.find('Angin_Knot').text
            gelombang = Row.find('Gelombang').text
            idjalur = Row.find('ID_Jalur').text
            jalur = Row.find('Jalur').text
            data.append("Tanggal : " + fromdate + " - " + todate)
            data.append("Wilayah : " + wilayah)
            data.append("Arah Angin : " + arahangin)
            data.append("Cuaca : " + cuaca)
            data.append("Kecepatan Angin : " + kecangin)
            data.append("Knot Angin : " +anginknot)
            data.append("Gelombang : " +gelombang)
            data.append("ID Jalur : " +idjalur)
            data.append("Jalur : " +jalur)
            data.append("")
            
    return data
        
server = SimpleXMLRPCServer(("localhost", 8000))
print ("Listening on port 8000 ...")
server.register_function(get_data, "get_data")
server.serve_forever()