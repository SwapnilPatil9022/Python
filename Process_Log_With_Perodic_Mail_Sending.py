# """ ----------- Process Log With Auto Mail Sender Application ---------------"""

#=================================================
# Required Python Packages
#=================================================
import os
import time 
import psutil
import urllib2
import smtplib
import schedule
from sys import *
from email.mime.text import MIMEText
form email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#=================================================
# Function name : is_connected
# Description : is_connected function check the internet connection.
# Author : Swapnil Ashok Patil
# Date : 01/01/2023
#=================================================
def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142',timeout = 1)
        return True
    except urllib2.URLError as err:
        return False

#=================================================
# Function name : MailSender
# Description : In MailSender function fill the details of sender and reciver and message etc.
# Author : Swapnil Ashok Patil
# Date : 01/01/2023
#=================================================
def MailSender(filename,time):
    try:
        fromaddr = "swapnilpatil46118@gmail.com"
        toaddr = "devapukale929@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome.
        Please find attached document which contains Log of Running process.
        Log file is created at : %s 

        This is auto gennerated mail.

        Thanks & Regards,
        Swapnil Ashok Patil
        """%(toaddr,time)

        Subject = """

        Process log generated at : %s
        """%(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))

        attachment = open(filename,"rb")

        p = MIMEBAse('application','octel-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment; filename= %s" %filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr,"xvfxeadltnyzbnoj")

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file successfully send to mail")

    except Exception as E:
        print("Unable to send mail.",E)

#=================================================
# Function name : ProcessLog
# Description : ProcessLog function create the new file on current Directory. 
# Author : Swapnil Ashok Patil
# Date : 01/01/2023
#=================================================
def ProcessLog(log_dir = 'Marvellous'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass


    separator = "-"*80

    log_path = os.path.join(log_dir,"MarvellousLog%s.log" %(time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Process Logger : "+time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except (psutil..NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for elements in listprocess:
        f.write("%s\n % element")

    print("Log file is successfully generated at location %s",%(log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path,time.ctime())
        endTime = time.time()

        print('Took %s secounds to send mail' %(endTime - startTime))
    else:
        print("There is no internet connect")

#=================================================
# Function name : main
# Description : Main function from where execution starts
# Author : Swapnil Ashok Patil
# Date : 01/01/2023
#=================================================
def main():
    print("-----Process Logger by Swapnil Patil-----")

    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used log record of running processess")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Absolutepath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

#=================================================
# Application starter
#=================================================
if __name__ == "__main__":
    main()
