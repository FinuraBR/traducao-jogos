default has_sql_knowledge = False

label day1_start: 
    #jump day1_30
    #$ $ chat_message("odxny: testing testing")

    #$ chat_message("incri: and then i beat him to death with hammers")

    #jump day2_start

    #jump day1_15

    #jump day2_7

    # jump day5_seekLove_chat
    # $ next_day_number = "3"
    # jump day3_41

    $ _preferences.afm_enable = True 

    #jump day4_31

    #$ persistent.seekLove = True
    $ chat_message("SYSTEM: THRIM entrou")

    play music "audio/music/lost_in_code_with_youlooped.ogg" loop fadein 2.0 fadeout 2.0 

    #jump day4_31

    ## end testing 
    #jump day5_seekLife_6
    #jump day5_seekLoss_chat
    #jump day5_seekLove_12
    #jump day2_moneyrain

    $ chat_message("elimf: e foi aí que eu literalmente peguei um punhado de lama e",fastmode=True)

    pause 2 

    $ chat_message("elimf: espera quem",fastmode=True)

    $ chat_message("incri: quem caralhos", ot="elimf, wnpep")

    # $ chat_message("incri: "+ascii_gun, ot="elimf, wnpep",fastmode=True)

    $ chat_message("elimf: {image=e_serious}", ot="wnpep",fastmode=True)

    $ chat_message("elimf: ?????????? ", ot="wnpep")

    $ chat_message("elimf: quem é esse kkkk ", ot="wnpep, incri")

    $ chat_message("wnpep: fale por favor ................")


    # [1] MC: uhhhh, oi! desculpa! eu não tenho certeza do que é isso

    $ player_choice(
        [
            ("uhhhh, oi! desculpa! eu não tenho certeza do que é isso", "day1_1"), 
            ("olá", "day1_2")
        ]
    )

label day1_1: 

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: federal ")

    $ chat_message("incri: puta de um federal ")

    $ chat_message("incri: o od precisa logar ", ot="elimf")

    $ chat_message("elimf: kkkk imagina um federal se infiltrando com um \"uhhhh, oi! desculpa!\" ")

    $ chat_message("elimf: sem chance de ser um federal ", ot="wnpep")

    $ chat_message("wnpep: é exatamente por isso que eles fariam desse jeito ")

    pause 1 

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: oh merda ")

    jump day1_3


    # [2] MC: olá
label day1_2: 
    $ points_seekLove += 1

    $ chat_message("wnpep: fale mais coisas por favor", ot="elimf")

    $ chat_message("elimf: olá ", ot="incri")

    $ chat_message("incri: VC É TÃÃÃÃÃO SUSPEITO CARA ",fastmode=True)

    $ chat_message("elimf: pode não ser um cara ",ot="incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: lambe meu buraco ")

    $ chat_message("elimf: oh céus! ")

    jump day1_3

label day1_3: 
    # end choices 

    $ chat_message("wnpep: não se preocupem. estou verificando")

    $ chat_message("elimf: algo interessante")

    $ chat_message("wnpep: um momento")

    pause 2

    $ chat_message("wnpep: hm")

    pause 2

    $ chat_message("wnpep: essa pessoa não é uma ameaça de nenhum tipo ")

    pause 1

    $ chat_message("wnpep: ...para ninguém ")

    $ chat_message("elimf: {image=e_crying}")

    $ player_choice(
        [
            ("vocês estão..... me verificando", "x")
        ]
    )

    $ chat_message("wnpep: na verdade, talvez sejam uma ameaça para si mesmos. de uma forma existencial ")

    $ chat_message("incri: tão te chamando de idiota")

    #$ chat_message("incri: {image=e_pain}")

    pause 1 

    # $ chat_message("elimf: "+ascii_grave, fastmode=True)

    $ chat_message("wnpep: não, não estou ", fastmode=True, ot="incri")

    $ chat_message("incri: vibes de idiota até agora com certeza ")

    $ chat_message("incri: {image=e_pain}")

    $ player_choice(
        [
            ("eu mal disse alguma coisa", "x")
        ]
    )

    $ chat_message("elimf: vibes muito bobas", ot="wnpep")

    $ chat_message("wnpep: você gosta da vida que leva, thrim? ")

    $ player_choice(
        [
            ("que porra vocês estão olhando", "day1_4"), 
            ("vocês estão blefando. eu sou super seguro", "day1_5")
        ]
    )

    # [1] MC: que porra vocês estão olhando?? 
label day1_4:

    $ chat_message("wnpep: isso importa? é tudo a mesma besteira chata e sem graça ")

    $ chat_message("wnpep: você deveria mirar mais alto. acho que você consegue fazer melhor ")

    $ chat_message("elimf: eu também achei ")

    $ chat_message("elimf: {image=e_orz}")

    $ player_choice(
        [
            ("q pariu", "x")
        ]
    )

    $ chat_message("incri: isso n vale o esforço ")

    $ chat_message("incri: onde está o od")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: od vem expulsar eles. chatão do caralho ")

    jump day1_6


    # [2] MC: vocês estão blefando. eu sou super seguro 
label day1_5: 
    $ points_seekLove += 1

    $ chat_message("wnpep: o que haha porque você tá numa vpn ou algo assim")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: kkkkkkkkkkkkkkkk a coisa mais fácil de contornar. eu amo anúncios de vpn ")

    $ chat_message("elimf: muito bom para os nossos negócios ")

    # MC: ... eu sou mais seguro que isso. 
    $ player_choice(
        [
            ("... eu sou mais seguro que isso.", "x"), 
        ]
    )

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: aham! :] ")

    jump day1_6
    

    # end choices
label day1_6:

    $ chat_message("incri: wnpep roda o bagulho nas coisas deles ")

    $ chat_message("elimf: kkkk \"bem-vinda nova pessoa, agora nos dê todas as suas economias\" ")

    $ player_choice(
        [
            ("ok, claro, leve meus dez dólares americanos inteiros", "day1_7"), 
            ("por favor, não faça isso. ", "day1_8")
        ]
    )

    # [1] MC: ok, claro, leve meus dez dólares americanos inteiros 
label day1_7: 
    $ points_seekLove += 1

    $ chat_message("elimf: eles estão mentindo wn")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: sabe. eu acho que não estão ")

    $ chat_message("elimf: bem, agora eu me sinto malvado.")

    $ chat_message("incri: quem se fode $10 são $10 roda o comando ")

    $ chat_message("incri: {image=e_letsgo}")

    jump day1_9


    # [2] MC: por favor, não faça isso. 
label day1_8:

    $ chat_message("incri: nos dê uma razão engraçada pra não fazer ")

    $ chat_message("elimf: nah isso é chato ")

    $ chat_message("elimf: temos coisas melhores pra fazer hoje do que tipo ")

    $ chat_message("elimf: arruinar uma vida aleatória ")

    $ chat_message("wnpep: não estou drenando nada, não se preocupe ")

    jump day1_9

    # end choices 
label day1_9: 

    $ chat_message("wnpep: inc por favor cale a boca um pouco, da maneira mais gentil possível ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: essa porra de chat é um saco ")

    $ chat_message("elimf: desloga então kkkk")

    $ chat_message("incri: vc gostaria disso ne")

    $ chat_message("elimf: mano")

    $ chat_message("wnpep: bem, de qualquer forma você está aqui agora. as ferramentas estão à direita")

    $ chat_message("elimf: oq vc quer dizer o incri ta bem ali")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: ..Eu...")

    $ chat_message("elimf: isso é vc me mostrando o dedo do meio")

    $ chat_message("elimf: vc tem seis dedos")

    $ chat_message("incri: uggghhgh")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)
    
    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ player_choice(
        [
            ("que porra é essa???", "x")
        ]
    )

    $ chat_message("elimf: hm. por favor NÃO fale sobre a buzina thrim",ot="incri")

    $ chat_message("incri: vc ta estragando tudo thrim",fastmode=True)

    $ player_choice(
        [
            ("???", "x")
        ]
    )

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("wnpep: qual é. boas maneiras básicas thrim.")

    $ player_choice(
        [
            ("EU???", "day1_horn_1"), 
            ("como vcs fazem isso quero entrar na onda", "day1_horn_2")
        ]
    )

label day1_horn_1: 
    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)
    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    jump day1_horn_3

label day1_horn_2: 
    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)
    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ player_choice(
        [
            ("maleducados do caralho", "x")
        ]
    )
    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)
    
    jump day1_horn_3

    # SEEKL SEGMENT 
label day1_horn_3: 

    # MC: então como tudo isso funciona? 
    $ player_choice(
        [
            ("que seja. então como tudo isso funciona? ", "x"), 
        ]
    )

    $ hack_notes.append("nova função: \nbuzina()")

    $ chat_message("wnpep: nós acessamos dados de uma variedade de empresas/agências governamentais")

    $ chat_message("wnpep: um programa gigante de backend está constantemente invadindo lugares e copiando informações para nós")

    $ chat_message("wnpep: e nós usamos essa informação para uma uh")

    $ chat_message("wnpep: gama de coisas")

    $ player_choice(
        [
            ("tipo hacking ético?", "x"), 
        ]
    )

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: baluartes da bondade, nós")

    $ chat_message("incri: como vc acabou de me chamar")

    $ chat_message("wnpep: uh alguns de nós são mais éticos que outros")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("wnpep: você conhece SQL? ")

    $ player_choice(
        [
            ("sim", "day1_10"), 
            ("não (tutorial)", "day1_11")
        ]
    )

    # [1] MC: sim 
label day1_10: 

    $ has_sql_knowledge = True 

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: então você tem uma ótima vantagem, campeão ")

    $ chat_message("elimf: mas, não pense que pode fazer tudo que o SQL faz. é bem limitado ")

    $ chat_message("wnpep: seekL é muito similar mas tem pequenas diferenças")

    jump day1_12

    # [2] MC: não 
label day1_11: 

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: sem problema. não é uma linguagem difícil de aprender") 

    $ chat_message("elimf: se você achar difícil...")

    #$ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: preocupante")

    $ chat_message("wnpep: vamos explicar um pouco da sintaxe")

    $ chat_message("wnpep: quando queremos olhar alguns dados, rodamos comandos como este:")

    $ chat_message("wnpep: `select *\nfrom nome_da_tabela`")

    $ chat_message("elimf: (essa não é uma tabela real então não tente digitar isso ainda)")

    $ chat_message("wnpep: {color="+color_syntax+"}SELECT{/color} é usado para dizer à tabela qual informação queremos dela")

    $ player_choice(
        [
            ("o que significa uma estrela? esse asterisco *", "x")
        ]
    )

    $ chat_message("wnpep: significa que estamos dizendo à tabela que queremos toda a informação que ela tem")

    $ chat_message("elimf: {color="+color_help+"}* = todos{/color}")

    $ chat_message("wnpep: {color="+color_syntax+"}FROM{/color} diz de qual tabela queremos pegar essa informação")

    $ chat_message("wnpep: então, você colocaria um nome de tabela real ali onde diz \"nome_da_tabela\"")

    $ chat_message("wnpep: junte tudo e essa query está dizendo-")

    $ chat_message("wnpep: \"por favor, me dê toda a informação que você tem da nome_da_tabela\"")

    jump day1_12

    # end choices 
label day1_12:

    $ chat_message("wnpep: alguma pergunta? ")

    $ player_choice(
        [
            ("não, isso é simples", "day1_13"), 
            ("eu talvez.......", "day1_14")
        ]
    )

    # [1] MC: sim, simples 
label day1_13:

    $ chat_message("elimf: ufa ")

    $ chat_message("wnpep: aqui, deixe-me te mostrar uma tabela de exemplo que temos")

    jump day1_15

    # [2] MC: na verdade não...
label day1_14:

    $ chat_message("incri: kkkkkkkkkkkk")

    #$ chat_message("incri: {image=e_pain}")

    $ chat_message("wnpep: aqui, deixe-me te mostrar uma tabela de exemplo que temos")

    jump day1_15

    # end choices 
label day1_15: 

    $ chat_message("wnpep: vá em frente e digite isso no console no canto superior direito ")

    $ chat_message("wnpep: `select * \nfrom table.example`")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["table.example"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day1_19"

    pause 0.5 
    $ tables_seen.append("table.example")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     xpos 1590 ypos 130 
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")

    $ chat_message("elimf: ou, percebeu como uma tabela acabou de aparecer na lista de tabelas na extrema direita?")

    $ chat_message("elimf: {color="+color_help+"}toda vez que você encontra uma nova tabela, ela é adicionada ao seu pequeno banco de referência pessoal ali{/color}")

    $ chat_message("wnpep: se você clicar nela, o console será preenchido com uma query básica para olhar a tabela")

    $ chat_message("wnpep: {color="+color_help+"}muito útil para apenas olhar uma tabela quando você não está familiarizado com o que há nela{/color}")

    $ chat_message("elimf: também tem uma {color="+color_help+"}folha de informações{/color} na mesma área onde compartilhamos anotações")

    $ chat_message("elimf: útil para procurar informações lá quando você estiver travado")

    $ chat_message("wnpep: de qualquer forma, digitando ou clicando, vá em frente e dê uma olhada lá thrim")

    $ chat_message("wnpep: `select * \nfrom table.example`")

    $ chat_message("wnpep: {image=e_wink}")

    $ player_choice(
        [
            ("ok, um momento", "wait_start"), 
            ("mas... por que isso é tão longo e feio...", "day1_17")
        ]
    )

# [1] MC: ok, um momento 

# [2] MC: por que isso é tão longo e feio... 
label day1_17:
    $ points_seekLove += 1

    $ chat_message("elimf: IGUAL AO MEU EX", ot="incri") 

    $ chat_message("incri: IGUAL AO MEU EX", fastmode=True)

    $ chat_message("elimf: eu ganhei de você caralho") 

    $ chat_message("incri: sem chance sua mensagem está abaixo da minha",ot="wnpep") 

    $ chat_message("wnpep: a do elimf apareceu primeiro.") 

    $ chat_message("elimf: AHAHAHAHAHA") 

    $ chat_message("incri: PUTA QUE PARIU",fastmode=True,ot="wnpep") 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("wnpep: desculpe.") 

    jump wait_start 

# label day1_18:
#     if first_flash:
#         pause 0.5 
#         play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
#         show highlight_large onlayer screens: 
#             pos highlight_frame_console_pos
#         $ first_flash = False 
    
#     # wait for input 
#     $ player_is_waiting = True 
#     $ _preferences.afm_enable = False 
#     $ waiting_label = "day1_19"

#     # if they arrive already ready to pass 
#     if player_can_pass:
#         $ player_is_waiting = False 
#         jump day1_19 
#     $ renpy.pause(hard=True)

label day1_19: 
    # hide highlight_large onlayer screens 
    # $ first_flash = True 
    # $ player_is_waiting = False 
    # $ _preferences.afm_enable = True 
    #$ tables_seen.append("table.example")
    
    # MC: feito 
    $ player_choice(
        [
            ("feito", "x"), 
        ]
    )

    $ chat_message("wnpep: okay, então. isso é uma query. e a saída que você vê é apenas uma pequena tabela de exemplo que construímos há muito tempo.", ot="elimf") 

    $ chat_message("elimf: você já sabe como funcionam tabelas de dados?") 

    # MC: feito 
    $ player_choice(
        [
            ("sim! sou bem versado nisso", "day1_19_1"), 
            ("não (tutorial)", "day1_19_2"), 
        ]
    )

label day1_19_1: 

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: ótimo. então podemos pular tudo isso, thrim.") 

    jump day1_24


label day1_19_2: 

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: sem problemas! vamos explicar um pouco.") 

    $ chat_message("elimf: uma tabela é apenas um armazenamento de informações sobre coisas") 

    $ chat_message("incri: resumo estúpido",ot="elimf") 

    $ chat_message("elimf: cada linha é uma coisa e cada coluna é uma informação") 

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: ok não não vc está sendo confuso") 

    $ chat_message("wnpep: thrim, nesta tabela há 5 colunas:") 

    $ chat_message("wnpep: {color="+color_help+"}table_id{/color} - isso é apenas um identificador único para cada linha. você pode ignorar isso na maior parte do tempo") 

    $ chat_message("wnpep: {color="+color_help+"}hacker_name{/color} - isso te diz sobre quem é cada linha entre nós quatro aqui. menos você") 

    $ chat_message("elimf: deveríamos atualizar e adicionar o thrim", ot="wnpep")

    $ chat_message("wnpep: {color="+color_help+"}chat_join_date{/color} - isso te diz quando cada um de nós entrou no seekL") 

    $ chat_message("elimf: então, tipo eu estou na linha 3, e diz que eu entrei em 12-12-2023, logo antes do natal")

    $ chat_message("elimf: faz sentido?")

    $ player_choice(
        [
            ("acho que sim", "x")
        ]
    )

    $ chat_message("wnpep: {color="+color_help+"}favorite_fruit{/color} - as frutas favoritas de todo mundo de uma enquete") 

    $ chat_message("wnpep: {color="+color_help+"}number_of_hacks{/color} - quantos hacks bem-sucedidos cada um de nós já realizou")  

    $ chat_message("incri: meu número deveria ser maior")

    $ chat_message("wnpep: bem-sucedidos sendo a palavra-chave aqui")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("wnpep: então, com base nessa informação, {color="+color_help+"}você pode me dizer quem aqui tem mais hacks concluídos?{/color}")  

    $ player_choice(
        [
            ("wnpep.", "day1_19_2_1"), 
            ("incri.", "day1_19_2_2"), 
            ("odxny.", "day1_19_2_3"), 
        ]
    )

label day1_19_2_1: 
    $ chat_message("wnpep: kkkk eu queria, mas não exatamente.")
    jump day1_19_2_cont

label day1_19_2_2: 
    $ chat_message("incri: secretamente vc tá certo. esses perdedores não sabem contar")

    $ chat_message("elimf: é vdd provs")

    $ player_choice(
        [
            ("droga", "x")
        ]
    )

    jump day1_19_2_cont


## correct choice
label day1_19_2_3: 
    $ points_seekLove += 1

    $ chat_message("wnpep: {image=e_sparkle}")

    $ chat_message("wnpep: sim! está certo!")

    $ chat_message("wnpep: se você quiser ver ainda mais claramente, pode rodar isso: `select hacker_name, number_of_hacks \nfrom table.example`")

    $ chat_message("wnpep: mas, essencialmente, {color="+color_help+"}a linha que tem 50 hacks também tem o nome do odxny nela{/color}")

    $ chat_message("wnpep: o que significa que esse é o número de hacks que ele fez!")

    $ chat_message("elimf: bom trabalho thrim")

    jump day1_24


## cont if wrong through tutorial 
label day1_19_2_cont: 

    $ chat_message("wnpep: pode te ajudar a ver melhor se você rodar isso: \n`select hacker_name, number_of_hacks \nfrom table.example`")

    $ chat_message("wnpep: ou, apenas, sabe, {color="+color_help+"}tente dar uma olhada nessas colunas de novo{/color}. aperte executar de novo, quero dizer.")

    $ chat_message("wnpep: nos avise quando terminar")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["hacker_name", "number_of_hacks"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["table.example"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None 
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
    
    jump day1_19_2_cont_2

label day1_19_2_cont_2:
    if first_flash:
        pause 0.5 
        play sound "audio/sfx/message_notification_01_001 tutorial.ogg"
        show highlight_large onlayer screens: 
            pos highlight_frame_console_pos 
        $ first_flash = False 

    # wait for input 
    $ player_is_waiting = True 
    $ waiting_label = "day1_19_2_cont_3"

    # if they arrive already ready to pass 
    if player_can_pass:
        $ player_is_waiting = False 
        jump day1_19_2_cont_3 
    $ renpy.pause(hard=True)



label day1_19_2_cont_3: 
    hide highlight_large onlayer screens 
    $ first_flash = True 
    $ player_is_waiting = False 
    $ player_choice(
        [
            ("pronto!", "x")
        ]
    )

    $ chat_message("wnpep: legal! então quem tem o nome ao lado do maior número de hacks?")

    $ player_choice(
        [
            ("elimf.", "day1_19_2_cont_3_1"), 
            ("odxny.", "day1_19_2_cont_3_2"), 
        ]
    )

label day1_19_2_cont_3_1:
    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: É O ODXNY, IMBECIL")

    $ chat_message("elimf: é esse tanto de massagem na mão que vc vai precisar kkkk ")

    $ chat_message("wnpep: ?? mão o que? ")

    $ chat_message("elimf: tipo como você sequer descobriu onde estávamos ",fastmode=True)

    # MC: vai se foder 
    $ player_choice(
        [
            ("vai se foder", "x")
        ]
    )

    $ chat_message("incri: vai se foder ")

    $ chat_message("wnpep: ah você quis dizer pegar na mão",fastmode=True)

    $ chat_message("elimf: vai se foder mais forte ")

    $ chat_message("incri: pomete? ")

    $ chat_message("wnpep: parem por favor ")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: ok ")

    $ chat_message("wnpep: podemos te ajudar no caminho thrim. é só pedir")

    $ player_choice(
        [
            ("okay....", "x")
        ]
    )

    jump day1_24


label day1_19_2_cont_3_2: 
    $ points_seekLove += 1

    $ chat_message("elimf: meu deus eles conseguiram")

    $ chat_message("wnpep: {image=e_sparkle}")

    $ chat_message("wnpep: ebaaaaa!!")

    $ chat_message("incri: isso é tão chato pra caralho")

    $ chat_message("wnpep: cala a boca inc")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: não")

    $ chat_message("wnpep: eba thrim!!")

    jump day1_24


    # end choices 
label day1_24: 

    # MC: meu nome não é thrim. não sei por que meu usuário foi definido pra isso 
    $ player_choice(
        [
            ("meu nome não é thrim. não sei por que meu usuário foi definido pra isso", "x")
        ]
    )

    $ chat_message("wnpep: é aleatório quando você entra, para fins de anonimato")

    # MC: ahhhh 
    $ player_choice(
        [
            ("ahhhh", "x")
        ]
    )

    $ chat_message("elimf: kkkk imagina se chamar incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: imagina não ter o maior número de hacks aqui")

    $ chat_message("elimf: é você pode imaginar isso. já que você tem tipo 4 no total né")

    $ chat_message("incri: O QUE")

    # odxny online

    pause 0.5
    $ chat_message("SYSTEM: ODXNY online")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: e aí chefão")

    $ chat_message("wnpep: temos alguém novo enquanto você estava fora")

    $ chat_message("odxny: Você verificou?")

    $ chat_message("wnpep: sim, tenho certeza que você já está fazendo isso também, mas não vi nada com que se preocupar")

    $ chat_message("incri: bane eles",fastmode=True)

    $ chat_message("elimf: {image=e_serious}")

    pause 1 

    $ chat_message("odxny: Por?")

    $ chat_message("incri: chato")

    $ chat_message("incri: irritante")

    $ chat_message("incri: idiota")

    $ chat_message("wnpep: você vai precisar de razões melhores")

    $ chat_message("incri: então a gente só deixa qualquer um entrar aqui??? ")

    $ chat_message("elimf: você era um qualquer uma vez ")

    $ chat_message("elimf: infelizmente agora te conhecemos ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("odxny: Eu farei minha própria investigação, sem relação com ser um idiota chato e irritante.")

    $ chat_message("odxny: Thrim, vamos marcar uma breve chamada só para verificar.")

    $ chat_message("odxny: Não vou bisbilhotar além do necessário.")

    # MC: não me importo com privacidade. pode ligar quando quiser
    $ player_choice(
        [
            ("não me importo com privacidade. pode ligar quando quiser", "x")
        ]
    )

    $ chat_message("odxny: .")

    pause 2

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("elimf: HEIN")

    $ chat_message("odxny: KKKKKKK",fastmode=True)

    $ chat_message("wnpep: essa é nova",fastmode=True)

    $ chat_message("incri: vc ta vendo agora")

    $ chat_message("odxny: Isso é hilário na verdade")

    $ chat_message("incri: eles vão nos afundar junto",fastmode=True)

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("odxny: Nah")

    $ chat_message("odxny: Eu cuido disso")

    # MC: hm?
    $ player_choice(
        [
            ("hm?", "x")
        ]
    )

    $ chat_message("odxny: Vamos acreditar na sua palavra e ligar agora.")

    $ chat_message("odxny: A menos que tenha sido só bravata")

    $ player_choice(
        [
            ("ÃH", "day1_27"), 
            ("como eu disse, a qualquer hora. me liga aí", "day1_28")
        ]
    )

    # [1] MC: ÃH
label day1_27: 

    $ chat_message("odxny: Hmmm")

    # MC: NÃO, EU FAÇO
    $ player_choice(
        [
            ("NÃO, EU FAÇO", "x")
        ]
    )

    jump day1_29

    # [2] MC: como eu disse, a qualquer hora. me liga aí
label day1_28: 
    $ points_seekLove += 1

    $ chat_message("odxny: Bem então.")

    $ chat_message("odxny: Eu esperava pagar pra ver seu blefe.")

    # MC: eu nunca vou recuar
    $ player_choice(
        [
            ("eu nunca vou recuar", "x")
        ]
    )

    jump day1_29 

    # end choices
label day1_29: 

    $ chat_message("odxny: Determinação interessante")

    $ chat_message("wnpep: ou tola")

    $ chat_message("odxny: Veremos.")


    #$ chat_message("odxny: Calling.")



    ## call time 
    jump go_to_call

    $ renpy.pause(hard=True)
