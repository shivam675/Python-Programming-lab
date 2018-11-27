from easygui import *
import sys
m=0


while 1:
    msg ="This Is A Universal Financial Operator(UFO)"
    title = "Categories"
    choices = ["Percent profit Calculator","Simple Interest Calculator", "Compound Interest Calculator","EMI Calculator","EXIT"]
    image="UFO.png"
    choice = buttonbox(msg,image=image,choices=choices)


     
    if choice=="Simple Interest Calculator":
        msg ="Input all * marked values"
        title = "Simple Intrest Calculator"
        q1=["Enter Your Principal Amount Number*"]
        q2=["Enter Your Rate of Intrest*"]
	q3=["Enter number of years*"]
	z=[q1,q2,q3]
	f=multenterbox(msg,title,z)
	q1=float(f[0])
	q2=float(f[1])
	q3=float(f[2])
        q4=(q1*q2*q3)/100
        print(q4)
        msgbox("Your simple intrest: " + str(q4))
    
   
    elif choice=="Compound Interest Calculator":
         msg ="Input all * marked values"
         title = "Compound Intrest Calculator"
         p=["Enter Your Principal Amount Number*"]
         r=["Enter Your Rate of Intrest*"]
	 t=["Enter number of years*"]
	 n=["Enter number of compounding periods per years*"]
	 z=[p,r,t,n]
	 f=multenterbox(msg,title,z)
	 p=float(f[0])
	 r=float(f[1])
	 t=float(f[2])
	 n=float(f[3])
         r=r/100
         q1=r/n
         q2=1+q1
         q3=n*t
         q4=q2**q3
         a=p*q4
         print(q1)
         print(q2)
         print(q3)
         print(q4)
         print(a)
         msgbox("Your Compund intrest : " + str(a))
   
    elif choice=="Percent profit Calculator":
        msg ="Input all * marked values"
        title = "Percent profit Calculator"
        cp=["Enter Cost Price*"]
	sp=["Enter Selling Price*"]
	ans=[""]
	z=[cp,sp]
	f=multenterbox(msg,title,z)	
	cp=float(f[0])
	sp=float(f[1])
	diff=sp-cp
	div=diff/cp
	answer=div*100
	ans=answer
           
        msgbox("Your Profit Percentage is : " + str(answer))

    elif choice=="EMI Calculator":
        msg ="Input all * marked values"
        title = "EMI Calculator"
        p=["enter Principle*"]
	r=["enter Rate of Interest*"]
	n=["enter Time Period*"]
	z=[p,r,n]
	f=multenterbox(msg,title,z)
	p=float(f[0])
	r=float(f[1])
	n=float(f[2])
	r=r/1200
	q=1+r
	q1=q**n
	t=p*r*q1
	deno=q1-1
	a=t/deno
	
	print(a)
        msgbox("Your Monthly EMI Is: " + str(a))

    else:
        sys.exit(0)


    
    










