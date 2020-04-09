#Importing pour necessary libraries and declaring them
import time
import datetime
import os
#working directory handling
home = os.path.expanduser('~')
os.chdir(home)
#settings directoru handling
settings = open ('list_settings','a')
settings.write(str(home))

#date handling
x = datetime.datetime.now()
year =(x.year)
julian =(x.strftime("%j"))
#Create a primary file handling object
primary = open ('data','a')
backup = open('backup','a')
#Prompt User to Add Title and displays date also appends it at the top of list
print ('Today is day '+ str(julian)+' of '+str(year))
print ('type done() when done')
title = input('Title:')
primary.write('\n  Day '+str(julian) + ' of '+str(year)+'\n')
backup.write('\n  Day '+str(julian) + ' of '+str(year)+'\n')
backup.write('\n          '+title+'\n')
primary.write('\n          '+title+'\n')
#defining our "infinite loop variables"
m = 1
asterisk = (': ')
#Adding "Infinite Loop"
while m < 1000 :
    #Defining our input variable in a continuous loop
    handle = input('*:')
    primary.write(str(m)+asterisk+ handle +'\n')
    backup.write(str(m)+asterisk+ handle +'\n')
    m = m+1
    if handle == 'done()':
        break
        time,sleep(1)
        print ('updating records')
        time.sleep(1)
        print('All done good to go')
else:
    print('records updated')

