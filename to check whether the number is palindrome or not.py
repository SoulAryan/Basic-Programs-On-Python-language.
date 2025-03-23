a=int(input("Enter a number="))
rev=0
num=a

while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10

if(a==rev):
    print("Entered number is palindrome",rev)
    
else:
    print("Entered number is not palindrome",rev)


