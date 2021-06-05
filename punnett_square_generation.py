from turtle import *

def write_text(text, text_color, direction="centre", size=40):
    color(text_color)
    write(text, align=direction, font=("Arial", size, "normal"))
    
##printing title
def print_title():
  setposition(0,170)
  write_text("Punnett Square Representation of Tay Sachs", "black", "center", 15)
    
    
##Making four square board for punnett square
speed(5)
penup()
setposition(-100,-100)
pendown()
for i in range(2):
    for i in range(4):
        forward(100)
        left(90)
    forward(100)
penup()
setposition(-100,0)
pendown()
for i in range(2):
    for i in range(4):
        forward(100)
        left(90)
    forward(100)
penup()

##Getting Parent alleles and printing them along the punnett square
setposition(-50,110)
genotype1= input("What are the first parents alleles?")
write_text(genotype1[0], "blue")
setposition(50,110)
write_text(genotype1[1],"blue")


setposition(-150,30)
genotype2= input("What are the second parents alleles?")
write_text(genotype2[0], "pink")
setposition(-150,-70)
write_text(genotype2[1],"pink")


print_title()