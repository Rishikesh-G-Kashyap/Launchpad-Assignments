def Remove(duplicate): 
	final_list = [] 
	for num in duplicate: 
		if num not in final_list: 
			final_list.append(num) 
	return final_list 
	  
# Driver Code 
duplicate = [1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3] 
print(Remove(duplicate))