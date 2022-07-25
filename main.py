import turtle as t
from states import States
from scorer import Scoreboard


screen = t.Screen()
screen.title("U.S. States Game")
screen.setup(width=900, height=700)
screen.bgpic("blank_states_img.gif")

host = States()
scorer = Scoreboard()

difs = ["easy", "hard"]
difficulty = ""
while difficulty not in difs:
    difficulty = screen.textinput(title="Game Mode", prompt="Choose a mode: Easy (10 mistakes) / Hard (5 mistakes)").lower()

if difficulty == "easy":
    MISTAKES = 10
else:
    MISTAKES = 5

game_on = True
while game_on:

    player_input = screen.textinput(title="State Box", prompt="Enter the name of State:").title()
    if player_input == "Exit":
        break
    host.write_state(player_input=player_input)
    scorer.write_score(score=host.score, mistakes=host.mistakes)

    if host.mistakes == MISTAKES:
        host.game_over()
        game_on = False
    elif host.score == 50:
        host.game_beat()
        game_on = False


# Save missed states to a csv file.
host.save_missed_states()

screen.exitonclick()
