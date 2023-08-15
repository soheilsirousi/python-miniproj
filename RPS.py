from random import randint

class Player:
    def __init__(self,name):
        self.__position = None
        self.name = name

    def set_position(self,position):
        self.__position = position

    def get_name(self):
        return self.name

    def get_position(self):
        return self.__position

class Game:
    def __init__(self):
        self.round = 3
        self.players = dict()
        self.attitudes = ['r','p','s']
        self.current_player = None

    def add_player(self,player):
        self.players[player] = 0

    def next_player(self):
        if not self.current_player:
            self.current_player = random.choice(self.players)
        else:
            current_index = self.players.index(self.current_player)
            next_index = (current_index + 1) % len(self.players)
            self.current_player = self.players[next_index]


    def single_play(self):
        while True:
            name = input('Ok, Please enter your name: ')
            user = Player(name)
            cpu = Player('CPU')
            self.add_player(user)
            self.add_player(cpu)
            self.current_player = user
            while self.round >= 0:
                user_position = input(f'{self.current_player.name} its your turn; type your choice (r, p or s)? ')
                cpu_position = self.attitudes[randint(0,2)]
                print(f'computer choice : {cpu_position}')
                if user_position == cpu_position:
                    print('Same!')
                    print(f'your points : {self.players[self.current_player]} computer points : {self.players[cpu]}')
                elif (user_position == 'p') and (cpu_position == 'r'):
                    self.players[self.current_player] += 1
                    print(f'1 point for {self.current_player.name}, points : {self.players[self.current_player]}')
                elif (user_position == 'r') and (cpu_position == 'p'):
                    self.players[cpu] += 1
                    print(f'1 point for Computer, points : {self.players[cpu]}')
                elif (user_position == 'p') and (cpu_position == 's'):
                    self.players[cpu] += 1
                    print(f'1 point for Computer, points : {self.players[cpu]}')
                elif (user_position == 's') and (cpu_position == 'p'):
                    self.players[self.current_player] += 1
                    print(f'1 point for {self.current_player.name}, points : {self.players[self.current_player]}')
                elif (user_position == 'r') and (cpu_position == 's'):
                    self.players[self.current_player] += 1
                    print(f'1 point for {self.current_player.name}, points : {self.players[self.current_player]}')
                elif (user_position == 's') and (cpu_position == 'r'):
                    self.players[cpu] += 1
                    print(f'1 point for Computer, points : {self.players[cpu]}')
                else:
                    print('Please enter valid input :( ')
                self.round -= 1

            if self.players[cpu] > self.players[user]:
                again = input('HAHA you lost!\n wanna play again (y/N)? ')
            elif self.players[cpu] < self.players[user]:
                again = input(f'{self.current_player.name} you win!\n wanna play again (y/N)? ')
            else:
                again = input('Ops draw!\n wanna play again (y/N)? ')

            if again == 'n':
                break


if __name__ == '__main__':
    game = Game()
    game.single_play()
    print('Game End!')
