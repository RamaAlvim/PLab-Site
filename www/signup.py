
<%
import sqlite3 as lite
import sys
from subprocess import call
import os 
import config
from server.page import html, textStyle, javascript
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)
html.setMetaUTF8(self)
html.endHead(self)
html.beginContent(self)




os.chdir(config.__WWW_DIR__)

con = lite.connect('test.db')

login = __GET__['login'][0]
password = __GET__['password'][0]

with con:    
    
    cur = con.cursor()    
    cur.execute("INSERT INTO Users (login,password) VALUES ('"+login+"', '"+password+"')")
    affectedRows = cur.rowcount
    if affectedRows >= 1:
        javascript.alert(self, "Process returned 0 (0x0)")
        javascript.redirect(self, "index.py")


html.endContent(self)
html.endHtml(self)
%>

