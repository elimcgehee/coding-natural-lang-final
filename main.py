import markovify
from story import *
from banner import *

f = open("corpus/corpus.txt")
file_contents = f.read()

# Build the model.
text_model = markovify.Text(file_contents)

game_state_name = "start"
while True:
    game_state = story[game_state_name]
    sentence = text_model.make_sentence()
    is_match = False
    while not is_match:
        sentence = text_model.make_sentence(tries=20)
        if sentence is None:
            continue
        for w in game_state["keywords"]:
            if w in sentence:
                is_match = True

    print(" ")
    print("'" + sentence + "'")
    print(" ")
    print(game_state["message"])
    print(" ")

    if "exit" in game_state:
        custom_fig = Figlet(font='banner')
        print(custom_fig.renderText('THE END'))
        print("Project Github: ")

    time.sleep(5)

    if "exit" in game_state:
        exit()

    choice = input("> ")
    if choice.lower() == "a":
        game_state_name = game_state["a"]
    else:
        game_state_name = game_state["b"]