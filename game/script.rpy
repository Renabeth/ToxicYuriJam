# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define evelyn = Character("Evelyn",color="#9e0b0b")
define valerie = Character("Valerie", color="#a881f7")
define kit = Character("Kit", color="#ff7033")
define landlord = Character("Landlord")



# The game starts here.
# labels act as bookmarks or chapter titles that assign a name to a specific point in your game's script
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    evelyn "You've created a new Ren'Py game."

    valerie "Once you add a story, pictures, and music, you can release it to the world!"




    # This ends the game.

    return
