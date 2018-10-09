# Amstrong Program				
def AmsN (x):				# Function definition
   sum=0				# Initiating sum	
   t=x					# Temporary variable
   while (t>0):   			# initating while loop
      d=t%10				
      sum += d**3
      t = t//10
   if sum==x:
      return "Amstrong number"
   else:
      return "Not An Amstrong number"   
x=int(input("Enter Number"))
print(AmsN(x)) 
