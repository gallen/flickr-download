## Purpose
Beginning January 8, 2019, free accounts will be limited to 1,000 photos and videos. I am not ready to upgrade to pro account, so I have to find a way to download all my photos and videos before deadline. [The official way](https://help.flickr.com/en_us/download-photos-or-albums-in-flickr-HJeLjhQskX) provided by flickr doesn't work well if you have a large amount(e.g. >5000) photos/videos or a lot of albums. So I just wrote this small tool to help myself and maybe you as well.

## Steps
1. Make sure having python(3.x) and git installed.

2. Install flickr python api package(use 'pip3' instead of 'pip' if you have both python2.x and python3.x installed and set python2.x as default).
    ```
    pip install flickr_api
    ```
    or 
    ```
    python -m pip install flickr_api
    ```

4. Clone this repository
    ```
    git clone https://github.com/gallen/flickr-download
    ```

5. Get authorization code.
    Go to 'flickr-download' folder and run command below,
    ```
    python auth.py
    ```
    This will open a browser window and navigate to flickr authentication page. Login with your flickr account(if not logged in already) and authorize access. 
    ![Authorize](https://user-images.githubusercontent.com/189514/50563971-4e300e00-0cef-11e9-80a3-2df493c32f06.png)
    ![image](https://user-images.githubusercontent.com/189514/50564206-2cd02180-0cf1-11e9-9e22-7b5ed6261062.png)


    The script will ask you 'oauth_verifier', just copy the verifier code got from flickr authorize page above.

    This will create a file 'auth.txt' same folder, this file contains the authorization code and will be used for next set.

6. Download your photos(Check [Notes for vides](#video-notes) first if you have videos to download)!
    Run command below.
    ```
    python download.py
    ```

## <a name="video-notes"></a>Notes for downloading videos.
The flickr python api doesn't support download videos. If you have videos in you albums, you'll need a little bit 'hacking'. 

1. First you'll need get 'cookies' from flickr website with your own account.
![cookies](http://g.recordit.co/6YaiYf8uG5.gif)

2. Then open 'download.py' and locate this line
```python
RAW_COOKIES = "=" # Replace '=' with your cookies
```
replace '=' with 'cookies' copied from previous step.


