import time
import subprocess as sp
import os
output = sp.getoutput('whoami --version')
print (output)
var = 1
cipherChoice = input("Enter your Cipher Choice Enc or Dec: ")
print(cipherChoice)
inFile = input("Input file path")
outFile = input("Output file path")
if (cipherChoice == "enc"):
    cipherKey = input("Enter your cipher key :")
    initialVector = input("Enter Initialization Vector: ")
    venki = 'openssl enc -aes-256-cbc -base64 -in\t' + str(inFile) +'\t -out\t' + str(outFile) +'\t-k\t' + str(cipherKey)  + '\t-iv\t' + str(initialVector)
    f= open("tmp.sh","w+")
    f.write(venki)
    f.close()
    output = sp.getoutput('sh ./tmp.sh')
    print (output)
elif (cipherChoice == "dec"):
    cipherKey = input("Enter your cipher key :")
    initialVector = input("Enter Initialization Vector")
    venki = 'openssl enc -aes-256-cbc -base64 -in ii -out gy -d -k\t' + str(cipherKey)  + '\t-iv\t' + str(initialVector)
    f= open("tmp.sh","w+")            
    f.write(venki)                         
    f.close()
else: 
  print('ssh')
