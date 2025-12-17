import chess

board = chess.Board()

while True:
    print(board)                  
    move = input("Move: ")        
    try:
        board.push_san(move)      
    except ValueError:
        print("Invalid move! Try again.")
    if board.is_game_over():      
        print("Game over!")
        print(board.result())
        break
