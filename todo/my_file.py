import os
import glob
import time

#This is section will only find list_settings  and print its location
settingsLocation = glob.glob('/home/**/listSettings', recursive = True)

print('Settings location\n:'+str(settingsLocation)[2:-2]+'\n')

#Modify working directory using listSettings parameters

dirSwitchInput = (str(settingsLocation)[2:-14])

switchDirectory = os.chdir(dirSwitchInput)

getCurrentWD = os.getcwd() #the new working directory

print('Operating from\n:'+getCurrentWD+'\n')

