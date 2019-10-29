test_list = [1, 2, 3, 2, 0, 65, 21, 4, 2, 10] 
print (str(test_list)) 
res_list = [] 
for i in range(0, len(test_list)) : 
	if test_list[i] == 2 : 
		res_list.append(i) 
print (str(res_list)) 
