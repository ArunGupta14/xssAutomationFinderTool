import requests
import time


def xssChecker1(base_url,url):
    payload = b'arun<>'
    resp = requests.get(f'{base_url}+{payload}')
    if payload in resp.text:
        print(">>>[xss vulnerability] ",url)
    else:
        print("not vulnerable")

def xssChecker(base_url,url):

    payload = b'd="ishaan<>'
    resp = requests.get(f"{base_url}+{payload}")
    page_content = resp.text
    
    if "alert(" in page_content and");" in page_content:
        print(">>>[xss vulnerability] ",url)
    else:
        xssChecker1(base_url,url)

with open("file.txt","r")as f:
    for line in f:
        try:
            url = line.strip()
            if 'id=' in url:
                base_url = url.split('d=')[0]
                res = requests.get(f'{base_url}')  
                xssChecker(base_url,url)

        except FileNotFoundError:
            print('File Not Found')
        except requests.ConnectionError:
            print('Connection Error')
        except KeyboardInterrupt:
            print("exit")