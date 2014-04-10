#ALGORITM
#1.Check horizontal
#first row   second row  third row
#[0][0]      [1][0]      [2][0]
#[0][1]      [1][1]      [2][1]
#[0][2]      [1][2]      [2][2]
#------------------------------------ 
#2.Check vertical
#fst clmn    scnd clmn   thrd clmn
#[0][0]      [0][1]      [0][2]
#[1][0]      [1][1]      [1][2]
#[2][0]      [2][1]      [2][2]
#------------------------------------    
#3.Check diagonal
#-first case            #-second case
# x                     #     x
#   x                   #   x
#     x                 # x
#[0][0]                 #[0][2]
#[1][1]                 #[1][1]
#[2][2]                 #[2][0]
 
[".X.",".X.",".X."] #vertical middle
["...","XXX","..."] #horizontal middle
["X..",".X.","..X"] #diagonal middle
 
def checkio(game_result):
#initial data
    xrow=[]
    orow=[]
    xcol=[]
    ocol=[]
    xdiag=[]
    odiag=[]
#list for final result
    fin=[]
#HORIZONTAL FUN
    for item in game_result:
        cntXinRow=item.count('X')
        xrow.append(cntXinRow)
        cntOinRow=item.count('O')
        orow.append(cntOinRow)
    #print xrow,orow
    if 3 in xrow:
        fin.append('X')
    elif 3 in orow:
        fin.append('O')
    elif (3 in xrow) and (3 in orow):
        fin.append('D')
    else:
        fin.append('D')
     
#VERTICAL FUN
#1.Making the list to store column values
    #initial additional empty lists and counter
    b=[]
    c=[]
    k=0
    while k<3:
        for item in range(len(game_result)):
            b.append(game_result[item][k])
        b=''.join(b)
        c.append(b)
        b=[]
        k+=1
#now we have 3 colums stored in c 
#2.Counting column values
    for item in c:
        cntXinCol=item.count('X')
        xcol.append(cntXinCol)
        cntOinCol=item.count('O')
        ocol.append(cntOinCol)
    #print xcol,ocol
    if 3 in xcol:
        fin.append('X')
    elif 3 in ocol:
        fin.append('O')
    elif (3 in xcol) and (3 in ocol):
        fin.append('D')
    else:
        fin.append('D')
 
#DIAGONAL FUN
#1.One diagonal
    #initial additional empty lists and counter
    b=[]
    c=[]
    k=2
    for item in range(len(game_result)):
        b.append(game_result[item][item])
    b=''.join(b)
    c.append(b)
    b=[]
#2.Second diagonal
    for item in range(len(game_result)):
        b.append(game_result[item][k])
        k-=1
    b=''.join(b)
    c.append(b)
 
#3.Counting diagonal values
    for item in c:
        cntXinDiag=item.count('X')
        xdiag.append(cntXinDiag)
        cntOinDiag=item.count('O')
        odiag.append(cntOinDiag)
    #print xdiag,odiag
    if 3 in xdiag:
        fin.append('X')
    elif 3 in odiag:
        fin.append('O')
    elif (3 in xdiag) and (3 in odiag):
        fin.append('D')
    else:
        fin.append('D')
 
#taking final decision based on vertical, horizontal and diagonal
    if 'X' in fin:
        return 'X'
    elif 'O' in fin:
        return 'O'
    else:
        return 'D'
     
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"
