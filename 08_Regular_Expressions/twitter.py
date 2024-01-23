#Here we try to extract username frm users url.
'''
url=input("URL: ").strip()
username=url.replace("https://twitter.com/","")
print(f"username: {username}")
#but this methed aint effective in the long run, there can be smthing else in place of http or url could hv some different structure
#to fix dat we use removeprefix fxn instead, as we know that username is alwayes gonna be in the end
url=input("URL: ").strip()
username=url.removeprefix("https://twitter.com/","")
print(f"username: {username}")

#no matter how many python fxn we use, it can never be perfect as it will be with regular exp
#re.sub= substitute,form= re.sub(pattern,repl,string,count=0,flags=0), count means how many time u want to find and replace

import re 
url=input("URL: ").strip()
username=re.sub(r"(^https?://)?(www\.)?twitter\.com/","",url)  #pploften write http instead of https, both works btw, so to deal with that we use"?" after "s" to make it opt.sm ppl might not even write write protocall at all, to deal with that we can make whole https:// part optional by closing in paranthesis and adding ?
print(f"username: {username}")

#if the user is chutia and gives completely different input
#anotherway to do same is

import re
url=input("URL: ").strip()
username=re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
if username:
    print(f"username:",username.group(2))  #we cant use group(1) as (www.) is also gonna be stored in username

#to still use group 1 we gotta do this
import re
url=input("URL: ").strip()
username=re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
if username:
    print(f"username:",username.group(1))
'''
#acc to twitter
import re
url=input("URL: ").strip()
username=re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9]+)$",url,re.IGNORECASE)
if username:
    print(f"username:",username.group(1))

#some other fxns
#    re.split(pattern,string,maxsplit=0,flags=0) -  split the string abt multipple charachters
#    re.findall(pattern,string,flags=0)          -  allows us to search for multiple copies of same pattern in different places in a stringso that we can manipulate more then just one.
