# Pizza represented as 2D array
# Each cell contains either a (M)ushroom or a (T)omato
# A slice has no holes and is represented by two rows and columns
# Slices must contain L cells of each ingredient and at most H in total
# No overlapping

# the TO-DO list:
# todo figure out how to cut up pizza


# Final Code:
class Pizza(object):
    def __init__(self, file):
        is_first_line = True
        self.PIZZA = []
        self.TOT_MUSHROOMS = 0
        self.TOT_TOMATOES = 0
        for row_index, row in enumerate(file):
            if is_first_line:
                data = row.split(" ")
                self.MIN_TOPPINGS = int(data[2])
                self.MAX_CELLS = int(data[3].strip())
                is_first_line = False
            else:
                self.PIZZA.append([])
                for char_index, char in enumerate(row):
                    if char_index < len(row) - 1:
                        self.PIZZA[row_index - 1].append(char)
                        if char == "M":
                            self.TOT_MUSHROOMS += 1
                        elif char == "T":
                            self.TOT_TOMATOES += 1
        self.used = []
        for i in range(len(self.PIZZA)):
            self.used.append([])
            for j in range(len(self.PIZZA[i])):
                self.used[i].append(False)

        self.prime_factors = []
        for num in range(self.MAX_CELLS):
            if num % self.MAX_CELLS == 0:
                self.prime_factors.append(num)

    def print_all(self):
        print("Pizza=")
        for row in self.PIZZA:
            print(str(row))
        print("mushrooms={0}, tomatoes={1}, max_cell_size={2}, min_toppings={3}, prime_factors={4}".format(
            self.TOT_MUSHROOMS, self.TOT_TOMATOES, self.MAX_CELLS, self.MIN_TOPPINGS, self.prime_factors))
        self.print_used()

    def print_used(self):
        for row in self.used:
            print(str(row))

    def get_slice(self, row_from, row_to, col_from, col_to):
        # Returns the cut of our pizza & marks the proper cells as being used
        # NOTE: The rows and columns given as parameters ARE INCLUDED in the final pizza slice
        for row in self.used[row_from:row_to + 1][col_from:col_to + 1]:
            for col in self.used[row_from:row_to + 1][col_from:col_to + 1]:
                self.used[row][col] = True
        return self.PIZZA[row_from:row_to + 1][col_from:col_to + 1]
    
    def get_height(self):
        return len(self.PIZZA)
    
    def get_width(self):
        return  len(self.PIZZA[0])


file = open("example.in")
pizza = Pizza(file)
pizza.print_all()

# Boyd
# IDEA: start by creating all the smallest slices you can, from there start adding rows/columns to each piece

row_start = -1
col_start = -1
have_slice = False
for row_index, row in enumerate(pizza.PIZZA):
    for col_index, topping in enumerate(row):
        if have_slice:
            if pizza.PIZZA[row_start][col_start] != topping:
                pizza.get_slice(row_start, row_index, col_start, col_index)

        else:
            row_start = row_index
            col_start = col_index
            have_slice = True

# Stu

STR_LIMITING_INGREDIENT = 'T'
remaining_tomatoes = pizza.TOT_TOMATOES
remaining_mushrooms = pizza.TOT_MUSHROOMS

if remaining_mushrooms < remaining_tomatoes:
    STR_LIMITING_INGREDIENT = 'M'
else:
    STR_LIMITING_INGREDIENT = 'T'

for y in range(pizza.get_height()):
	for x in range(pizza.get_width()):
		if pizza.used[y][x]:
			continue
		
		while (True):
			# potential slice dimensions
			xstart = x
			xend = x + 1
			ystart = y
			yend = y + 1
			
			# option 1: do nothing
			tomatoes = 0
			mushrooms = 0
			
			for y in range()

   
   


# Luc
# TODO Split graph into tetris-style array.
pizza.MAX_CELLS
