import time
try: 

    from googlesearch import search 

except ImportError:  

    print("No module named 'google' found") 

  
# to search 
a=1
query = input("Enter your search")
  

for j in search(query, tld="co.in", num=30, stop=30, pause=20): 
    a=a+1
    time.sleep(1)
    print(str(a)+ "  " + j) 
