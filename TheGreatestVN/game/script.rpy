# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[ename]")
define e = Character("Main")
define am = Character("am")
define as = Character("as")
define an = Character("an")

# The game starts here.

label start:
    "In the middle of the room there is a man"
    python:
        ename = renpy.input("What is his name again?",length=32)
        ename = ename.strip()

        if not ename:
            ename = "John doe"
        
    "He slowly opens his eyes, only to be confused as he looks about himself"
    e "Where am I?"
    e "Oh, yeah ...the cafe, I had fallen asleep while working on my game again"
    e "I should get something to wake myself up"
    "He finds some money in his pocket and goes to the counter"
    "What do you get?"
    menu:
        "Honey Citrus Mint Tea":
            #block of code to run
            jump HCMTAM
        
        "Caramel Macchiato":
            #block of code to run
            jump CMAS
        
        "White Hot Chocolate":
            #block of code to run
            jump WHCAN
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
label HCMTAM:
    "Good taste! It's no surprise this comes with health benefits. You can rely on it to help with sore throats and drowsy mornings"
    "It goes well with the cold season, warms you from the inside"
    "It is sweet and nice"
    "It reminds of the best person you've ever met"
    e "This is probably the best tea I have ever had, I should get this more often"
    am "Oh you're here again"
    e "Eh!... How did you know where I am."
    am "You always come here to run away from your parents"
    e "Ha-ah, yeah they often don't let me work peacefully at home, What did you wanna tell me"
    am "I just have some good news for you. I got into college"
    e "Woo-hoo! No that just makes me sad ..."
    am "eh! why?"
    e "Doesn't that mean you will be going away?"
    am "Oh, yes it does."
    e "Where are you going?"
    am "Australia"
    e "That's great, let me take that in for a bit."
    am "I understand, aren't you going to college for studying game design?"
    e "Yeah, I was going to Singapore, to get a diploma"
    am "Yeah, I'm sure you can get anywhere with grades like yours"
    e "I know we have friends for 7 years now, but please let me act on my emotions for now"
    e "I am jealous of you in every form imaginable"
label CMAS:
    "Caramel Macchiato"
label WHCAN:
   "White Hot Chocolate"


     
