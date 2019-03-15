from functools import reduce
class Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return str(self.name)


class Game:
    def __init__(self):
        self.game_status = [1, 3, 5, 7]

    def display(self):
        for i in range(len(self.game_status)):
            print("{} -     ".format(i+1), " |"*self.game_status[i])

        #print("The reverse of {} is {}.".format(lst, reverseListLit(lst)))


    def take_a_match(self, player, row, count):
        if not self.game_status:
            print("is empty - you lost")
        if self.game_status[row] !=0 and self.game_status[row] >= count:
            self.game_status[row] -= count
            print("done")

    def win_loose(self):
        a = self.game_status[0]
        b = self.game_status[1]
        c = self.game_status[2]
        d = self.game_status[3]

        output = 0
        a^=b
        a^=c
        a^=d

        if a == 3:
            print("you won")
        else:
            print("you lost")


    def running(self, spieler1, spieler2):
        while True:
            self.display()
            print(str(spieler1.get_name) + "  its your turn")
            zeile = input("Which row?   : ")
            anzahl = input("how many?   : ")
            self.take_a_match(spieler1, zeile, anzahl)
            self.win_loose()
            while True:
                self.display()
                print(spieler2.get_name + "  its your turn")
                zeile = input("Which row?   : ")
                anzahl = input("how many?   : ")
                self.take_a_match(spieler1, zeile, anzahl)
                self.win_loose()
                False


def main():
    """ Launcher """

    print(".#####...######..##..##..######..........##...##..##..##..######..######..######..######..#####............####............####..")
    print(".##..##....##....###.##....##............###.###..##..##..##........##......##....##......##..##..............##..........##..##.")
    print(".##..##....##....##.###....##............##.#.##..##..##..####......##......##....####....#####............####...........######.")
    print(".##..##....##....##..##....##............##...##..##..##..##........##......##....##......##..##..........##........##....##..##.")
    print(".#####...######..##..##..######..........##...##...####...######....##......##....######..##..##..........######....##.....####..")
    #print(".................................................................................................................................")

    print()
    name1 = input("Type player #1 name (#1 will play first nigga): ")
    name2 = input("Type player #2 name")

    player1 = Player(name1)
    player2 = Player(name2)

    game = Game()
    game.display()

    game.running(player1, player2)



    # print("The reverse of {} is {}.".format("fs", "sd"))

    exit(0)


if __name__ == "__main__":
    main()
