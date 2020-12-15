This is the implement of tree_baesd AI in a tic-tac-toe game.  
  
Rules: 
==
This game requires two players who hold x and o pieces respectively. The player who successfully places a certain number of pieces on the horizontal, vertical or diagonal successively is the winner. Compared with traditional tic-tac-toe games, the newly added rule is that, at the end of each turn, there is a 25% chance that the other player's turn gets skipped and the current player gets to go again.  
  

  
How to run:  
==
  
play with tree+NN-based AI or tree-based AI or baseline AI(random) or human
--
run run.py  
  
Game flow:  
Choose to play with tree+NN-based AI or the others.  
If you choose to play with tree+NN-based AI, there are 5 sizes of boards with different targets can choose to play.  
Choose to go fisrt or go second. If you choose go first, you will use o and your opponent will use x, vice verse.    
Game begin. Put your pieces in available positives.    
Once any player meets the victory condition or the board is full, game's over.    

If you choose to play with the others, you will de the following steps:  
Choose the size of chess board first.     
Then choose the win condition.    
Choose to play with random player or tree-based AI or human, if you choose AI: choose the depth of the search tree and numbers of nodes in each layer of tree.  
Choose to go fisrt or go second. If you choose go first, you will use o and your opponent will use x, vice verse.  
Game begin. Put your pieces in available positives.  
Once any player meets the victory condition or the board is full, game's over.   
  
  
  
  

Make dataset
--
open dataset.py  

change parameter  
```python
inputs, outputs = get_batch(4, 3, 15, 2, data,25,6)  # (target to win ,tree depth,number of nodes each layer, 2 means tree-based AI will be x(second to play, list to store data, numbers of games, board size)  
with open("data%d.pkl" % 6, "wb") as f: pk.dump((inputs, outputs), f)  # 6 means board size 

```
run dataset.py and datax.pkl will be generated. (may need a long time)
  
Train models
--
open nn.py  
You can change model in NN( )  
change board_size (should be the same as the size you choose to generate datax.pkl)
Our datasets are too big to upload.
run nn.py and modelx.pth will be generated, you will also get two graphs about trainning result.

100 battle between tree+NN-based AI and tree-based AI
--  
open nnbattle.py    
set correct board_size on line 20 (should be the same as the size you choose to train model)  
alternative generated models are in ./models 
change parameter    
```python
c = chessboard(7)                         # 7 means size of chessboard  
res, turns, pieces = game2(c, 3, 3, 15, 2)  # tree-based+NN AI play at first (board, rule,depth,node, p1)
```
if you want tree-based+NN AI play at second, run game3( )  
run nnbattle.py and one bar graph about performance will be generated.   



Results:
==
We have already finished run 100 battles between tree between tree-based AI(second to play) and baseline AI(random) on several different size of chessboards.  
The result is in ./result. 
For each size, we have three figures:
1. the numbers of pieces the winner drops each game 
     orange means first player (tree-based+NN AI) win    
     blue means second player(tree-based AI) win 
     green means draw 
2. trainning average loss
3. trainning target ouput

size: 3x3            wining goal: 3 in a row       depth: 3     nodes of each layer: 15 
size: 4x4            wining goal: 3 in a row       depth: 3     nodes of each layer: 15
size: 5x5            wining goal: 3 in a row       depth: 3     nodes of each layer: 15
size: 6x6            wining goal: 4 in a row       depth: 3     nodes of each layer: 15
size: 7x7            wining goal: 4 in a row       depth: 3     nodes of each layer: 8

Introduction of functions:  
==


Functions in tree_related_functions.py:  
--
exminimax 
--
Use special minimax tree to get the utility of put piece ona certain position of chessboard  

paremeters:  
board：3 dimensions matrix   
d: dimension, if you play o, d=1, if you play x, d=2  
rule: numbers of pieces in a row to win  
action: (x,y) the position you want to put piece   
depth: depth of the tree  
node: number of nodes searched each layer of the tree  
l: vector to count how many nodes searched   

return:  
score : if o has an edge, it will be positive. If it can win the game in less depth, it will get bigger score. If not it will use special method to count the score of the state in the final depth   


make_act, recover_act: make action and undo action  
--

AI_action  
--
Put all the valid actions into the tree and choose the one makes best score  
  
paremeters:  
board：3 dimensions matrix   
d: dimension, if you play o, d=1, if you play x, d=2  
rule: numbers of pieces in a row to win  
depth: depth of the tree  
node: number of nodes searched each layer of the tree  
  
return:   
(score,position),nodes  
  
    
  
Functions in score.py:  
--
score:  
--
compare the max numbers of the x and o in a row which has a potential to reach the goal ( if the goal is 3 pieces in a row, the max numbers of o in state "xoox" is 0, since oo has no chance to become ooo ) and get the score of a certain state  
  
paremeters:  
matrix: one dimension matrix generated by board[1]-board[2], so it will have 0, 1, -1  
rule: numbers of pieces in a row to win  
  
return:  
score:   
if max of o in a row >max of x in a row:  
    return 0.5  
elif max of o in a row<max of x in a row:  
    return  -0.5  
else :  
    return 0  
  
together_row:  
--
get max number of pieces that have potential to meet the goal in a certain row   
  
paremeters:  
vec: one dimension matrix generated by board[1]-board[2], so it will have 0, 1, -1  
d: dimension, if you play o, d=1, if you play x, d=2  
rule: numbers of pieces in a row to win   
  
return:  
max_ to: max number of pieces that have potential to meet the goal in a certain row   
