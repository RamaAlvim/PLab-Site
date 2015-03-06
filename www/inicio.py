
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








html.endContent(self)
html.endHtml(self)
%>