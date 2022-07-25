#Getting to know urllib module.

import urllib.request
import json

#finding format and making file
def make_file(url):
    number = []
    item = '/'
    for index,elem in enumerate(list(url)):
        if elem == item:
            number.append(index)
    return url[max(number)+1:]

#another way of finding format
# if url.find('/'):
#   print(url.rsplit('/',1)[1])


def downloader_with_extra_stuff():
    print("1: Html Format ")
    print("2: Json Format ")
    print("3: Download File")
    print("4: Url Info")
    flag = int(input("Please select: "))

    try:
        # Html
        if flag == 1:
            request_url = urllib.request.urlopen('https://httpbin.org/html')
            data = request_url.read()
            print(data)

        # json
        elif flag == 2:
            with urllib.request.urlopen('https://httpbin.org/json') as url:
                data = json.loads(url.read().decode())
                print(data)


        #for download url need to have Specified type like : .png , .pdf 
        elif flag == 3:
            url = input("url : ")
            path = input("path : ")
            urllib.request.urlretrieve(url, path + make_file(url))
            print("file downloaded.")

        elif flag == 4:
            url = input("url : ")
            url_parse = urllib.request.urlparse(url)
            print(url_parse)

    except:
        print("something wrong happend!")



downloader_with_extra_stuff()



