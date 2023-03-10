import random
class Ship:
    def __init__(self,size):
        self.row = random.randrange(0,9)
        self.col = random.randrange(0,9)
        self.size=size
        self.orientation = random.choice(["h","v"])
        self.indexes = self.compute_indexes()

    def compute_indexes(self):
        start_index = self.row*10+self.col
        if self.orientation == "h":
            return[start_index + i for i in range(self.size)]
        elif self.orientation== "v":
            return[start_index + i*10 for i in range(self.size)]


class Player:
    def __init__(self):
        self.ships =[]
        self.search=["U" for i in range(100)]
        self.place_ships(sizes=[5,4,3,3,2])
        list_of_list=[ship.indexes for ship in self.ships]
        self.indexes = [index for sublist in list_of_list for index in sublist]

    def place_ships(self,sizes):
        for size in sizes:
            placed=False
            while not placed:
                ship = Ship(size)
                possible =True
                for i in ship.indexes:
                    if i >=100:
                        possible=False
                        break
                    new_row=i//10
                    new_col=i%10
                    if new_row!=ship.row and new_col!=ship.col:
                        possible=False
                        break

                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            possible=False
                            break
                if possible:
                    self.ships.append(ship)
                    placed=True

    def show_ships(self):
        indexes=["-" if i not in self.indexes else "X" for i in range(100)]
        for row in range(10):
            print(" ".join(indexes[(row-1)*10:row*10]))

class Game:
    def __init__(self):
        self.player1= Player()
        self.player2 =Player()
        self.player1_turn=True
        self.over = False

    def make_move(self,i):
        player=self.player1 if self.player1_turn else self.player2
        opponent= self.player2 if self.player1_turn else self.player1
        if i in opponent.indexes:
            player.search[i]="H"

            for ship in opponent.ships:
                sunk=True
                for i in ship.indexes:
                    if player.search[i]=="U":
                        sunk=False
                        break
                if sunk:
                    for i in ship.indexes:
                        player.search[i]="S"
        else:
            player.search[i]="M"
        self.player1_turn = not self.player1_turn
            