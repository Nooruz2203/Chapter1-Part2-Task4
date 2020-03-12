print ("Number of hours for the first timestamp: ")
a = int(input())
print("Number of minutes for the first timestamp: ")
b = int(input())
print ("Number of hours for the second timestamp: ")
a1 = int(input())
print("Number of minutes for the second timestamp: ")
b1 = int(input())

c = ((a*360)+(b*60)+30)
c1 = ((a1*360)+(b1*60)+10)
y = c1 - c

print("Number of seconds for the first timestamp", c, "seconds")
print("Number of seconds for the second timestamp", c1, "seconds")

print("The number of seconds between them:", y)
