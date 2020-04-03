#adding a date function
import datetime
x = datetime.datetime.now()
year =(x.year)
julian =(x.strftime("%j"))

#List Decoration
top_sec = ('**********Less is More**********')
end_sec = ('**********End of List**********')

print (top_sec)
#data entry section
print ('Today is day '+ str(julian))
item1 = input('1:')
item2 = input('2:')
item3 = input('3:')
item4 = input('4:')
item5 = input('5:')
#end data entry section

print (end_sec)

def daily_handler():
    writer = open('daily.txt','a')
    writer.write('Daily\n')
    writer.write('\n1.'+item1)
    writer.write('\n2.'+item2)
    writer.write('\n3.'+item3)
    writer.write('\n4.'+item4)
    writer.write('\n5.'+item5)

def master_handler():
    master = open('masterfile.txt','a')
    master.write('\n')
    master.write('\n  Day '+str(julian) + ' of '+str(year))
    master.write('\n1.'+item1)
    master.write('\n2.'+item2)
    master.write('\n3.'+item3)
    master.write('\n4.'+item4)
    master.write('\n5.'+item5)

file_handler = input('1.Write to Daily\n2.Append to Master\n:')

if file_handler == '1':
    daily_handler()
    master_handler()
    print('updating records..')
elif file_handler == '2':
    print("Master Only")
    master_handler()

else:
    print(endList)
    print ('program exiting goodbye')



