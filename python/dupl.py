def dubli(A):
	temp=[]
	if len(A) >0:
		temp=[A[0]]
	for i in range(len(A)):
		if len(temp) > 0 and temp[len(temp)-1]!= A[i]:
			temp.append(A[i])

	print(temp)

dubli([5,5,6,7,10,5])