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

for line in html:
   #print line
   m = re.search(' <p class="row" data-latitude="((-)?[0-9]+(\.[0-9]+)?)" data-longitude="((-)?[0-9]+(\.[0-9]+)?)" .* <a href="(/apa/.*.html)" .*<small>(.*([Pp]aradise|[Uu]nser|[Ii]rving|[Pp]aseo|[Uu]niverse|[Gg]olf [Cc]ourse).*)</small>',line)
   if m:
      print "Found Listing"

# Lets show off the stuff in the grouping so we'll just re-run through the loop
for line in html:
   #print line
   m = re.search(' <p class="row" data-latitude="((-)?[0-9]+(\.[0-9]+)?)" data-longitude="((-)?[0-9]+(\.[0-9]+)?)" .* <a href="(/apa/.*.html)" .*<small>(.*([Pp]aradise|[Uu]nser|[Ii]rving|[Pp]aseo|[Uu]niverse|[Gg]olf [Cc]ourse).*)</small>',line)
   if m:
      # This is the latitude Stuff
      print m.group(1) # First Match is the Data Latitude
      print m.group(2) # Second Match is the - symbol
      print m.group(3) # Third Match is the .### section of the data latitude
      # This is the longitude stuff
      print m.group(4) # First Match is the Data Longitude
      print m.group(5) # Second Match is the - symbol
      print m.group(6) # Third Match is the .### section of the data Longitude
      # This is the link to the appartment
      print m.group(7) # A href we can use to create our own "custom" craigslist page
      # This is the approximate location
      print m.group(8) # The section we limited our search to
      print m.group(9) # The word in the section that we found (and thus successfully matched)

      
# Really cool is that to add another area we just add |<name of area> and we're done.