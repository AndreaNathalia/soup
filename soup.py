#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re
import shutil
#,sys,csv,json

#url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
#try:
    #html_content = requests.get(url).text
#except:
 #   print("unable to get {url}")
 #   sys.exit(1)

# Parse the html content, this is the Magic ;)
#soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

#print(soup.title)
#print(soup.title.string)

#for div in soup.find_all("div"):
 #   print(div)
  #  print("--------------------------")


ItemSeparator = ("\n-----------------------------------------------------------------------------------\n")
PartsSeparator = ("\n===================================================================================\n")

url="http://ufm.edu/Portal"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

print("")
print("")
print("                                    ANDREA REYES ")
print(PartsSeparator)
print("")

# ------------- PHASE 1 ----------------
print("1. Portal ")
print("")

# GET TITLE
print("GET the title and print it: ",soup.title.string)
print(ItemSeparator)

#----

# GET ADRESS
adress =""

for a in soup.find_all("a"):
    search = a['href']

    if search == "#myModal":
        adress = a.text

# PRINT ADRESS
print("GET the Complete Address of UFM: ",adress)
print(ItemSeparator)

#---

# GET PHONE NUMBER AND EMAIL
phone =""
email=""

#phone
for p in soup.find_all("a"):
    search = p['href']

    if search == "tel:+50223387700":
        phone = p.text

#email
for e in soup.find_all("a"):
    search1 = e['href']

    if search1 == "mailto:inf@ufm.edu":
        email = e.text

# PRINT NUMBER AND EMAIL
print("GET the phone number and info email: ")
print("- Phone Number: ", phone)
print("- E-mail: ", email)
print(ItemSeparator)

#---

# GET ALL ITEM THAT ARE PART OF THE UPPER NAV MENU

#nav = soup.find('div', attrs={'class':'row'})
#print(nav.text)

#estudios
#nav_estudios = soup.find('div', class_="menu-key")
#print(nav_estudios.a.string)


nav_facultades = soup.find(id="menu-table")
print("GET all item that are part of the upper nav menu: ")
print(nav_facultades.text)
print(ItemSeparator)

#---

# FIND ALL PROPERTIES THAT HAVE href
hrf =""
print("Find all properties that have href: ")
for hr in soup.find_all("a"):
    hrf= (hr.get('href'))
    print(hrf)

print(ItemSeparator)

#---

# GET href OF "UFMail" BUTTON
ufmail_button = soup.find(id="ufmail_")
ufmail_button_href = ufmail_button.get('href')
print("GET href of 'UFMail' button: ")
print(ufmail_button_href)
print(ItemSeparator)

#---

# GET href "MiU" BUTTON
miu_button = soup.find(id="miu_")
miu_button_href = miu_button.get('href')
print("GET href 'MiU' button: ")
print(miu_button_href)
print(ItemSeparator)

#---

# GET hrefs OF ALL <img>
imgh =""
print("GET hrefs of all <img>: ")
for i in soup.find_all("img"):
    imgh= (i.get('src'))
    print(imgh)

print(ItemSeparator)

#---

# COUNT ALL <a>
contador = 0
for a_labels in soup.find_all("a"):
    contador = contador + 1

print("Count all <a>: The TOTAL number of <a> tags is: ", contador)
print(ItemSeparator)

print(PartsSeparator)


# ------------- PHASE 2 ----------------
url2="https://ufm.edu/Estudios"
html2 = requests.get(url2).text
soup2 = BeautifulSoup(html2, 'html.parser')

print("2. Estudios ")
print("")

estudios_href=""
# NOW NAVIGATE to /Estudios
for estudios in soup.find_all("a", href = True):
    if estudios.text == "Estudios":
        estudios_href = estudios.get('href')

print("Now navigate to /Estudios: ")
print(estudios_href)
print(ItemSeparator)

# DISPLAY ALL ITEMS FROM "topmenu"
top_menu = soup2.find("div", id="topmenu")
print("Display all items from 'topmenu': ")   
print(top_menu.text)
print(ItemSeparator)

#---

# DISPLAY ALL "Estudios"
print("Display ALL 'Estudios': ")
titles = soup2.find_all('div', class_="estudios",limit=5)
for i in titles:
    print("- ", i.text)

print(ItemSeparator)

#---

# DISPLAY FROM "leftbar" ALL <li> ITEMS
print("Display from 'leftbar' all <li> items: ")
leftbar = soup2.find_all('div',class_="leftbar", limit=4)
for bar in leftbar:
    print(bar.ul.text)
print(ItemSeparator)

#----

# GET AND DISPLAY ALL AVAILABLE SOCIAL MEDIA WITH ITS LINKS (href) 
print("Get and display all available social media with its links: ")
social = soup2.find('div', class_="social pull-right")
a=social.find_all("a")
a_href =""
for media in a:
    a_href = media['href']
    print(a_href)
print(ItemSeparator)

#---

# COUNT ALL <a>
contador2 = 0
for a_tags in soup2.find_all("a"):
    contador2 = contador2 + 1

print("Count all <a>: ", contador2)
print(ItemSeparator)
print(PartsSeparator)


# ------------- PHASE 3 ----------------
url3="https://fce.ufm.edu/carrera/cs/"
html3 = requests.get(url3).text
soup3 = BeautifulSoup(html3, 'html.parser')

print("3. CS ")
print("")

# GET TITLE
print("GET the title: ",soup3.title.string)
print(ItemSeparator)

#----

# DOWNLOAD the "FACULTAD de CIENCIAS ECONOMICAS" logo
print("Download the 'FACULTAD de CIENCIAS ECONOMICAS' logo: ")
find_logo =soup3.find_all("a", href = "https://fce.ufm.edu")
for logo in find_logo:
    img = logo.find("img")['src']
gt = requests.get(img, stream = True)
show_logo = open('logo.jpg', 'wb')
gt.raw.decode_content = True
shutil.copyfileobj(gt.raw,show_logo)
print(show_logo)
print(ItemSeparator)


#---

# GET FOLLOWING <meta>: "title", "description" ("og")
Mtitle =""
metaT = soup3.find('meta', attrs={'property':'og:title'})['content']
for i in metaT:
    Mtitle = metaT

descr = ""
descript = soup3.find('meta', {'property':'og:description'})['content']
for j in descript:
    descr = descript

print("Get <meta>: title: ")
print(Mtitle)
print("")
print("Get <meta>: description: ")
print(descr)
print(ItemSeparator)

#---

# COUNT ALL <a>
contador3 = 0
for a_s in soup3.find_all("a"):
    contador3 = contador3 + 1

print("Count all <a>: ", contador3)
print(ItemSeparator)

#---

# COUNT ALL <div>
contador4 = 0
for divs in soup3.find_all("div"):
    contador4 = contador4 + 1

print("Count all <div>: ", contador4)
print(ItemSeparator)










print("")

