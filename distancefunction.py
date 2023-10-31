#basic word distance calculator

def wdistance(x,y):
	#Match the length of the words
	while len(x)<len(y):
		x = x+"-"
		#print("concatenating x")

	while len(y)<len(x):
		y = y+"_"
		#print("concatenating y")

	#set loop variables
	#print("preparing to calculate n=",len(x))
	n=len(x)
	d=0
	i=0

	#calculate distance
	while i<n:
		print("This is iteration",i,"of the loop")
		print("Distance is currently:",d)
		print("Testing",x[i],"vs",y[i])
		if x[i]!=y[i]:
				print("Adding:",2**(-i-1))
				
				d=d+2**(-i-1)
				print('Current Total:',d)
				print("----------")
				i+=1
		else:
			print('Current Total:',d)
			print("----------")
			i+=1
	print("The final distance is",d)
	return(d)


#loop until done
##while again == 'y':
	#gather input
#	a=input()
#	print("Second word?")
#	b=input()

	#calculate
#	d=wdistance(a,b)

	#output
#	print("The distance between",a,"and",b,"is",d)
#	again=input('Again?')


