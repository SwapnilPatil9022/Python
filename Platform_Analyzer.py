import sys
import os
import psutil
import socket
import platform
import time
import datetime
import wmi


#This is Platform Analyser Which Shows Our Platform Specification 

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    return "%d:%02d" % (hour, minutes)

def main():

    Date= str(datetime.date.today())
    Time_t1 = time.localtime()
    current_time = str(time.strftime("%H-%M-%S",Time_t1))

    current_time1 = str(time.strftime("%H:%M:%S",Time_t1))
    filename=str(str(current_time)+str(Date)) 
    File1= open( str(filename +".txt"),"w")

    Device_Name =str(socket.gethostname())
    Machine_Type = str(platform.machine())
    Processor_Name =str(platform.processor())
    Platform_Type =str(platform.platform())
    OS_Name=str(platform.system())
    Architecture= str(platform.architecture())
    OS_Version =str(platform.version())    

    Total_Ram=str(((psutil.virtual_memory().total)/1000000000))
    Used_Ram=str(((psutil.virtual_memory().used)/1000000000))
    Available_Ram=str(((psutil.virtual_memory().available)/1000000000))    

    User_name =str(os.getlogin())

    Total_Cores = str( psutil.cpu_count())
    Logical_Cores=str(psutil.cpu_count(logical=True))
    Physical_Cores=str(psutil.cpu_count(logical=False))

    battery = psutil.sensors_battery()


    print("-----------------WelCome to System Analyser By Swapnil Patil-----------------\n")
    File1.write("-----------WelCome to System Analyser By Swapnil Patil-----------\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Current Date of Creating File:                            "+ Date + "\n")
    File1.write("Current Time of Creating File:                            "+ current_time1 +"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Device  Related Information \n")
    File1.write("Device Name:                                             "+  Device_Name+"\n")
    File1.write("User Name:                                               "+User_name+"\n")    
    File1.write("Architecture:                                            "+Architecture+"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Processor Related Information \n")
    File1.write("Machine Type:                                            "+Machine_Type+"\n")
    File1.write("processor Name:                                          "+ Processor_Name+"\n")
    File1.write("Platform Type:                                           "+ Platform_Type+"\n")
    File1.write("Operating system Name:                                   "+OS_Name+"\n")
    File1.write("Operating System Version:                                "+ OS_Version+"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Cores Related Information \n")
    File1.write("Total Number of Cores:                                   "+Total_Cores +"\n")
    File1.write("Total Number of Logical Cores:                           "+Logical_Cores +"\n")
    File1.write("Total Number of Physical Cores:                          "+Physical_Cores +"\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Ram Related Information \n")
    File1.write("Total Size of Ram:                                       "+Total_Ram + "GB\n")
    File1.write("Used  Ram:                                               "+ Used_Ram + "GB\n")
    File1.write("Available Ram:                                           "+ Available_Ram+ "GB\n")
    File1.write("-----------------------------------------------------------------------------\n")
    File1.write("Battery Related Information \n")    
    File1.write("Battery percentage :                                     " + str(battery.percent) +"\n")
    File1.write("Power plugged in :                                       " + str(battery.power_plugged)+"\n")
    File1.write("Battery left(Hours:Minutes) :                            " + str(convert(battery.secsleft))+"\n")

    File1.write("-----------------------------------------------------------------------------\n")

    print("-------------------------------------------------------------------------------")
    print("----------------Your PlatForm Details Are Successsfully Analyzed---------------")
    print("-------------------------------------------------------------------------------")
    print("-----------------Thank you For Using PlatForm Analyzer-------------------------")
    File1.write("------------------Thank you For Using PlatForm Analyzer------------------\n")
    File1.write("------------------------PPA AANI  LB CHI PUNYAYI-------------------------\n") 


if __name__ == "__main__":
    main()

    