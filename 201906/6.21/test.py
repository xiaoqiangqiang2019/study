import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
 
#data = {'params.businessTypeCode=&params.deptName=&page.currentPage=1&page.limit=20&page.option=next&page.start=0&page.rowCount=424523&listGrid.col=1%2C2%2C3%2C4%2C5&listGrid.type=ro%2Cro%2Cro%2Cro%2Cro'}
data = {'params.businessTypeCode': '', 'params.deptName': '', 'page.currentPage': '1', 'page.limit': '20', 'page.option': 'next', 'page.start': '0', 'page.rowCount': '424523', 'listGrid.col': '1%2C2%2C3%2C4%2C5', 'listGrid.type': 'ro%2Cro%2Cro%2Cro%2Cro'}

r = requests.post("http://wzzxbs.mofcom.gov.cn/WebProBA/NEW_BA/approveApply/loadPublicityData.action", data=data, headers=headers)
print(r.text)