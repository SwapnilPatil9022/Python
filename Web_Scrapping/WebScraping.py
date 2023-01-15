import bs4
import requests

def Web_Scrapping(url_path):
    res = requests.get(url_path)

    print(type(res))

    # print(res.text)

    soup = bs4.BeautifulSoup(res.text)
    print(type(soup))

    title = soup.select('title')
    print(title[0].getText())

    print("Title is ")
    print(title[0].getText())

    arr = soup.select(".mw-headline")

    for element in arr:
        print(element.text)

def main():
    URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    Web_Scrapping(URL)

if __name__ == "__main__":
    main()
