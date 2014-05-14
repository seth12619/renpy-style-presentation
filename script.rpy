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
image bg black = "bgBl.png"
image bg adsa = "bgK.png"
image bg office = "bgO.png"

#Character sprites

image guard normal = "guard.png"

image adi normal = "bMate.png"
image adi2 normal = "bMateB.png"

image pro normal = "protest.png"
image proG normal = "girlP.png"

image lit normal = "Cirno.png"

image psyA normal = "carlo.png"
image psyB normal = "jaoie.png"
image psyC normal = "rico.png"

image chi normal = "close.png"
image ian normal = "tele.png"

image cat mask = "catellmask.png"
image cat normal = "catell.png"

# Declare characters used by this game.
define secu = Character('Guard', color="#c8ffc8")
define adsa = Character('ADSA', color="#ff0000")
define fr = Character('Chi', color="#ffcb05")
define lit = Character('Cirno', color="#f75b68")
define fr2 = Character('Ian', color="#ececea")     
define wom = Character('Woman A', color="#cc5cf2")

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
    
    "" "Of all the days, I had to eat outside today. Now I have to trek all the way back in this heat... Ugh..."
    
label reasoning:
    scene bg gate
    play music "bgmMain.mp3" fadein 2
    with fade
    
    show guard normal
    with wipeleft
    
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
        
    hide guard normal
    with wipeleft
        
label warmth:
    scene bg road
    with fade
    
    "" "Almost there..."
    
    show adi normal at left
    with wipeleft
    show adi2 normal
    with wipeleft
    
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
    
    "" "Arrgh, why must I cross thee Sun, when I journey around the campus?!?"
    
    "?" "[MC!t]!"
    
    show chi normal
    with wiperight
    
    MC "Oh! It's Chi!"
    
    fr "[MC!t], I've been looking everywhere for you! So... Umm..."
    
    fr "It's my birthday this Saturday, it would be great if you’ll celebrate it with the gang!"
   
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
    
    show lit normal
    with wiperight
    
    "?" "Yo! [MC!t]!"
    
    MC "Yes?"
    
    lit "I'm Cirno! We're groupmates for Lit, I need to know what you want to do for our Play"
    
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
        un "Shy aren't you? I guess you're not that Socially Bold, being in the production has its perks after all"
        jump dom
        
    else:
        un "The fine with anything kind of person huh? Leaving it up to luck since you're fine with anything is pretty understandable"
        
label dom:
        
    lit "Oh okay, so here's what you're going to do..."
    
    lit "*blah* *blah* *blah* And you put the potatoes there"
    
    menu:
            lit "You got it?"
            
            "Yeah, I'll be working on it as soon as possible":
                $ response = True
            
            "Wait, that seems to be too much; can you distribute the tasks more efficiently? Inform me of the changes as well via Facebook":
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
    
    "?" "Hey [MC!t]! Come over here, I got something awesome on my laptop!"
    
    show ian normal
    with wipeleft
    
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
    
    "Guidon Newspaper" "Sanggu crippl--"
    
    "" "next page"
    
    "Guidon Newspaper" "'Blue Eagle the King' to be replaced by 'Wrecking Ball'"
    
    un "{color=#ffa500}Openness to Change{/color} is the acceptance of new ideas"
    
    un "{color=#ffa500}SELF-RELIANCE{/color} is showing showing confidence in anyone's own abilities to do something without the help of others"

    menu:
            "" "I see... I guess it received a few complaints due to being too old"
            
            "Blue Eagle the King has been played in the campus for years, no need to change it":
                $ response = True
            "I agree, it is most definitely the majority's decision, and this little change won't hurt":
                $ response = False
            "It's alright, wrecking ball is not really that bad a song.":
                $ response = 1
                
    if response is True:
        un "You don't seem to be open to new ideas, but you believe in your own opinions. I like that song though..."
        jump perf
    if response is False:
        un "You seem to be open to new ideas, but you get easily swayed by others. We are gonna wreck 'em all."
        jump perf
    else:
        un "You're cool with new ideas, but you still think about these ideas deeply. Good job!."
    
label perf:
    scene bg gonz
    with fade
    
    "" "I can see it! Once I make a turn here..."
    
    show pro normal
    with wipeleft
    
    "Group of Students" "We want air-con! Tuition too high, or we go home! We want air-con! Tuition too high, or we go home!"

    "" "Seems like I've just met the radical 'THAC' group, which stands for {color=#f9ecb6}Tuition High thus Air-Con{/color}"
    
    un "{color=#ffa500}PERFECTIONISM{/color} is unacceptance of having mistakes or flaws"
    
    un "{color=#ffa500}TENSION{/color} is the inability to relax in some nerve wracking situations"
    
    show pro at Move((0.5,0.6), (0.25, 0.6), 1,
        xanchor="center", yanchor="center")
    
    show proG normal
    with wiperight
    
    wom "We dying of heat, get nya hert!"
    
    menu:
            "" "That woman..."
            
            "Grab the woman's banner, and throw it on the ground while stating that her grammar's horrible":
                $ response is True
        
            "Calmly tell the students to tone the noise down since they might disturb the classes":
                $ response is False
            
            "Approach woman and whisper that she should work on her English and grammar a bit more":
                $ response is 1
                
    if response is True:
        un "Nobody's perfect, but you expect everything to be perfect. Perfectionism drives the world and you'll impose it with force."
        jump priv
    if response is False:
        un "You aren't too particular about the details and you prefer to resolve things peacefully. "
        jump priv
    else:
        un "Good job avoiding conflict while correcting her mistakes. You tread the path of perfection peacefully."
                
label priv:
    scene bg gonz2
    with fade
    
    "" "Alright! There it is! Once I get to that area I will--"
    
    show psyA normal at left
    with wiperight
    show psyB normal
    with wiperight
    show psyC normal at right
    with wiperight

    "Group of Psychology Students" "Bro! Please answer a few of our questions! It's for a project! Please!"
    
    "" "D*mn it! I'm trapped!"
    
    un "{color=#ffa500}PRIVATENESS{/color} is preferring to keep personal and confidential affairs to oneself"
    
    un "{color=#ffa500}APPREHENSION{/color} is self-doubt or the anxiety or fear that something bad might happen"
    
    MC "Alright, but let me ask you a question afterwards ok?"
    
    "" "This might be a chance to ask about that voice..."
    
    hide psyA normal
    with wipeleft
    hide psyC normal
    with wiperight
    
    "Psych. Student B" "Okay, umm sir; do you happen to have any insecurities?"
    
    
    menu:
            MC "Umm... Err..."
            
            "I don't have any insecurity, next question?":
                $ response = True
            "Sorry, too private, I can't answer that, I can answer that I do have insecurities though.":
                $ response = False
            "I don't like how my face is, I mean look at it... I don't like how big my legs are too...":
                $ response = 1
                
    if response is True:
        un "You're confident about yourself and genuine about the situation."
        jump vigil
    if response is False:
        un "You need your own space, but you're a self-assured person."
        jump vigil
    else:
        un "You're very insecure about youself and I could see that you're an open book."
                
label vigil:
    
    hide psyB normal
    with wiperight
    show psyC normal
    with wiperight
    "Psych. Student C" "Okay sir, now for our second out of 344 questions..."
    
    MC "Excuse me, I need to go to the washroom for a bit"
    
    show psyA normal at left
    with wiperight
        
    "Psych. Student A" "Sure go ahead, please come back though, we're counting on you!"\
    
    "" "You wish. 344 questions will take hours!"
    
    scene bg wash
    with fade
    
    "" "Washing my face feels so goo--"
    
    un "{color=#ffa500}VIGILANCE{/color} is the state of being wakeful or alert to environmental factors or stimuli"
    
    un "{color=#ffa500}ABSTRACTEDNESS{/color} is the quality of openness to abstract ideas, fantasy, and imagination"
    
    play music "bgmMask.mp3" fadein 2
    
    "" "That voice urrgh!"
    
    "" "*splash*"
    
    "" "What the?!?"
    
    show cat mask
    with dissolve
    
    "" "A man in all black, complete set. Black jacket with a mask... Is right behind me..."
    
    "" "I wouldn't have noticed him if not for the mirror"

    menu:
            "" " This is creepy... What should I do?"
            
            "KYAAAA!!! THIEF! CRIMINAL! *attack the person*":
                $ response = True
            "Tap the man at the back, and whisper 'Heil Hydra' ":
                $ response = False
            "Tell the man that he might want to remove the mask, it's summer after all, it's quite hot outside":
                $ response = 1
                
    if response is True:
        un "Wow, straight and quick to a skeptical conclusion. Can't you at least imagine that I'm a fairy godmother or something? At the most, you'll survive."
        jump catell
    if response is False:
        un "Heil! No worries at all with my very suspicious clothing? Very imaginative of you to think that Hydra exists..."
        jump catell
    else:
        un "Yes, it is quite hot after all... Not even alert to my presence? No perspective? Very practical."
                
label catell:
    
    "" "Hmm... Now that he talks about it... Huh?"
    
    MC "Wait, you're that--"
    
    scene bg black
    with dissolve
    
    scene bg adsa
    with fade
                
    MC "Urrgh... Murgle..."
    
    "" "What happened? I remember that I had to go to the ADSA due to a text, but then multiple things happened"
    
    MC "Where. Am. I?"
    
    play music "bgmCatell.mp3" fadein 2
    
    show cat mask
    with wiperight
    
    #catell wearing mask comes in
    
    un "Welcome to the ADSA, [MC!t]! Come on in!"
    
    scene bg office
    with fade
    show cat mask
    with wipeleft
    
    un "You must be wondering where you are, what just happened to you, or what my identity is."
    
    un "Well..."
    
    #replace mask sprite with catell sprite
    
    hide cat mask
    with dissolve
    show cat normal
    with dissolve
    
    un "I am Raymond Catell, the Dean who called you here."
    
    MC "W-What? So what happened? Why am I here? Why did I get a message to come over here?"
    
    cat "The events you've gone through aren't coincidential, they are part of a test."
         
    MC "What? A test? I thought I passed ACET with no complications?"
    
    cat "Oh yes you did pass splendidly, but this test checks for your 16 Personality Factors!"
    
    cat "I developed it over several decades of research!"
    
    MC "Wow, you must be really old..."
    
    cat "I did it to be able to judge someone by his or her personality. For me, there are two types of traits—{color=#ff0000}surface traits{/color} and {color=#0c00ff}source traits{/color}"
    
    cat "{color=#ff0000}Surface traits{/color} represent the personality characteristics easily seen by others"
    
    cat "{color=#0c00ff}Source traits{/color} on the other hand, are the basic traits that underlie the surface traits"
    
    cat "For example, shyness and being quiet are surface traits that relate to the source trait of introversion"
    
    MC "So?"
    
    cat "I identified 16 source traits and developed an assessment questionnaire out of it. It’s called “The Sixteen Personality Factor (16 PF) Questionnaire.” Isn’t that great?"
    
    MC "Yes, yes, it is very great! But how do you measure it?"
    
    cat "These 16 source traits are treated as trait dimensions  in which there are two opposite traits at each end with a range of possible degrees for each trait measurable along dimension"
    
    MC "Wow, that's really amazing! So I was under an experiment the entire time?"
    
    cat "Yes. Everyone directly and indirectly made you make several choices based on the 16 Personality Factors"
    
    cat "What of it?"
    
    MC "Bonus Points?"
    
label credits:
    
    play music "bgmCredits.mp3" fadein 2
    
    scene bg black
    
    "" "--Credits--"
    
    "Credits" "Information: 'Essentials of 16PF Assessment' by Heather E.P. Cattell, James M. Schuerger"
    
    "Credits" "Background Images and Sprites: Nina Sanchez and Aemielvin Loremia"
    
    "Credits" "Programmers: Seth Legaspi and Kenley Tan"
    
    "Credits" "Researchers: Jennifer Pagay and Wendell Laxamana"
    
    "Credits" "Music: Umineko naku no koro ni Musicbox Blue - Disc 1"
    
    "Credits" "Music: Shingeki no Kyojin - Original Soundtrack by Hiroyuki Sawano"
    
    "Credits" "Music: Mahou Shoujo Madoka Magica Special CD 6 by Yuki Kajiura"
    
    "Credits" "Story by the Teampura Group"
    
    "Credits" "Run by the Ren'Py visual novel engine"
    
    "Note" "No people were killed or hurt in the making of this vn... Probably."
            
    return
