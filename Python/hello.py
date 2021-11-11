import random
   
class Game:
    
    hands = { 0: "グー", 1:"チョキ", 2:"パー" }
    decision = { 0:"引き分け", 1:"負け", 2:"勝ち"}

class GameStart:
    
    print("じゃんけん・・・")

    def Judge(self, player):
        
        if 0 <= player <= 2:
            self.player = player

            com = random.randint(0,2)

            print("あなたは" + Game.hands[player] + "をだしました")
            print("あいては" + Game.hands[com] + "をだしました")
            decision = (self.player - com + 3) % 3

            print("勝敗結果は" + Game.decision[decision] + "です")

            return decision

        else:
            print("0～2の範囲で数字を入力してください")
            return 0

draw = 0

while draw == 0:
    game = GameStart()
    try:
        player_hand = int(input("0=グー, 1=チョキ, 2=パー: "))
        draw = game.Judge(player_hand)
    except ValueError:
        print("数値で入力してください")
        draw == 1