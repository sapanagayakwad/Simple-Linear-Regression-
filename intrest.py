# Take Principal (P) ,  Period (N) Years , Rate of intrest (R) %p.a.and

P= float(input("Pleae Enter The Principal In INR : "))
N= float(input("Pleae Enter The Period In Year : "))
R= float(input("Pleae Enter The Rate of Intrest  In %.p.a. :  "))



# calculate simple Intrest 

I= (P*N*R)/100


# calculaye  Amount 

A = P + I

# print above Result

print(f'simple intrest for given values is {I:.2f} INR ')
print(f'Amount is {A:.2f} INR')     


