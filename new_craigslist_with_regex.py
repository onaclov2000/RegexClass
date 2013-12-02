# 
# Author: Tyson Bailey
# Email : tyson at(@) dot(.) onaclovtech dot(.) com
# 

# Using this as a reference:
# http://albuquerque.craigslist.org/apa/
import urllib2
import re

response = urllib2.urlopen('http://albuquerque.craigslist.org/apa/')
html = response.read().splitlines()
# do something
response.close()  # best practice to close the file


# Data looks like this:
#<p class="row" data-latitude="35.186800" data-longitude="-106.665200" data-pid="4189919428"> 
#  <a href="/apa/4189919428.html" class="i" data-id="0:00A0A_jev2p8Ibo5J"></a> 
#  <span class="star"></span> 
#  <span class="pl"> 
#    <span class="date">Dec  2</span>  
#    <a href="/apa/4189919428.html">Beautiful Charming Home</a> 
#  </span> 
#  <span class="l2">  
#    <span class="price">$1500</span>
#    / 3br - 3450ft&sup2; -  
#    <span class="pnr"> 
#      <small> (Ventana Ranch (west))</small> 
#      <span class="px">
#        <span class="p">
#          pic&nbsp;<a href="#" class="maptag" data-pid="4189919428">map</a>
#        </span>
#      </span> 
#    </span>  
#  </span> 
#</p>

# In General DON'T Try to parse HTML using regex, but for a specific set of data (that you know ahead of time) 
# and a simple search
# Using REGEX is probably ok, in this case we're only looking for these specific kinds of paragraphs, 
# what would have been BETTER is to have used something like Beautiful Soup or some other HTML parser, 
# and then search the CONTENTS of the strings for what you're looking for.

# Lets do something a little more interesting
# Lets make a custom html page that will display the links to ONLY the things we're looking for.
print """
<html>
   <head>
      <title> My CUSTOM Craigslist Housing Search</title>
   </head>
   <body>
      <table>
         <tr>
            <th>Latitude</th>
            <th>Longitude</th>
            <th>Location</th>
            <th>Link</th>
         </tr>
"""
for line in html:
   #print line
   m = re.search(' <p class="row" data-latitude="((-)?[0-9]+(\.[0-9]+)?)" data-longitude="((-)?[0-9]+(\.[0-9]+)?)" .* <a href="(/apa/.*.html)" .*<small>(.*([Pp]aradise|[Uu]nser|[Ii]rving|[Pp]aseo|[Uu]niverse|[Gg]olf [Cc]ourse|[Ee]llison|[vV]entana|[nN]orth [vV]alley).*)</small>',line)
   #print "HI"
   if m:
      # This is the latitude Stuff
      print '         <tr>'
      print '            <td>' + m.group(1) # First Match is the Data Latitude
      print '            <td>' + m.group(4) # First Match is the Data Longitude
      print '            <td>' + m.group(8) # First Match is the Data Location
      print '            <td><a href="http://albuquerque.craigslist.com' + m.group(7) + '">Take a look</a>'# First Match is the Data Latitude
      print '         </tr>'
      
print """
   </body>
</html>
"""