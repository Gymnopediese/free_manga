import requests
import os
import threading

site = input("which site :")
manga_name = input("manga please : ").replace(" ", "-")
scan = input("which chapter? (0 to get all) : ")

def mkdirr(test):
    try:
        os.mkdir(test)
    except:
        pass

def link_to_image(url, folder, dir):
	img_data = requests.get(url).content
	print(url)
	print(img_data)
	if "https://" in str(img_data):
		return (0)
	mkdirr(dir)
	with open(folder, 'wb') as handler:
		handler.write(img_data)
	return (1)

def get_scan(site, manga_name, scan):
    manga_name = manga_name.replace(" ", "-", 10023)
    for i in range(1,200):
        try:
            name = manga_name + "/" + scan + "/" + str(i) + ".png"
            mkdirr(manga_name)
            mkdirr(manga_name + "/" + scan)


            url = f"{site}/{manga_name}/{scan}/{str(i)}.jpg"

            if link_to_image(url, name, manga_name + "/" + scan + "/") == 0:
                print("no such file " + name)
                break

        except Exception as e:
            print(e)
            break
if "-" in scan:
    sp = scan.split("-")
    for i in range(int(sp[0]),int(sp[1]) + 1):
        x = threading.Thread(target=get_scan, args=(site, manga_name, str(i)))
        x.start()
elif scan == "0":
    scan = input("how many?")
    for i in range(1,int(scan)):
        x = threading.Thread(target=get_scan, args=(site, manga_name, str(i)))
        x.start()
else:
    get_scan(site, manga_name, scan)