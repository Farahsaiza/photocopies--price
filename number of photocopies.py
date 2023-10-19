N=int(input("enter the number of photocopies "))
if N<= 10:
    P=N* 0.30
    print("The total amount  is: ",P,"DH")
elif N>10 and N <=20 :
    P= 10* 0.30 + (N-10)*0.25
    print("The total amount is : ",P,"DH")
else:
    P= 10*0.30+20*0.25+(N-30)*0.20
    print("The total amount is: ", P,"DH")
