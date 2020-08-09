#import re 
#text = 'A random string.'
#pattern = re.compile('A random string.')
#result = pattern.search(text)
#print(result)

#import re 
#text = "A random string."
#pattern = re.compile('r') 
#result = pattern.search(text)
#print(result)


#import re 
#text = "A random B string.ABC"
#pattern = re.compile('[ABC]') 
#result = pattern.search(text)
#print(result)



#Gives None
#import re 
#text = "A random B string."
#pattern = re.compile('ABC') 
#result = pattern.search(text)
#print(result)



#import re
#text = "A random string."
#pattern = re.compile("[rdm]")
#result = pattern.search(text)
#print(result)



#Gives Error
#import re
#text = "A random string. abc"
#pattern = re.compile("a-c")
#result = pattern.search(text)
#print(result)


#import re 
#text = "A random string"
#pattern = re.compile("[a-c]")
#result = pattern.search(text)
#print(result)

#To find word
#import re
#text = "random string."
#pattern = re.compile('[a-zA-Z]+')
#result = pattern.search(text)
#print(result)


#To find any word with numbers
#import re
#text = 'random34657 is string.'
#pattern = re.compile('[a-zA-Z0-9]+')
#result = pattern.search(text)
#print(result)




#I dont skip the period(.) by using backward slash(\) and  although  code runs
#And if i use \ it gives Error


#import re
#text = "A random string. Myname4689@Website.com  This is good string"
#pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+")
#result = pattern.search(text)
#print(result)

#import re
#text = 'A random string. M.y-name_4689@Website.com This is good string'

#pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+")


#Gives None
#pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+")

#result = pattern.search(text)
#print(result)




#This gives only one email
#import re
#text = 'A random string. M.y-name_4689@Website.com This is good string Isthi34@right.email'

#pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+")

#result = pattern.search(text)
#print(result)





import re
text = 'A random string. M.y-name_4689@Website.com This is good string Isthis34@right.email'

pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+")

result = pattern.findall(text)
print(result)
