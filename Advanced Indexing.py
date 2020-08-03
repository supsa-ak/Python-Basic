#Indexing



#digits=[0,1,2,3,4,5,6,7,8,9]
#print(digits[0])
#print(digits[-1])
#print(digits[-10])


#not working
#print(digits[10])
#print(digits[11])
#print(digits[-11])
#print(digits[-len(digits)])
#print(digits[+len(digits)])

#Slicing 

#digits=[0,1,2,3,4,5,6,7,8,9]
#print(digits[:3])
#print(digits[0:3])
#print(digits[0:9])

#Gives Empty List
#print(digits[9:0])
#name='sarthak kalpande'
#print(name[:8])
#print(name[:7])
#print(name[:6])
#print(name[:9])
#print(name[-9:-6])

#Gives empty
#print(name[-6:-9])

#digits=[0,1,2,3,4,5,6,7,8,9]
#print(digits[:-1])

#print(digits[0:-1])
#print(digits[:1])
#print(digits[:2])
#Gives Empty
#print(digits[:0])


# Gives Whole List
#print(digits[:])
#print(digits[:10])
#print(digits[:11])
#print(digits[:1000])

#print(digits[5:])
#print(digits[5:9])

#striding

#digits=[0,1,2,3,4,5,6,7,8,9]
#print(digits[0:10:1])
#print(digits[0:10:])

#Gives Error
#print(digits[0:10:0])


#print(digits[0:10:2])
#print(digits[:11:2])
#print(digits[:11:3])
#print(digits[-9:-4:1])

#digits=[0,1,2,3,4,5,6,7,8,9]
#print(digits[::-1])

#Gives Empty
#print(digits[0:0:-1])

#prints Reverse
#print(digits[5:1:-1])

#print(digits[::-2])

#print(digits[5:0:-1])








#digits=[0,1,2,3,4,5,6,7,8,9]

#len function

#print(len(digits))
#print(-len(digits))




#Gives first 0 index value
#Here at in square bracket the value of index #is 0
#print(digits[-len(digits)])



#Gives error 
#Here positive len value which is index value #is 10 and there is no no. on index value 10 #so error
#print(digits[len(digits)])



#For Loop in slicing
#correct hai
#for i in range(len(digits)):
  #print(digits[:i])



#for i in range(5):
#  print(i)


#digits=[0,1,2,3,4,5,6,7,8,9]

#for i in range(10):
#  print(digits[:i])


digits=[0,1,2,3,4,5,6,7,8,9]

#for i in range(len(digits)):
 # print(digits[i:i+3])
  
  
#for i in range(len(digits)):
#  print(digits[i:i+10])



#for i in range(len(digits)-2):
#  print(digits[i:i+3])



#window_size=3
#for i in range(len(digits)-2):
 # print(digits[i:i+window_size])
  
#window_size=5
#for i in range(len(digits)-4):
#  print(digits[i:i+window_size])



#window_size=7
#for i in range(len(digits)-(window_size-1)):
  #print(digits[i:i+window_size])

#Now above fraction of code i have to put only #window_size and the work is done

window_size=6
for i in range(len(digits)-(window_size-1)):
  print(digits[i:i+window_size])
