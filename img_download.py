
#  """------------ Auto Image Downloader using Web Scrapping ---------------"""

#=================================================
# Required Python Packages
#=================================================
from bs4 import *
import requests
import os

#=================================================
# Function name : folder_create
# Description : folder_create function create a current directory
# Author : Swapnil Ashok Patil
# Date : 15/01/2023
#=================================================
def folder_create(images):
    try:
        folder_name = input("Enter Folder Name :-")
        os.mkdir(folder_name)
    except:
        print("Folder Exist with that name!")
        folder_create()

    download_images(images,folder_name)

#=================================================
# Function name : download_images
# Description : download_images function from download the Images.
# Author : Swapnil Ashok Patil
# Date : 15/01/2023
#=================================================
def download_images(images,folder_name):
    count = 0

    print(f"Total {len(images)} Image Found!")

    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]

            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]

                        except:
                            pass


            try:
                r = requests.get(image_link).content
                try:
                    r = str(r,'utf-8')

                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpj","wb+")as f:
                        f.write(r)

                count += 1

            except:
                pass

        if count == len(images):
            print("All Images Downloaded!")
        else:
            print(f"Total {count} Images download Out of {len(images)}")

#=================================================
# Function name : main
# Description : Main function from where execution starts
# Author : Swapnil Ashok Patil
# Date : 15/01/2023
#=================================================
def main():
    print("------Auto_Image_Downloader_using_Web_Scrapping_By Swapnil_Patil-------")

    print("Application name : Auto Image Downloader")

    url = ("https://www.google.com")

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'html.parser')

    images = soup.findAll('img')

    folder_create(images)

#=================================================
# Application starter
#=================================================
if __name__ == "__main__":
    main()








"""
# importing google_images_download module
from google_images_download import google_images_download 

# creating object
response = google_images_download.googleimagesdownload() 

search_queries =['The smartphone also features an in display fingerprint sensor.',
	'The pop up selfie camera is placed aligning with the rear cameras.',
	'''In terms of storage Vivo V15 Pro could offer
	up to 6GB of RAM and 128GB of onboard storage.''',
	'The smartphone could be fuelled by a 3 700mAh battery.',]


def downloadimages(query):
	# keywords is the search query
	# format is the image file format
	# limit is the number of images to be downloaded
	# print urls is to print the image file url
	# size is the image size which can
	# be specified manually ("large, medium, icon")
	# aspect ratio denotes the height width ratio
	# of images to download. ("tall, square, wide, panoramic")
	arguments = {"keywords": query,
				"format": "jpg",
				"limit":4,
				"print_urls":True,
				"size": "medium",
				"aspect_ratio":"panoramic"}
	try:
		response.download(arguments)
	
	# Handling File NotFound Error 
	except FileNotFoundError: 
		arguments = {"keywords": query,
					"format": "jpg",
					"limit":4,
					"print_urls":True, 
					"size": "medium"}
					
		# Providing arguments for the searched query
		try:
			# Downloading the photos based
			# on the given arguments
			response.download(arguments) 
		except:
			pass

# Driver Code
for query in search_queries:
	downloadimages(query) 
	print() 
"""