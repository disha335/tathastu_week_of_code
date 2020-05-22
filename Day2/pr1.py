sum=0
n=int(input('Enter a number'))
if n%2==0:
    print('This number is even')
else:
    print('This number is odd')
a=2
k=n//2
while k>=a:
    if n%a==0:
        print(' Not a Prime number')
    a=a+1
    k=n//a
print('Prime number')
while n>0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if n==sum:
    print('Palindrome number')
else:
    print('Not a palindrome number')
c=n
while c>0:
    r=c%10
    sum=sum+r**3
    c=c/10
if n==sum:
    print('Armstrong number')
else:
    print('Not armstrong')

