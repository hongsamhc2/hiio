# import requests
# from bs4 import BeautifulSoup


# r = requests.get('https://twentytwentyone.tistory.com')
# print(r.__dict__)

# r = r.text
# s = BeautifulSoup(r,'html.parser')
# t = s.select('link')
# for tt in t:
#     print(tt['href'])
# #"https://twentytwentyone.tistory.com/manage/newpost/54?type=post&returnURL=https%3A%2F%2Ftwentytwentyone.tistory.com%2Fmanage%2Fposts%23"

import re
p = re.compile('[\n]+')
with open('./asset/notion_style.css','r') as f:
    d = f.read()
    d = re.sub(p,'',d)
    d = d.split('}')
    
    for i,dd in enumerate(d):
        if i<=5:
            if "@" in dd:
                d[i] = dd+'}'
            continue
        dd = dd.split('{')
        if dd[0] =="" or "page" in dd[0]:
            continue
        if "@" in dd[0]:
            dd[1] = dd[1].split(',')
            dd[1] =  ','.join([ ".notion-style .page-body "+c for c in dd[1]])
            d[i] = '{'.join(dd)+'}'
            print(dd[1],dd[0],d[i])
            continue            
 
        dd[0] = dd[0].split(',')
        dd[0] =  ','.join([ ".notion-style .page-body "+c for c in dd[0]])
        print(dd[0])
        d[i] = '{\n'.join(dd)
    d = list(filter(lambda x:x!='',d))
    d = '}\n'.join(d)+'}'
with open('./asset/notion_style.min.css','w') as f:
    f.write(d)