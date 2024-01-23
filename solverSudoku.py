board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            if j == 8 :
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) #returns the pos of the empty
    return None

def valid (bo,num,pos):
    #check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #check the column
    for j in range (len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    #turns the 9x9 to a 3x3 where x,y is the start of 3x3
    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3, box_x*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def solve_board(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10): #backtracking occurs here with recursion
        if (valid(bo,i, (row,col))):
            bo[row][col] = i
            if solve_board(bo):
                return True
            bo[row][col] = 0
    return False
    #if a solution is valid,it replaces the square with the valid number and it continues to the next square
    #if there is an invalid input during recursion, it doesn't change the square and leaves it at 0 and goes back to the previous changed square
    #since there was an invalid input, it means the previous square was incorrect. so what happens is that the square gets put back to 0 and continues getting values from the for loop
    #This continues until a correct valid input into the square.
    #this is backtracking as if the program finds a square invalid, it goes back to the previous square and tries a different value. 

print_board(board)
solve_board(board)
print("--------------------------------------------")
print_board(board)

