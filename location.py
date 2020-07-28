from bs4 import BeautifulSoup
import requests as req
import colorama
from colorama import Fore,Back,Style
colorama.init()
enc = 'utf-8'
print('----------HaCkLoCaTiOn_v_1.0----------')
password=input(b'\xd0\x92\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xbb\xd0\xb8\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb7\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xba\xd0\xbb\xd1\x8e\xd1\x87: '.decode(enc)).strip()
def get_location():
 while True:
  bssid=input('\n' + b'\xd0\x92\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5 BSSID: '.decode(enc)).strip().replace(' ','').replace(':','').upper()
  if bssid=='0' or bssid=='exit' or bssid=='e' or bssid=='s' or bssid=='q':
   break
  response=req.get("https://mobile.maps.yandex.net/cellid_location/?wifinetworks="+bssid+":-65&app=ymetro")
  soup=BeautifulSoup(response.text,'lxml')
  if(soup.error!=None):
   print(Fore.RED+b'\xd0\x9e\xd1\x88\xd0\xb8\xd0\xb1\xd0\xba\xd0\xb0: \xd0\xbd\xd0\xb5 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xbe\xd1\x81\xd1\x8c \xd0\xbd\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb8 \xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f!'.decode(enc)+Style.RESET_ALL)
   file_log=open('log.txt','a+',encoding='utf-8')
   file_log.write('BSSID:'+bssid+';'+'LOCATION:'+'NOT_FOUND\n')
   file_log.close()
   file_current=open('current.txt','w+',encoding='utf-8')
   file_current.write('BSSID:'+bssid+';\n'+'LOCATION:'+'NOT_FOUND\n')
   file_current.close()
  else:
   print(Fore.GREEN+b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f \xd0\xb1\xd1\x8b\xd0\xbb\xd0\xbe \xd1\x83\xd1\x81\xd0\xbf\xd0\xb5\xd1\x88\xd0\xbd\xd0\xbe \xd0\xbd\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xbe!'.decode(enc)+Style.RESET_ALL)
   sKey,mKey,eKey='latitude=','longitude=','nlatitude='
   location=str(soup.coordinates).replace('"','').strip()
   location=location[location.find(sKey)+len(sKey):location.find(eKey)-1].replace(mKey,'').strip().split()
   mapLink="https://yandex.ru/maps/?mode=search&text="+location[0]+"%2C"+location[1]+"&z=16"
   response=req.get(mapLink)
   soup=BeautifulSoup(response.text,'lxml')
   adress=str(soup.find("div","toponym-card-title-view__description").text)
   description=soup.find("div","card-encyclopedia-view__description _collapsed")
   if description:
    description=str(description.text)
   else:
    description='NONE'
   wikiLink=soup.find("a","card-encyclopedia-view__source")
   if wikiLink:
    wikiLink=str(wikiLink.get('href').strip().replace(' ','_'))
   else:
    wikiLink='NONE'
   file_log=open('log.txt','a+',encoding='utf-8')
   file_log.write('BSSID:'+bssid+';'+'LOCATION:'+' '.join(location)+';'+'ADRESS:'+adress+';'+'DESCRIPTION:'+description+';'+'MAP:'+mapLink+';'+'WIKI:'+wikiLink+';\n')
   file_log.close()
   file_current=open('current.txt','w+',encoding='utf-8')
   file_current.write('BSSID:'+bssid+';\n'+'LOCATION:'+' '.join(location)+';\n'+'ADRESS:'+adress+';\n'+'DESCRIPTION:'+description+';\n'+'MAP:'+mapLink+';\n'+'WIKI:'+wikiLink+';\n')
   file_current.close()
   print(b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82 \xd1\x83\xd1\x81\xd0\xbf\xd0\xb5\xd1\x88\xd0\xbd\xd0\xbe \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd1\x91\xd0\xbd \xd0\xb2 '.decode(enc)+Fore.GREEN+'current.txt.'+Style.RESET_ALL)
 print(b'\xd0\xa1\xd0\xbf\xd0\xb0\xd1\x81\xd0\xb8\xd0\xb1\xd0\xbe \xd0\xb7\xd0\xb0 \xd0\xb8\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 HackLocation v 1.0 by ald15!'.decode(enc) +'\n')
 return 0
def get_password():
 response=req.get("https://bit.ly/30WfrPd")
 soup=BeautifulSoup(response.text,'lxml')
 keys=soup.find("textarea","textarea").text.split()
 return keys
def compare_password(pas):
 passwords=get_password()
 if passwords.count(pas)==1:
  get_location()
 else:
  print(Fore.RED+b'\xd0\x9b\xd0\xb8\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb7\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xba\xd0\xbb\xd1\x8e\xd1\x87 \xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd, \xd0\xbf\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb1\xd1\x83\xd0\xb9\xd1\x82\xd0\xb5 \xd0\xb4\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb9!'.decode(enc)+Style.RESET_ALL)
compare_password(password)
ex=input(b'\xd0\xa7\xd1\x82\xd0\xbe\xd0\xb1\xd1\x8b \xd0\xb2\xd1\x8b\xd0\xb9\xd1\x82\xd0\xb8, \xd0\xbd\xd0\xb0\xd0\xb6\xd0\xbc\xd0\xb8\xd1\x82\xd0\xb5 Enter...'.decode(enc))
