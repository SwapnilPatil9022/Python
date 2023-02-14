"""
            --------- Auto Downloader using Automation python -----------
    Automation script which downloads specific file and store into the current directory of application.
"""

#=================================================
# Required Python Packages
#=================================================
import requests
import re
from urllib.parse import urlparse
from sys import*
import os

#=================================================
# Function name : is_downloadable
# Description : is_downloadable function is find the url and download the data.
# Author : Swapnil Ashok Patil
# Date : 10/01/2023
#=================================================
def is_downloadable(url):
	h = requests.head(url, allow_redirects = True)
	header = h.headers
	content_type = header.get('content-type')
	if 'text' in content_type.lower():
		return False
	if 'html' in content_type.lower():
		return False
	return True

#=================================================
# Function name : get_filename_from_cd
# Description : get_filename_from_cd function is phach the file.
# Author : Swapnil Ashok Patil
# Date : 10/01/2023
#=================================================
def get_filename_from_cd(cd):
	a = urlparse(cd)
	return os.path.basename(a.path)

#=================================================
# Function name : Download_Data
# Description : Download_Data function read the file and download data.
# Author : Swapnil Ashok Patil
# Date : 10/01/2023
#=================================================
def Download_Data(url):
	allowed = is_downloadable(url)

	if allowed:
		try:
			res = requests.get(url, allow_redirects = True)
			res.raise_for_status()
			filename = get_filename_from_cd(url)
			fd = open(filename, "wb")

			for buffer in res.iter_content(1024):
				fd.write(buffer)

			fd.close()
			return True
		except Exception as E:
			return False
	else:
		return False

#=================================================
# Function name : main
# Description : Main function from where execution starts
# Author : Swapnil Ashok Patil
# Date : 04/01/2023
#=================================================
def main():
	print("-----Downloader using Automation by Swapnil Patil-----")

	print("Application name : "+argv[0])

	if (len(argv) == 2):    
	    if (argv[1] == "-h") or (argv[1] == "-H"):
		        print("This Script is used to traverse specific directory")
		        exit()

	    if (argv[1] == "-u") or (argv[1] == "-U"):
		        print("usage : ApplicationName AbsolutePath_of_Directory")
		        exit()

    # URL : this is link for download data
	url = 'https://www.google.com/favicon.ico'

	result = Download_Data(url)

	if result:
	    print("File successfully downloader")
	else:
	    print("Failed to download")

#=================================================
# Application starter
#=================================================
if __name__ == "__main__":
    main()