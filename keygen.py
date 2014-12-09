#Key generator
#Generates a unique key for your apps to use based on a simple random text algorithm
#author :terrameijar

import random

#num = 6 #number of characters to generate
try:
    a = int(raw_input("How long[characters] do you want your password to be? "))
    if a == 0:
    	print("Then what's the point of using a password generator in the first place huh?")
    	quit()
    else:    	
        num = a
        key = ""
        key = key + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #ensures that the first letter is always in caps
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ!@#$%^&*()_+'
        for letter in range(num-1):
    	    key += random.choice(letters)
        print ('random letter:'  + str(key))

except ValueError:
	print("Please enter a valid number next time")