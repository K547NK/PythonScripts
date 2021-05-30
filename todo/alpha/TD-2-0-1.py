#Importing pour necessary libraries and declaring them
import time
import datetime
import os
#working directory handling
settingsDirectory = os.path.expanduser('~/Documents/ToDo/settings/')
home = os.path.expanduser('~/Documents/ToDo/')
#settings directoru handling
settings = open ('/home/nigel/Documents/ToDo/settings/list_settings','a')
settings.write(str(settingsDirectory))
os.chdir(home)
#date handling
x = datetime.datetime.now()
year =(x.year)
julian =(x.strftime("%j"))
#Create a primary file handling object
primary = open ('todo','a')
backup = open('/home/nigel/Documents/ToDo/backup/todo_backup','a')
#backup handling in a separate folder
def _backupTitle_():
    backup.write('\n  Day '+str(julian) + ' of '+str(year)+'\n')
    backup.write('\n          '+title+'\n')
    os.chdir(home)
def _backup_():
    backup.write(str(m)+asterisk+ handle +'\n')
    os.chdir(home)
def _primaryTitle_():
    primary.write('\n  Day '+str(julian) + ' of '+str(year)+'\n')
    primary.write('\n          '+title+'\n')
def _primary_():
    primary.write(str(m)+asterisk+ handle +'\n')
#Prompt User to Add Title and displays date also appends it at the top of list
print ('Today is day '+ str(julian)+' of '+str(year))
print ('type done() when done')
title = input('Title:')
_primaryTitle_()
_backupTitle_()
#defining our "infinite loop variables"
m = 1
asterisk = (': ')
#Adding "Infinite Loop"
while m < 1000 :
    #Defining our input variable in a continuous loop
    handle = input('*:')
    _primary_()
    _backup_()
    m = m+1
    if handle == 'done()':
        time.sleep(1)
        print ('updating records')
        time.sleep(1)
        print('All done good to go')
        break
