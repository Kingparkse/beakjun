board = input()

answer = []
i = 0
while i < len(board):
    if board[i:i+4] == 'XXXX':
        answer.append('AAAA')
        i += 4
    elif board[i:i+2] == 'XX':
        answer.append('BB')
        i += 2
    elif board[i] == '.':
        answer.append('.')
        i += 1
    else:
        break

ans = ''.join(answer)
if len(board) == len(answer):
    print(answer)
else:
    print(-1)