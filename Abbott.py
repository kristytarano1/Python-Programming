from mechanize import *

br = mechanize.urlopen('https://www.behindthename.com/random/')


print(br.title())
