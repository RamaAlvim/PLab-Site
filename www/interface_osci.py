<%
from server.page import html, textStyle
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)

%>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="scripts.js" language="JavaScript"></script>

<%

html.setMetaUTF8(self)
html.endHead(self)
html.beginContent(self)
%>

"""
    actScale = getScale()
    nextScale = ""
    backScale = ""
    strSca = str(actScale).split("." )[0]
    if strSca == "5":
        backScale = "1.0e"+str(int(str(actScale).split("e" )[1])+1)
        nextScale = "2."+str(actScale).split("." )[1]
    elif strSca == "2":
        backScale = "5."+str(actScale).split("." )[1]
        nextScale = "1."+str(actScale).split("." )[1]
    elif strSca == "1":
        backScale = "2."+str(actScale).split("." )[1]
        nextScale = "5.0e"+str(int(str(actScale).split("e" )[1])-1)


"""
<button type="button" onclick="point_it('autoscale')">AutoScale</button>
<button type="button" onclick="point_it('run')">RUN</button>
<button type="button" onclick="point_it('stop')">STOP</button>
<button type="button" onclick="point_it('apply:pulse')">GEN PULSE</button>
<button type="button" onclick="point_it('apply:RAMP')">GEN RAMP</button>
<button type="button" onclick="point_it('apply:NOISE')">GEN NOISE</button>

<%
html.endContent(self)
html.endHtml(self)
%>


def scale2(request):
    osci.main(":timebase:main:scale 5.0e-2")
    return redirect()
def scale3(request):
    osci.main(":timebase:main:scale 5.0e-3")
    return redirect()
def scale4(request):
    osci.main(":timebase:main:scale 5.0e-4")
    return redirect()

def scale5(request):
    osci.main(":timebase:main:scale 5.0e-5")
    return redirect()
def scale6(request):
    osci.main(":timebase:main:scale 5.0e-6")
    return redirect()

def scale7(request):
    osci.main(":timebase:main:scale 5.0e-7")
    return redirect()
def scale8(request):
    osci.main(":timebase:main:scale 5.0e-8")
    return redirect()
def scale9(request):
    osci.main(":timebase:main:scale 5.0e-9")
    return redirect()
def scale10(request):
    osci.main(":timebase:main:scale 5.0e-10")
    return redirect()
