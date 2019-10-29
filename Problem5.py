def reverseWords(input): 
	inputWords = input.split(" ") 
	inputWords=inputWords[-1::-1] 
	output = ' '.join(inputWords)
	return output 
if __name__ == "__main__":
	a=str(input("Enter a phrase or a sentence: "))
print (reverseWords(a))