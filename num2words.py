num = {
    1 : 'one',2 : 'two',3 : 'three',4 : 'four',5 : 'five',6 : 'six',7 : 'seven',8 : 'eight',9 : 'nine',10 : 'ten',11 : 'eleven',12 : 'twelve',13 : 'thirteen',14 : 'fourteen',15 : 'fifteen',16 : 'sixteen',17 : 'seventeen',18 : 'eighteen',19 : 'nineteen',20 : 'twenty',30 : 'thirty',40 : 'fourty',50 : 'fifty',60 : 'sixty',70 : 'seventy',80 : 'eighty',90 : 'ninty',100 : 'hundred',1000 : 'thousand'
}

hnum = [100,200,300,400,500,600,700,800,900]

n = int(input("Enter Number : "))

if n in num:
    print("num2words :",num[n].capitalize())
else:
    if n in hnum:
        print("num2words :",num[n//100],"Hundred")
    elif n>100:
        m = n//10 
        m = m%10
        if m==0:
            print("num2words :",num[n//100].capitalize()+num[100].capitalize()+num[n%10].capitalize())
        elif n%10==0:
            print("num2words :",num[n//100].capitalize()+num[100].capitalize()+num[m*10].capitalize())
        elif n%100 in num:
            print("num2words :",num[n//100].capitalize()+num[100].capitalize()+num[n%100].capitalize())
        else:
            print("num2words :",num[n//100].capitalize()+num[100].capitalize()+num[m*10].capitalize()+num[n%10].capitalize())
    else:
        print("num2words :",num[n-n%10].capitalize()+num[n%10].capitalize())