import os
import json, re, webbrowser, socket, time, sys, codecs

def internet_on(host="8.8.8.8", port=53, timeout=3):
    """
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain (DNS/TCP)
.	"""
    try:
        #response = urr.urlopen('https://www.google.co.in', timeout=10)
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host,port))
        return True
    except exception as e:
        return False

def childRet(dta):
    chldData = dta
    for i in range(0,len(chldData)):
        try:
            #print("Name: "+chldData[i]["name"])
            #print("URL: "+chldData[i]["url"])
            r_entry = {"name" : chldData[i]["name"],
                       "url" : chldData[i]["url"],
                       "nameList" : re.sub("[^\w]", " ",  chldData[i]["name"].lower()).split(),
                       "urlList" : re.sub("[^\w]", " ",  chldData[i]["url"].lower()).split(),
                       }
            r_data.append(r_entry)
        except:
            childRet(chldData[i]["children"])
    

def authFunc(fd,q):
    if q>=1 and q<=len(fd):
        webbrowser.open_new(fd[q-1]["url"])
    else:
        print("Invalid input.")
        q = int(input("Enter a valid result no. to be opened: "))
        authFunc(fd,q)

    
bookmark_id = 1
r_data = []

user = "C:\\Users\\_UserName_\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks" #Replace _UserName_ with your device's username. 
input_file = codecs.open(user, encoding='utf-8')
data = json.load(input_file)



for i in range(0,len(data["roots"]["bookmark_bar"]["children"])):
    try:
        #print("Name: "+data["roots"]["bookmark_bar"]["children"][i]["name"])
        #print("URL: "+data["roots"]["bookmark_bar"]["children"][i]["url"])
        r_entry = {"name" : data["roots"]["bookmark_bar"]["children"][i]["name"],
                   "url" : data["roots"]["bookmark_bar"]["children"][i]["url"],
                   "nameList" : re.sub("[^\w]", " ",  data["roots"]["bookmark_bar"]["children"][i]["name"].lower()).split(),
                   "urlList" : re.sub("[^\w]", " ",  data["roots"]["bookmark_bar"]["children"][i]["url"].lower()).split(),
                    }
        r_data.append(r_entry)
    except:
        childRet(data["roots"]["bookmark_bar"]["children"][i]["children"])
for i in range(0,len(data["roots"]["other"]["children"])):
    try:
        #print("Name: "+data["roots"]["other"]["children"][i]["name"])
        #print("URL: "+data["roots"]["other"]["children"][i]["url"])
        r_entry = {"name" : data["roots"]["other"]["children"][i]["name"],
                   "url" : data["roots"]["other"]["children"][i]["url"],
                   "nameList" : re.sub("[^\w]", " ",  data["roots"]["other"]["children"][i]["name"].lower()).split(),
                   "urlList" : re.sub("[^\w]", " ",  data["roots"]["other"]["children"][i]["url"].lower()).split(),
                    }
        r_data.append(r_entry)
    except:
        childRet(data["roots"]["other"]["children"][i]["children"])
query = input("Enter search query: ")

fin_data = []
entry_num = 1

for i in range(0,len(r_data)):
    if query.lower() in r_data[i]["nameList"] or query.lower() in r_data[i]["urlList"]:
        print("Result No."+str(entry_num))
        entry_num+=1
        print("Name:",r_data[i]["name"])
        print("URL:",r_data[i]["url"])
        fin_entry = {"name" : r_data[i]["name"],
                     "url" : r_data[i]["url"]
                    }
        fin_data.append(fin_entry)

checkRes = int(input("Enter the result no. to be opened: "))

authFunc(fin_data,checkRes)
