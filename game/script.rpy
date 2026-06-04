# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Evelyn",color="#b0d5f5")
define v = Character("Valerie", color="#a881f7")
define k = Character("Kit", color="#ff7033")
define l = Character("Landlord")



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
    # music - loops | sound - plays once

    show eileen happy at left

   
    # Scene 1 - Game Starts Here
    play music "audio/sfx_knocking.mp3" volume 0.2 #kit knocking
    e "uggghhh..."
    e "hhhhhhhhhhhhhhhhhhhhhhhhhh,,,"
    e "Not again..."
    e "What time even is it?"

    #FIRST CHOICE
    menu:
        "Stay in bed":
            jump stay_in_bed
            

        "Answer the door":
            jump answer_door
         
    
    #Eve and Val talk in bed
label stay_in_bed:
    "Ughh,, I'm too hungover for this"
    "It'll probably stop."
    "Eventually."
    "Looks like Val is still passed out. Lucky bitch."
    "I can barely hear her breathing, it's cute in a way."
    v "*yawwwn* Good morning baby."
    v "...who's banging?"
    e "I dunno some dipshit."
    v "Prolly the neighbor, doesn't she know we're trying to sleep?"
    e "I know, what kind of person bangs on someone's door so early?"
    "I glance over at our alarm clock."
    "It's 3PM."
    
    menu:
        "Do drugs":
            "drugs are cool"
            jump memory_hallucination_1
        
        "Fuck my girlfriend":
            jump sesbian_lex

        "Answer the door":
            jump answer_door_alt


    #add walking sound effects
label answer_door:
    stop music fadeout 1.0
    e "Alriiiight I'm coming."
    "I struggle to sit up, hangover's a total bitch."
    "I rest my hand on my rickety ass bed."
    e "AGH,,, fuck.."
    "I wince as a used needle enters the palm of my hand."
    "Damn, shit. I forgot to throw out the needles from last night."
    "Shows me for getting too relaxed."
    #show eileen normal at right (val's sprite)
    v "mmmnmmm?"
    e "Sorry, stabbed myself. Go back to bed."
    #fade out Valerie's sprite
    play sound "audio/sfx_knocking.mp3" volume 0.2
    "Right, almost forgot about that."
    "Alright, alright I'm here. Stop the banging for god's sake."
    "I open the door, the sunlight from the hallway balcony is so bright it immediately blinds me."
    "Before I can even get a word out her voice pierces my ears."
    k "EEEEEEEEEEEEEEEEEEEEEEEEEVVVEEEEEEEEEEE!!!! ⋆ ˚｡⋆୨୧˚"
    "Oh god."
    "Still slamming my eyes shut from the daylight, I can feel her wrap her arms so tight around me that I feel my ribcage through my skin."
    "I finally open my eyes to be greeted with her all-too happy grinning visage."
    e "I've told you it's Evelyn-"
    k "AWWWWW, but Eve is just SUCH a cute nickname!!"
    e "-and can you please stop yelling. Val is asleep."
    e "If you wanna talk, move it into the hallway..."
    e "without me."
    "I slam the door shut. Back to my sanctuary of darkness."
    "Her incessant shouting manages to reach me even through the cheap, busted up, plywood door."
    k "OKAY WELL, I'M GONNA BRING BY SOME FRUIT LATER!!! SEE YOU THEN!!! ♡⋆ ˚｡⋆୨୧˚"
    k "ALSO MY MOM SAYS YOU CAN HAVE ANOTHER MONTHS EXTENSION ON YOUR RENT!!! ⋆ ˚｡⋆୨୧˚"
    "I wander back to bed and slam my face into my pillow. Thankfully no needles this time."
    #show vals sprite
    v "mmm? Good morning baby."
    e "Hey, Kit came by."
    v "Ughh, did you cover for me?"
    e "... in a way"
    v "Whatever, as long as she's gone."
    e "Yeah totally... except she's coming back in a little bit to bring us more fruit."
    v "Noooooooo… shiiiit."
    e "It couldn't have been that bad."
    v "You literally don't get it."
    v "Last time she asked if she could borrow my buttplug."
    v "In front of all my coworkers."
    v "I wanted to kill myself. Frankly, I still might, we have a razor somewhere in this shithole I'm sure."
    v "While you look for it I'll start drowning myself in the sink."
    e "I think there might be too many mold infested dishes in there, you might have a better chance of dying from disease than any attempt at drowning."
    v "Welp, there goes that plan."
    "Valerie lays down next to me in a huff, she's so light I can barely feel her hit the bed."
    #add stomach growling sfx
    "Well I guess I'm not much better, wish we had money for takeout."
    "Wish we had money at all."
    v "Guess suicide's off the menu. What do you wanna do today?"

    menu:
        "Sit around and do nothing":
            "nothing"
        "Fuck":
            "fuck"
        "Listen to some music":
            "music"

    #end scene
    return

label memory_hallucination_1:
    "Scene - memory hallucination 1"

#The "sex" scene
label sesbian_lex:
    "lesbian sex haha"

label answer_door_alt:
    stop music fadeout 1.0
    k "What are your plans for today?"
    
    menu:
        "Sit around and do nothing":
            ""
        "Fuck":
            jump sesbian_lex
        "Listen to some music":
            ""
        


label good_ending:
    

label suicide_ending:
    

label bad_touch_ending:
    

label infidelity_ending:

# This ends the game.

    #return