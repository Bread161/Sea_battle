import random

class Ship:
    def __init__(self, points):
        self.points = points
        self.is_alive = True

class Board:
    def __init__(self):
        self.ships = []
        self.hits = []
        self.misses = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def shoot(self, x, y):
        if (x, y) in self.hits or (x, y) in self.misses:
            raise Exception("You have already shot at this point!")

        hit_ship = None
        for ship in self.ships:
            if (x, y) in ship.points:
                hit_ship = ship
                break

        if hit_ship:
            hit_ship.points.remove((x, y))
            if len(hit_ship.points) == 0:
                hit_ship.is_alive = False
            self.hits.append((x, y))
            return True
        else:
            self.misses.append((x, y))
            return False

    def is_all_ships_destroyed(self):
        for ship in self.ships:
            if ship.is_alive:
                return False
        return True

class Game:
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()

    def setup_boards(self):
        self._setup_board(self.player_board)
        self._setup_board(self.computer_board, is_computer=True)

    def _setup_board(self, board, is_computer=False):
        ship_lengths = [3, 2, 2, 1, 1, 1, 1]
        for length in ship_lengths:
            while True:
                points = []
                x = random.randint(1, 6)
                y = random.randint(1, 6)
                direction = random.choice(['horizontal', 'vertical'])
                for i in range(length):
                    if direction == 'horizontal':
                        point = (x + i, y)
                    else:
                        point = (x, y + i)
                    if point[0] > 6 or point[1] > 6:
                        break
                    points.append(point)

                if len(points) == length:
                    is_valid = True
                    for ship in board.ships:
                        for point in points:
                            if point in ship.points:
                                is_valid = False
                                break
                        if not is_valid:
                            break

                    if is_valid:
                        ship = Ship(points)
                        board.add_ship(ship)
                        break

        if is_computer:
            print("Computer board has been set up!")
        else:
            print("Your board has been set up!")

    def play(self):
        while True:
            print("Your turn to shoot:")
            x = int(input("Enter x-coordinate: "))
            y = int(input("Enter y-coordinate: "))
            try:
                hit = self.computer_board.shoot(x, y)
                if hit:
                    print("Hit!")
                    if self.computer_board.is_all_ships_destroyed():
                        print("Congratulations! You won!")
                        break
                else:
                    print("Miss!")
            except Exception as e:
                print(str(e))

            print("Computer's turn to shoot:")
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            try:
                hit = self.player_board.shoot(x, y)
                if hit:
                    print("Computer hit your ship!")
                    if self.player_board.is_all_ships_destroyed():
                        print("Sorry, you lost!")
                        break
                else:
                    print("Computer missed!")
            except Exception as e:
                print(str(e))


# Создаем экземпляр игры
game = Game()
# Настраиваем игровые доски
game.setup_boards()
# Начинаем игру
game.play()
