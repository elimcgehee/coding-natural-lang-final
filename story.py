# Main Story

story = {
    # Start Message
    "start": {
        "message": "You enter the Hogwarts castle and approach the sorting hat... After a few minutes, it is finally your turn! Do you (a) approach the hat, or (b) run away like a coward?",
        "keywords": [ "castle" ],
        "a": "end",
        "b": "run"
    },

    # Main Game
    "run": {
        "message": "Good choice! Why do what everyone else does... Now that you've fled, do you go to (a) Hagrid's shack, or (b) The Forbidden Forest?",
        "keywords": [ "run" ],
        "a": "shack",
        "b": "forest"
    },
    "forest": {
        "message": "You make it to the foot of the forest, but you hear some sketchy sounds. Do you (a) proceed, or (b) go back?",
        "keywords": [ "forest" ],
        "a": "forestend",
        "b": "run"
    },
    "shack": {
        "message": "You enter Hagrid's shack, but no one is home... Do you (a) yell for Hagrid, or (b) leave the shack?",
        "keywords": [ "Hagrid" ],
        "a": "yell",
        "b": "run"
    },
    "yell": {
        "message": "You get Hagrid's attention, and he comes back!. He gives you a dagger! Do you (a) go back to the sorting hat, or (b) stick around with Hagrid?",
        "keywords": [ "wand" ],
        "a": "sortinghat",
        "b": "yell"
    },
    "sortinghat": {
        "message": "You make it back to the sorting hat... Do you feel (a) anxious, or (b) excited?",
        "keywords": [ "hat" ],
        "a": "anxious",
        "b": "excited"
    },
    "anxious": {
        "message": "You feel nervous about sorting... Dumbledore places the hat on your had... The hat yells... 'HUFFLEPUFF!' Do you accept this placement? (a) for 'yes', or (b) for 'no'?",
        "keywords": [ "Hufflepuff" ],
        "a": "huffleaccept",
        "b": "huffledecline"
    },
    "excited": {
        "message": "You feel excited about sorting... Dumbledore places the hat on your had... The hat yells... 'SLYTHERIN!' Do you accept this placement? (a) for 'yes', or (b) for 'no'?",
        "keywords": [ "Slytherin" ],
        "a": "slytherinaccept",
        "b": "slytherindecline"
    },
    "huffleaccept": {
        "message": "Congradulations! You are now an honorary Hufflepuff! Press (a) or (b) to continue...",
        "keywords": [ "Hufflepuff" ],
        "a": "continuehp",
        "b": "continuehp"
    },
    "slytherinaccept": {
        "message": "Congradulations! You are now an honorary Slytherin! Press (a) or (b) to continue...",
        "keywords": [ "Slytherin" ],
        "a": "continuesl",
        "b": "continuesl"
    },

    # Hufflepuff Path
    "continuehp": {
        "message": "Voldemort is standing in front of you minding his business... Do you (a) kill him with the dagger or (b) run to tell a professor?",
        "keywords": [ "Voldemort" ],
        "a": "hufflewin",
        "b": "hufflelose"
    },
    "hufflewin": {
        "message": "You did it! You killed Voldemort! YOU WIN!",
        "keywords": [ " " ],
        "exit": True
    },
    "hufflelose": {
        "message": "You tried to run, but it was too late... Voldemort detected your presense with his evil powers, and killed you. GAME OVER!",
        "keywords": [ " " ],
        "exit": True
    },


    # Slytherin Path
    "continuesl": {
        "message": "Voldemort is standing in front of you minding his business... Do you (a) kill him with the dagger or (b) join his cause?",
        "keywords": [ "Voldemort" ],
        "b": "slytherwin",
        "a": "slytherlose"
    },
    "slytherlose": {
        "message": "You tried to do it, but you hesitated... Voldemort detected your presense with his evil powers, and killed you. GAME OVER!",
        "keywords": [ " " ],
        "exit": True
    },
    "slytherwin": {
        "message": "You alert Voldemort of your presense, and explain yourself... He accepts and let's you join his cause! YOU WIN! (At least for now...)",
        "keywords": [ " " ],
        "exit": True
    },

    # Endings
    "end": {
        "message": "Wrong choice... GAME OVER!",
        "keywords": [ " " ],
        "exit": True
    },
    "forestend": {
        "message": "You ran into a troll and died... GAME OVER!",
        "keywords": [ " " ],
        "exit": True
    },
    "leaveshack": {
        "message": "You leave the shack... How boring... GAME OVER!",
        "keywords": [ " " ],
        "exit": True
    },
    "slytherindecline": {
        "message": "The hat never lies... GAME OVER!",
        "keywords": [ " " ],
        "exit": True
    },
    "huffledecline": {
        "message": "The hat never lies... GAME OVER!",
        "keywords": [ " " ],
        "exit": True
    },
}