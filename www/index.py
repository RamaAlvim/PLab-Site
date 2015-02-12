<html>
<%
from server.page import html, textStyle

html.beginHead(self)
html.setMetaUTF8(self)
html.endHead(self)
%>
<body>

<form action="login.py">
Login:<br>
<input type="text" name="login" value="">
<br>
Passwd:<br>
<input type="text" name="password" value="">
<br><br>
<input type="submit" value="Submit">
</form>
<a href="signup.html"> Cadastre </a><br>
<a href="listUsers.py"> Listar Usuários </a>
#<!-- PERL USAGE -->
#<pl%

#use area qw( areaOfCircle );

#$areaOfFirstCircle = areaOfCircle(5);
#print "The area of the circle is: $areaOfFirstCircle <br>";


#print "Hello world of Perl command line". "<br>";
#print "Hello world of Perl command line2";
#%pl>

</body>
</html>







