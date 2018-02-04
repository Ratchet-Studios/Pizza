# Pizza represented as 2D array
# Each cell contains either a (M)ushroom or a (T)omato
# A slice has no holes and is rpresented by two rows and columns
# Slices must contain L cells of each ingredient and at most H in total
# No overlapping

#Final Code:





#Boyd's Workspace


file = open("example.in")
PIZZA = []
MIN_TOPPINGS = 0
MAX_CELLS = 0
is_first_line = True
for line in file:
    if is_first_line:
        data = line.split(" ")

        is_first_line = False
    PIZZA.append([])
    for index in range(len(line)):
        PIZZA[index].append(line[index])





#Stu




#Luc