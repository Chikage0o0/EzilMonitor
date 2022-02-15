import requests,json,time,os
def get():
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        }
        url="https://stats.ezil.me/current_stats/"+address+"/workers/paginated?page=1&coin=eth&per_page=30&name="
        res = requests.get(url, headers=headers,timeout=10)
        data=json.loads(res.text)
        num=data["data"]["totals"]["workers"]["online"]
        return num
    except:
        print("无法访问Ezil api")
        return -1

def sendMessage(i):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
        }
        url="http://www.pushplus.plus/send?token=80552687615d49fcb2974e75958f82f8&title=掉线&content="+i+"&template=txt"
        res = requests.get(url, headers=headers,timeout=10)
    except:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" 无法通知api")

def main():
    try:
        f = open("i.txt","r")
        i=int(f.read())
        f.close
    except:
        i=0
    ii=get()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" 在线"+str(ii)+"台机器")
    if ii>i:
        with open("i.txt",'w') as f:
            f.write(str(ii))
    if (ii<i):
        if ii==-1:
            sendMessage("无法访问Ezil api")
        else:
            sendMessage("掉线了"+str(i-ii)+"台机器")
        with open("i.txt",'w') as f:
            f.write(str(ii))

if __name__ == '__main__':
    address = os.environ["ADDRESS"]
    token=os.environ["TOKEN"]
    main()
