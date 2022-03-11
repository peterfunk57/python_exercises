#!/usr/bin/python3

import cgitb
import cgi

cgitb.enable ()

vars = cgi.FieldStorage ()

nombre = vars.getvalue('nombre')

print ("Content-type: text/html")
print ()
print ("<html>")
print ("<body>")
print ("<h2>Bienvenido {0}<h2>".format(nombre))
print ("</body>")
print ("</html>")

