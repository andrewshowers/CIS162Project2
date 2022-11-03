print('----------------- \n'
      '|     |    |    | \n '
      '----------------- \n'
      '|     |    |    | \n '
      '----------------- \n'
      '|     |    |    | \n'
      '-----------------')


def printBoard(b):
    count = 0
    for i in b:
        print(i + "\t", end='')
        count = count + 1
    if count % 3 == 0:
        print()

def chooseWord(words, used, word):
    for i in words:
        if i == word:
            used.append(word)
            words.remove(word)
            return True
    else:
        return False

def main():
    board = ["" for i in range(0, 9)]
    words = [ "hen", "bee", "less", "air", "bits", "lip", "soda", "book", "lot"]
    used = []
    gameOver = False
    player = 1

    while gameOver is False:
        print(*words)
        print('Player ' + str(player) + ' is currently choosing')
        x = False
        currentword = ''
        while x is False:
            uinput = input('Please enter a word')
            if chooseWord(words, used, uinput) is True:
                currentword = uinput
                player += 1
                player %= 2
                break
            print('Please enter a valid word')
        location = int(input('which position would you like to put your word in'))
        board[location] = currentword
        printBoard(board)


main()

