#导入需要的模块
import urllib.request
import json
#这里做个示范，读取用户输入
#ip_addr = input(str('输入IP地址：'))
ip_addr = '182.16.86.197'
#定义请求地址
api_url = 'https://api.godaddy.com/v1/domains/mg0003.com/records/A/@'

#直接做一个函数，传入API地址和更改的IP
def update_NS(api_url,ip_addr):
    #定义http请求头
    head = {}
    #定义服务器返回json数据给我们
    head['Accept'] = 'application/json'
    #定义我们发送的数据为json
    head['Content-Type'] = 'application/json'
    #定义身份认证信息
    head['Authorization'] = 'Authorization: sso-key e4NE7kmZMqzf_UGHBz2gxuuJ5pSndWc8122:XaskWvdtgmHMEJp4HsBkd8'

    #定义解析记录
    records_a = {
    "data" : ip_addr,
    "ttl" : 600
    }
  
    #定义需要发送给服务器的数据为put_data这个列表，包含上面的解析记录
    put_data = [records_a]

    #错误处理
    try:
        #定义请求，包含请求地址，请求头，请求方式，并把put_data从json转换为字符串格式，再转换成bytes
        req = urllib.request.Request(api_url,headers = head,data = json.dumps(put_data).encode(),method = "PUT")
        rsp = urllib.request.urlopen(req)
        #根据官方文档我们只需要知道服务器返回码即可，200为成功，这里获取服务器的返回码
        code = rsp.getcode()
        #判断是否成功
        if code == 200:
            print('成功更改域名解析：'+ip_addr)
        else:
            print('更改失败！')
    #原谅我偷懒。官方有400/401/422等错误，这里统一处理了
    except:
        print('错误！')

#执行一下函数，并传入请求地址和我们输入的IP
update_NS(api_url,ip_addr)