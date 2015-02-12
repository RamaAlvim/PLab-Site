
<%
import sqlite3 as lite
import sys
from subprocess import call
import os 
import config
from server.page import html, textStyle
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)
html.setMetaUTF8(self)
html.endHead(self)
html.beginContent(self)




os.chdir(config.__WWW_DIR__)

con = lite.connect('test.db')
con.row_factory = lite.Row

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Users")

    rows = cur.fetchall()

    for x in rows:
        print str(x['Id']) + "<br>"

html.endContent(self)
html.endHtml(self)
%>
