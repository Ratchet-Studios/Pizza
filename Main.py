# Pizza represented as 2D array
# Each cell contains either a (M)ushroom or a (T)omato
# A slice has no holes and is represented by two rows and columns
# Slices must contain L cells of each ingredient and at most H in total
# No overlapping

# the TO-DO list:

import math
import sys
# Final Code:
import math


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
        self.MT_ratio = self.TOT_MUSHROOMS / self.TOT_TOMATOES
        self.used = []
        for i in range(len(self.PIZZA)):
            self.used.append([])
            for j in range(len(self.PIZZA[i])):
                self.used[i].append(False)

        self.prime_factors = self.get_factors(self.MAX_CELLS)

    def get_factors(self, num):
        returner = []
        for possible_factor in range(1, num + 1):
            if num % possible_factor == 0:
                returner.append(possible_factor)
        return returner

    def print_all(self):
        print("Pizza=")
        for row in self.PIZZA:
            print(str(row))
        print("mushrooms={0}, tomatoes={1}, max_cell_size={2}, min_toppings={3}, prime_factors={4}".format(
            self.TOT_MUSHROOMS, self.TOT_TOMATOES, self.MAX_CELLS, self.MIN_TOPPINGS, self.prime_factors))
        self.print_used()

    def print_used(self):
        print("self.used=")
        for row in self.used:
            print(str(row))

    # TODO add checks to ensure slices cannot overlap
    def get_slice(self, row_from, row_to, col_from, col_to):
        """ Returns the cut of our pizza & marks the proper cells as being used
            NOTE: The rows and columns given as parameters ARE INCLUDED in the final pizza slice
            returns -1 if is_valid = False"""
        if (pizza.is_valid_slice(row_from, row_to, col_from, col_to)):
            """The bug came from me assuming used[rows_from_to][cols_from_to] would get the correct 2d array.
            Instead, used[rows_from_to] returns a 2d list of the correct rows, so calling
            used[rows_from_to][cols_from_to] will just get the correct rows, and then get a splice of those rows, not
            the elements in each row"""

            for row_index, row in enumerate(self.used[row_from:row_to + 1]):
                for col_index, col in enumerate(row[col_from:col_to + 1]):
                    self.used[row_index][col_index] = True
            return self.PIZZA[row_from:row_to + 1][col_from:col_to + 1]
        return -1

    def get_height(self):
        return len(self.PIZZA)

    def get_width(self):
        return len(self.PIZZA[0])

    def is_valid_slice(self, row_from, row_to, col_from, col_to):
        '''Ensure slices are valid, do not overlap and contain the correct number of ingredients'''

        # Slice isn't outside of the pizza
        if row_from < 0 or row_to >= pizza.get_height() or col_from < 0 or col_to >= pizza.get_width():
            return False

        # Correct number of ingredients
        num_mushrooms, num_tomatoes = 0, 0
        for row_index, row in enumerate(self.PIZZA[row_from:row_to + 1]):
            for col_index, col in enumerate(row[col_from:col_to + 1]):
                if (self.PIZZA[row_index][col_index] == 'T'):
                    num_tomatoes += 1
                else:
                    num_mushrooms += 1
        if num_tomatoes < pizza.MIN_TOPPINGS or num_mushrooms < pizza.MIN_TOPPINGS or num_tomatoes + num_mushrooms > pizza.MAX_CELLS:
            return False

        # check for overlaps
        for row in self.used[row_from:row_to + 1]:
            for col in row[col_from:col_to + 1]:
                if (col):
                    return False

        return True

    # TODO add checks to ensure slices cannot overlap
    def get_slice(self, row_from, row_to, col_from, col_to, should_mark_as_used=True):
        """ Returns the cut of our pizza & marks the proper cells as being used
            NOTE: The rows and columns given as parameters ARE INCLUDED in the final pizza slice
            returns -1 if is_valid = False"""
        assert self.is_valid_slice(row_from, row_to, col_from, col_to)
        if should_mark_as_used:
            for row_index, row in enumerate(self.PIZZA[row_from:row_to + 1]):
                for col_index, col in enumerate(row[col_from:col_to + 1]):
                    self.used[row_index][col_index] = True
        return [x[col_from:col_to + 1] for x in self.PIZZA[row_from:row_to + 1]]


def get_height(self):
    return len(self.PIZZA)


def get_width(self):
    return len(self.PIZZA[0])


file = open("example.in")
pizza = Pizza(file)


# pizza.print_all()



def validate_solution(slices):
    print('Solution\n')
    num_slices = 0
    print(num_slices)
    for slice in slices:
        # for every item in each slice count mushrooms and tomatoes and ensure that they are more than the minimum
        # and the sum is less than the maximum else invalidate and do not print, do not increment counter
        for row in range(slice[0], slice[2] + 1):
            for col in range(slice[1], slice[2] + 1):
                print('{} {} {} {}'.format(slice[0], slice[1], slice[2], slice[3]))
                num_slices+=1


# Boyd
# IDEA: start in top-left corner, place the larges block you can(try to keep the M-T ratio close to that of the PIZZA)

def calc_MT_ratio(slice):
    tot_M = 0
    tot_T = 0
    for row_index, row in enumerate(slice):
        for col_index, col in enumerate(row):
            if col == "M":
                tot_M += 1
            elif col == "T":
                tot_T += 1
    assert tot_T != 0, "slice=" + str(slice)
    return tot_M / tot_T


# Get every possible shape's dimensions, from 1x1 up to the max dictated by MAX_CELLS
shapes = []
for x in range(1, pizza.MAX_CELLS + 1):
    factors = pizza.get_factors(x)
    for factor_index in range(len(factors)):
        if (factors[factor_index], factors[-(factor_index + 1)]) not in shapes:
            shapes.append((factors[factor_index],
                           factors[-(factor_index + 1)]))
print("shapes={}".format(shapes))

for row_index, row in enumerate(pizza.PIZZA):
    for col_index, col in enumerate(row):
        if pizza.used[row_index][col_index]:
            continue
        slice_indexes = []
        # find all the valid slices
        for shape in shapes:
            if pizza.is_valid_slice(row_index, row_index + shape[0], col_index, col_index + shape[1]):
                slice_indexes.append((row_index, row_index + shape[0], col_index, col_index + shape[1]))

        # Greedily select the best piece, looking for a M:T ratio similar to that of the entire pizza
        best_ratio = pizza.MT_ratio * 10  # just an arbitrarily choose a bad ratio
        best_slice_indexes = []
        for slice_index in slice_indexes:
            ratio = calc_MT_ratio(pizza.get_slice(
                slice_index[0], slice_index[1], slice_index[2], slice_index[3], should_mark_as_used=False))
            # normalise the slice's M:T ratio to be the same (either <=1 or >1) as the pizza M:T ratio
            if pizza.MT_ratio > 1 >= ratio or ratio <= 1 < pizza.MT_ratio:
                ratio = 1 / ratio
            if abs(pizza.MT_ratio - ratio) < abs(pizza.MT_ratio - best_ratio):
                best_ratio = ratio
                best_slice_indexes = slice_index
        print("best_slice for PIZZA[{}][{}] = {}".format(row_index, col_index, best_slice_indexes))
        if best_slice_indexes != []:
            # mark the best slice as being 'used' on the pizza so that it won't be overlapped next time
            pizza.get_slice(best_slice_indexes[0], best_slice_indexes[1], best_slice_indexes[2], best_slice_indexes[3])
print("\n\n\nprint_all")
pizza.print_all()
print("\n\n\nSTU")

# Stu


STR_LIMITING_INGREDIENT = 'T'
remaining_tomatoes = pizza.TOT_TOMATOES
remaining_mushrooms = pizza.TOT_MUSHROOMS

if remaining_mushrooms < remaining_tomatoes:
    STR_LIMITING_INGREDIENT = 'M'
else:
    STR_LIMITING_INGREDIENT = 'T'
slices = []
for y in range(pizza.get_height()):
    for x in range(pizza.get_width()):
        if pizza.used[y][x]:
            continue

        # potential slice dimensions
        xstart = x
        xend = x
        ystart = y
        yend = y
        while (xend - xstart + 1) * (yend - ystart + 1) < pizza.MAX_CELLS:

            # option 1: do nothing
            tomatoes = 0
            mushrooms = 0

            for y2 in range(ystart, yend + 1):
                for x2 in range(xstart, xend + 1):
                    if pizza.PIZZA[y2][x2] == 'T':
                        tomatoes += 1
                    elif pizza.PIZZA[y2][x2] == 'M':
                        mushrooms += 1

            # the difference between remaining tomatoes and remaining mushrooms if we choose option 1
            option_1_difference = math.fabs((remaining_tomatoes - tomatoes) - (remaining_mushrooms - mushrooms))

            # option 2: move one across
            xend += 1
            if xend >= pizza.get_width() or pizza.used[yend][xend] or (
                            (xend - xstart + 1) * (yend - ystart + 1) > pizza.MAX_CELLS):
                option_2_difference = sys.maxsize  # can't do this option
            else:
                tomatoes = 0
                mushrooms = 0

                for y2 in range(ystart, yend + 1):
                    for x2 in range(xstart, xend + 1):
                        if pizza.PIZZA[y2][x2] == 'T':
                            tomatoes += 1
                        elif pizza.PIZZA[y2][x2] == 'M':
                            mushrooms += 1

                # the difference between remaining tomatoes and remaining mushrooms if we choose option 2
                option_2_difference = math.fabs((remaining_tomatoes - tomatoes) - (remaining_mushrooms - mushrooms))

            xend -= 1  # undo the change while we test option 3

            # option 3: move one down
            yend += 1
            if yend >= pizza.get_height() or pizza.used[yend][xend] or (
                            (xend - xstart + 1) * (yend - ystart + 1) > pizza.MAX_CELLS):
                option_3_difference = sys.maxsize  # can't do this option
            else:
                tomatoes = 0
                mushrooms = 0

                for y2 in range(ystart, yend + 1):
                    for x2 in range(xstart, xend + 1):
                        if pizza.PIZZA[y2][x2] == 'T':
                            tomatoes += 1
                        elif pizza.PIZZA[y2][x2] == 'M':
                            mushrooms += 1

                # the difference between remaining tomatoes and remaining mushrooms if we choose option 3
                option_3_difference = math.fabs((remaining_tomatoes - tomatoes) - (remaining_mushrooms - mushrooms))

            yend -= 1  # undo the change

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

        tomatoes = 0
        mushrooms = 0

        for y2 in range(ystart, yend + 1):
            for x2 in range(xstart, xend + 1):
                pizza.used[y2][x2] = True
                if pizza.PIZZA[y2][x2] == 'T':
                    tomatoes += 1
                elif pizza.PIZZA[y2][x2] == 'M':
                    mushrooms += 1

        remaining_mushrooms -= mushrooms
        remaining_tomatoes -= tomatoes

        slices.append([ystart, xstart, yend, xend])
        print("sliced between rows (" + str(ystart) + "," + str(yend) + ") and columns (" + str(xstart) + "," + str(
            xend) + ")")

validate_solution(slices)
