print("Enter marks of 3 subjects: ")

sub1 = int(input("Sub 1: "))
sub2 = int(input("Sub 2: "))
sub3 = int(input("Sub 3: "))

total = ((sub1+sub2+sub3)/300)*100

if total>=40 and sub1>=33 and sub2>=33 and sub3>=33:
    print("Pass")
else:
    print("Fail")