def hangman(word):
    wrong = 0
    stages = ["","吊","吊","吊","吊","吊","吊","吊"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "文字を予想してね:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
            print(" ".join(board))
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print(" ".join(stages[0:e]))
            if "_" not in board:
                print("あなたの勝ち")
                print(" ".join(board))
                win = True
                break
    if not win:
        print("あなたの負け！")


hangman("cat")


