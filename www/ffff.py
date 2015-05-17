<html>
<%
from server.page import html, textStyle

import mechanize
import re

html.beginHead(self)
html.setMetaUTF8(self)
html.endHead(self)
%>
<body>

<%

def checkForToA(username, password):
    import mechanize
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    browser = mechanize.Browser()
    browser.set_handle_robots(False)

    browser.addheaders = [('User-agent', 'Firefox')]
    start = 0
    continuar = True
    links = []

    print("Connecting: ")
    print("\tUsername: "+username)

    browser.open("https://mycusthelp.info/IIE/_cs/Login.aspx")
    browser.select_form(nr=0)
    browser.form['txtUsername'] = username
    browser.form['txtPassword'] = password
    response1 = browser.submit()
    html = response1.read() + "dsas"
    
    print("\tPrograms")

    browser.open("https://mycusthelp.info/IIE/_cs/COList.aspx?fid=5")
    #
    
    html = browser.response().get_data()

    

    html = html[html.index("Brazil") - 100: html.index("Brazil")].replace("'id'",  "  'id'")
    t = "fdfsfd    'id':'111111'"
    m = re.match("[^\"]*\W*id[^:]*:\D*(\d+)", html)
    aa = ""
    if m:
        aa = m.group(1)
    
    print("\tBSWB Id: " + str(aa))    

    browser.open("https://mycusthelp.info/IIE/_cs/CODetails.aspx?ot=2&fid=5&oi=" + str(aa))


    html = browser.response().get_data()
    
    if "passport" in html.lower():
        print("\tPassport: OK") 

    
    if html.count('erms') > 2:
        return True
        print "\tToA!!!"
        inemail.sendEmail("TOA", *cred)
    else:
        return False

userPwd = 'bernardo.godinho.oliveira@gmail.com', 'ber029347'

if checkForToA(*userPwd):
    print "ToA: Yes" 

else:
    print "ToA: No" 


%>


</body>
</html>







