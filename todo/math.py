import os
import time
home = os.path.expanduser('~')
os.chdir(home)
cwd = os.getcwd()
print(cwd)
n = 50
m = -n
files = open('samples','a')
while n > m :
 print ('N is ' +str(n) )
 files.write('\n''N is '+str(n)+' M is '+ str(m))
 time.sleep(1)
 n-=1
 m+=1
 if n == m:
  print ('N at '+str(n)+' M at '+str(m) )
  break
  print ('curse is broken')
  files.write('\n curse is broken')
