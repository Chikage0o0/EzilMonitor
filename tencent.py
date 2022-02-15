# 腾讯云函数 
# 运行环境python3.6
# 需要在环境变量配置address,token和tmpfile
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
        url="http://www.pushplus.plus/send?token="+token+"&title=EZIL通知&content="+i+"&template=txt"
        res = requests.get(url, headers=headers,timeout=10)
    except:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" 无法通知api")

def main():
    try:
        f = open(tmpfile,"r")
        i=int(f.read())
        f.close
    except:
        i=0
    print(i)
    ii=get()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" 在线"+str(ii)+"台机器")
    if ii>i:
        if ii==-1:
            sendMessage("无法访问Ezil api")
        else:
            sendMessage("上线了"+str(ii-i)+"台机器")
            with open(tmpfile,'w') as f:
                f.write(str(ii))
    if (ii<i):
        if ii==-1:
            sendMessage("无法访问Ezil api")
        else:
            sendMessage("掉线了"+str(i-ii)+"台机器")
            with open(tmpfile,'w') as f:
                f.write(str(ii))


# 云函数入口
def main_handler(event, context):
    global address,token,tmpfile
    address = os.environ.get('address')
    token=os.environ.get('token')
    tmpfile=os.environ.get('tmpfile')
    main()