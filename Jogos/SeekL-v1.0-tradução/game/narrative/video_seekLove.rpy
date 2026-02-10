label day5_seekLove_call: 
    hide screen seekL_ui 
    scene black 
    hide screen phonecall_window_real with pixellate 
    stop music fadeout 0.5
    $ first_line = True 

    $ in_call = True 
    #$ chat_location = "DAY " +next_day_number+ " - CALL"

    $ _preferences.afm_enable = True 

    pause 2 

    play music "audio/music/Digital_Dreamlooped.ogg" loop fadein 2.0 fadeout 2.0 

    pause 3

    # show screen credits_1 with Dissolve(2.0) 
    # pause 2 
    # hide screen credits_1 with Dissolve(0.5)
    
    show screen credits_2 with Dissolve(2.0) 
    pause 4
    hide screen credits_2 with Dissolve(2.0)


    # show screen credits_3 with Dissolve(2.0) 
    # pause 2 
    # hide screen credits_3 with Dissolve(0.5)

    show screen credits_4 with Dissolve(2.0) 
    pause 4
    hide screen credits_4 with Dissolve(2.0)

    show screen credits_5 with Dissolve(2.0) 
    pause 2 
    hide screen credits_5 with Dissolve(2.0)

    pause 4
    menu: 
        "Alô?":
            pass
    $ first_line = False 
    
    voice "audio/voice/day5/o5-001.ogg"
    o "Então você cumpriu sua parte do acordo."

    menu:
        "Você achou que eu não cumpriria?":
            voice "audio/voice/day5/o5-002.ogg"
            o "Não, mas eu ainda tinha que pegar no seu pé de alguma forma."
            menu:
                "Estou destinado(a) a nunca receber o devido reconhecimento, né?":
                    pass
            voice "audio/voice/day5/o5-003.ogg"
            o "Eu aprecio o fato de você ter atendido."
            menu:
                "Agora sim.":
                    pass 
        "Ahh! É você! ":
            voice "audio/voice/day5/o5-004.ogg"
            o "O quê? Achou que eu estava te dando um número aleatório?"
            menu:
                "Não! Eu só... torci muito para que fosse o seu, mas não quis criar expectativas.":
                    pass
            voice "audio/voice/day5/o5-005.ogg"
            o "Isso é... bom de ouvir."
            voice "audio/voice/day5/o5-006.ogg"
            o "Bem, não precisa mais ficar na expectativa. Eu já parei de te provocar... na maior parte."
            menu:
                "Ah, valeu... hein?! Na maior parte?!":
                    pass

    voice "audio/voice/day5/o5-007.ogg"
    o "Então, agora que já resolvemos isso..."
    menu:
        "Ei!":
            pass

    show cg romantic 
    camera:
        ypos -522 xpos 1395 zoom 1.58
        linear 5.0 xpos 324
    with dissolve
    voice "audio/voice/day5/o5-008.ogg"
    o "Agora que já resolvemos isso, fico feliz em ouvir sua voz."
    voice "audio/voice/day5/o5-009.ogg"
    o "Eu deveria ter planejado uma conversa, mas, sinceramente, não pensei muito além deste passo."

    menu:
        "Isso não parece com você.":
            pass

    show cg romantic 
    camera:
        xpos -1494 ypos 1683 zoom 2.0
        linear 5.0 ypos 2169
    with dissolve
    voice "audio/voice/day5/o5-010.ogg"
    o "Eu sei."
    voice "audio/voice/day5/o5-011.ogg"
    o "Eu estava tentando agir um pouco como você."
    menu:
        "Estava?":
            pass
    voice "audio/voice/day5/o5-012.ogg"
    o "Estava. Foi estranho, mas quase um pouco emocionante. "
    voice "audio/voice/day5/o5-013.ogg"
    o "É assim que você se sente quando apronta dessas?"
    menu:
        "Às vezes! Tente fazer isso mais vezes para ver.":
            pass
    voice "audio/voice/day5/o5-014.ogg"
    o "Acho que vou tentar."
    voice "audio/voice/day5/o5-015.ogg"
    o "Mudando de assunto, como está o tempo aí onde você está agora?"

    menu:
        "Está bem agradável, queria que você pudesse sentir.":
            voice "audio/voice/day5/o5-016.ogg"
            o "Se ao menos eu tivesse alguma renda extra recém-adquirida."
            menu:
                "Que pena.":
                    pass
            voice "audio/voice/day5/o5-017.ogg"
            o "Acho que teremos que deixar para a imaginação."
        "Terrível!":
            voice "audio/voice/day5/o5-018.ogg"
            o "Então parece que você precisa sair daí por um tempo."
            menu:
                "Ah, é?":
                    pass
            voice "audio/voice/day5/o5-019.ogg"
            o "Só estou dando uma sugestão."
        "Por quê, precisa de umas ideias de viagem?":
            voice "audio/voice/day5/o5-020.ogg"
            o "Só estou puxando assunto."
            menu:
                "Uhum. Sei.":
                    pass
            voice "audio/voice/day5/o5-021.ogg"
            o "O quê?"

    menu:
        "Você é tão transparente.":
            pass
    voice "audio/voice/day5/o5-022.ogg"
    o "Eu sei. Nem valeu a pena tentar disfarçar essa."
    voice "audio/voice/day5/o5-023.ogg"
    o "Ainda assim, a oferta está de pé."
    menu:
        "Acho que eu gostaria disso. Mas só com uma condição.":
            pass
    voice "audio/voice/day5/o5-024.ogg"
    o "E qual seria?"
    menu:
        "Responda sua própria pergunta. Como está o tempo aí onde você está?":
            pass
    voice "audio/voice/day5/o5-025.ogg"
    o "E por que eu te diria isso? "
    voice "audio/voice/day5/o5-026.ogg"
    o "Alguns de nós ainda se importam com a privacidade. "
    menu:
        "Aham. Sei. ":
            pass
    pause 1
    show cg romantic 
    camera:
        zoom 0.57 xpos 486 ypos 540
        linear 4.0 zoom 0.5
    with dissolve 
    voice "audio/voice/day5/o5-027.ogg"
    o "Hah. Não está ruim, na verdade. Tem uma brisa boa."
    voice "audio/voice/day5/o5-028.ogg"
    o "É... estranho."
    voice "audio/voice/day5/o5-029.ogg"
    o "Não é incomum, mas de alguma forma parece diferente. Um diferente bom."

    menu: 
        "Talvez seja um sinal.":
            voice "audio/voice/day5/o5-030.ogg"
            o "Pode ser. Pode não ser nada também."
            menu:
                "Isso importa?":
                    pass
            voice "audio/voice/day5/o5-031.ogg"
            o "Acho que não... Eu só gosto."
            voice "audio/voice/day5/o5-032.ogg"
            o "Eu gosto."
        "Está frio? Calor?":
            voice "audio/voice/day5/o5-033.ogg"
            o "Um pouco frio. Mas eu gosto assim. "
            voice "audio/voice/day5/o5-034.ogg"
            o "Sempre estive acostumado com minhas salas de servidores geladas."
            voice "audio/voice/day5/o5-035.ogg"
            o "Eu gosto disso. Gosto do frio. "
            voice "audio/voice/day5/o5-036.ogg"
            o "Eu gosto... desse sentimento. "

    pause 2
    voice "audio/voice/day5/o5-037.ogg"
    o "Obrigado."
    menu:
        "Pelo quê?":
            pass
    show cg romantic 
    camera:
        zoom 1.0 xpos -891 ypos 1091
        linear 4.0 xpos -729
    with dissolve 
    voice "audio/voice/day5/o5-038.ogg"
    o "Por estar aqui."
    voice "audio/voice/day5/o5-039.ogg"
    o "Por me ligar e... conversar sobre nada comigo."
    voice "audio/voice/day5/o5-040.ogg"
    o "Por me deixar divagar sobre o tempo e qualquer outra coisa. "
    pause 1
    voice "audio/voice/day5/o5-041.ogg"
    o "Parece que uma porta se entreabriu. Como se coisas melhores estivessem por vir."
    voice "audio/voice/day5/o5-042.ogg"
    o "Hum. Se é que isso faz sentido."
    menu:
        "Faz sentido. Fico feliz em ouvir isso.":
            pass 
    voice "audio/voice/day5/o5-043.ogg"
    o "Fico feliz. "
    voice "audio/voice/day5/o5-044.ogg"
    o "Eu gosto de saber que você está feliz."
    menu:
        "É?":
            pass 
    voice "audio/voice/day5/o5-045.ogg"
    o "É. "
    pause 1 
    voice "audio/voice/day5/o5-046.ogg"
    o "Eu tenho que começar a desempacotar as coisas, mas... podemos nos falar de novo em breve?"
    menu: 
        "Eu adoraria. Nos vemos então?":
            pass 
    show cg romantic 
    camera:
        zoom 0.5 xpos 486 ypos 540
    with dissolve 
    voice "audio/voice/day5/o5-047-seeyousoon.ogg"
    o "Até breve."

    $ quick_menu = False 
    $ persistent.seekLove = True
    $ _preferences.afm_enable = False 

    pause 1 
    show screen game_over_good_text with Dissolve(2.0) 
    
    pause 

    hide screen game_over_good_text with dissolve

    scene black 
    camera: 
        subpixel True pos (0,0) zoom 1.0
    with dissolve

    stop music fadeout 3.0 

    pause 4 

    return