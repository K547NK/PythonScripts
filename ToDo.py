import time
timestr = time.strftime("%Y&m%d-%H")

#Simple ToDo List
topList = ('**********Less is More**********')
endlist = ('**********End of List**********')

#Simple ToDo List

def list_one():
   print (topList)
   item1 = input('1:')
   item2 = input('2:')
   item3 = input('3:')
   item4 = input('4:')
   item5 = input('5:')

file_handler = input('Append to What file[daily/master]:')

if file_handler == 'daily':
   writer = open(timestr.txt,'a')
   writer.write(list_one)  

elif file_handler == 'master':
   master = open('ToDo_Masterfile.txt'.'a')
   master.write(list_one)

else:
   print(endList)
   print ('program exiting goodbye')
 

   
