num1 = float(input('Enter a Number: '))
num2 = float(input('Enter a Number: '))
num3 = float(input('Enter a Number: '))
avg = (num1 + num2 + num3) / 3
print ('The average of these numbers is', avg)
if avg > num1 and avg > num2 and avg > num3:
    print ('%f is higher than %f, %f, %f.' %(avg, num1, num2, num3))
elif avg > num1 and avg > num2:
    print ('%f is higher than %f, %f.' %(avg, num1, num2))
elif avg > num1 and avg > num3:
    print ('%f is higher than %f, %f.' %(avg, num1, num3))
elif avg > num2 and avg > num3:
    print ('%f is higher than %f, %f.'%(avg, num2, num3))
elif avg > num1:
    print ('%f is just higher than %f.' %(avg, num1))
elif avg > num2:
    print ('%f is just higher than %f.'%(avg, num2))
elif avg > num3:
    print ('%f is just higher than %f.'%(avg, num3))
else:
    print ('Invalid Input.')