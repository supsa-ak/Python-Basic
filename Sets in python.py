#s =  {'blueberry','rasberry'}
#print(s)

#s.add('strawberry')
#print(s)

#s.add('blueberry')
#print(s)


#list_of_numbers = [1,2,3,3,4,4,4,5]
#no_duplicate_set = set(list_of_numbers)  
#no_duplicate_list = list(no_duplicate_set)
#list_of_numbers = no_duplicate_list
#print(list_of_numbers)

library_1 = {'Harry potter','Hunger games','Lord of rings'}

library_2 = {'Harry potter','Romeo and Juliet'}


#all_in_town = library_1.union(library_2)
#all_in_town = library_2.union(library_1)
#print(all_in_town)


#at_both_libraries = library_1.intersection(library_2)
#at_both_libraries = library_2.intersection(library_1)
#print(at_both_libraries)

diff_1 = library_1.difference(library_2)
diff_2 = library_2.difference(library_1)
print(diff_1)
print(diff_2)
