grid=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

crd=[]
cnt=0
def search(x, y):
    if grid[x][y]==2:
        print 'found at %d,%d' % (x, y)
        crd.append((x,y))
        return True
    elif grid[x][y] == 1:
        print 'wall at %d,%d' % (x, y)
        return False
    elif grid[x][y] == 3:
        print 'visited at %d,%d' % (x, y)
        return False
    
    print 'visiting %d,%d' % (x, y)

    # mark as visited and add coord to the list
    grid[x][y] = 3
    crd.append((x,y))

    # explore neighbors clockwise starting by the one on the right(S->W->N->E)
    if ((x < len(grid)-1 and search(x+1, y))        #South
        or (y > 0 and search(x, y-1))               #West
        or (x > 0 and search(x-1, y))               #North
        or (y < len(grid)-1 and search(x, y+1))):   #East
        return True
    print 'Blocked place %d, %d'%(x,y)
    return False

def checkio(grid):
    stack = []
    way=[]
    search (1,1)
    for i in range(len(crd)):
        stack.append(crd[i])
        if i==(len(crd)-1):
            break
        elif crd[i+1][1]>stack[0][1]:
            way.append('E')
            stack.pop()
        elif crd[i+1][1]<stack[0][1]:
            way.append('W')
            stack.pop()
        elif crd[i+1][0]>stack[0][0]:
            way.append('S')
            stack.pop()
        elif crd[i+1][0]<stack[0][0]:
            way.append('N')
            stack.pop()
    way=''.join(way)
    return way
    
print checkio(grid)
