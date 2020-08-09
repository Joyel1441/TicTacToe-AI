#Coded by Joyel
import random

print("Computer: O")
print("Player: X")
print("\n")
print("Who goes first: ")
print("1.Player goes first")
print("2.Computer goes first")
switch=0
t=0
while True:
    choice=int(input("Choice: "))
    print("\n")
    if choice == 1:
      print("Player goes first")
      switch=0
      break
    elif choice == 2:
      print("Computer goes first")
      switch=1
      break
    else:
      print("Enter number between 1 and 2")
  


boardx = [" + "," + "," + ",
         " + "," + "," + ",
         " + "," + "," + "]

def drawBoard(board,action=False,pos=0,symbol=" X "):
  
  
  if action==True:
      board[pos]=symbol
  
  print("\n") 
  print(board[0]+"|"+ board[1]+"|"+board[2])
  print("-----------")
  print(board[3]+"|"+ board[4]+"|"+board[5])
  print("-----------")
  print(board[6]+"|"+ board[7]+"|"+board[8])
  print("\n")
     
  return board
  
board = drawBoard(boardx)
positionsOccupied=[]
computerWins = False

def posCheck(pos,positionsOccupied=positionsOccupied):
  if pos in positionsOccupied:
    return 0
  else:
    positionsOccupied.append(pos)
    return 1
            
def evaluate(board):
  if checkWinner(" O ",board2=board):
    score = 1
    return score
  elif checkWinner(" X ",board2=board):
    score = -1
    return score
  elif checkBoardFullStatus() == 0:
    score = 0
    return score
  else:
    return None
     
     
def minimax(board,isMaximizing):
  score = evaluate(board)
  if score != None:
    return score
    
  if isMaximizing:
    bestScore = -10000
    for i in range(9):
      if board[i] == " + ":
        board[i] = " O "
        score = minimax(board,False)
        board[i] = " + "
        bestScore = max(score,bestScore)
    return bestScore
  else:
    bestScore = 10000
    for i in range(9):
      if board[i] == " + ":
        board[i] = " X "
        score = minimax(board,True)
        board[i] = " + "
        bestScore = min(score,bestScore)
    return bestScore
  
def computerGoesFirst():
  movesAvailable = [index for index,value in enumerate(board) if value==" + "]
  for letter in [" O "," X "]:
     for i in movesAvailable:
        boardCopy=board[:]
        boardCopy[i]=letter
        if checkWinner(symbol=letter,board2=boardCopy) == 1:
          k = i
          return k
  cornersOpen = []
  for i in movesAvailable:
    if i in [0,2,6,8]:
      cornersOpen.append(i)
  if len(cornersOpen) > 0:
    q = random.randrange(0,len(cornersOpen))
    return cornersOpen[q]
  if 4 in movesAvailable:
     k = 4
     return k 
  edgesOpen = []
  for i in movesAvailable:  
    if i in [1,3,5,7]:
      edgesOpen.append(i) 
  if len(edgesOpen) > 0:   
      q = random.randrange(0,len(edgesOpen))     
  return edgesOpen[q] 
    
  
def computeK():
  if computerWins == False:
     movesAvailable = [index for index,value in enumerate(board) if value==" + "]
     for i in movesAvailable:
        boardCopy=board[:]
        boardCopy[i]=" O "
        if checkWinner(symbol=" O ",board2=boardCopy) == 1:
          k = i
          return k 
  bestScore = -10000
  for i in range(9):
   if board[i] == " + ":
     board[i] = " O "
     score = minimax(board,False)
     board[i] = " + "
     if score > bestScore:
       bestScore = score
       k = i   
  return k    

def player(boardplayer=board,pos=0,symbolX=" X "):
   board=drawBoard(boardplayer,action=True,pos=pos,symbol=symbolX)

def computer(boardcomp=board,symbolO=" O "):
       if switch == 0:
          k = computeK()
       else:
          k = computerGoesFirst()
       posCheck(k)
       board=drawBoard(boardcomp,action=True,pos=k,symbol=symbolO)
         
          
def checkWinner(symbol,board2=[[],[],[]]): 
 win_states = [
 [board2[0],board2[3],board2[6]]
 ,[board2[1],board2[4],board2[7]]
  ,[board2[2],board2[5],board2[8]]
  ,[board2[0],board2[1],board2[2]]
  ,[board2[3],board2[4],board2[5]]
  ,[board2[6],board2[7],board2[8]]
  ,[board2[0],board2[4],board2[8]]
  ,[board2[2],board2[4],board2[6]]
  ]
 return [symbol,symbol,symbol] in win_states

def checkBoardFullStatus():
  if (board[0] != " + " and board[1] != " + " and
     board[2] != " + " and board[3] != " + " and
     board[4] != " + " and board[5] != " + " and 
     board[6] != " + " and board[7] != " + " and
     board[8] != " + "):
     return 0
  else:
    return 1
  
  

for turn in range(10):
  if checkBoardFullStatus() == 0:
    print("Draw")
    break
  w=0
  if turn%2 == switch:
    print("Your turn")
    while(True):
        while(True):      
            k=int(input("Enter position(1-9): "))  
            k=k-1              
            if k >= 0 and k <= 8:
              break
            else:
              print("Enter number between 1 and 9")
        z = posCheck(k)
        if z == 1:
            player(pos=k)
            boardCopy2 = board[:]
            w=checkWinner(symbol=" X ",board2=boardCopy2)
            break
        else:
          print("Position already occupied")
    if w==1:
      print("Player wins")
      break
  else:
    print("Computer's turn")
    computer()
    boardCopy3 = board[:]
    w=checkWinner(symbol=" O ",board2=boardCopy3)
    if w==1:
      print("Computer wins")
      computerWins = True
      break
      

 
