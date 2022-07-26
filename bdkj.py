from posixpath import split
import requests
import os
#
#
# 本电科技桃币签到 小程序
#
# cron 0 9 * * *  bdkj.py
#
# 7-26 签到
#
# ========= 青龙--配置文件 =========
# 变量格式: export wToken=' kiwis-wtoken的值 '
# 抓https://www.bdkjcdn.com/wapi下任意请求头的kiwis-wtoken填入变量
#

#if "wToken" in os.environ:  # 判断 wToken是否存在于环境变量
#    wtoken_list = os.environ['wToken'].split('&')  # 读取系统变量 以 & 分割变量
#    if len(wtoken_list) > 0:  # 判断 WSKEY 数量 大于 0 个
#        print(wtoken_list)
#        else:  # 判断分支
#            logger.info("wToken变量未启用")  # 标准日志输出
#            sys.exit(1)  # 脚本退出
#    else:  # 判断分支
#        logger.info("未添加wToken变量")  # 标准日志输出
#        sys.exit(0)  # 脚本退出


# Token
wtoken=os.environ.get('wToken') 

headers = {
    'Connection': 'keep-alive',
    'xweb_xhr': '1',
    'kiwis-wtoken': wtoken,
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
    'Content-Type': 'application/json;charset=UTF-8',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wx003e375904180915/51/page-frame.html',
    'Accept-Language': 'en-us,en',
    'Accept-Encoding': 'gzip, deflate',
}

# 签到
Daily_session = requests.session()
Daily_url = 'https://www.bdkjcdn.com/wapi/activity/daily_sign'
requests.packages.urllib3.disable_warnings()
Daily_respose = Daily_session.get(url=Daily_url, headers=headers, verify=False)
# print(Daily_respose.status_code)
print(Daily_respose.text)

# 检查是否签到成功
Sign_session = requests.session()
Sign_url = 'https://www.bdkjcdn.com/wapi/activity/today_is_sign'
requests.packages.urllib3.disable_warnings()
Sign_respose = Sign_session.get(url=Sign_url, headers=headers, verify=False)
# print(Sign_respose.status_code)
# print(Sign_respose.text)
if((str(Sign_respose.text.split('"signToday":', -1)
        [1]).split("}", -1)[0]) == "true"):
    print("签到成功")
if((str(Sign_respose.text.split('"signToday":', -1)
        [1]).split("}", -1)[0]) == "false"):
    print("签到失败")

# 当前用户信息
user_info_session = requests.session()
user_info_url = 'https://www.bdkjcdn.com/wapi/user/user_info'
requests.packages.urllib3.disable_warnings()
user_info_respose = user_info_session.get(
    url=user_info_url, headers=headers, verify=False)
# print(user_info_respose.status_code)
# print(user_info_respose.text)

print("当前桃币为"+str(user_info_respose.text.split('"restTaoCoin":', -1)
      [1]).split("}", -1)[0])
