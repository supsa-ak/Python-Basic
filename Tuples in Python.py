#t=(1,2,3)
#print(t[0])
#print(t[2])




#This is structured

#credit_card1 = (1234123412341234,'sak brro',425,234)
#credit_card2 = (1234123412341234,'sak brro',425,234)
#credit_cards = [credit_card1,credit_card2]
#print(credit_cards)



#Unpacking Tuple

#person = ('babu',13,'pizza')
#(name,age,favfood) = person

#print(name)
#print(age)
#print(favfood)


# Gives error bcauz second person delets first #one
#person = ('babu',13,'pizza')
#person = (name,age,favfood)

#print(name)
#print(age)
#print(favfood)


#person = ('babu',13,'pizza')
#name,age,favfood = person

#print(name)
#print(age)
#print(favfood)


person1 = ("Nancy-pants",25,'pizza')
person2 = ("Joe-shirt",20,'pasta')

people = [person1,person2]

for name, age ,favfood in people:
  print(name)
  print(age)
  print(favfood)
  print()
