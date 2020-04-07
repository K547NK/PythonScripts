#Importing pour necessary libraries and declaring them
import time
import datetime
x = datetime.datetime.now()
year =(x.year)
julian =(x.strftime("%j"))
#Create a primary file handling object
primary = open ('data','a')
backup = open('backup','a')
#Prompt User to Add Title and displays date also appends it at the top of list
print ('Today is day '+ str(julian)+' of '+str(year))
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
    if handle == 'done':
        break
        print ('updating records')
else:
    print('records updated')

