import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_datetime(f):
    m=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    lf=f.split()
    y=int(lf[3])
    m=m.index(lf[2])+1
    d=int(lf[1])
    h=int(lf[4].split(":")[0])
    mi=int(lf[4].split(":")[1])
    dt=datetime(y,m,d,h,mi)
    return dt

url='https://www.rbc.ru/'
s=requests.get(url)
print(s.status_code)
#print(s.text[:300],end="...есть ещё")
soup = BeautifulSoup(s.text,"html.parser")
news=soup.find_all('div',class_='main__feed js-main-reload-item')
url='http://127.0.0.1:8000/addnew/'
for n in news:
    title=n.find('span',class_='main__feed__title-wrap').text.strip()
    sdt=n['data-modif-date']
    dt=get_datetime(sdt)
    #dt=datetime.fromisoformat(sdt)
    nu=n.find('a',class_='main__feed__link js-yandex-counter')['href']
    print(title,sdt,nu,sep='  ')
    #print(dt.strftime("%y-%m-%d %H:%M:%S"))
    d={'title':title,'url':nu,'date':dt.isoformat()}
    url='http://127.0.0.1:8000/addnew/'
    s=requests.get(url,params=d)
    print(s.text)
    #break