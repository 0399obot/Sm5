import os,time,sys,shutil
from warn.warn import *

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print(f"""{kun}
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••       
	    ;	S P A M  S M S - C A L L  ;          0399obot
   		;---------------------------;    Xplorteks'xX
     	;     Project  :  Setiaji   ;
	   	                               2021
 IG  :   https://instagram.com/setiaji.ios
  WEB:   http://actslowly.6te.net
••••••••••••••••••••••••••••••••••••••••••••••••••••••••
{kan}
•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
Notice:Tools ini hanya dapat digunakan menggunakan Number Indonesia
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
•••
1. Call Gratis 3×
•••••••••••••
2. CALL Verifikasi
•••••••••••••••••••
{kun}""")
		pilih=int(input('setiaji/> '))

		if pilih == 1:
			import src.callw
		elif pilih == 2:
			import src.call
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/Sm5/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
