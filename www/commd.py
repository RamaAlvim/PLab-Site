<%
from server.page import html, textStyle
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)
html.setMetaUTF8(self)
html.endHead(self)
html.beginContent(self)

def write(cmd):
    try:
        import visa;
        rm = visa.ResourceManager("@py")
        inst = rm.open_resource("TCPIP::192.168.134.102")
        inst.write(cmd)
    except:
        print(u"Não encontrado")


login = __GET__['cmd'][0]
write(login)

html.endContent(self)
html.endHtml(self)
%>
