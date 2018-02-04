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
for row_index, row in enumerate(file):
    if is_first_line:
        data = row.split(" ")
        MIN_TOPPINGS = int(data[2])
        MAX_CELLS = int(data[3].strip())
        is_first_line = False
    else:
        PIZZA.append([])
        for char_index, char in enumerate(row):
            if char_index < len(row)-1:
                PIZZA[row_index-1].append(char)

for row in PIZZA:
    print(str(row))



#Stu




#Luc