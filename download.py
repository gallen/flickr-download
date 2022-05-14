import flickr_api as f
import sys
import os
from pathlib import Path
from sanitize_filename import sanitize

import requests

#!!! Get flikr web site cookie and copy here.
RAW_COOKIES = "=" # Replace '=' with your cookies
cookies = {i.split('=')[0].strip(): i.split('=')[1].strip() for i in RAW_COOKIES.split(';')}

# Save video
VEDIO_DOWNLOAD_URL = "https://www.flickr.com/video_download.gne?id="
VEDIO_FILE_EXT = ".mp4"

def saveVideo(id):
    url = VEDIO_DOWNLOAD_URL + id
    path = id + VEDIO_FILE_EXT
    with requests.get(url, cookies=cookies)  as r, open(path, 'wb') as f:
        f.write(r.content)

f.set_keys(api_key = 'afd399772a5436d0c16e73f090b79905', api_secret = 'f25318015dc14df1')

try :
    email = input("Please type your email for your flickr account:")
    try :
        f.set_auth_handler("./auth.txt")
    except IndexError : pass
    u = f.Person.findByEmail(email)
    psc = u.getPhotosets()

    finished = set()
    if os.path.exists("finished.txt"):
        with open("finished.txt") as fIn:
            lines = fIn.readlines()
        finished = {s.strip() for s in lines}
    #with open("photoset.txt", "w") as f:

    with open("finished.txt", "a") as fOut:
        count = 0
        for ps in psc:
            #f.write(ps.title + "\n");
            title = sanitize(ps.title)
            if title in finished:
                print("Photo set: " + title + " already downloaded(skipped)")
                continue

            idSet = set()
            idFile = title + ".txt"

            if not os.path.exists(title):
                print("Creating directory " + title)
                os.mkdir(title)
            os.chdir(title)

            if os.path.exists(idFile):
                with open(idFile) as idF:
                    lines = idF.readlines()
                idSet = {s.strip() for s in lines}

            pInfo = ps.getPhotos().info
            with open(idFile, "a") as ids:
                for page in range(pInfo.pages):
                    for p in ps.getPhotos(page=page+1) :
                        print("Saving photo " + p.id)
                        if p.id not in idSet:
                            if p.media == 'video':
                                if RAW_COOKIES == "=":
                                    continue
                                else:
                                    saveVideo(p.id)
                            else:
                                p.save(p.id)
                            count += 1
                            ids.write(p.id + "\n")
                            ids.flush()
                        else:
                            print(p.id + " already downloaded(skipped)")
                    print(str(count) + " photos saved.")

            print ("Download " + title + " finished.")
            fOut.write(title + "\n")
            fOut.flush()
            os.chdir("..")
        print("All photo sets downloaded! Bye!")
except :
    print("Unexpected error.\n")
    raise