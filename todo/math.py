#importing system libraries
import os
import time
import platform
import glob

# Auto detect system platform
get_os = platform.system()
print('runnin on '+ get_os)

#Defining a funtction that for a vanilla install that is 
def fresh():
  directory = input('enter path for working directory:')
  home = os.path.expanduser(directory)
  os.chdir(home)
  cwd = os.getcwd()
  settings =  open('list_settings','a')
  settings.write(str(cwd))
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
    print ('N at '+str(n)+' M at '+str(m))
    print ('curse is broken')
    files.write('\n curse is broken \n')
    break
#
def rem():
  reader = open (remember,'r')
  print ('writing to' + reader.readline())
  directory = str(reader.readline())
  home = os.path.expanduser(directory)
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
    print ('N at '+str(n)+' M at '+str(m))
    print ('curse is broken')
   files.write('\n curse is broken \n')
   break

memory = glob.glob('/home/**/**/list_settings',recursive = True)
remember = (str(memory)[2:-2])

if memory == True:
   print(remember)
else:
    print ('nothing to see')

