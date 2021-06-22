from os import link
import requests,pprint
from bs4 import BeautifulSoup
e={}
g=[]
f=1
a=requests.get("https://www.collegedekho.com/btech-mechanical_engineering-colleges-in-india/")
b=BeautifulSoup(a.content,"html5lib")
for c in b.find_all("div",{"class":"title"}):
    fn=1
    d={}
    for i in c.find_all("a",{"target":"_blank"}):
        r=i.get_text().replace("  ","")
        d["collage_name"+str(f)]=r.replace("\n","")
        f+=1
        kl=str(i).split()[1]
        link="https://www.collegedekho.com"+kl.replace("href=","")
        an=requests.get(link.replace('"',""))
        soup=BeautifulSoup(an.content,"html5lib")
        for h in soup.find_all("div",{"class":"collegeAddress"}):
            ty=1
            for li in h.find_all("div",{"class":"data"}):
                if ty==1:
                    tuu=li.get_text().replace("  ","")
                    d["contact_no."]=tuu.replace("\n","")
                elif ty==2:
                    tuu=li.get_text().replace("  ","")
                    d["email_id"]=tuu.replace("\n","")
                elif ty==3:
                    tuu=li.get_text().replace("  ","")
                    d["web"]=tuu.replace("\n","")
                elif ty==4:
                    tuu=li.get_text().replace("  ","")
                    d["address"]=tuu.replace("\n","")
                else:
                    pass
                ty+=1
        link1=link.replace('"',"")+"/reviews"
        try:
            bn=requests.get(link1)
            cs=BeautifulSoup(bn.content,"html5lib")
            for u in cs.find_all("div",class_="star-dv"):
                d["rating"]=u.get_text().replace("  ","")
        except:
            pass
    for j in c.find_all("li"):
        if fn==1:
            pass
        elif fn==2:
            d["type"]=j.get_text().replace("Type:","")
        elif fn==3:
            pass
        fn+=1
    g.append(d)
pprint.pprint(g)