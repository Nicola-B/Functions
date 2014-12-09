#Nicola Batty
#09/12/2014
#Functions spot check2

#define functions

def get_grid_row(a_row_length):
    # draws a single row using |_
    for each_square in range(a_row_length):
        this_row = '|_' * (a_row_length)
        # add closing | to row
        this_row = this_row + '|'
    return this_row

def display_grid(a_grid_size, a_row):
    # display top of grid using _ as top of each square
    print(' _' * a_grid_size)
    # display rows of |_| for each row
    for row_count in range(a_grid_size):
        print(a_row)

def get_grid_size():
    valid_grid = "false"
    while valid_grid == "false":
        this_grid_size = int(input("please enter the size of the grid(max 20): "))
        if this_grid_size <= 20:
            if this_grid_size >= 0:
                valid_grid = "true"
    return this_grid_size

# main program
grid_size = get_grid_size()
row_to_draw = get_grid_row(grid_size)
display_grid(grid_size, row_to_draw) 
