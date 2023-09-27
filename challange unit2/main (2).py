class player:

  def player(self):
    print("the player is playing a cricket")

class Batsman(player):
  def play(self):
    print("the batman is bating.")

class Bowler(player):
  def play(self):
    print("the bowlwer is boling.")

batsman=Batsman()
bowler=Bowler()


batsman.play()
bowler.play()