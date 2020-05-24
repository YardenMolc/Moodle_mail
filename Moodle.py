#!/usr/bin/env python
# coding: utf-8

# In[3]:


# moodle course update checker : automatically checks for updates in courses registered on moodle
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass
import datetime
now = datetime.datetime.now()
import time

def Emailer(text, subject, recipient):
    import win32com.client as win32   

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    mail.send


# credentials for login
username = # enter your user name 



# take password as input from terminal, it won't be visible
password = getpass.getpass("Password:")

# start a browser session
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe') # change the parameter with the path of chromedriver

# open link in browser

browser.get('https://techwww.technion.ac.il/tech_ident/')
browser.find_element_by_id('00').click()

# login

nameElem = browser.find_element_by_name('loginfmt')
nameElem.send_keys(username)

passElem = browser.find_element_by_name('passwd')
passElem.send_keys(password)
time.sleep(2)
browser.find_element_by_id('idSIButton9').click()
time.sleep(2)

browser.find_element_by_id('idSIButton9').click()
time.sleep(2)
try: browser.find_element_by_id('idSIButton9').click()
except: ""

flag=False
count=0
send=False
while(True):
    count+=1
    print("try number: ", count)
    if (flag==True): time.sleep(5)
    course = "https://moodle.technion.ac.il/course/view.php?id=772"
    browser.get(course)
    section_id = "section-5"
    x_path_selector = "//li[@id='" + section_id + "']/*//a"
    links = len(browser.find_elements(By.XPATH, x_path_selector))

    flag=True
    if(links >1 and send==False):
        #f = open("text3.txt","r+")
        text= #enter the text you want to send to your prof
        
        subject= # enter the subject
        recipent= # prof email
        Emailer(text,subject,recipent)
        print("success")
        send=True
        break;

