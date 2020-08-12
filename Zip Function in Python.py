#list1 = [1,2,3,4,5]
#list2 = ['one','two','three','four','five']
#zipped = list(zip(list1,list2))
#print(zipped)


#Python was always trunky
#here 6 has been skipped
#list1 = [1,2,3,4,5,6]
#list2 = ['one','two','three','four','five']
#zipped = list(zip(list1,list2))
#print(zipped)

#here six has been skipped
#list1 = [1,2,3,4,5]
#list2 = ['one','two','three','four','five','six']
#zipped = list(zip(list1,list2))
#print(zipped)


#for (l1,l2) in zip(list1,list2):
#  print(l1)
#  print(l2)



#This is another method of bulk type casting
#items = "guy"
#counts = 43
#prices = 0.234

#items,counts,prices = str(items),str(counts),str(prices)

#print(type(items))
#print(type(counts))
#print(type(prices))


items = ['Apple','Banana','Orange']
counts = [3,6,4]
prices = [0.99,0.25,0.50]

sentences = []
#zipping = list(zip(items,counts,prices))
#print(zipping)
for (item,count,price) in zip(items,counts,prices):
  item,count,price = str(item),str(count),str(price)
  sentence = 'I bought '+count+' '+item+'s at '+price+' cents each.'
  sentences.append(sentence)

print(sentences)
