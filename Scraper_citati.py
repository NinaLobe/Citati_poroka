from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


url = "http://quotes.yourdictionary.com/theme/marriage/"

response = urlopen(url).read()
soup = BeautifulSoup(response)


print soup.html.title.string
mylinks = soup.findAll("p", { "class" : "quoteContent" })

for i,line in enumerate(mylinks):
    if i<5:
        print " Citat" + str(i+1) + ":  " + line.string
    else:
        print""
        print "To je vse!!!!!"
        break