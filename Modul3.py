import os

os.system('cls') #clear screen
'''
for i in range(10):
    print("hello world")

for i in range(1, 10, 2): #går från ett till tio och ökar med två
    print(str(i+1) + " hello world")

i = int(input("välj ett tal "))
for i in range(1, i, 2): 
    print(str(i+1) + " hello world")

i = 0
while True:
    print("hängt")
    i = i + 1
    if i == 10:
        break
    #i += 1  samma sak
'''
    
for table in range(0, 12):
    for product in range(1, 11):
        print(f"Tabell {table+1}) {table+1} * {product} ={(table+1)*product}")