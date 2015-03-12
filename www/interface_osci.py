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
<button type="button" onclick="point_it('autoscale')">AutoScale</button>

<%
html.endContent(self)
html.endHtml(self)
%>
