### 
### Author: Jordan Walker
### Course: CSc 110
### Description: This program takes a character and a shape from the user 
###              and displayes that shape made out of that character.
###

def down(character):
    i = 11
    e = 0
    while i >0:
        print(" " * (e) + str(character) * i)
        i -= 2
        e+=1
def up(character):
    i = 1
    e = 5
    while i<12:
        print(" "*(e)+str(character)*i)
        i+=2
        if e>0:
            e-=1
def line(amount):
    i=0
    while i<amount:
        print("|---------|")
        i+=1
shape = str(input("Enter shape to display:\n"))
tile = str(input("Enter arrow character:\n"))
row = int(input("Enter row-area height:\n\n"))
if shape == "house":
    up(tile)
    line(row)
elif shape =="plumbbob":
    up(tile)
    line(row)
    down(tile)
elif shape=="hourglass":
    down(tile)
    up(tile)
