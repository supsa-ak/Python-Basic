#Immutable Datatypes
#Tuples
#int,str,bool,float

#Mutable Datatypes
#list
#set
#dict
#OrdereDict


# Gives Error
#t = [1,2,3]
#t[0] = 7
#print(t)


# Gives Error
#d = {('the':2),'sa':8}
#d.pop('the')
#print(d)

#can't add key value pair to dict
#Gives Error
#d = {'the':2,'sa':8}
#d.add('pa':7)
#print(d)



#Gives Error
#t = (1,2,3)
#t[0] = 7
#print(t)

#This pa dont have to be remove bcauz it is tuple and tuple are Immutable cannot remove
#d = {('pa'):2,'sa':8}
#d.pop('pa')
#d.remove[0]
#print(d)


#This code is just a mess
#from Collection import OrdereDict
#d = {('pa'):2,'sa':8}
#d.pop('pa')
#d.remove[0]
#print(d)


#OrdereDict is not working
#from Collections import OrdereDict
#d = {('the'):2,'sa':8}
#d.pop('the')
#print(d)


#Gives Error
#t = (1,2,3,[4,5,6])
#t[3] = 7
#print(t)
 
 
#t = (1,2,3,[4,5,6])
#t[3][0] = 7
#print(t)

#Gives Error
t = (1,2,3,(4,5,6))
t[3][0] = 7
print(t)
