row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))

a = int(position/10)
b = int(position-a*10)

a=a-1
b=b-1

if a == 0:
    map[b][a]="X"
elif a==1:
    map[b][a]="X"
else:
    map[b][a]="X"
   

print(f"{row1}\n{row2}\n{row3}")
