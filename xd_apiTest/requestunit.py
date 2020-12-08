import requests

class RequestUtil():
    def __init__(self):
        pass
    def get_url(self,path):
        url='https://api.xdclass.net'+path
        return url

    def request(self,url,method,headers=None,param=None,content_type=None):
        try:
            if method=='get':
                result=requests.get(url,params=param,headers=headers,verify=False).json()
                return result
            elif method=='post':
                if content_type=='application/json':
                    result=requests.post(url=url,json=param,headers=headers,verify=False)
                    return result
                else:
                    result=requests.post(url=url,data=param,headers=headers,verify=False)
                    return result
            else:print("http method not allowed")
        except Exception as e:
            print("http报错：{0}".format(e))

if __name__=='__main__':
    r=RequestUtil()
    # url=r.get_url('/pub/api/v1/web/all_category')
    # response=r.request(url,'get')
    # print(response)

    url1=r.get_url('/pub/api/v1/web/web_login')
    data={"phone":"15900516719","pwd":"cuipei1001?"}
    headers={"content_type":"application/x-www-form-urlencoded"}
    response1=r.request(url1,'post',param=data,headers=headers)
    print(response1.text)




