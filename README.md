# EzilMonitor
## 简介
这是一个超级简单的监控EZIL在线机器数量并发送到[PUSHPLUS](https://www.pushplus.plus)
## Github Action
不推荐
### 准备工作
1. 点击右上角的FORK，并切换至自己仓库
2. 点击**Settings**->**Secrets**->**Actions**
   ![Secrets](img/1.jpg)
3. 点击右上角**New repository secret**
4. 第一个**Name**为`ADDRESS`，**Value**为钱包地址如
   0x0000000000000000000000000000000000.zilxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
5. 第二个**Name**为`TOKEN`，**Value**可到[PUSHPLUS](https://www.pushplus.plus/push1.html)扫描二维码获取

### 查看Actions
如果没有意外的话，已经可以运行了，1min自动监控一次

现在打开`.github/workflows/EzilMonitor.yml`文件，并编辑将
```
#  schedule:
#    - cron: '0 */2 * * *'
```
改为
```
  schedule:
    - cron: '0 */2 * * *'
```

## 腾讯云函数
推荐
1. 将tencent.py内容粘贴进入云函数，运行环境Python3.6
2. 设置环境变量`address`,`token`和`tmpfile`
3. tmpfile推荐放在挂载的文件系统中，如果挂载文件系统，设置为`/mnt/i.txt`,不挂载则为`/tmp/i.txt`

