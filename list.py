try:
	import requests,os,sys
	from bs4 import BeautifulSoup as bs
	if sys.version[0]=="2":
		print ("  Warning(INFO): gunakan python 3.7")
		sys.exit()
	else:pass
except Exception as E:
	print ("  Warning(ERROR): "+str(E))
	sys.exit()
def save(data,file):
	try: os.mkdir("result")
	except: pass
	try:
		open("result/"+str(file),"a").write(str(data)+"\n")
	except Exception as E:
		print ("  Warning(ERROR): "+str(E))
		sys.exit()
	print ("  Warning(INFO): berhasil menyimpan: result/"+file)
def get(url,file,type):
	try:
		s=requests.Session()
		r=s.get(url)
	except requests.exceptions.ConnectionError:
		print ("  Warning(ERROR): koneksi error")
		sys.exit()
	b=bs(r.content,"html.parser")
	print ("\n")
	if type=="baidu":
		for ua in b.findAll("td",{"class":"uas_useragent"}):
			hasil=str(ua).replace('<td class="uas_useragent" colspan="3">','').replace('</td>','')
			save(hasil,file)
	elif type=="chrome":
		for ua in b.findAll("td",{"class":"useragent"}):
			save(ua.text,file)
	elif type=="firefox" or type=="yandex":
		for ua in b.findAll("span",{"class":"code"}):
			save(ua.text,file)
class main:
	def banner(self):
		print ("""
     ╦ ╦┌─┐┌─┐┬─┐  ╔═╗┌─┐┌─┐┌┐┌┌┬┐
     ║ ║└─┐├┤ ├┬┘  ╠═╣│ ┬├┤ │││ │
     ╚═╝└─┘└─┘┴└─  ╩ ╩└─┘└─┘┘└┘ ┴
   {C}odded   : Billal
   {V}ersion  : 0.1
   {G}ithub   : https://github.com/billal1412
   {I}nspirasi: Karjok
================================================
             © 2019 Billal Fauzan
================================================""")
	def menu(self):
		print ("""
  LIST:
    {1}.Baidu Browser
    {2}.Chrome
    {3}.FireFox
    {4}.Yandex Browser""")
	def pil(self):
		print ("\n  Pilih Type Browser ")
		p=input("    root@ua~#> ")
		if p in ["1","01"]:
			url="http://m.webapps-online.com/online-tools/user-agent-strings/dv/browser301264/baidu-browser?"
			print ("  Simpan Useragent ")
			file=input("    root@ua/file#> ")
			get(url,file,"baidu")
		elif p in ["2","02"]:
			url="https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/"
			print ("  Simpan Useragent ")
			file=input("    root@ua/file#> ")
			get(url,file,"chrome")
		elif p in ["3","03"]:
			url="https://www.whatismybrowser.com/guides/the-latest-user-agent/firefox"
			print ("  Simpan Useragent ")
			file=input("    root@ua/file#> ")
			get(url,file,"firefox")
		elif p in ["4","04"]:
			url="https://www.whatismybrowser.com/guides/the-latest-user-agent/yandex-browser"
			print ("  Simpan Useragent ")
			file=input("    root@ua/file#> ")
			get(url,file,"yandex")
main=main()
main.banner()
main.menu()
main.pil()
