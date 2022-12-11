# Python program to check if
# given mobile number is valid
import re

def isValid(s):
	
	# 1) Begins with 0 or 91
	# 2) Then contains 6,7 or 8 or 9.
	# 3) Then contains 9 digits
	Pattern = re.compile("("+"|1)?[212]{3}?[456]{3}?[7890]{4}?")
	return Pattern.match(s)

# Driver Code
s = "12124567890"
if (isValid(s)):
	print ("Valid Number")	
else :
	print ("Invalid Number")
