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

# Assuming we don't use a HTML Parser (which I'll describe below)
# Since we're not using REGEX things get a lot trickier. Here's how.
# We don't have any knowledge other than the item we're looking for, 
# since we can't really use
# wild cards in the latitude,longitude attributes, so we'll need to know when we've found
# <p class="row" data-latitude=", THEN we can search for SMALL, to decide if it's a "line" we wish to use
# unfortunately we would have to do a search on that SECTION for each of the options (I think I had 6 of them)
# Also problematic is that we're going to want to search in all lowercase or something otherwise we have 2 times
# the searching to do.
# Once we decide its a good link, we have to grab the latitude using a split (or something), same with the longitude,
# and the url.
# This example shows how powerful matching AND grouping is, because we can find a specific something
# and pull the relevant data out.

# HTML PARSER
# If you have an html parser, you can probably set it up so you're ONLY looking at the P classes you want.
# Then you can do the search, but still you'll have to manage roughly 6 searches (using lowercase for everything)
# and then navigate to the appropriate attributes, but either way you'll have to do 6 separate searches

for line in html:
   # Of course if we're
   # using an HTML parser then some of this gets way easier. For example, if we wanted to 
   # print out the stuff between <small></small> since we're already on that element when we 
   # do our search, we just print the data, in the below case since I'm still using manual
   # parsing techniques, we'd have to figure out where <small> and </small> are and do a 
   # string extraction from the <small> start location + 6, to the start of </small>, but 
   # I digress
   # 
   # might get us where we are looking, but there *could* be stuff that is similar and you might get data
   # that isn't what you're looking for, but oh well, our later if/thns *should* parse that out.
   if line.find('<p class="row" data-latitude="') != -1:
   
      # We're in the right area.
      # First we need to figure out where "small" starts, otherwise we'll have a hard time being sure
      # that we are grabbing ONLY the areas where the "small" stuff says it's in the below.
      start_of_small = line.lower().find("<small>")
      
      # We also need to consider when we have stuff after /small that doesn't make sense so 
      # we should limit our search to only <small>stuff</small>
      #
      end_of_small = line.lower().find("</small>")
      if line.lower().find("paradise",start_of_small,end_of_small) != -1:
         # Figure out the latitude,long,link information
         print "Found Listing 1"
      elif line.lower().find("unser",start_of_small,end_of_small) != -1:
         print "Found Listing 2"
      elif line.lower().find("irving",start_of_small,end_of_small) != -1:
         print "Found Listing 3"
      elif line.lower().find("paseo",start_of_small,end_of_small) != -1:
         print "Found Listing 4"
      elif line.lower().find("universe",start_of_small,end_of_small) != -1:
         print "Found Listing 5"
      elif line.lower().find("golf course",start_of_small,end_of_small) != -1:
         print "Found Listing 6"
         
# Phew that was a lot of work (and I made mistakes hte first time, I didn't realize we 
# needed to be within the "small section", I forgot that find returns -1 if it doesn't find anything
# AND we needed 6 copies of that, now if something changes you *might* have to change it in 6 places
# DRY principle HATES that (DRY is Don't Repeat Yourself)

# Really Annoying is that to add another area we have to add 
#      elif line.lower().find("new place",start_of_small,end_of_small) != -1:
#         print "Found Listing 6"
# and depending on the code, we're going to have more than just "found listing 6", we'll have to add in the stuff
# that grabs the url, the lat/long etc, in each (which maybe is only a function call away, but it's still copy/paste
# stuff which is no fun.
