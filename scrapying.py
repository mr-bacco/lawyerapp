############################################################
# Project: web application for data science / web scraping #
# Author: bac [and_bac]                                    #
# Date: 2019                                               #
# Include file which should do web scraping                #
############################################################

############## Web scraping example START ##############

from bs4 import BeautifulSoup # used for web scraping
bs = BeautifulSoup
# this is a block of code for web scraping 

# example as following 
with open("./templates/home.html") as file:
    soup = bs(file)

soup = bs("<html>data</html>")
print(soup.prettify)



############## Web scraping example END ##############