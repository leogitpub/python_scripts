stra= "01000111011001010110010101101011011100110110011001101111011100100100011101100101011001010110101101110011"
stra =  stra[0:]
message = ""
while stra != "":
    i = chr(int(stra[:8], 2))
    message = message + i
    stra = stra[8:]
print(message)


# initializing string

test_str = "A "


# printing original string

print("The original string is : " + str(test_str))


# using join() + ord() + format()
# Converting String to binary

res ='0'+('0'.join(format(ord(i), 'b') for i in test_str))


# printing result

print("The string after binary conversion : " + str(res))
