from turtle import Turtle
import pandas

# CONVERTING STATES DATA TO A DICTIONARY
data = pandas.read_csv("50_states.csv")
# print(data)

states = data.state.tolist()
x_coord = data.x
y_coord = data.y


coords = {}
for state in states:
    coords[state] = []

# print(coords)
i = 0
for key in coords:
    coords[key].append(x_coord[i])
    coords[key].append(y_coord[i])
    i += 1
# print(coords)

# CREATING THE STATES CLASS
ALIGN = "center"
FONT = ("courier", 10, "bold")
FONT_GAME_0VER = ("courier", 20, "bold")


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.score = 0
        self.mistakes = 0
        self.guessed_states = []
        self.missed_states = []

    def write_state(self, player_input):
        if player_input in self.guessed_states:
            self.mistakes += 1
        elif player_input in coords:
            self.goto(x=coords[player_input][0], y=coords[player_input][1])
            self.write(player_input, align=ALIGN, font=FONT)
            self.score += 1
            self.guessed_states.append(player_input)
        else:
            self.mistakes += 1

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("GAME OVER", align=ALIGN, font=FONT_GAME_0VER)

    def game_beat(self):
        self.goto(0, 0)
        self.pencolor("blue")
        self.write("YOU GUESSED ALL STATES! YOU BEAT THE GAME!", align=ALIGN, font=FONT_GAME_0VER)

    def save_missed_states(self):
        all_states = []
        for keys in coords:
            all_states.append(keys)

        self.missed_states = [item for item in all_states if item not in self.guessed_states]

        # Alternative code for missed states:
        # for check_state in all_states:
        #     if check_state not in self.guessed_states:
        #         self.missed_states.append(check_state)

        missed_states_data = pandas.DataFrame(self.missed_states, columns=["states"])
        missed_states_data.to_csv("missed_states.csv")
