# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg bonChon = "bgA.png"
image bg gate = "bgB.png"
image bg road = "bgC.png"
image bg costa = "bgD.png"
image bg prac = "bgG.png"
image bg gonz = "bgH.png"
image bg mvp = "bgE.png"
image bg redRoad = "bgF.png"
image bg gonz2 = "bgL.png"
image bg wash = "bgJ.png"

# Declare characters used by this game.
define secu = Character('Guard C', color="#c8ffc8")
define adsa = Character('ADSA', color="#ff0000")
define fr = Character('Close Friend G', color="#ffcb05")
define lit = Character('Lit Group Mate B', color="#f75b68")
define fr2 = Character('Friend A', color="#ececea")     

define un = Character ('Unknown', color="#d4d4d2")
define cat = Character('Catell', color="#0096fd")

# Slow text.
define cellRing = Character(_("Cellphone"), 
            color="#ffffff", 
            what_slow_cps=70)

# The game starts here.
label start:
    scene bg bonChon
    play music "bgmStart.mp3" fadein 2
    with dissolve
    
    #MC - Dynamic Character
    $ MC = DynamicCharacter("MC", color=(192, 64, 64, 255))
    $ MC = ""

    "" "Ugh, another day in school... Another day facing the heat of this forsaken Summer..."
    
    "" "Curse you Sun."
    
    "" "It's so hot that I've even forgotten my name... Eh... What was it again?"
    
    $ MC = renpy.input(_("Please input your name, and press enter (You can leave it blank and press enter)")) or _("Exchange Student A")
    
    "" "That's it! My name's [MC!t]!"
    
    cellRing "Toot! Toot!... {nw}"
    
    extend "Tick!"
    
    MC "I wonder what this is all about... Hmm..."
    
    adsa "Please be advised that you have a REQUIRED appointment in the dean's office. You are expected to come as early as possible today. Thank you."
    
    stop music
    
    MC "Umm... What the F***?!?!?"
    
    "" "Thus I began my journey to the Dean's office"
    
    "" "Have I mentioned that I was outside the school eating lunch? Now I have to trek all the way back in this heat... Ugh..."
    
label reasoning:
    scene bg gate
    play music "bgmMain.mp3" fadein 2
    with fade
    
    secu "Good Afternoon sir. The climate's quite sizzling today isn't it?"
    
    un "{color=#ffa500}REASONING{/color} is the process of thinking about something in a logical manner to form a conclusion"
    
    un "{color=#ffa500}WARMTH{/color} is showing of enthusiasm, affection or kindness to others"
    
    menu:
            "" "Umm... Uhh... What was with that voice at the end? Err..."
            
            "Yeah, I don't really like this kind of weather":
                $ response = True
                
            "Nah. Our weather is bipolar, it suddenly changes now and then;  it might get better soon":
                $ response = False
            "Good Afternoon":
                $ response = 1
                
    if response is True:
        un "It seems like you have a very Concrete Type of Reasoning... You might have some difficulty with analogies"
        jump warmth
        
    if response is 1:
        un "It seems as though you are neither, when it comes to Concrete or Abstract type of Reasoning, maybe you're both?"
        jump warmth
        
    else:
        un "It seems you are capable of Abstract Reasoning and can easily make use of analogies"
        
label warmth:
    scene bg road
    with fade
    
    "" "Almost there..."
    
    menu:
            "" "Oh looks its my classmates! I guess I should..."
            
            "Approach them, say hello and make excuse that you need to go to the DEAN's office":
                $ response = True
            
            "Avoid them and take another direction":
                $ response = False
            
            "Say 'Hi!'":
                $ response = 1
            
    if response is True:
        un "It seems as though you're pretty outgoing and enthusiastic."
        jump liveliness
        
    if response is False:
        un "It seems as though you are quite distant, a farcry from Warmth."
        jump liveliness
    
    else:
        un "It seems as though you can be pretty outgoing, yet distant, thus leading to a middleground when it comes to Warmth"
        
label liveliness:
    scene bg mvp
    with fade
    
    "" "Arrgh, why must I cross thee Sun, when I walk to places in this school?!?"
    
    "?" "[MC!t]!"
    
    MC "Oh! It's close friend A!"
    
    fr "[MC!t], I've been looking everywhere for you! So... Umm..."
    
    fr "It's my birthday this Saturday, it would be great if you’ll celebrate it with me and my friends!"
   
    un "{color=#ffa500}LIVELINESS{/color} is being happy or excited, while being confident at expressing it."
    
    un "{color=#ffa500}RULE CONSCIOUSNESS{/color} is the respect for rules and authorities"
    
    "" "Again with that voice... It sounds so near yet..."
            
    fr "[MC!t]?"
        
    menu:     
            "" "Err..."
            
            "Yes of course I'll go to the party! Party! Party!":
                $ response = True
            
            "Ok, I am going":
                $ response = False
                
            "Alright, I'll text you if I can go or not":
                $ response = 1
                
    if response is True:
        un "It seems you have the penchant for exhibiting Liveliness, such as excitement over a party"
        jump rule
    
    if response is False:
        un "Very serious indeed. Not very lively are you?"
        jump rule
    
    else:
        un "Not jumping immediately to such a chance to have fun? Considering it even? It seems as though you're at the inbetween when it comes to liveliness"
                
label rule:
    
    fr "Yay! I hope you come! It's going to be so much fun! By the way you can also stay overnight!"
    
    "" "What? O-V-E-R-N-I-G-H-T? Overnight?!? Is this for real? I have to think about this carefully..."
    
    menu:       
            "" "Hmm..."
            
            "I'm sorry, I have a curfew, it's only up until 10pm":
                $ response = True
            
            "Of course, nevermind the curfew that I have, as long as I'm with you":
                $ response = False
            
            "Oh, I see, ok. I'll text you":
                $ response = 1
                
    if response is True:
        un "That's very rule conscious of you, a wise choice; we wouldn't want to get in trouble now do we?"
        jump Social
        
    if response is False:
        un "As long as you're with your friend hmm? Very interesting, who cares about the rules when you can be with friends after all"
        jump Social
        
    else:
        un "Not sure if you should stick with your curfew or stay overnight with your friend? Bordering on both? It seems as though you are conscious about the rules, yet are willing to forego them as well"
        
label Social:
    scene bg prac
    with fade
    
    "" "Alright, a party. Seems like this day's getting interesting..."
    
    "?" "Yo! [MC!t]!"
    
    MC "Yes?"
    
    lit "We're groupmates for Lit, I need to know what you want to do for our Play"
    
    un "{color=#ffa500}SOCIAL BOLDNESS{/color} is one's comfort and confidence in social situations"
    
    un "{color=#ffa500}DOMINANCE{/color} is a person's disposition to assert control over others"
    
    menu:
            "" "That voice again, I really hope I'm not going crazy though... Hmm..."
            
            "I want to act! I shall expose my talent! WAHAHAHAHA!":
                $response = True
            
            "Can I be part of the Production, like props? I'm quite shy after all...":
                $response = False
                
            "You can place me anywhere, anything's fine with me":
                $response = 1
                
    if response is True:
        un "You seem to be pretty Socially Bold, fear not the crowd after all, but the grades"
        jump dom
        
    if response is False:
        un "Shy are you? I guess you're not that Socially Bold, being in the production has its perks after all"
        jump dom
        
    else:
        un "The fine with anything kind of person huh? Leaving it up to luck since you're fine with anything is pretty understandable"
        
label dom:
        
    lit "Oh okay, so here's what you're going to do..."
    
    lit "*blah* *blah* *blah* And you put the potatoes there"
    
    menu:
            lit "You got it?"
            
            "Okay, I'll get to working on it as soon as possible":
                $ response = True
            
            "Wait, that seems a bit too much, can you distribute the tasks more efficiently? Inform me of the changes as well via Facebook":
                $ response = False
            
            "Okay":
                $ response = 1
            
    if response is True:
        un "Quick on accepting it aren't you? Are you sure you're not easily led? Well, with this they can't complain that you freeloaded or are doing easier tasks"
        jump sensitive
        
    if response is False:    
        un "Wow, taking the lead immediately, that's pretty Bossy; but someone needs to lead after all"
        jump sensitive
        
    else:
        un "Just going with the flow? Seems like you don't really care that much, who knows you might take the lead, or continue on going with the flow depending on what happens"
    
label sensitive:
    scene bg redRoad
    with fade
    
    "" "Alright; I can see the building now... I don't even know where ADSA is..."
    
    "?" "Hey [MC!t]! Come over here, I need to show you something on my laptop!"
    
    "" "Oh, it's Friend A! Hmm... I wonder what he wants to show me..."
    
    un "{color=#ffa500}SENSITIVITY{/color} is showing appreciation of other's feelings"
    
    un "{color=#ffa500}EMOTIONAL STABILITY{/color} is the mental state of calmness and compusure"
    
    "" "Weird... That voice again... But now to watch this..."
    
    fr2 "This show's about how this man fights for a wish; but he finds out at the end that the wish can only be granted in ways he thinks it's possible"
    
    fr2 "It ends with him losing everything in his life, and later on succumbs to a wound he got in the fight"
    
    menu:
        "" "This show is... This is!!!"
        
        "*cries* It's great":
            $ response = True
        "It's so inspiring":
            $ response = False
        "It's nice":
            $ response = 1
        "It's a bit too cliché... I wonder what Friend A thinks about this show":
            $ response = 2
        "No Comment.":
            $ response = 3
            
    if response is True:
        un "Very sensitive of you... This show is pretty deep about Fate after all..."
        jump open
    if response is False:
        un "Wow, it looks as though you're Reactive, the show is very inspiring after all"
        jump open
    if response is 1:
        un "That's quite unsentimental of you, though the show is indeed quite nice"
        jump open
    if response is 2:
        un "Very realistic, you were able to watch it while being aware of reality itself"
        jump open
    else:
        un "No Comment... Maybe you're sensitive enough to take into account your friend's feelings about the show, and also calm enough not to comment..."
        
label open:
    scene bg costa
    with fade
    
    "" "Oh my, seems like the Guidon's paper stack is quite high; it won't hurt to read one"

    menu:
            "" "stub dialogue"
            
            "Blue Eagle the King has been played in the campus for years, no need to change it":
                $ response = True
            "I agree, it is most definitely the mejority's decision, and this little change won't hurt":
                $ response = False
            "It's alright, wrecking ball is not really that bad a song.":
                $ response = 1
                
    if response is True:
        un "stub dialogue"
        jump perf
    if response is False:
        un "stub dialogue"
        jump perf
    else:
        un "stub dialogue"
    
label perf:
    scene bg gonz
    with fade
    
    menu:
            "" "Stub dialogue"
            
            "Grab the woman's banner, and throw it on the ground while stating that her grammar's horrible":
                $ response is True
        
            "Calmly tell the students to tone the noise down since they might disturb the classes":
                $ response is False
            
            "Approach woman and whisper that she should work on her English and grammar a bit more":
                $ response is 1
                
    if response is True:
        un "Stub Dialogue"
        jump priv
    if response is False:
        un "Stub dialogue"
        jump priv
    else:
        un "Stub dialogue"
                
label priv:
    scene bg gonz2
    with fade
    
    menu:
            "" "Umm... Err..."
            
            "I don't have any insecurity, next question?":
                $ response = True
            "Sorry, too private, I can't answer that, I can answer that I do have insecurities though.":
                $ response = False
            "I don't like how my face is, I mean look at it... I don't like how big my legs are too...":
                $ response = 1
                
    if response is True:
        un "Stub dialogue"
        jump vigil
    if response is False:
        un "Stub dialogue"
        jump vigil
    else:
        un "Stub dialogue"
                
label vigil:
    scene bg wash
    with fade
    
    menu:
            "" "Stub dialogue"
            
            "KYAAAA!!! THIEF CRIMINAL! *attack the person*":
                $ response = True
            "Tap the man at the back, and whisper 'Heil Hydra' ":
                $ response = False
            "Tell the man that he might want to remove the mask, it's summer after all, it's quite hot out":
                $ response = 1
                
    if response is True:
        un "Stub dialogue"
        jump catell
    if response is False:
        un "Stub dialogue"
        jump catell
    else:
        un "Stub dialogue"
                
label catell:
                
    "" "Catell should intro himself here"
            
    return
