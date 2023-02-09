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

    url = ("https://www.amazon.in/s?k=laptop&crid=13FMWB6PBBAUY&sprefix=laptop%2Caps%2C360&ref=nb_sb_noss_1")

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'html.parser')

    images = soup.findAll('img')

    folder_create(images)

#=================================================
# Application starter
#=================================================
if __name__ == "__main__":
    main()
