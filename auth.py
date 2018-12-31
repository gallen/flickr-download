import flickr_api as f
import sys
import os
from pathlib import Path
import webbrowser

print(os.getcwd())
# Retrieve access token 
f.set_keys(api_key = 'afd399772a5436d0c16e73f090b79905', api_secret = 'f25318015dc14df1')
a = f.auth.AuthHandler()
perms = "read"
url = a.get_authorization_url(perms)
webbrowser.open(url)
verifier = input("Pleaes type 'oauth_verifier': ")
a.set_verifier(verifier)
a.save("auth.txt")