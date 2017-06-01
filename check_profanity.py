
import urllib
# URL (Universe Resource Locators)

def read_text():
    #Input directory of file you would like check
    quotes = open("")
    #allows you to work with files on your computer
    #input takes in the address or file you want open
    # open(name[, mode[,buffering]])
    #Is a built in function
    #open returns an on object (variable) of the file type
    contents_of_file = quotes.read() #allows you to read the contents of he movie quotes
    print contents_of_file
    quotes.close() #closes files
    check_profanity(contents_of_file)




def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check) # urllib takes information from the internet
    #urlopen takes in a link from a website
    output = connection.read() #result from the program online
    #print output
    connection.close()
    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
        print 'This document has no curse words!'
    else:
        print "Coudl not scan the document properly."


read_text()
