from bs4 import BeautifulSoup
import requests
import pandas as pd
ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
header={"User-Agent":ua}
response=requests.get("https://www.yellowpages.com.au/find/medical-centres/qld",headers=header)
soup=BeautifulSoup(response.content,"html.parser")
print(soup.title.get_text())

mylist=[]

def extraction(url):
  ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
  header={"User-Agent":ua}
  response=requests.get(url,headers=header)
  soup=BeautifulSoup(response.content,"html.parser")
  return soup.find_all("div",class_="Box__Div-sc-dws99b-0 iOfhmk MuiPaper-root MuiCard-root PaidListing MuiPaper-elevation1 MuiPaper-rounded")

def transformation(centers):

  for c in centers:
    name=c.find("a",class_="MuiTypography-root MuiLink-root MuiLink-underlineNone MuiTypography-colorPrimary").text


    try:
      address=c.find("div", class_= "Box__Div-sc-dws99b-0 bKFqNV").text
    except:
      address=None

    try:
      phone=c.find("div", class_="Box__Div-sc-dws99b-0 drWGzL").text
      #print(phone)
    except:
      phone=None

    #website=c.find("a", class_="MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite jss367 MuiButton-textPrimary MuiButton-fullWidth")['href=']
    try:

      timings=c.find("div",class_="Box__Div-sc-dws99b-0 QzObd").text
      #print(timings)
    except:
      timings=None

    info={"Name":name,"Address":address,"Phone":phone,"Opens until":timings}
    #print(info)
    mylist.append(info)
  #return
  return  mylist


def load():
  df=pd.DataFrame(mylist)
  return df

for x in range(1,11):
  print("Downloading page" ,x)
  centers=extraction(f'https://www.yellowpages.com.au/find/medical-centres/qld/page-{x}')
  transformation(centers)

df_paidlisting=load()
df_paidlisting

mylist=[]

def extraction(url):
  ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
  header={"User-Agent":ua}
  response=requests.get(url,headers=header)
  soup=BeautifulSoup(response.content,"html.parser")
  return soup.find_all("div",class_="Box__Div-sc-dws99b-0 iOfhmk MuiPaper-root MuiCard-root FreeListing MuiPaper-elevation1 MuiPaper-rounded")

def transformation(centers):
  for c in centers:
    name=c.find("a",class_="MuiTypography-root MuiLink-root MuiLink-underlineNone MuiTypography-colorPrimary").text

    try:
      address=c.find("div", class_= "Box__Div-sc-dws99b-0 bKFqNV").text
    except:
      address=None

    try:
      phone=c.find("div", class_="Box__Div-sc-dws99b-0 drWGzL").text
    except:
      phone=None

    #website=c.find("a", class_="MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite jss367 MuiButton-textPrimary MuiButton-fullWidth")['href=']

    try:
      timings=c.find("div",class_="Box__Div-sc-dws99b-0 QzObd").text
    except:
      timings=None

    info={"Name":name,"Address":address,"Phone":phone,"Opens until":timings}
    mylist.append(info)
  
  return  mylist


def load():
  df=pd.DataFrame(mylist)
  return df

for x in range(1,11):
  print("Downloading page" ,x)
  nextpage=extraction(f'https://www.yellowpages.com.au/find/medical-centres/qld/page-{x}')
  transformation(nextpage)

df_freelisting=load()
df_freelisting

df=pd.concat([df_paidlisting,df_freelisting])
df.to_csv("medical_centers.csv",index=False)
df
