# Pizza represented as 2D array
# Each cell contains either a (M)ushroom or a (T)omato
# A slice has no holes and is represented by two rows and columns
# Slices must contain L cells of each ingredient and at most H in total
# No overlapping

# the TO-DO list:

import math
import sys


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
        for row_index, row in enumerate(self.used[row_from:row_to + 1][col_from:col_to + 1]):
            for col_index, col in enumerate(self.used[row_from:row_to + 1][col_from:col_to + 1]):
                self.used[row_index][col_index] = True
        return self.PIZZA[row_from:row_to + 1][col_from:col_to + 1]

    def get_height(self):
        return len(self.PIZZA)

    def get_width(self):
        return len(self.PIZZA[0])


file = open("example.in")
pizza = Pizza(file)
pizza.print_all()

# Boyd
# IDEA: start by creating all the smallest slices you can, from there start adding rows/columns to each piece

row_start = -1
col_start = -1
have_slice = False
slices = []
for row_index, row in enumerate(pizza.PIZZA):
    for col_index, topping in enumerate(row):
        if have_slice:
            if pizza.PIZZA[row_start][col_start] != topping:
                # todo also check that the requested slice hasn't already been taken
                slices.append(pizza.get_slice(row_start, row_index, col_start, col_index))
                have_slice = False
            elif row_start + 1 < pizza.get_height():
                if pizza.PIZZA[row_start][col_start] == pizza.PIZZA[row_start + 1][col_start]:
                    # todo also check that the requested slice hasn't already been taken
                    slices.append(pizza.get_slice(row_start, row_start + 1, col_start, col_start))
                    have_slice = False

        else:
            row_start = row_index
            col_start = col_index
            have_slice = True
print("\n\n\n[BOYD]Result after making some slices:")
pizza.print_all()

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
			
		# potential slice dimensions
		xstart = x
		xend = x + 1
		ystart = y
		yend = y + 1
		while (True):
			
			# option 1: do nothing
			tomatoes = 0
			mushrooms = 0
			
			for y in range(ystart, yend):
				for x in range(xstart, xend):
					if pizza.PIZZA[y][x] == 'T':
						tomatoes += 1
					elif pizza.PIZZA[y][x] == 'M':
						mushrooms += 1
			
			# the difference between remaining tomatoes and remaining mushrooms if we choose option 1
			option_1_difference = math.abs((remaining_tomatoes - tomatoes) - (remaining_mushrooms - mushrooms))
			
			# option 2: move one across
			xend += 1
			if xend == pizza.get_width():
				option_2_difference = sys.maxsize # can't do this option
			else:
				tomatoes = 0
				mushrooms = 0
				
				for y in range(ystart, yend):
					for x in range(xstart, xend):
						if pizza.PIZZA[y][x] == 'T':
							tomatoes += 1
						elif pizza.PIZZA[y][x] == 'M':
							mushrooms += 1
				
				# the difference between remaining tomatoes and remaining mushrooms if we choose option 2
				option_2_difference = math.abs((remaining_tomatoes - tomatoes) - (remaining_mushrooms - mushrooms))
			
			xend -= 1 # undo the change while we test option 3
			
			# option 3: move one down
			yend += 1
			if yend == pizza.get_height():
				option_3_difference = sys.maxsize # can't do this option
			else:
				tomatoes = 0
				mushrooms = 0
				
				for y in range(ystart, yend):
					for x in range(xstart, xend):
						if pizza.PIZZA[y][x] == 'T':
							tomatoes += 1
						elif pizza.PIZZA[y][x] == 'M':
							mushrooms += 1
				
				# the difference between remaining tomatoes and remaining mushrooms if we choose option 3
				option_3_difference = math.abs((remaining_tomatoes - tomatoes) - (remaining_mushrooms - mushrooms))
			
			yend -= 1 # undo the change
			
			# time to decide which opion to take
			# we want to minimize difference between the remaining mushrooms and remaining tomatoes
		
			if option_3_difference <= option_2_difference and option_3_difference <= option_1_difference:
				# option 3 wins! we're going to expand our slice one down!
				yend += 1
			elif option_2_difference <= option_1_difference:
				# option 2 wins! we're going to expand our slice one across!
				xend += 1
			else:
				# option 1 wins! we're not going to change our slice size
				break

# Luc
# TODO Split graph into tetris-style array.
pizza.MAX_CELLS
