# Pizza represented as 2D array
# Each cell contains either a (M)ushroom or a (T)omato
# A slice has no holes and is rpresented by two rows and columns
# Slices must contain L cells of each ingredient and at most H in total
# No overlapping

# the TO-DO list:
#todo figure out how to cut up pizza


#Final Code:





#Boyd's Workspace


file = open("example.in")
PIZZA = []
is_first_line = True
TOT_MUSHROOMS = 0
TOT_TOMATOES = 0
global MAX_CELLS
global MIN_TOPPINGS
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
                if char == "M":
                    TOT_MUSHROOMS += 1
                elif char == "T":
                    TOT_TOMATOES += 1

def print_pizza():
    for row in PIZZA:
        print(str(row))
    
    
used = []
for i in range(len(PIZZA)):
    used.append([])
    for j in range(len(PIZZA[i])):
        used[i].append(False)

def print_used():
    for row in used:
        print(str(row))




#Stu




#Luc