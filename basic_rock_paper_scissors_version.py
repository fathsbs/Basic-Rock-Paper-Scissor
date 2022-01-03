print('Rock...')
print('Paper...')
print('Scissor...')

#input player
player1 = input('Player 1, make your move: ')
player2 = input('Player 2, make your move: ')


if player1 == 'rock' and player2 == 'scissor':
    #logic rock vs scissor
    print('player1 wins!')
elif player1 == 'rock' and player2 == 'paper':
    #logic rock vs paper
    print('player2 wins!')
elif player1 == 'paper' and player2 == 'scissor':
    #logic paper vs scissor
    print('player2 wins!')
elif player1 == 'paper' and player2 == 'rock':
    #logic paper vs rock
    print('player1 wins!')
elif player1 == 'scissor' and player2 == 'rock':
    #logic scissor vs rock
    print('player2 wins!')
elif player1 == 'scissor' and player2 == 'paper':
    #logic scissor vs paper
    print('player1 wins!')
elif player1 == player2:
    #logic if they are using same move
    print('it\'s a tie')
else:
    #logic if the input are betweem rock, paper, and scissor
    print('Something went wrong!')    