

<html>
<body>

<%

import sqlite3 as lite
import sys
from subprocess import call
import os 
import config

os.chdir(config.__WWW_DIR__)

con = lite.connect('test.db')

login = __GET__['login'][0]
password = __GET__['password'][0]

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Users WHERE login = '"+login+"' and password = '"+password+"'")

    rows = cur.fetchall()

    for row in rows:
        print row

%>

</body>
</html>
