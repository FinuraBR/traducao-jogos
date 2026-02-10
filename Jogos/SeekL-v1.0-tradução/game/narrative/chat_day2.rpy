label day2_start: 

    play music "audio/music/server_room_chiller_versionlooped.ogg" loop fadein 2.0 fadeout 2.0 

    $ player_choice(
        [
            ("oi de novo", "day2_1"), 
            ("voltei. pode me vaiar de novo", "day2_2"), 
            ("boooooooooooooooooooooooooooom dia!", "day2_3")
        ]
    )


label day2_1: 

    $ chat_message("wnpep: o não-tira retorna")

    #MC: what a title. can i earn a cooler one?
    $ player_choice(
        [
            ("que título. posso ganhar um mais legal?", "x")
        ]
    )

    $ chat_message("wnpep: bem, não estamos nos anos noventa, então. não")

    $ chat_message("elimf: fale por você eu tenho um banner GIGANTESCO do Hackerman")

    $ chat_message("elimf: pra dar motivação e coragem", ot="wnpep")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: isso não é")

    $ chat_message("wnpep: quer saber, vou deixar essa passar")

    $ chat_message("elimf: bem diferente de vc", ot="wnpep")

    $ chat_message("wnpep: me recuso a deixar você me forçar a fazer algo")

    $ chat_message("wnpep: explicar as coisas só vai me fazer sentir velho de novo",ot="elimf")

    $ chat_message("elimf: você que perde")

    $ chat_message("elimf: eu poderia ter aprendido algo")

    pause 1 

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("wnpep: quer dizer. você quer aprender alguma coisa? ")
    
    jump day2_4


label day2_2: 
    $ points_seekLove += 1

    $ chat_message("incri: não me diga o que fazer ")

    $ chat_message("wnpep: {image=e_letsgo}")

    $ chat_message("incri: talvez eu sjea legal só por issp então")

    #MC: well i'm not going to stop you
    $ player_choice(
        [
            ("bom, não sou eu que vou te impedir", "x")
        ]
    )

    $ chat_message("wnpep: podemos ver um pouco disso?")

    $ chat_message("incri: faz o favor de se foder")

    $ chat_message("wnpep: é, tudo bem",ot="elimf")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: chocada",fastmode=True)
    
    jump day2_4


label day2_3:
    $ points_seekLove += 1

    $ chat_message("elimf: obriiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiigaaaaaaaaaaaaaaaaaaaado")

    #MC: yyyouuuureeeeeeee weeeellcoommmmeeeeeeeeeeee
    $ player_choice(
        [
            ("deeeeeeeeeee naaaaaaaaaaaaaaaaaaaaaaaaaaaaaada", "x")
        ]
    )

    $ chat_message("elimf: vc é tipo. uma ondinha na minha poça. vc é gente boa")

    $ chat_message("wnpep: na verdade, minha opinião pode estar piorando.")

    $ chat_message("elimf: abrace a recém-descoberta presença de alguém inútil, mas divertido")

    #MC: now hold on
    $ player_choice(
        [
            ("opa, calma aí", "x")
        ]
    )

    jump day2_4
 

label day2_4: 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: cala a boca cala a boca cala a boca")

    $ chat_message("elimf: cuidado, vamos distrair o incri e arruinar a \"arte\" dele ", ot="incri")

    $ chat_message("incri: cala a bocaaaa")

    $ chat_message("incri: vc é um puta perdedor. desgraçado. idiota", ot="elimf")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: burro também")

    # incri typing

    $ chat_message("wnpep: vamos mudar um pouco o rumo da conversa",ot="incri")

    $ chat_message("wnpep: incri, como está o progresso? ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: enfia no s eu")

    pause 1

    $ chat_message("wnpep: tudo bem ")

    $ chat_message("elimf: vc continua deixando isso acontecer")

    $ chat_message("wnpep: eu sei, e mesmo assim continuo pisando no mesmo ancinho", ot="incri")

    $ chat_message("incri: não q vc se importe mas to quase acabando")

    $ chat_message("incri: merda de gov de baixo nível é facillll")

    #MC: is that what ur looking at? 
    $ player_choice(
        [
            ("é nisso que vc tá mexendo? ", "x")
        ]
    )

    $ chat_message("incri: o q vc tem a ver. tira. cagueta")

    $ chat_message("elimf: sua cabeça explode quando o caixa pergunta se vc achou tudo o que queria")

    $ chat_message("wnpep: espero que não, eles só estão tentando fazer o trabalho deles")

    #MC: sorry, i was just curious about your process w the program
    $ player_choice(
        [
            ("desculpa, eu só fiquei curioso sobre seu processo com o programa", "x")
        ]
    )

    $ chat_message("elimf: a sinceridade não. manobra ousada",ot="incri")

    $ chat_message("incri: puxar saco não vai funcionar")

    $ chat_message("incri: minhas técnicas estão além d vc")

    pause 2

    $ chat_message("incri: na verddae")

    $ chat_message("incri: eu acabei de pensar numa cois")

    $ chat_message("elimf: lá vem", ot="incri")

    $ chat_message("incri: vou te ensinar um coisa SÓ")

    $ chat_message("incri: é tão fácil que até vc deve entender")

    #MC: …thanks
    $ player_choice(
        [
            ("...valeu", "x")
        ]
    )

    $ chat_message("incri: busca em banco d dados e tals")

    $ chat_message("incri: vc acha as coisas e me fala e eu faço a porra da parte avançada")

    $ chat_message("wnpep: isso soa um pouco")

    $ chat_message("elimf: incri descobre uma jogada de xadrez de 1000 de qi: fazer outra pessoa fazer o trabalho",ot="wnpep")

    $ chat_message("wnpep: tirou as palavras da minha boca")

    $ chat_message("wnpep: não conseguiu resistir ao canto da sereia do trabalho não remunerado")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: seus cuzões invejosos não é issp")

    $ chat_message("incri: é educativo")

    $ chat_message("incri: estou sendo tão PRESTATIVO",ot="elimf, wnpep")

    $ chat_message("elimf: aham, com certeza", ot="wnpep")

    $ chat_message("elimf: {image=e_orz}", ot="wnpep")

    $ chat_message("wnpep: nós jamais duvidaríamos de você")

    #MC: I would be very grateful
    $ player_choice(
        [
            ("Eu ficaria muito grato", "x")
        ]
    )

    $ chat_message("incri: nunca mais me peça nda", ot="elimf")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: meu deus eles ainda tão nessa")

    $ chat_message("wnpep: temos que dar crédito pela pura falta de vergonha na cara")

    #MC: er, you didn't have to do all this
    $ player_choice(
        [
            ("er, você não precisava fazer tudo isso", "x")
        ]
    )

    $ chat_message("incri: não agora eu tenho q")

    $ chat_message("incri: vamo mostrar pra esss palhaços do caralho")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: entra no programa")

    #### SEEKL SEGMENT BEGINS 

    #MC: i'm in. like since i logged in
    $ player_choice(
        [
            ("eu tô dentro. tipo, desde que eu loguei", "day2_5"), 
            ("você que entra no programa", "day2_6")
        ]
    )

label day2_5: 
    $ chat_message("incri: cala a boca e escuta ")
    jump day2_7


label day2_6: 
    $ points_seekLove += 1
    $ chat_message("incri: vc é tãããão engraçado hahahahaha")
    jump day2_7

label day2_7:

    $ chat_message("incri: eu já tenho o número do distintvo dele ")

    $ chat_message("incri: vai lá e puxa a tabela: #azgov.police_info#")
    pause 0.5
    $ tables_seen.append("azgov.police_info")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.police_info"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_9"

    $ chat_message("elimf: vc tá no arizona????")

    $ chat_message("incri: não tô não seu merd a")

    $ chat_message("incri: eu só tava de passagem ",ot="wnpep")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: fico desconfortável sabendo tanto sobre o incri ",ot="elimf")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: arizona... ",ot="incri")

    $ chat_message("incri: merda ",fastmode=True)

    $ chat_message("incri: {color="+color_help+"}puxa logo thrim{/color}",ot="wnpep")

    $ chat_message("wnpep: lembre-se ")

    $ chat_message("wnpep: `select * \nfrom azgov.police_info`")

    $ chat_message("wnpep: ou {color="+color_help+"}clique na tabela na sua lista de tabelas{/color} e aperte executar")

    $ chat_message("wnpep: {image=e_wink}")

    jump wait_start

# label day2_8:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False
#     $ waiting_label = "day2_9"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_9 
#     $ renpy.pause(hard=True)

label day2_9:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 
    #MC: I see the table now. 
    $ player_choice(
        [
            ("Estou vendo a tabela agora. ", "x")
        ]
    )

    $ chat_message("incri: ok vc tá vendo o número do distintvo ")

    $ chat_message("incri: {color="+color_help+"}55242{/color} ")
    pause 0.2
    $ hack_notes.append("badge: \n55242")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ player_choice(
        [
            ("sim, estou vendo ", "day2_10"), 
            ("não?", "day2_11")
        ]
    )

    #[1] MC: yes, i see it 
label day2_10: 
    $ points_seekLove += 1

    $ chat_message("incri: fácil ")
    jump day2_12


    #[2] MC: no? 
label day2_11: 

    $ chat_message("incri: na {color="+color_help+"}coluna badge_no{/color} idiota ")

    #$ chat_message("incri: {image=e_pain}")

    #MC: ok. yes. i see it. 
    $ player_choice(
        [
            ("ok. sim. estou vendo.", "x")
        ]
    )

    $ chat_message("incri: seu idiota ")
    jump day2_12


label day2_12: 
    $ chat_message("incri: nome pfv ")

    #MC: Bruce Johnson 
    $ player_choice(
        [
            ("diz \"Bruce Johnson\"", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("name: \n'Bruce Johnson'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("wnpep: o tira tinha cara de bruce? ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: tinha cara de fdp ")

    $ chat_message("incri: ok vc pode olhar esta tabela agora ")

    $ chat_message("incri: #azgov.marriage#")
    pause 0.5
    $ tables_seen.append("azgov.marriage")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.marriage"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_17"

    #MC: why? 
    $ player_choice(
        [
            ("por que uma tabela de casamentos??", "x")
        ]
    )

    $ chat_message("incri: ????") 

    $ chat_message("incri: quem se importa??????",ot="elimf, wnpep")

    $ chat_message("elimf: por que vc tá indo atrás de um tira incri ",ot="wnpep")

    $ chat_message("incri: pq ele me fodeu ",ot="wnpep")

    $ chat_message("wnpep: você levou uma multa de estacionamento? ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: meu tempo na vaga tinha acabado d vencer") 

    $ chat_message("incri: ditador do tempo estúpido, cuzão, imbecil ")

    $ chat_message("elimf: quanto tempo de atraso ")

    $ chat_message("incri: tipo 1 min ")

    $ chat_message("elimf: ah ",ot="wnpep")

    $ chat_message("wnpep: só 1 min de atraso? ")

    $ chat_message("incri: SIM ")

    $ chat_message("wnpep: ok. entendo ",ot="incri")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: EU VOU LIMPAR A CARTEIRA DELE ")

    $ chat_message("wnpep: vai com tudo, estrela! ",ot="elimf")

    $ chat_message("elimf: é pra isso que a gente tá aqui", ot="wnpep") 

    $ chat_message("wnpep: vamos massacrar essa conta poupança! ")

    $ chat_message("wnpep: {image=e_sparkle}")

    $ player_choice(
        [
            ("tudo isso por uma multa de estacionamento? o quê??", "day2_13"), 
            ("ebaa!", "day2_14")
        ]
    )


    # [1] MC: all over a parking ticket? what?? 
label day2_13:
    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: VC NÃO PRECISA ESTAR AQUI") 

    $ chat_message("incri: VC PODE IR EMBORA")

    #MC: I'M NOT LEAVING I WAS JUST ASKING A QUESTION 
    $ player_choice(
        [
            ("EU NÃO VOU SAIR, SÓ ESTAVA FAZENDO UMA PERGUNTA", "x")
        ]
    )

    $ chat_message("incri: PARA DE FAZER ISSO ")
    jump day2_15

    #[2] MC: yay! 
label day2_14:
    $ points_seekLove += 1

    $ chat_message("incri: DESTRUA ")
    jump day2_15


   
label day2_15:

    # MC: but, how are we getting to his savings account through marriage records? 
    $ player_choice(
        [
            ("mas, como vamos chegar na conta poupança dele através de registros de casamento? ", "x")
        ]
    )

    $ chat_message("elimf: todo mundo tem segredos ")

    $ chat_message("elimf: e algumas pessoas têm cônjuges ")

    $ chat_message("elimf: que não sabem de todos os segredos ",ot="incri, wnpep")

    $ chat_message("incri: ^ isso ",ot="wnpep")

    $ chat_message("wnpep: eu conto tudo para minha esposa. essa coisa de extorsão nunca funcionaria comigo ")

    pause 1

    $ chat_message("elimf: VC É CASADO?? ")

    $ chat_message("wnpep: o que ")

    pause 1

    $ chat_message("wnpep: ah ")

    $ chat_message("wnpep: {image=e_serious}")

    pause 2 

    $ chat_message("wnpep: corretor automático haha ")

    $ chat_message("wnpep: esposa = amiga ",ot="elimf")

    $ chat_message("elimf: como que isso vira isso no corretor") 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: não consigo processar essa informação pare de falar imediatamente ",ot="wnpep")

    $ chat_message("wnpep: eu não sou casado ")

    $ chat_message("elimf: ok agora pare de falar ",ot="incri")

    $ chat_message("incri: OK ")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA BUZINAR")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI MANDA BUZINAR")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: {color="+color_help+"}VAI OLHAR A TABELA{/color}")

    $ chat_message("incri: #AZGOV.MARRIAGE#")

    jump wait_start


# label day2_16:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False
#     $ waiting_label = "day2_17"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_17 
#     $ renpy.pause(hard=True)

label day2_17:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    #MC: i see it 
    $ player_choice(
        [
            ("estou vendo", "x")
        ]
    )

    $ chat_message("incri: tá vendo o bruce? ")

    #MC: no... i don't think so 
    $ player_choice(
        [
            ("não... acho que não", "x")
        ]
    )

    $ chat_message("incri: então adiciona uma cláusula where, seu burro ")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["spouse_name"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.marriage"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("mid", "M2635187")] 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_22"

    $ chat_message("wnpep: nós ainda não mostramos as cláusulas where pra thrim ")

    $ chat_message("elimf: VC É CASADO ")

    $ chat_message("wnpep: não sou casado ")

    $ chat_message("elimf: {image=e_baby}")

    #MC: i heard wnpep was married 
    $ player_choice(
        [
            ("ouvi dizer que o wnpep é casado", "x")
        ]
    )

    $ chat_message("elimf: EU TAMBÉM OUVI DIZER QUE O WNPEP É CASADO", ot="wnpep")

    $ chat_message("wnpep: ok thrim, {color="+color_syntax+"}WHERE{/color} é algo que você coloca depois da instrução from.")

    $ chat_message("wnpep: é como {color="+color_help+"}um filtro que você usa quando só se importa com certos registros{/color}")

    $ chat_message("wnpep: tipo, se estivéssemos olhando a table.example de novo e eu quisesse ver minhas informações")

    $ chat_message("wnpep: eu adicionaria isto ao final do meu código: {color="+color_syntax+"}where hacker_name = 'wnpep'{/color}")

    #$ chat_message("wnpep: does that make sense? ")

    $ chat_message("wnpep: a instrução inteira ficaria \n`select * \nfrom table.example \nwhere hacker_name = 'wnpep'`")

    $ chat_message("elimf: exceto que {color="+color_help+"}vc não precisa usar aspas quando está procurando por números{/color}")

    $ chat_message("elimf: tipo, se eu quisesse ver quem tem mais de 30 hacks eu poderia escrever ")

    $ chat_message("elimf: `select hacker_name \nfrom table.example\nwhere number_of_hacks > 30`")

    $ chat_message("elimf: faz sentido?")

    $ chat_message("elimf: {image=e_orz}")

    $ player_choice(
        [
            ("entendi. sei o que fazer", "day2_18"), 
            (".................", "day2_19")
        ]
    )

    #[1] MC: i get it. i know what to do 
label day2_18:
    $ points_seekLove += 1

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: ótimo! ")

    jump day2_20

    #[2] MC: ................. 
label day2_19:

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: isso é tipo tão bási co vc ta de sacanagem comigo ")

    #MC: dick
    $ player_choice(
        [
            ("babaca", "x")
        ]
    )

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: sim. bem. aqui. melhor ajudar ")

    $ chat_message("wnpep: `select * \nfrom azgov.marriage \nwhere full_name = 'bruce johnson'`")

    jump day2_20 

label day2_20: 
    $ chat_message("incri: me avisa quando vc terminr de {color="+color_help+"}achar o tira idiota na tbl de casamento{/color}")

    jump wait_start


# label day2_21:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_22"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_22 
#     $ renpy.pause(hard=True)

label day2_22:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    $ chat_message("incri: achou ele?" )

    #MC: yes -- his spouse is named "laura crane" 
    $ player_choice(
        [
            ("sim -- a esposa dele se chama \"laura crane\"", "day2_23"), 
            ("sim -- a esposa dele se chama \"deide costa\"", "day2_24")
        ]
    )

label day2_23: 
    pause 0.2
    $ hack_notes.append("wife: \n'Laura Crane'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("wnpep: pode ser o nome de solteira e não o nome legal dela agora" )

    jump day2_25 


label day2_24: 
    $ points_seekLove += 1

    $ chat_message("wnpep: nome do meio? ", ot="incri")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA BUZINAR")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: v hnvhnv nnv  nv jmj ")

    $ chat_message("incri: j  hnvg gb nbm", ot="wnpep")

    pause 0.5

    $ chat_message("SYSTEM: INCRI offline") 
    $ incri_online = False

    pause 1.0

    $ chat_message("SYSTEM: INCRI online") 
    $ incri_online = True 

    $ chat_message("incri: nv n v nbvb v nm  uj,",ot="elimf")

    $ chat_message("elimf: a socada no teclado começou ")

    $ chat_message("wnpep: olha a boca ")

    pause 1

    $ chat_message("incri: :) ")

    $ chat_message("incri: thrim ")

    $ player_choice(
        [
            ("quantos teclados você quebra por dia", "x")
        ]
    )

    $ chat_message("wnpep: a esposa é 'Laura Crane' inc ", ot="incri")
    pause 0.2
    $ hack_notes.append("wife: \n'Laura Crane'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("incri: :) ")

    jump day2_25 

label day2_25: 
    # odxny logs on 
    pause 0.5
    $ chat_message("SYSTEM: ODXNY online") 

    $ chat_message("odxny: Olá a todos.")

    $ chat_message("elimf: o incri é do arizona e o wnpep é casado ")

    $ chat_message("odxny: O quê? ",ot="wnpep, incri")

    $ chat_message("incri: {image=e_letsgo}", ot="wnpep",fastmode=True)

    $ chat_message("incri: EU NÃO SOU ", ot="wnpep")

    $ chat_message("wnpep: foi um mal-entendido ", ot="odxny")

    $ chat_message("odxny: O que aconteceu com o sigilo? ")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: eu não sei, estou na miséria ")

    $ chat_message("odxny: Qual o hack atual? ")

    $ chat_message("incri: EU ESTOU TENTANDO EXTORQUIR UM TIRA MAS VCS NÃO PARAM DE ME INTERROMPER ")

    $ chat_message("odxny: {image=e_serious}")

    $ chat_message("odxny: Desculpas. Isso parece importante.", ot="incri")

    $ chat_message("incri: THRIM ")

    $ chat_message("incri: PRECISAMOS DE EMAILS") 

    #MC: WHERE DO I GET EMAILS 
    $ player_choice(
        [
            ("ONDE EU CONSIGO EMAILS", "x")
        ]
    )

    $ chat_message("incri: #irs.contacts#")
    pause 0.5
    $ tables_seen.append("irs.contacts")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I80397-693")] 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_27"

    $ chat_message("elimf: ei, quando conseguimos dados da receita federal, pera",ot="wnpep")

    $ chat_message("wnpep: isso é meio louco", ot="odxny") 

    $ chat_message("odxny: Uma semana atrás.") 

    $ chat_message("elimf: doideira") 

    $ chat_message("elimf: wnpep, isso vai ser bom pro seu último hack, né?")

    $ chat_message("wnpep: lol",ot="incri") 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: VAI ACHAR O EMAIL DO BRUCE THRIM") 

    $ chat_message("elimf: {color="+color_help+"}COM UM DELICIOSO USO DA CLÁUSULA WHERE{/color}") 

    jump wait_start

    # wait for code to run 
# label day2_26:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_27"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_27 
#     $ renpy.pause(hard=True)

label day2_27:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    $ chat_message("incri: ESTOU ESPERANDO") 

    #MC: ok i got it 
    $ player_choice(
        [
            ("ok, peguei", "x")
        ]
    )

    #MC: brucemjohn11@copmail.com
    $ player_choice(
        [
            ("bruce.johnson@copmail.com", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("email: \n'bruce.johnson\n@copmail.com'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5 

    $ chat_message("incri: OK AGORA O EMAIL DA LAURA")   
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I20210-713"), ("irs_id", "I24270-766")] 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day2_29"

    $ chat_message("odxny: Lendo aqui. E a questão do nome de solteira?")  

    $ chat_message("odxny: O sobrenome dela pode ser Crane ou Johnson, na minha opinião.")  

    $ chat_message("incri: ENTÃO PROCURE PELOS DOIS NOMES????", ot="wnpep")  

    $ chat_message("wnpep: crane + johnson")  

    #MC: at the same time? 
    $ player_choice(
        [
            ("ao mesmo tempo?", "x")
        ]
    )

    $ chat_message("wnpep: {color="+color_help+"}você pode usar um OR{/color}")  

    $ chat_message("wnpep: {color="+color_syntax+"}where full_name = 'laura johnson' \nor full_name = 'laura crane'{/color}") 

    $ chat_message("wnpep: {image=e_wink}")

    #MC: ok ok ok 
    $ player_choice(
        [
            ("ok ok ok", "x")
        ]
    )

    jump wait_start

    # // wait for code to run and see both results 
# label day2_28:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_29"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_29 
#     $ renpy.pause(hard=True)

label day2_29:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    $ chat_message("odxny: Então, qual parece ser a melhor correspondência? ") 

    $ chat_message("wnpep: estou procurando também ") 

    #MC: i think it's.... 
    $ player_choice(
        [
            ("eu acho que é...", "x")
        ]
    )

    $ player_choice(
        [
            ("lauracrane78@wahoo.com", "day2_30"), 
            ("laura.crane.johnson@eeemail.com", "day2_32"), 
            ("crazee_js_girl@eeemail.com", "day2_31")
        ]
    )

    #[1] MC: [ two wrong answer options ] 
label day2_30: 

    jump day2_31 

label day2_31: 

    $ chat_message("wnpep: discordo. laura.crane.johnson é muito mais provável ")
    pause 0.2 
    $ hack_notes.append("email wife: \n'laura.crane.\njohnson\n@eeemail.com'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("wnpep: combina com o sobrenome do bruce + o nome de solteira dela ") 

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: ok. thrim se recomponha ") 

    #MC: you can fucking do this yourself 
    $ player_choice(
        [
            ("você pode fazer essa porra sozinho", "x")
        ]
    )

    $ chat_message("incri: passa o ip wnpep ") 

    $ chat_message("elimf: OOHHHHHHHH")

    #MC: I'm sorry. I'm sorry. I'm sorry. 
    $ player_choice(
        [
            ("Desculpa. Desculpa. Desculpa.", "x")
        ]
    )

    $ chat_message("incri: fala assim comigo de novo pra vc ver ") 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: pra ver o que acontece ") 

    $ chat_message("odxny: Calma. ") 

    $ chat_message("incri: tô calmo") 

    $ chat_message("odxny: Claro. ") 

    jump day2_33 

    #[2] MC: laura.crane.johnson@eeemail.com 
label day2_32:     
    $ points_seekLove += 1

    $ chat_message("wnpep: concordo. todos os outros não parecem tão prováveis ") 
    pause 0.2
    $ hack_notes.append("email wife: \n'laura.crane.\njohnson\n@eeemail.com'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("elimf: acho que vcs estão subestimando a garota doida do js ")

    $ chat_message("elimf: j johnson ")

    $ chat_message("elimf: só to dizendo ",ot="wnpep")

    $ chat_message("wnpep: lol ", ot="odxny")

    $ chat_message("odxny: Muitas possibilidades para j. Apenas volte se o outro email não funcionar, eu acho ")

    $ chat_message("wnpep: ou envie a mesma informação para os dois ")

    $ chat_message("odxny: Verdade. Lmao ",ot="incri")

    $ chat_message("incri: ok. agora.") 

    jump day2_33 

   
    # end choices  
label day2_33: 
    $ chat_message("incri: {image=e_orz}")

    $ chat_message("incri: vou guardar esse email pra caso precise") 

    $ chat_message("incri: agora temos mais um passo ")

    #MC: which is...? 
    $ player_choice(
        [
            ("que é...?", "x")
        ]
    )

    $ chat_message("odxny: Achar algo para usar como chantagem.") 

    $ chat_message("odxny: É trivial quando você tem o email deles. ")

    $ chat_message("incri: {image=e_baby}")

    $ chat_message("incri: aff eu odeio essa parte. procurar. chato ")

    $ chat_message("wnpep: bem, que tipo de segredos você guardaria de sua esposa? ")

    $ chat_message("elimf: por que você não nos conta wn ")

    $ chat_message("elimf: o especialista em casamentos ")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: casado ",ot="wnpep")

    $ chat_message("wnpep: não sou casado ")

    $ player_choice(
        [
            ("infidelidade?", "day2_34"), 
            ("problemas financeiros?", "day2_35"),
            ("não sei. pode ser qualquer coisa", "day2_36")
        ]
    )

    #[1] MC: infidelity? 
label day2_34: 
    $ points_seekLove += 1

    $ chat_message("incri: pera. gênio. SIM ")

    $ chat_message("incri: ELE TINHA CARA DE CORNO")

    $ chat_message("odxny: Tipo a esposa dele o traía? ")

    $ chat_message("incri: NÃO ELE É O TRAIDOR") 

    $ chat_message("odxny: Então. Não é corno. Ela é a corna.") 

    $ chat_message("incri: IMAGINA NÃO SABER O QUE É UM CORNO") 

    $ chat_message("odxny: VOCÊ LITERALMENTE NÃO SABE ",ot="elimf")

    $ chat_message("elimf: OUVI DIZER QUE O WNPEP É CORNO", fastmode=True) 

    $ chat_message("wnpep: EU NÃO SOU CASADO")
    
    jump day2_37

    #[2] MC: money problems?   

label day2_35: 
    $ points_seekLove += 1

    $ chat_message("odxny: Comum, mas... ALGUÉM perdeu nossa rede bancária. ")

    $ chat_message("elimf: {image=e_baby}")

    $ chat_message("elimf: eu já pedi desculpas ")

    #MC: how did you lose access? I thought we made copies of data 
    $ player_choice(
        [
            ("como vocês perderam o acesso? Pensei que fazíamos cópias dos dados", "x")
        ]
    )

    $ chat_message("odxny: Às vezes damos azar e as pessoas apagam nossos arquivos.") 

    $ chat_message("elimf: FOI ACIDENTE mano ", ot="incri")

    $ chat_message("incri: inconveniente pra caralho perder isso ")

    $ chat_message("incri: ainda tô puto pra ser sincero ")

    $ chat_message("incri: {image=e_serious}")

    $ chat_message("wnpep: também estou meio desapontado. ")

    $ chat_message("elimf: não... o desapontamento não...")

    $ chat_message("wnpep: seja melhor.")

    $ chat_message("odxny: Conseguiremos mais dados eventualmente.")

    $ chat_message("odxny: enquanto isso, porém, o que mais poderíamos procurar? ")

    $ player_choice(
        [
            ("infidelidade?", "day2_34"), 
            ("não sei. pode ser qualquer coisa", "day2_36")
        ]
    )

    #[3] MC: not sure. could be anything 
label day2_36: 

    $ chat_message("odxny: Nem um palpite? Decepcionante.", ot="elimf") 

    $ chat_message("elimf: traição ")

    $ chat_message("elimf: infidelidade ")

    $ chat_message("elimf: a maior traição conjugal ")

    $ chat_message("wnpep: eles podem ter um relacionamento aberto. nunca presuma ")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: as estatísticas estão do meu lado ")

    $ chat_message("odxny: Concordo. É mais provável que este policial seja monogâmico. Mas, quem sabe? ")

    $ chat_message("elimf: vc queria que mais relacionamentos fossem abertos wn")

    $ chat_message("elimf: sem motivo")

    $ chat_message("wnpep: sem opinião",ot="elimf")

    $ chat_message("elimf: casado")

    # pause 0.2
    # play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos

    jump day2_37

    # end choices 
label day2_37: 

    $ chat_message("incri: use o email do bruce pra ver se ele tá aqui thrim ")

    $ chat_message("incri: #secretsmooch.users#")
    pause 0.5
    $ tables_seen.append("secretsmooch.users")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["ss_alias"] 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["secretsmooch.users"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("ss_cid", "72770-SS")] # this needs to change to allow a join find to work later on. i'm not sure why it didn't work
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False
        waiting_label = "day2_39"

    $ chat_message("elimf: o bom e velho secretsmooch")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: vergonhoso. esse site é especificamente para traição ",ot="incri")

    $ chat_message("elimf: pera, tenho uma pergunta CRÍTICA pro grupo")

    $ chat_message("wnpep: ?", ot="elimf")

    $ chat_message("elimf: se vc estivesse traindo seu cônjuge e tivesse uma conta no secretsmooch")

    $ chat_message("elimf: qual seria seu nome de usuário")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: sério?",ot="elimf")

    $ chat_message("elimf: obrigatório responder",ot="incri")

    $ chat_message("elimf: o meu obviamente seria LordeDoSexo")

    $ chat_message("odxny: Sem 420?")

    $ chat_message("elimf: {image=e_pain}")
    
    $ chat_message("elimf: que tipo de maconheiro básico vc acha que eu SOU")

    $ chat_message("odxny: Quer dizer.")

    $ chat_message("elimf: incri sua vez")

    $ chat_message("incri: c0m3d0rDpUt4s69")

    $ chat_message("elimf: KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK?????")

    $ player_choice(
        [
            ("uau uh. muito legal!", "day2_37_inc_1"), 
            ("isso é incrivelmente estúpido", "day2_37_inc_2")
        ]
    )

label day2_37_inc_1: 
    $ points_seekLove += 1

    $ chat_message("incri: vlw")

    jump day2_37_inc

label day2_37_inc_2: 

    $ chat_message("incri: pls como se o seu fosse ser irado")

    jump day2_37_inc

label day2_37_inc: 

    $ chat_message("wnpep: não deveria usar esse tipo de linguagem para mulheres em um nome de usuário")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: ah tá bom especialista em esposas")

    $ chat_message("wnpep: eu não sou casado")

    $ chat_message("elimf: responda a pergunta wnpep")
    
    $ chat_message("wnpep: não tenho uma resposta porque eu não trairia.")

    $ chat_message("incri: ela tá no quarto com vc agora")

    $ chat_message("wnpep: quem?")

    $ chat_message("incri: idiota")

    $ chat_message("elimf: ok e vc thrim")

    $ chat_message("elimf: vamos precisar da sua resposta")

    $ chat_message("elimf: {image=e_orz}")

    $ player_choice(
        [
            ("mas o wnpep não respondeu!", "day2_37_1"), 
            ("ok fácil. o meu seria...", "day2_37_2")
        ]
    )

# sexlord
# where 420 
# basic stoner u think i am 

label day2_37_1: 

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: lol vc acha que tem a mesma liberdade aqui que o wnpep")

    $ chat_message("incri: responde peão")

    $ player_choice(
        [
            ("puta que pariu. o meu seria...", "x")
        ]
    )

    jump day2_37_2

label day2_37_2: 

    $ player_choice(
        [
            ("AmanteSecreto", "day2_37_2_A"), 
            ("campeaoDoPunho92", "day2_37_2_B"), 
            ("na_preguica_e_na_punheta", "day2_37_2_C")
        ]
    )

label day2_37_2_A: 

    $ chat_message("elimf: {image=e_pain}")
    
    $ chat_message("elimf: vc é inacreditavelmente chato")

    $ chat_message("wnpep: é meio romântico. para um nome de usuário de traição.")

    $ player_choice(
        [
            ("olha...", "x")
        ]
    )

    jump day2_37_2_cont

label day2_37_2_B: 
    $ points_seekLove += 1

    $ chat_message("elimf: CAMPEÃO?")

    $ chat_message("incri: provavel q seja mentira. provavel q nunca tenha feito")

    $ player_choice(
        [
            ("vc não me conhece", "x")
        ]
    )

    $ chat_message("incri: honestamente, sem vibe de fisting")

    $ chat_message("wnpep: o que exatamente é uma \"vibe de fisting\"")

    $ chat_message("incri: é vc com certeza não tem também")

    jump day2_37_2_cont


label day2_37_2_C: 
    $ points_seekLove += 1

    $ chat_message("elimf: ah COM CERTEZA irmão")

    $ player_choice(
        [
            ("todo dia irmão", "x")
        ]
    )

    $ chat_message("elimf: todo dia")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: juvenil.")

    $ chat_message("incri: vergonha alheia concordo")

    $ chat_message("elimf: KKKK")

    jump day2_37_2_cont


label day2_37_2_cont: 

    $ chat_message("wnpep: não temos um hack para fazer?")

    $ chat_message("elimf: espera aí. qual o do odxny")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("incri: lol como se eles fossem responder")

    $ chat_message("elimf: nunca se sabe")

    $ chat_message("odxny: Estou bem, obrigado.")

    $ chat_message("elimf: suspiro dos mais pesados")

    $ chat_message("incri: te nomeamos c0m3d0rDpUt4s70")

    $ chat_message("odxny: De volta ao hack.")

    $ chat_message("incri: TÁ BOM")

    $ chat_message("incri: THRIM")

    $ chat_message("incri: {color="+color_help+"}VERIFIQUE O EMAIL DO BRUCE NA TABELA DO SECRETSMOOCH IMEDIATAMENTE{/color}")

    jump wait_start

    # waits for MC 
# label day2_38:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos 
#         $ first_flash = False 
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day2_39"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day2_39 
#     $ renpy.pause(hard=True)

label day2_39:
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 

    # MC: i got it! he's totally here! 
    $ player_choice(
        [
            ("consegui! ele tá totalmente aqui!", "x")
        ]
    )

    $ chat_message("incri: EU SABIA ")

    $ chat_message("incri: EU TE PEGUEI, PORRA ")

    $ chat_message("incri: me dá o nome de usuário ")

    $ chat_message("incri: {image=e_letsgo}")

    #MC: alias? 
    $ player_choice(
        [
            ("apelido?", "x")
        ]
    )

    $ chat_message("incri: seja lá como se chama deus ")

    #MC: it's "OfficerOral" 
    $ player_choice(
        [
            ("é \"OficialOral\"", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("alias: \n'OfficerOral'")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK ",ot="odxny")

    $ chat_message("odxny: Ha. Sério? ",ot="elimf")

    $ chat_message("elimf: PUTA MERDA ",fastmode=True)

    $ chat_message("wnpep: vergonhoso. ",ot="elimf")

    $ chat_message("elimf: OFICIAL EU FUI UM MENINOOOOOO MAUUUUUUUUUU ")

    $ chat_message("wnpep: vc é um cara?????? ")

    $ chat_message("elimf: eu não sou um ")

    pause 2 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: ah meu deus do céu você fez isso comigo ")

    $ chat_message("wnpep: VOCÊ PODERIA TER SE RECUSADO A RESPONDER", ot="incri")

    $ chat_message("incri: \"OficialOral\" ")

    $ chat_message("incri: ele tá fudido ")

    $ chat_message("incri: vlw thrim ")

    $ chat_message("incri: {image=e_sparkle}")

    $ player_choice(
        [
            ("de nada. eu acho", "day2_40"), 
            ("não sei se eu realmente fiz alguma coisa ", "day2_41")
        ]
    )

    #[1] MC: no problem. i think 
label day2_40: 
    $ points_seekLove += 1

    $ chat_message("wnpep: vc foi ótimo! tenha orgulho ")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: dominou os comandos básicos do seekL ")

    $ chat_message("elimf: tão bom em digitar coisas que as pessoas te mandam digitar! ")

    $ chat_message("elimf: estou batendo palmas na vida real ")

    #MC: .... thanks. 
    $ player_choice(
        [
            (".... valeu.", "x")
        ]
    )

    $ chat_message("wnpep: ebaa!") 

    $ chat_message("wnpep: {image=e_sparkle}")

    jump day2_42

    #[2] MC: i don't know if i did anything really 
label day2_41: 

    $ chat_message("incri: vc não fez eu tava tentando ser um bom líder") 

    $ chat_message("incri: fazer vc se sentir legal por ")

    $ chat_message("incri: escrever o código mais bosta que eu já vi ")

    $ chat_message("incri: {image=e_pain}")

    #MC: have u ever said anything nice to anyone ever 
    $ player_choice(
        [
            ("você já disse algo legal pra alguém na vida", "x")
        ]
    )

    $ chat_message("incri: eu sou a pessoa mais legal que vc vai conhecer ")

    jump day2_42

    # end choices

label day2_42: 

    $ chat_message("odxny: Quanto você vai pedir?") 

    $ chat_message("incri: silêncio por $50k ")

    $ chat_message("incri: 20% pra vc chefe? ")

    $ chat_message("odxny: Obrigado. Sim ")

    pause 1.5

    $ chat_message("SYSTEM: EXTORSÃO ENVIADA - BRUCE.JOHNSON@COPMAIL.COM")

    $ chat_message("incri: ahhhhhhhhhh")

    #MC: how long will it take for him to respond? 
    $ player_choice(
        [
            ("quanto tempo vai levar para ele responder?", "x")
        ]
    )

    $ chat_message("wnpep: alguns levam dias, outros levam minutos ")

    $ chat_message("wnpep: só depende da pessoa ")

    pause 1.0

    $ chat_message("SYSTEM: RESPOSTA - BRUCE.JOHNSON - Isso é palhaçada. Esse não é meu perfil. Vou enviar essa ameaça para a polícia. ")

    #$ chat_message("incri: oh he's fast ")
    $ player_choice(
        [
            ("nossa, ele é rápido", "x")
        ]
    )

    $ chat_message("odxny: Um pouco irritado. ")

    $ chat_message("elimf: típico ",ot="incri")

    $ chat_message("incri: hora da réplica ")

    pause 0.5

    $ chat_message("SYSTEM: EXTORSÃO ENVIADA - BRUCE.JOHNSON@COPMAIL.COM ")

    $ chat_message("elimf: o que você mandou dessa vez? ")

    $ chat_message("incri: segredo ",ot="odxny")

    $ chat_message("incri: {image=e_orz}",ot="odxny")

    $ chat_message("odxny: Eu consigo ver o que ele enviou. Brutal. ")

    $ chat_message("incri: vou pegar o dinheiro dele ")

    pause 0.5

    $ chat_message("SYSTEM: RESPOSTA - BRUCE.JOHNSON - Por favor, não. Estou transferindo agora. Sinceramente, desculpe. ")

    $ chat_message("incri: EU NUNCA PERCO")

    $ chat_message("incri: {image=e_letsgo}")

    pause 0.5

    jump day2_moneyrain

label day2_moneyrain:

    #play sound "audio/sfx/chaching.mp3"

    play chat "audio/sfx/Casino_Jackpot_001.ogg" loop fadeout 0.2

    # make it rain money??  
    show money_rain onlayer screens

    $ force_scroll_down()

    pause 0.5

    $ chat_message("SYSTEM: PLANO DE PAGAMENTO INICIADO PARA - $ 50 , 000")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA BUZINAR")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI MANDA BUZINAR")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: TÃO FÁCIL FÁCIL FÁCIL CIL CIL CIL CIL ",ot="elimf")

    $ chat_message("elimf: uau, esse foi o mais rápido até agora ",ot="incri")

    pause 0.2

    hide money_rain onlayer screens with Dissolve(0.5)
    stop chat fadeout 0.5

    $ force_scroll_down()

    pause 0.5 

    $ chat_message("incri: AHHHHHHHHHHHHHHHH")
     
    $ chat_message("incri: LIBERDADE. ESTOU LIVREEEEEEEE ")

    $ chat_message("incri: {image=e_letsgo}")

    pause 0.2

    $ chat_message("elimf: uau, sério? esse é o seu último ")

    $ chat_message("incri: SIM ")

    $ chat_message("wnpep: ah. acho que só me resta um também ")

    $ chat_message("elimf: espera, eu também ")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("wnpep: meu deus? ",ot="odxny")

    $ chat_message("odxny: Está quase na hora. ",ot="incri")

    $ chat_message("incri: EU SOU UM DEUS DO CARALHO ")

    $ chat_message("incri: NINGUÉM É MEU DONO, EU SOU O DONO DELES ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: EU SOU O DONO DE TODOS ELES ",ot="elimf")

    $ chat_message("elimf: com todo respeito, dá pra calar a porra da boca ")

    $ chat_message("incri: EU PODERIA SER SEU DONO TAMBÉM ")

    $ chat_message("elimf: vc tentou. eu vi há um mês. falhou miseravelmente ")

    pause 2 

    $ chat_message("incri: não era eu ")

    $ chat_message("elimf: não minta pra mim inc ",ot="incri")

    $ chat_message("incri: eu seria seu dono se tentasse ")

    $ chat_message("incri: de primeira ",ot="elimf")

    $ chat_message("elimf: lol ",ot="incri")

    $ chat_message("incri: DE PRIMEIRA ",ot="wnpep")

    $ chat_message("wnpep: uau, parabéns incri! por favor, relaxe ")

    $ chat_message("incri: CHAT estraga-prazeres ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: jhkfejkhws0-0h  0909  999  9f9g9   ")

    # incri logs off 

    $ chat_message("wnpep: mas. de qualquer forma. é louco. nunca pensei que tudo isso acabaria tão cedo. ")

    # MC: what do you mean? 
    $ player_choice(
        [
            ("como assim?", "x")
        ]
    )

    $ chat_message("odxny: Todos vieram aqui com metas definidas. Essas metas estão quase cumpridas. ")

    $ chat_message("odxny: Quando estiverem, vou fechar isso aqui para sempre. ")

    # MC: why?? what about if i have goals? 
    $ player_choice(
        [
            ("por quê?? e se eu tiver metas? ", "x")
        ]
    )

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: Eu realmente não me importo. Sem ofensa. ")

    $ chat_message("odxny: Já está na hora. ")

    # MC: then... you won't ever talk to each other again? 
    $ player_choice(
        [
            ("então... vocês nunca mais vão se falar?", "x")
        ]
    )

    $ chat_message("wnpep: a vida é feita de encontros e despedidas ")

    $ chat_message("wnpep: é assim que as coisas são ")

    pause 1 

    $ chat_message("elimf: essa é uma citação dos muppets ")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: assisti no último natal. ótimo filme ")

    $ chat_message("elimf: com sua esposa? ")

    $ chat_message("wnpep: sim!") 

    pause 2 

    $ chat_message("elimf: O QUÊ ")

    $ chat_message("wnpep: espere ")

    $ chat_message("wnpep: não, eu li errado, eu li errado ",ot="elimf")

    $ chat_message("elimf: O PACTO DE PRIVACIDADE",ot="odxny")

    $ chat_message("odxny: Então. Aproveite seu curto tempo aqui, thrim. Nosso último membro. ")

    $ player_choice(
        [
            ("merda, preciso enfiar toda a minha diversão aqui então", "day2_43"), 
            ("Somos apenas navios passando em um fuso horário indeterminado, hein", "day2_44")
        ]
    )


    # [1] MC: shit I gotta cram all my enjoyment in then
label day2_43:

    $ chat_message("elimf: não sabia que vc curtia o corre")

    # MC: u know it
    $ player_choice(
        [
            ("tá ligado", "x")
        ]
    )

    $ chat_message("wnpep: não tenho certeza se é assim que a alegria funciona")

    jump day2_45


    # [2] MC: We're just ships passing in an undetermined time zone, huh
label day2_44:
    $ points_seekLove += 1

    $ chat_message("odxny: Obrigado pelo idioma sincero e editado.")

    # MC: I had to offer an equally fine allusion
    $ player_choice(
        [
            ("Tive que oferecer uma alusão igualmente refinada", "x")
        ]
    )

    $ chat_message("elimf: e é mesmo. amo filmes")

    jump day2_45


    # end choices
label day2_45:

    $ chat_message("incri: chore menos thrim")

    $ chat_message("incri: vc vai sair daqui um pouco menos estúpido graças a mim")

    # MC: of course
    $ player_choice(
        [
            ("claro", "x")
        ]
    )

    $ chat_message("incri: eu terminei, então vc tá por conta própria. sem mais ajuda minha")

    # MC: I think I got that, yeah. thanks for helping earlier tho
    $ player_choice(
        [
            ("Acho que entendi, sim. valeu pela ajuda mais cedo", "x")
        ]
    )

    $ chat_message("incri: finalmente um pouco de     GRATIDÃO")

    $ chat_message("wnpep: olha o que você fez. você deu poder a eles")

    $ chat_message("elimf: vai virar um suserano")

    $ chat_message("wnpep: de outro servidor? deus me livre",ot="incri")

    $ chat_message("incri: foda-se vcs dois")

    $ chat_message("elimf: não, tipo. na vida em geral")

    $ chat_message("elimf: com chapéu e tudo")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: você tá chapado agora")

    $ chat_message("elimf: :^)")

    $ chat_message("odxny: Adoraria ver o incri administrando algo.")

    $ chat_message("incri: obrigado")

    $ chat_message("odxny: De uma distância segura.")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: foda-se vc também")

    # dms

    $ chat_message("odxny: Não vou mentir, estou um pouco impressionado.",c="admin")

    # MC: how so?
    $ player_choice(
        [
            ("como assim?", "x")
        ]
    )

    $ chat_message("odxny: Conseguir fazer o incri ser algo perto de prestativo é uma grande proeza",c="admin")

    $ chat_message("odxny: Tenho que dar crédito onde é devido.",c="admin")

    $ player_choice(
        [
            ("já era hora!!", "day2_46"), 
            ("foi uma luta, mas chegamos lá", "day2_47")
        ]
    )


    # [1] MC: about time!!
label day2_46:
    $ points_seekLove += 1

    $ chat_message("odxny: Você não pode ouvir, mas estou batendo palmas para você.",c="admin")

    # MC: well now it just feels sardonic
    $ player_choice(
        [
            ("bem, agora parece sarcástico", "x")
        ]
    )

    $ chat_message("odxny: Vou parar de bater palmas, então.",c="admin")

    # MC: no keep doing that
    $ player_choice(
        [
            ("não, pode continuar", "x")
        ]
    )

    $ chat_message("odxny: Como desejar.",c="admin")

    jump day2_48


    # [2] MC: it was a struggle but we got there
label day2_47:

    $ chat_message("odxny: Nunca esqueceremos seu sacrifício.",c="admin")

    # MC: do I get a medal? or a plaque?
    $ player_choice(
        [
            ("Eu ganho uma medalha? ou uma placa?", "x")
        ]
    )

    $ chat_message("odxny: Posso te mandar dinheiro suficiente para um sanduíche comemorativo.",c="admin")

    # MC: two sandwiches?
    $ player_choice(
        [
            ("dois sanduíches?", "x")
        ]
    )

    $ chat_message("odxny: Fechado.",c="admin")

    jump day2_48


label day2_48:
    # end choices 

    # MC: did you message just to congratulate me tho?
    $ player_choice(
        [
            ("você mandou mensagem só para me parabenizar?", "x")
        ]
    )

    $ chat_message("odxny: Bem, em parte. Achei um pouco estranho fazer isso no chat principal.",c="admin")

    $ chat_message("odxny: Mas também estava me perguntando se você queria ligar de novo.",c="admin")

    # MC: oh?
    $ player_choice(
        [
            ("oh?", "x")
        ]
    )

    $ chat_message("odxny: Apenas para conversar. Sem interrogatório desta vez.",c="admin")

    # MC: no insults?
    $ player_choice(
        [
            ("sem insultos?", "x")
        ]
    )

    $ chat_message("odxny: Depende.",c="admin")

    $ chat_message("odxny: Vou tentar me conter, no entanto.",c="admin")

    $ chat_message("odxny: {image=e_serious}",c="admin")

    # MC: i'll accept that risk, then
    $ player_choice(
        [
            ("vou aceitar esse risco, então", "x")
        ]
    )

    $ chat_message("odxny: Excelente.",c="admin")


    ## call time 
    jump go_to_call

    $ renpy.pause(hard=True)