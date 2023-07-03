import turtle
import random
import time

class game:
    def __init__(self, player_1,player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.game_box = ["*"] * 101  # Game box array to store the attributes of each position

    def generate_board(self):
        arr = list(range(2, 100))
        random.shuffle(arr)
        n = random.randint(15, 25)
        s1 = "LLLLSSSSRRMM"
        s3 = "123456"
        s2 = [str(i) for i in range(101)]
        for i in range(n):
            num = arr.pop()
            if num <= 10:
                attribute = random.choice(s1[:4] + s1[8:12])
            elif num >= 91:
                attribute = random.choice(s1[4:12])
            else:
                attribute = random.choice(s1)
            if attribute == "R" or attribute == "M":
                attribute += random.choice(s3)
            else:
                if attribute == "S":
                    temp = random.choice(s2[1:((num // 10) - (0 if (num % 10) else 1)) * 10])
                    attribute += temp
                else:
                    temp = random.choice(s2[((num // 10) + (1 if (num % 10) else 0)) * 10 + 1:])
                    attribute += temp
            self.game_box[num] = attribute

    def visualize_board(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor('wheat')
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(-300, -230)
        t.pendown()
        x, y = -300, -280

        for i in range(11):
            t.penup()
            t.goto(x, y + 50)
            t.pendown()
            t.forward(500)
            y += 50
        x, y = -350, -230
        t.left(90)
        for i in range(11):
            t.penup()
            t.goto(x + 50, y)
            t.pendown()
            t.forward(500)
            x += 50
        t.right(90)
        t.penup()
        t.goto(-345, -230)
        t.pendown()
        self.co_ordinates = [(0, 0), ]
        c = 1
        for _ in range(5):
            for __ in range(10):
                t.penup()
                t.forward(50)
                t.pendown()
                t.write(c)
                self.co_ordinates.append(t.position())
                c += 1
            t.left(90)
            t.up()
            t.forward(50)
            t.down()
            t.left(90)
            for __ in range(10):
                t.write(c)
                self.co_ordinates.append(t.position())
                t.penup()
                t.forward(50)
                t.pendown()
                c += 1
            t.right(90)
            t.penup()
            t.forward(50)
            t.pendown()
            t.right(90)
        t.color('purple')
        t.pensize(2)
        for i, attribute in enumerate(self.game_box):
            if (attribute != "*"):
                t.penup()
                t.goto(self.co_ordinates[i][0] + 25, self.co_ordinates[i][1])
                t.pendown()
                t.write(attribute,font=('Germania One',9,'bold'))
        t.hideturtle()

    def roll_dice(self):
        return random.randint(1,6)

    def initialize_game(self):
        self.player_1_pos=self.player_2_pos=1
        self.p1 = turtle.Turtle()
        self.p2 = turtle.Turtle()
        self.p1.hideturtle()
        self.p2.hideturtle()
        self.p1.speed(0)
        self.p2.speed(0)
        self.p1.shape('circle')
        self.p2.shape('square')
        self.p1.color('red')
        self.p2.color('blue')
        self.p1.penup()
        self.p2.penup()
        self.p1.goto(-500,200)
        self.p1.stamp()
        self.p1.goto(-480, 185)
        self.p1.write(self.player_1,font=('Hoefler Text',20,'bold'))
        self.p2.goto(-500, 150)
        self.p2.stamp()
        self.p2.goto(-480, 135)
        self.p2.write(self.player_2, font=('Hoefler Text', 20, 'bold'))
        self.p1.goto(self.co_ordinates[self.player_1_pos][0] + 10, self.co_ordinates[self.player_1_pos][1] + 20)
        self.p2.goto(self.co_ordinates[self.player_2_pos][0] + 10, self.co_ordinates[self.player_2_pos][1] + 35)
        self.p1.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=1)
        self.p2.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=1)
        self.p1.showturtle()
        self.p2.showturtle()
        self.p1.speed(1)
        self.p2.speed(1)
        self.t=turtle.Turtle()
        head=turtle.Turtle()
        head.penup()
        head.hideturtle()
        head.speed(0)
        head.goto(-25,275)
        head.write("Press E to exit the game.",font=('Courier',20,'bold'),align='center')
        self.t.hideturtle()
        self.t.penup()
        self.t.color('forest green')
        style = ('Courier', 18, 'italic')
        self.t.goto(250, 140)
        self.t.write(self.player_1+",\nIt's your turn.\nPress A to roll the dice.\n",font=style)
        self.turn=1

    def end_game(self):
        if (Game.player_1_pos == 100):
            k = turtle.textinput("Congratulations!", Game.player_1 + " has won.\nPress any key to exit.")
        elif (Game.player_2_pos == 100):
            k = turtle.textinput("Congratulations!", Game.player_2 + " has won.\nPress any key to exit.")
        self.wn.bye()


    def make_move(self,player):
        if(self.turn!=player) :return
        self.turn=1-self.turn
        move = self.roll_dice()
        self.t.goto(250, 100)
        style = ('Courier', 18, 'italic')
        style2=('Copperplate',15,'bold')
        if(player==1):
            self.t.write(self.player_1+",You got " + str(move)+".",font=style)
        else:
            self.t.write(self.player_2 + ",You got " + str(move)+".",font=style)
        if(player==1):
            pos = self.player_1_pos
        else :
            pos = self.player_2_pos
        if (self.game_box[pos][0] == "M"):
            if (int(self.game_box[pos][1:len(self.game_box[pos])]) == move and pos + move <= 100):
                if(player==1):
                    self.player_1_pos = pos + move
                else:
                    self.player_2_pos = pos + move
            elif(pos + move > 100):
                self.t.goto(250,60)
                self.t.write("But you can't make a move of "+str(move),font=style2)
                time.sleep(0.3)
            else:
                self.t.goto(250, 50)
                self.t.write("But you can only make a move of "+self.game_box[pos][1:len(self.game_box[pos])]+"\nFrom this position.", font=style2)
                time.sleep(0.3)
        elif (self.game_box[pos][0] == "R"):
            if (int(self.game_box[pos][1:len(self.game_box[pos])]) != move and pos + move <= 100):
                if (player == 1):
                    self.player_1_pos = pos + move
                else:
                    self.player_2_pos = pos + move
            elif (pos + move > 100):
                self.t.goto(250, 60)
                self.t.write("But you can't make a move of " + str(move), font=style2)
                time.sleep(0.3)
            else:
                self.t.goto(250, 50)
                self.t.write("But you can't make a move of " + self.game_box[pos][1:len(self.game_box[pos])] + "\nFrom this position.",font=style2)
                time.sleep(0.3)
        elif (pos + move <= 100):
            if (player == 1):
                self.player_1_pos = pos + move
            else:
                self.player_2_pos = pos + move
        else:
            self.t.goto(250, 60)
            self.t.write("But you can't make a move of " + str(move), font=style2)
            time.sleep(0.3)

        if(player==1):
            self.p1.goto(self.co_ordinates[self.player_1_pos][0] + 10, self.co_ordinates[self.player_1_pos][1] + 20)
        else:
            self.p2.goto(self.co_ordinates[self.player_2_pos][0] + 10, self.co_ordinates[self.player_2_pos][1] + 35)
        x,y=250,60
        if(player==1):
            while (self.game_box[self.player_1_pos][0] == "L" or self.game_box[self.player_1_pos][0] == "S"):
                self.t.goto(x,y)
                y-=30
                if(self.game_box[self.player_1_pos][0] == "L"):
                    self.t.write("Nice! You went up by ladder. ",font=style2)
                else:
                    self.t.write("Oops! You got bitten by snake. ", font=style2)
                time.sleep(0.3)
                self.player_1_pos = int(self.game_box[self.player_1_pos][1:len(self.game_box[self.player_1_pos])])
                self.p1.goto(self.co_ordinates[self.player_1_pos][0] + 10, self.co_ordinates[self.player_1_pos][1] + 20)
        else:
            while (self.game_box[self.player_2_pos][0] == "L" or self.game_box[self.player_2_pos][0] == "S"):
                self.t.goto(x, y)
                y-=30
                if (self.game_box[self.player_2_pos][0] == "L"):
                    self.t.write("Nice! You went up by ladder. ", font=style2)
                else:
                    self.t.write("Oops! You got bitten by snake. ", font=style2)
                time.sleep(0.3)
                self.player_2_pos = int(self.game_box[self.player_2_pos][1:len(self.game_box[self.player_2_pos])])
                self.p2.goto(self.co_ordinates[self.player_2_pos][0] + 10, self.co_ordinates[self.player_2_pos][1] + 35)
        time.sleep(1)
        self.t.clear()
        if(self.player_1_pos!=100 and self.player_2_pos!=100):
            self.t.goto(250, 140)
            if(player==0):
                self.t.write(self.player_1 + ",\nIt's your turn.\nPress A to roll the dice.\n",font=style)
            else:
                self.t.write(self.player_2 + ",\nIt's your turn.\nPress B to roll the dice.\n",font=style)
        else:
            self.end_game()

def print_rules():
    print("Snake and Ladder Game")
    print("------------------------------")
    print("Rules:")
    print("1. Players take turns to roll a dice and move their tokens.")
    print("2. If a player lands on a square with a L i.e ladder, they will move up to the top of the ladder.")
    print("   The top of the ladder is given by the number which is after L.")
    print("   Example:If there is L79 on square 35, then there is ladder from 35 to 79.")
    print("3. If a player lands on a square with a S i.e snake, they will move down to the tail of the snake.")
    print("   The tail of the snake is given by the number which is after S.")
    print("   Example:If there is S21 on square 72, then there is snake at 72 whose tail is ar 21.")
    print("4. If a player lands on a square with a M i.e. Only allowed move ,then he is restricted to make only one move which is given by number after M.")
    print("   Example:If there is M4 on square 69,then player can move from that square only if the dice roll is 4.")
    print("5. If a player lands on a square with a R i.e Restricted Move ,then he can't make a move which is given by number after R.")
    print("   Example:If there is R4 on square 69,then player can move from that square only if the dice roll is anything except 4.")
    print("6. The first player to reach the 100 is the winner.\n\n\n")


print_rules()
print("Please make your move/roll the dice when it will ask u to make move.")
print("Press 1 to start the game.\n")
if(int(input())==1):
    print("Enter name of player 1.")
    a = input()
    print("Enter name of player 2.")
    b = input()

    Game = game(a, b)
    Game.generate_board()
    Game.visualize_board()
    Game.initialize_game()
    Game.wn.onkey(lambda k='A': Game.make_move(1), 'A')
    Game.wn.onkey(lambda k='B': Game.make_move(0), 'B')
    Game.wn.onkey(lambda k='a': Game.make_move(1), 'a')
    Game.wn.onkey(lambda k='b': Game.make_move(0), 'b')
    Game.wn.onkey(Game.wn.bye, 'E')
    Game.wn.onkey(Game.wn.bye, 'e')
    Game.wn.listen()
    Game.wn.mainloop()




