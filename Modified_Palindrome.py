# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# my_str = "_!E#@y#k"

# To take input from the user
my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

""" Function to check if it is possible to 
convert the string into palindrome """
def checkPalindrome(str) :
	
	n = len(str) 
	
	# Counting number of characters that should be changed. 
	count = 0
	for i in range(0, int(n / 2)) : 
		if (str[i] != str[n - i - 1]) : 
			count = count + 1
	
	# If count of changes is less than or equal to 1 
	if(count <= 1) : 
		return True
	else : 
		return False

# Driver Code
str = no_punct
if (checkPalindrome(str)) : 
	print ("Yes") 
else : 
	print ("No")