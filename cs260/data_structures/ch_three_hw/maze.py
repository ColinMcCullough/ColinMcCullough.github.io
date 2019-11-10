from stack import Stack


def getmaze():
    '''returns maze text file'''
    file = open('maze.txt','r')
    x = file.read()
    return x.split('\n')  

def str_list(string):
    '''converts string to list'''
    return list(string)

def list_str(lst):
    '''converts list to string'''
    return ''.join(lst)

def update_maze(maze,row,col):
    '''adds trail on maze of previous positions'''
    string_lst = str_list(maze[row])
    string_lst[col] = '.'
    maze[row] = list_str(string_lst)

def run_maze(maze):
    '''main maze run function, returns solution'''
    stack = Stack()
    numrows = len(maze)
    numcols = len(maze[0])
    curr_row,curr_col = 1,0
    postions = ((-1,0),(0,1),(1,0),(0,-1))
    found = False

    while not found:
        for i in range(0,4):
            searchrow,searchrcol = curr_row + postions[i][0], curr_col + postions[i][1] 
            if searchrow in range(numrows) and searchrcol in range(numcols):
                if maze[searchrow][searchrcol] == '0':
                    stack.push([searchrow,searchrcol])
                elif maze[searchrow][searchrcol] == 'X':
                    stack.push([searchrow,searchrcol])
                    found = True
        update_maze(maze,curr_row,curr_col)
        current_pos = stack.pop()
        curr_row,curr_col = current_pos[0], current_pos[1]

    return current_pos

def main():
    maze = getmaze()
    solution = run_maze(maze)
    print(f'Solution found{solution}')

main()