# chat
    # day1: 7 total, 5 possible
    # day2: 16 total, 14 possible 
    # day3: 16 total, 12 possible
    # day4: 14 total, 12 possible 

    # 5+14+12+12 = 43

    # call (2 each)
    # day1: 3 total, 3 possible (6)
    # day2: 5 total, 5 possible (10)
    # day3: 4 total, 4 possible (8)
    # day4: 4 total, 4 possible (8)

    # 6+10+8+8 = 32

    # 75 total 

    # which end 
    # points_seekLove <= 25 = loss 
    # points_seekLove 25-50 = life 
    # points_seekLove >= 50 = love 

label day5_start: 

    $ chat_message("elimf: iae thrim")

    play music "audio/music/server_roomlooped.ogg" loop fadein 2.0 fadeout 2.0 

    # MC: sup!
    $ player_choice(
        [
            ("iae!", "x")
        ]
    )

    $ chat_message("elimf: vc ta PREPARADO")

    $ chat_message("elimf: vc ta ANIMADO")

    $ chat_message("elimf: {image=e_letsgo}")

    $ player_choice(
        [
            ("pra???", "day5_1"), 
            ("SIMMM", "day5_2")
        ]
    )


    #[1] MC: for???
label day5_1: 
    $ points_seekLove -= 1

    $ chat_message("elimf: o último dos hacks")

    #MC: oh!
    $ player_choice(
        [
            ("ah!", "x")
        ]
    )

    $ chat_message("wnpep: {image=e_serious}")

    $ chat_message("wnpep: e então restou apenas um",ot="elimf")

    $ chat_message("elimf: que momento")

    jump day5_3


    #[2] MC: YEAH
label day5_2: 
    $ points_seekLove += 1

    $ chat_message("elimf: SIMMMMMMMMM",ot="incri")

    $ chat_message("incri: vc nem sabe oq ta acontecendo")

    $ chat_message("elimf: não acabe com o entusiasmo desenfreado deles")

    $ chat_message("wnpep: desenfreado")

    $ chat_message("elimf: o entretenimento desprotegido deles")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: aff")

    jump day5_3


    # end choices
label day5_3: 

    $ chat_message("elimf: o dia chegou")

    $ chat_message("elimf: o suspense. é tipo suspensão")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("odxny: Sim, estarei finalizando e executando meu hack hoje.")

    $ chat_message("incri: qual a sensação de ser o último")

    $ chat_message("odxny: Acredito que o ditado seja \"deixar o melhor para o final\"?")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: que desculpa mais esfarrapada")

    $ chat_message("odxny: O que aconteceu com me chamar de 'chefe'?")

    $ chat_message("incri: foi um erro",ot="wnpep")

    $ chat_message("wnpep: então qual é o trabalho?")

    $ chat_message("odxny: É um hack bem simples. Sem dinheiro envolvido desta vez.")

    $ chat_message("incri: entao pra que fazer")

    $ chat_message("elimf: pelo bem dos nossos companheiros ou algo assim ne pep")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("wnpep: perto o suficiente",ot="odxny")

    $ chat_message("odxny: Mais para o nosso bem. Preciso gerenciar algumas coisas finais para o servidor.")

    $ chat_message("incri: chato")

    $ chat_message("wnpep: existe algo que não seja chato pra você")

    $ chat_message("incri: dinheiro")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("elimf: KKKK")

    ## seekL segment 

    $ chat_message("odxny: Thrim, a fim de ajudar? ")

    $ player_choice(
        [
            ("eu adoraria!", "day5_4"), 
            ("claro, por que não", "day5_5")
        ]
    )


    #[1] MC: i would like that!
label day5_4: 
    $ points_seekLove += 1

    $ chat_message("odxny: Ótimo. Legal.")

    jump day5_6


    #[2] MC: sure why not
label day5_5: 
    $ points_seekLove -= 1

    $ chat_message("odxny: ok")

    jump day5_6


    # end choices
label day5_6: 

    $ chat_message("elimf: uauuu que cavalheirismo")

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("wnpep: ou ousado")

    $ chat_message("wnpep: com apenas alguns dias e od já está deixando thrim tocar no servidor")

    $ chat_message("elimf: então é assim que tudo acaba")

    #MC: ty for the votes of confidence
    $ player_choice(
        [
            ("obg pelos votos de confiança", "x")
        ]
    )

    $ chat_message("elimf: rlxa eu confio em vc")

    $ chat_message("elimf: na sua habilidade de quebrar coisas",ot="incri")

    $ chat_message("elimf: {image=e_pain}",ot="incri")

    $ chat_message("incri: se vc vai matar o servidor me deixa fazer isso eu mereço")

    $ chat_message("odxny: Alguns dos seus hacks já tentaram.")

    pause 1 

    $ chat_message("incri: meus hacks sao perfeitos")

    $ chat_message("elimf: feitamente ruins")

    $ chat_message("incri: {image=e_letsgo}")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: cala a boca vc queria hackear como eu otario")

    $ chat_message("wnpep: todos nós trememos diante de seus feitos")

    $ chat_message("incri: pq caralhos vc ta perguntando dos meus pes tarado")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: nem eh assim q se escreve essa porra")

    pause 1 

    $ chat_message("wnpep: não devo reagir. a reação é a assassina da mente")

    $ chat_message("wnpep: permitirei que passe sobre mim e através de mim.",ot="elimf")

    $ chat_message("elimf: KKKKKKKKKKKKKKKKKKKKK")

    $ chat_message("odxny: Faltaram algumas linhas aí.")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: por favor, apenas comece o hack")

    $ chat_message("odxny: Kkkk")

    #MC: so whatre we doing today?
    $ player_choice(
        [
            ("então, o que vamos fazer hoje?", "x")
        ]
    )

    $ chat_message("odxny: Preparando o desligamento do servidor, na verdade. Só preciso deixar tudo no lugar.")

    $ player_choice(
        [
            ("ah...", "day5_7"), 
            ("finalmente. reze suas preces, hacker de merda", "day5_8")
        ]
    )


    #[1] MC: oh...
label day5_7: 
    $ points_seekLove += 1

    $ chat_message("odxny: {image=e_serious}")

    $ chat_message("odxny: Tinha que ser feito uma hora.",ot="incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: thrim ja ta chorando kkkk")

    $ chat_message("elimf: deixa eles se concentrarem ")

    jump day5_9


    #[2] MC: finally. say ur prayers hacker scum 
label day5_8: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: grosso")

    $ chat_message("elimf: que seja indolor senhor por favor nós oramos ",ot="incri")

    $ chat_message("incri: vamo logo comecar isso",fastmode=True)

    $ chat_message("incri: {image=e_letsgo}")

    jump day5_9 


    # end choices 
label day5_9: 

    $ chat_message("elimf: eles têm que colocar o fio e o grande botão vermelho")

    $ chat_message("elimf: ou aquelas caixas com alavanca que os mineradores usam")

    $ chat_message("wnpep: o detonador?")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: é assim que se chama mesmo")

    $ chat_message("elimf: que loucura",ot="odxny")

    $ chat_message("odxny: Não vai ser nada especial. Sem fogos de artifício do Paciência.")

    $ chat_message("odxny: Mas podemos fazer uma contagem regressiva.")

    $ chat_message("wnpep: tipo, agora?")

    $ chat_message("elimf: precisamos de tempo pra ensinar o incy a contar até 5")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: eu sei contar ate 5 ")

    $ chat_message("elimf: prova")

    $ chat_message("incri: 1")

    $ chat_message("odxny: {image=e_baby}")

    $ chat_message("odxny: Ok, já chega.")

    $ chat_message("elimf: ah",ot="odxny")

    ## instructions

    $ chat_message("odxny: Thrim, este será um pouco diferente. ")

    $ chat_message("odxny: Para desligar o servidor, precisamos saber a senha de execução. ")

    #MC: i'm assuming u already know that, right? 
    $ player_choice(
        [
            ("presumo que você já saiba, certo? ", "x")
        ]
    )

    $ chat_message("odxny: Certo, mas...")

    $ chat_message("odxny: ...onde está a graça nisso? ")

    $ chat_message("odxny: {image=e_orz}")

    $ chat_message("elimf: intrigante ",ot="wnpep")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("wnpep: od? ",fastmode=True)

    $ chat_message("odxny: Eu escondi pedaços da senha em algumas tabelas que você vasculhou nos últimos dias. ")

    $ chat_message("odxny: Pronto para uma caçada? ")

    $ player_choice(
        [
            ("isso vai ser difícil...............", "day5_10"), 
            ("mds. SIM", "day5_11")
        ]
    )


    #[1] MC: is this going to be hard............... 
label day5_10: 
    $ points_seekLove -= 1

    $ chat_message("odxny: Não mais difícil do que o que você já fez? ")

    $ chat_message("odxny: Desculpe. Pensei que seria divertido. ")

    $ chat_message("odxny: {image=e_baby}")

    jump day5_12


    #[2] MC: omg. YES 
label day5_11: 
    $ points_seekLove += 1

    $ chat_message("odxny: KKKKK ")

    $ chat_message("odxny: Sim. Ha. Ok, legal. ",ot="wnpep")

    $ chat_message("wnpep: adoro o entusiasmo, thrim ")

    $ chat_message("wnpep: {image=e_wink}")

    jump day5_12


    # exit choices 
label day5_12: 

    $ chat_message("incri: nao faz merda thrim ")

    $ chat_message("incri: vc teve tipo")

    $ chat_message("incri: TRES professores ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("elimf: mas se vc fizer merda, td bem ")

    $ chat_message("elimf: pra deixar claro a gente n vai te perdoar mas. ")

    $ chat_message("elimf: vc nunca mais vai nos ver depois disso mesmo entao quem se importa",ot="wnpep")

    $ chat_message("wnpep: eu vou te perdoar! ")

    $ chat_message("wnpep: {image=e_sparkle}")

    $ chat_message("incri: cala a boca ",ot="odxny")

    $ chat_message("odxny: Pronto pra começar? ")

    $ player_choice(
        [
            ("mais do que nunca...", "day5_13"), 
            ("sim!! vamos lá!! ", "day5_14")
        ]
    )


    #[1] MC: as i'll ever be...
label day5_13: 
    $ points_seekLove -= 1

    $ chat_message("odxny: Certo.")

    jump day5_15


    #[2] MC: yes!! let's go!! 
label day5_14: 
    $ points_seekLove += 1

    $ chat_message("odxny: Perfeito. ")

    jump day5_15


    # end choices 
label day5_15: 

    ## PART ONE 

    $ chat_message("odxny: Parte um-- {color="+color_help+"}se alguém estivesse traindo o cônjuge, acho que um ótimo pseudônimo seria \"butt_slutt_wutt\"{/color}")
    pause 0.2
    $ hack_notes.append("ótimo pseudônimo: \n\"butt_slutt_wutt\"")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["secretsmooch.users"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("ss_cid", "98605-SS")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day5_19"

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: O QUE ",ot="incri")

    $ chat_message("incri: ??Q????? ",ot="wnpep",fastmode=True)

    $ chat_message("wnpep: por que estamos de volta nisso... ",ot="elimf")

    $ chat_message("wnpep: {image=e_baby}",ot="elimf")

    $ chat_message("elimf: KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK",fastmode=True)

    $ player_choice(
        [
            ("desculpa. O QUÊ ", "day5_16"), 
            ("oh, um pseudônimo muito DIGNO de se usar", "day5_17")
        ]
    )


    #[1] MC: i'm sorry. WHAT 
label day5_16: 
    $ points_seekLove -= 1

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: SÓ ACEITA ANTES QUE MINHA CONFIANÇA ACABE POR FAVOR...")

    jump day5_18


    #[2] MC: oh, a most DIGNIFIED alias to use
label day5_17: 
    $ points_seekLove += 1

    $ chat_message("odxny: Por favor KKK ")

    jump day5_18


    # end choices 
label day5_18: 

    $ chat_message("elimf: gênio. eu devia ter tido essa ideia")

    $ chat_message("elimf: od de onde vc tirou isso ")

    $ chat_message("odxny: {image=e_serious}")

    $ chat_message("odxny: Do fundo, bem do fundo. ")

    #$ chat_message("elimf: oh but of course, of course",ot="odxny")

    $ chat_message("odxny: Thrim. {color="+color_help+"}Se importa de pegar um e-mail que seja perfeito para esse pseudônimo?{/color}")

    # MC: right away! 
    $ player_choice(
        [
            ("agora mesmo! ", "x")
        ]
    )

    jump wait_start 


    # runs code -- searches for "butt_slutt_wutt" in secretsmooch.users 
label day5_19: 

    #MC: got it! "4242" 
    $ player_choice(
        [
            ("peguei! \"4242\"", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("parte um: \n4242")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: o padrão fede a vergonha alheia, ou seja, AFF ")

    $ chat_message("incri: só fala logo e acaba com isso")

    $ chat_message("odxny: Nenhum palpite? ")

    $ chat_message("wnpep: acho que sei o que é kkk")

    $ chat_message("elimf: {image=e_baby}")

    $ chat_message("elimf: ??? ",ot="wnpep")

    $ chat_message("wnpep: já teve um celular com T9, thrim? ")

    $ player_choice(
        [
            ("não, mas...", "day5_20"), 
            ("mds. sim. 4242 é... ", "day5_21")
        ]
    )


    #[1] MC: no, but... 
label day5_20: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: 4242 = haha.")

    $ chat_message("wnpep: {image=e_wink}")

    jump day5_22


    #[2] MC: omg. yes. 4242 is... 
label day5_21: 
    $ points_seekLove += 1

    #MC: \"haha\". LOL 
    $ player_choice(
        [
            ("\"haha\". KKK", "x")
        ]
    )

    $ chat_message("wnpep: estamos certos, od? ")

    jump day5_22


    # end choices
label day5_22: 

    $ chat_message("odxny: Kkkk. Sim. ",ot="incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: só fica mais vergonhoso ",ot="elimf")

    $ chat_message("elimf: chefe. você mudou. ")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("odxny: Não tenho permissão para me divertir de vez em quando? ")

    $ chat_message("elimf: me diga onde o od está amarrado pfv ")

    $ chat_message("odxny: KKKK ")

    $ player_choice(
        [
            ("que fofo kkk. adorei", "day5_23"), 
            ("T9 no ano atual. loucura", "day5_24")
        ]
    )


    #[1] MC: that's so cute lol. love that 
label day5_23:
    $ points_seekLove += 1

    $ chat_message("odxny: Uh. Sim, valeu ",ot="incri")

    $ chat_message("incri: {image=e_pain}",ot="elimf")

    $ chat_message("incri: ECAA ",ot="elimf",fastmode=True)

    $ chat_message("elimf: o clima ta estranho para com iss ")

    pause 1 

    $ chat_message("elimf: ou me inclui ")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("odxny: Não. ")

    jump day5_25


    #[2] MC: T9 in current year. crazy 
label day5_24: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: eu diria que deveriam trazer de volta! era muito mais rápido para digitar ")

    $ chat_message("elimf: {image=e_baby}")

    $ chat_message("elimf: isso só pode ser mentira ")

    $ chat_message("wnpep: não é! ")

    jump day5_odm_1# day5_25 


label day5_odm_1: 

    $ chat_message("odxny: Oi. Fico feliz que você esteja entrando no jogo.",c="admin")

    $ chat_message("odxny: Sei que não é muito, mas eu queria fazer algo.",c="admin")

    $ chat_message("odxny: Não queria deixar as coisas naquele tom de ontem.",c="admin")

    $ player_choice(
        [
            ("isso é... muito gentil", "day5_odm_2"), 
            ("faz sentido. agradeço", "day5_odm_3")
        ]
    )


    #[1] MC: thats…really sweet
label day5_odm_2:
    $ points_seekLove += 1

    $ chat_message("odxny: É só um joguinho bobo. Não queria que as coisas ficassem estranhas e tristes.",c="admin")

    #MC: it'll still be sad but it is making me smile
    $ player_choice(
        [
            ("ainda vai ser triste, mas está me fazendo sorrir", "x")
        ]
    )

    $ chat_message("odxny: Isso é tudo que posso pedir.",c="admin")

    jump day5_odm_4


    #[2] MC: appreciate it
label day5_odm_3: 
    $ points_seekLove -= 1

    $ chat_message("odxny: Sim. Claro.",c="admin")

    jump day5_odm_4


    # end choices
label day5_odm_4: 

    $ chat_message("odxny: Se as coisas puderem terminar bem, então estou feliz.",c="admin")

    #MC: bit of a pivot from a few days ago
    $ player_choice(
        [
            ("uma bela mudança de alguns dias atrás", "x")
        ]
    )

    $ chat_message("odxny: Eu sei. Os outros estão certos, eu amoleci.",c="admin")

    #higher favor
    if points_seekLove > 25: 

        $ chat_message("odxny: Não tenho certeza se é algo ruim.",c="admin")

        #MC: yeah?
        $ player_choice(
            [
                ("é?", "x")
            ]
        )

        $ chat_message("odxny: Não estou prometendo nada. Apenas... expondo meus pensamentos.",c="admin")

        #MC: thats okay!
        $ player_choice(
            [
                ("tudo bem!", "x")
            ]
        )

    #lower favor
    else: 

        $ chat_message("odxny: Coisa boba de se fazer.",c="admin")

        #MC: is it?
        $ player_choice(
            [
                ("é?", "x")
            ]
        )

        $ chat_message("odxny: Sim. Eu me permiti esquecer a data de validade de tudo isso.",c="admin")

        #MC: right…
        $ player_choice(
            [
                ("certo...", "x")
            ]
        )


    # end branching

    $ chat_message("odxny: Mas fico feliz que você fez parte disso.",c="admin")


    # low favor
    # if points_seekLove <= 25: 

    $ chat_message("odxny: Obrigado, por tornar isso divertido.",c="admin")

    #MC: of course
    $ player_choice(
        [
            ("claro", "x")
        ]
    )

    # high favor
    # else: 

    #     $ chat_message("odxny: Thank you stranger, for making this fun.",c="admin")

    #     #MC: heh. of course
    #     $ player_choice(
    #         [
    #             ("heh. of course", "x")
    #         ]
    #     )

    # end branching

    $ chat_message("odxny: Agora vamos voltar ao que interessa.",c="admin")

    jump day5_25



    # end choices 
label day5_25: 

    $ chat_message("odxny: Pronto para o próximo?")


    ## PART TWO 

    $ chat_message("odxny: Parte dois -- {color="+color_help+"}Alguém na PRIDE fez um pedido de cobertura estranho para claim_type = \"TERMINATE\". Se importa de pegar o e-mail dele?{/color}") 
    pause 0.2
    $ hack_notes.append("tipo de pedido: \n\"TERMINATE\"")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I83277-164")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day5_29"

    $ chat_message("incri: ?? ",ot="elimf")

    $ chat_message("elimf: ah isso é uma piada interna... ")

    $ chat_message("elimf: {image=e_baby}")

    $ chat_message("elimf: me sinto tão excluído :( ")

    $ player_choice(
        [
            ("cara. eu também", "day5_26"), 
            ("oh hooooooooo eu entendi! ", "day5_27")
        ]
    )


    #[1] MC: brother. me too 
label day5_26: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: ah, que ótimo começo ",ot="incri")

    $ chat_message("incri: kkkkkkkk",ot="odxny")

    $ chat_message("odxny: Você vai entender. ")

    jump day5_28


    #[2] MC: oh hooooooooo i got this! 
label day5_27: 
    $ points_seekLove += 1

    $ chat_message("odxny: Nunca duvidei. ")

    jump day5_28


    # end choices 
label day5_28: 

    #$ chat_message("odxny: Use whatever seekL logic you'd like. ")

    $ chat_message("odxny: E {color="+color_help+"}me avise quando encontrar o e-mail.{/color}")

    jump wait_start 


    # runs code -- "Arnold Schwarzenegger" in joins pride.claims to irs.contacts 
label day5_29: 

    #MC: \"OWIE\"?? 
    $ player_choice(
        [
            ("\"OWIE\"??", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("parte dois: \nOWIE")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("elimf: eu quando eu ")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: eu quando eu quando ",ot="incri")

    $ chat_message("incri: q porra de senha é essa")

    $ chat_message("incri: {image=e_baby}")

    $ chat_message("odxny: São as iniciais dos membros originais... ")

    pause 2

    $ chat_message("wnpep: ah. que fofo! ",ot="incri,elimf")

    $ chat_message("wnpep: {image=e_heart}",ot="incri,elimf")

    $ chat_message("incri: cringe ",ot="elimf",fastmode=True)

    $ chat_message("elimf: cringe pra caralho ",fastmode=True)

    $ player_choice(
        [
            ("sem \"T\" :( ", "day5_30"), 
            ("ah. um pequeno memorial na despedida", "day5_31")
        ]
    )


    #[1] MC: no "T" :( 
label day5_30: 
    $ points_seekLove -= 1

    $ chat_message("odxny: ....\"TOWIE\"? ",ot="elimf")

    $ chat_message("elimf: estamos entrando em linguagem de bebê aqui ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: naonaonaonaonaonao")

    jump day5_32 


    #[2] MC: aw. a lil memorial in the sendoff 
label day5_31: 
    $ points_seekLove += 1

    $ chat_message("odxny: Um pouco. ",ot="wnpep")

    $ chat_message("wnpep: ahhhh. ")

    jump day5_32


    # end choices 
label day5_32:

    $ chat_message("odxny: Okay. Segunda parte, \"OWIE\". Bom trabalho. ")

    #MC: tytyty! 
    $ player_choice(
        [
            ("vlwvlwvlw!", "x")
        ]
    )

    ## PART THREE 

    $ chat_message("odxny: Parte três -- {color="+color_help+"}O \"seekL\" pode estar prestes a morrer, mas alguém tem que garantir que nada desmorone depois e cobrir todos os nossos rastros.{/color}")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I36375-168")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day5_36"

    $ chat_message("odxny: {color="+color_help+"}Pode me encontrar o e-mail para esse living_contact?{/color}")
    pause 0.2
    $ hack_notes.append("morte: \n\"seekL\"")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ player_choice(
        [
            ("... isso é VAGO", "day5_33"), 
            ("okay... acho que sei em qual tabela ir.", "day5_34")
        ]
    )



    #[1] MC: ... this is VAGUE 
label day5_33: 
    $ points_seekLove -= 1

    $ chat_message("wnpep: {image=e_sparkle}")

    $ chat_message("wnpep: vamos lá thrim! não desista! ")

    $ chat_message("elimf: {image=e_sparkle}")

    $ chat_message("elimf: é!! uhul uhul uhul",ot="incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: trivial ")

    #MC: I'M THINKING.... 
    $ player_choice(
        [
            ("ESTOU PENSANDO....", "x")
        ]
    )

    jump day5_35 


    #[2] MC: okay... i think i know the table to go to. 
label day5_34: 
    $ points_seekLove += 1

    $ chat_message("odxny: Excelente. ",ot="wnpep")

    $ chat_message("wnpep: fácil demais para o thrim! ")

    $ chat_message("wnpep: {image=e_sparkle}")

    jump day5_35


    # end choices 
label day5_35: 

    $ chat_message("wnpep: esta é a última parte? ")

    $ chat_message("odxny: Sim. Chegando ao fim. ")

    $ chat_message("incri: vai thrim. nos mate ")

    $ chat_message("incri: {image=e_serious}")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: KKK ",ot="odxny")

    $ chat_message("odxny: Me avise quando tiver. ")

    jump wait_start 


    # runs code -- finds odxny in living_contact and connects to irs.contacts for email 
label day5_36: 

    #MC: \"TYVM\"?
    $ player_choice(
        [
            ("\"TYVM\"?", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("parte três: \nTYVM")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: chega de merda brega nao ")

    $ chat_message("odxny: Espere aí. Significa...")

    $ chat_message("odxny: \"Thank you very much (Muito obrigado). Por toda a grana preta.\" ")

    pause 1 

    $ chat_message("incri: ok. concordo ")

    $ chat_message("incri: {image=e_orz}")

    $ chat_message("incri: obg mundo idiota",ot="elimf")

    $ chat_message("elimf: mm sim. obg ")

    $ chat_message("elimf: minha vida definitivamente melhorou devido à estupidez deles ")

    pause 1

    $ chat_message("odxny: \"...E obrigado por estar aqui comigo.\" ")

    $ chat_message("incri: CHEGA",ot="elimf,wnpep")

    $ chat_message("elimf: VAAAAAIA",ot="wnpep",fastmode=True)

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("wnpep: obrigado a você também. ")

    #MC: aww. thought you all didn't care about each other 
    $ player_choice(
        [
            ("aww. pensei que vocês não se importavam uns com os outros ", "x")
        ]
    )

    $ chat_message("incri: EU ODEIO MUITO TODOS VCS ")

    $ chat_message("elimf: ate eu </3 ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: especialmente vc porra ")

    $ chat_message("elimf: como meu coração partido se consertará ",ot="wnpep")

    $ chat_message("wnpep: então é isso? ")

    $ chat_message("odxny: \"4242OWIETYVM\". É isso.") 

    $ chat_message("odxny: Obrigado por me fazer a vontade, Thrim. ")

    ## END SEGMENT 

    $ chat_message("elimf: nosso líder impecável e maravilhoso vence de novo")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("wnpep: sempre um prazer te ver trabalhar")

    $ chat_message("wnpep: {image=e_wink}")

    # if low favor
    if points_seekLove <= 25: 

        $ chat_message("odxny: Não foi o mais elegante, mas obterá a resposta que preciso.")

    # if good favor
    else: 

        $ chat_message("odxny: Você me lisonjeia.")

        $ chat_message("odxny: Mas sim, acho que foi muito bem.")

    # end branches

    $ chat_message("incri: foi.. . ok")

    $ chat_message("incri: {image=e_baby}")

    $ chat_message("elimf: tudo graças ao nosso bebê prodígio thrim")

    $ player_choice(
        [
            ("obg pelo elogio muito sincero", "day5_37"), 
            ("sempre feliz em ajudar", "day5_38")
        ]
    )


    #[1] MC: thank u for the very sincere compliment
label day5_37: 
    $ chat_message("elimf: {image=e_sparkle}")

    $ chat_message("elimf: dnd meu companheiro incrivelmente talentoso")

    #MC: truly we are both great minds
    $ player_choice(
        [
            ("verdadeiramente, nós dois somos grandes mentes", "x")
        ]
    )

    $ chat_message("elimf: os mais talentosos",ot="incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: vcs vao me deixar enjoado")

    jump day5_41

    

    #[2] MC: always glad to assist
label day5_38: 

    $ chat_message("elimf: vc é nosso pequeno thrim")

    $ chat_message("elimf: {image=e_heart}")

    $ player_choice(
        [
            ("vocês todos são Frankenstein então?", "day5_39"), 
            ("????", "day5_40")
        ]
    )


    #[2-1] MC: are u all frankenstein then?
label day5_39: 

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: não reivindico isso")

    $ chat_message("elimf: nem pelo jaleco irado?")

    $ chat_message("wnpep: o quê?? não")

    $ chat_message("elimf: :^(")

    jump day5_41


    #[2-2] MC: ????
label day5_40: 

    $ chat_message("elimf: deixa pra la",ot="wnpep")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: seu novo dever de casa é ler Frankenstein")

    $ chat_message("elimf: ou assistir O Jovem Frankenstein")

    $ chat_message("wnpep: um substituto aceitável")

    jump day5_41


    # end subchoices

    # end choices
label day5_41: 

    $ chat_message("incri: affffff")

    $ chat_message("incri: {image=e_baby}")

    $ chat_message("elimf: o que te aflige")

    $ chat_message("incri: quanto tempo temos q esperar")

    #$ chat_message("odxny: We can't all target chronically online cops.")

    $ chat_message("elimf: tão impaciente pra nos ver partir")

    $ chat_message("elimf: vc não vai sentir nossa falta, querido incy")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("incri: querido o quê")

    $ chat_message("elimf: meu incy")

    $ chat_message("elimf: tipo inky mas com c",ot="incri")

    $ chat_message("incri: ruim",fastmode=True)

    $ chat_message("wnpep: é bem ruim")

    $ chat_message("wnpep: parece in-see")

    $ player_choice(
        [
            ("eu li como inky!", "day5_42"), 
            ("ah... parece mesmo...", "day5_43")
        ]
    )


    #[1] MC: i read it as inky!
label day5_42: 

    $ chat_message("elimf: meu bebê prodígio sempre me apoia")

    jump day5_44


    #[2] MC: oh... it does...
label day5_43: 

    $ chat_message("elimf: ninguém reconhece minhas artes e trabalhos")

    jump day5_44


    # end choices
label day5_44: 

    pause 1 

    stop music fadeout 3.0 

    $ chat_message("odxny: Para voltar ao assunto, vou começar a contagem regressiva em alguns minutos.")

    $ chat_message("incri: {image=e_pain}")

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

    $ chat_message("incri: a gente tem q esperar por isso")

    play music "audio/music/lost_in_code_with_youlooped.ogg" fadein 3.0 

    $ chat_message("incri: pq eu to entediado")

    $ chat_message("elimf: que reviravolta")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI DIZ BUZINA AÍ")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("incri: cala a boca",ot="odxny")

    $ chat_message("odxny: Nos dá um tempo extra para nos despedirmos.")

    $ chat_message("elimf: ahhhhhhhhhhh")

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("incri: o thrim ta contagiando a porra de vcs dois")

    $ chat_message("incri: seus sentimentais de merda")

    #MC: pls
    $ player_choice(
        [
            ("pfv", "x")
        ]
    )
    hide bg odxny_bg
    hide spr 
    hide fade_lower
    hide fg odxny_fg onlayer screens
    hide call_frame

    $ chat_message("incri: eu podia ta fazendo outras coisas")

    $ chat_message("elimf: recebendo mais multas de estacionamento pra ter mais hacks pra hackear")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("incri: foi só uma vez e a culpa foi deles eu nem tinha passado do tempo")

    $ chat_message("incri: babaca do caralho só queria me fazer pagar")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: honestamente 50k nem foi suficiente eu devia ter cobrado mais")

    # incri typing

    jump day5_choose_end 



label day5_choose_end: 

    python: 
        if points_seekLove <= 25: 
            renpy.jump("day5_seekLoss_chat")
        elif points_seekLove <= 50: 
            renpy.jump("day5_seekLife_chat")
        else: 
            renpy.jump("day5_seekLove_chat")


label day5_seekLoss_chat: 

    $ chat_message("wnpep: bem. provavelmente deveríamos fazer algo antes de partirmos")

    $ chat_message("wnpep: alguma ideia?")

    $ chat_message("odxny: Nenhuma no momento.",ot="elimf")

    $ chat_message("elimf: eu tenho uma",fastmode=True)

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("wnpep: acho que consigo adivinhar o que você quer.")

    pause 1 

    $ chat_message("incri: fbi na casa")

    $ chat_message("elimf: merda")

    $ player_choice(
        [
            ("o quê?", "x")
        ]
    )

    pause 2 

    ## NEED A CRASH SOUND 
    stop music 
    #play sound "audio/sfx/ui_menu_back_001 hangup.ogg"

    $ quick_menu = False
    $ _preferences.afm_enable = False 

    $ persistent.seekLoss = True 

    show screen game_over
    pause 4.0 
    show screen game_over_text with Dissolve(2.0) 
    #pause 3.0 
    #play sound "audio/sfx/ui_menu_back_001 hangup.ogg"

    

    # program shuts down

    # end

    $ renpy.pause(hard=True)


label day5_seekLife_chat: 

    $ chat_message("wnpep: o importante é que agora podemos comemorar e nos despedir")

    $ chat_message("elimf: claro que temos que estourar umas garrafas antes de ir",ot="incri")

    $ chat_message("incri: só to aqui pra ver vcs idiotas nao perceberem o quanto vao sentir minha falta")

    $ chat_message("incri: {image=e_crying}")

    $ chat_message("elimf: uhhhhhhh")

    $ chat_message("wnpep: admito que vou sentir um pouco de falta disso, mas sabíamos dos termos desde o início")

    $ chat_message("wnpep: para coisas melhores")

    $ chat_message("incri: tipo o que")

    $ chat_message("incri: o que é melhor que eu")

    $ player_choice(
        [
            ("você meio que tá pedindo pra levar uma", "day5_seekLife_1"), 
            ("nada, sinceramente. eles simplesmente não entendem", "day5_seekLife_2")
        ]
    )


    #[1] MC: ur kind of setting yourself up there
label day5_seekLife_1: 

    $ chat_message("incri: seja la o que eles disserem, estao errados")

    $ chat_message("wnpep: desculpe por colocar minha filha em primeiro lugar")

    $ chat_message("incri: sua filha consegue fazer os hacks que eu faço")

    $ chat_message("elimf: nessa ele te pegou")

    $ chat_message("wnpep: é, claro, você me pegou")

    $ chat_message("wnpep: vou admitir que você é melhor que a filha que eu segurei e criei")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: é isso aí otario")

    jump day5_seekLife_3


    #[2] MC: nothing honestly. they just dont get it
label day5_seekLife_2: 

    $ chat_message("incri: obrigado")

    pause 1

    $ chat_message("incri: espera")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: KKKK",ot="incri")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: vai se foder para de me zoar porra")

    $ chat_message("odxny: Como assim, eles sem dúvida estão sendo sinceros.",ot="wnpep")

    $ chat_message("wnpep: ahahahaha",fastmode=True)

    jump day5_seekLife_3


    # end choices
label day5_seekLife_3: 

    $ chat_message("elimf: kkkkkkkk")

    $ chat_message("elimf: foi divertido enquanto durou")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: somos muitos navios partindo ao mesmo tempo. navios amigos acenando com nossas velas")

    # dms

    # SET ADMIN CHAT ON OR SOMTH

    $ chat_message("odxny: Últimas palavras antes do fim?", c="admin")

    #$ active_window = "admin"

    #MC: last call already huh
    $ player_choice(
        [
            ("última chamada já, hein", "x")
        ]
    )

    $ chat_message("odxny: Sim. Nem o elimf enrolou sobre isso.", c="admin")

    $ chat_message("odxny: Todos eles foram pelo menos um pouco lúcidos quando se tratava de seus objetivos.", c="admin")

    #MC: that almost sounded like a compliment
    $ player_choice(
        [
            ("isso quase soou como um elogio", "x")
        ]
    )

    $ chat_message("odxny: Eu sei dar uns desses de vez em quando. Eles mereceram.", c="admin")

    #MC: you sound like youve grown a little fond of them
    $ player_choice(
        [
            ("parece que você se afeiçoou um pouco a eles", "x")
        ]
    )

    $ chat_message("odxny: Talvez. ", c="admin")

    $ chat_message("odxny: {image=e_serious}", c="admin")

    $ chat_message("odxny: Mas isso não significa que não vou desligar as coisas.", c="admin")

    #MC: I wasnt expecting you to change course
    $ player_choice(
        [
            ("eu não esperava que você mudasse de ideia", "x")
        ]
    )

    $ chat_message("odxny: Mas você quer algo.", c="admin")

    #MC: ha. you got me
    $ player_choice(
        [
            ("ha. você me pegou", "x")
        ]
    )

    #MC: i was just hoping that maybe...our talks and your time with everyone swayed you to give people another shot
    $ player_choice(
        [
            ("eu só esperava que talvez... nossas conversas e seu tempo com todos o convencessem a dar outra chance às pessoas", "x")
        ]
    )

    $ chat_message("odxny: Você acha que conversar com o incri moveu a agulha em uma direção positiva?", c="admin")

    $ chat_message("odxny: Brincadeira. Eu tenho pensado muito, pra falar a verdade.", c="admin")

    $ chat_message("odxny: E acho que você pode estar certo.", c="admin")

    #MC: i'm glad.
    $ player_choice(
        [
            ("fico feliz.", "x")
        ]
    )

    $ chat_message("odxny: Pode não consertar nada. ", c="admin")

    #MC: that's true
    $ player_choice(
        [
            ("é verdade", "x")
        ]
    )

    $ chat_message("odxny: Mas eu vou tentar.", c="admin")

    #MC: thats more than enough for me
    $ player_choice(
        [
            ("isso é mais do que suficiente para mim", "x")
        ]
    )

    $ chat_message("odxny: Obrigado.", c="admin")

    $ chat_message("odxny: {image=e_heart}", c="admin")

    # general

    $ chat_message("incri: então vamos explodir essa porra ou o que")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("odxny: Vou desligar tudo em, digamos, 60 segundos. Tempo suficiente para um último adeus.")

    $ chat_message("wnpep: parece bom",ot="elimf")

    $ chat_message("elimf: vou sentir um pouco a falta de todos vcs. e depois esquecer que tudo não foi um sonho")

    $ chat_message("elimf: vcs estarão lá no fundo de cada bong")

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("wnpep: que honra.",ot="incri")

    $ chat_message("incri: adeus nao vou sentir falta de nenhum de vcs")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: chorem pq vcs nao vao mais me ver")

    $ chat_message("elimf: já estou com os lenços prontos",ot="odxny")

    $ chat_message("odxny: 30 segundos.",fastmode=True)

    $ chat_message("wnpep: não posso reutilizar a citação dos Muppets, mas vou pensar com alguma gentileza sobre este encontro e partida")

    $ chat_message("incri: uau profundo")

    $ chat_message("wnpep: que fique registrado que eu tentei",ot="odxny")

    $ chat_message("odxny: Direi que também gostei um pouco disso.")

    $ chat_message("odxny: {image=e_orz}")

    $ chat_message("odxny: Obrigado a todos por participarem e desejo-lhes o bem.")

    #MC: thank you all for tolerating me in the short time i was here
    $ player_choice(
        [
            ("obrigado a todos por me tolerarem no pouco tempo que estive aqui", "x")
        ]
    )

    $ chat_message("wnpep: não foi incômodo algum",ot="elimf")

    $ chat_message("elimf: eu me diverti com isso rlxa")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("odxny: Concordo. Obrigado por estar aqui.")

    #MC: of course!
    $ player_choice(
        [
            ("claro!", "x")
        ]
    )

    $ chat_message("odxny: E com isso, estamos em 5")

    $ chat_message("odxny: 4",ot="wnpep")

    $ chat_message("wnpep: adeus a todos!")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("odxny: 3",ot="incri,elimf",fastmode=True)

    $ chat_message("incri: {image=e_pain}",ot="elimf")

    $ chat_message("incri: adeus perdedores ",ot="elimf")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: até nunca mais :^)",fastmode=True)

    $ chat_message("odxny: 2",fastmode=True)

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
            ("adeus!!!!!!", "day5_seekLife_4"), 
            ("AHHHHHHHHHHHHH", "day5_seekLife_5")
        ]
    )


    #[1] MC: goodbye!!!!!!
label day5_seekLife_4: 

    $ chat_message("wnpep: viva bem!")

    jump day5_seekLife_6


    #[2] MC: AHHHHHHHHHHHHH
label day5_seekLife_5: 

    $ chat_message("elimf: AHHHHHHHHHHHHHHHHHHHHHHH!!!!")

    jump day5_seekLife_6


    # end choices
label day5_seekLife_6: 

    $ chat_message("odxny: 1",fastmode=True)

    # server shut down

    pause 1 

    play sound "audio/sfx/ui_menu_back_001 hangup.ogg"

    $ quick_menu = False
    $ _preferences.afm_enable = False 

    hide screen seekL_ui 

    pause 4 

    ##### for platonic route camera pans ###########################
    show cg platonic 
    camera:
        zoom 1.60 xpos -2313 ypos -486
        linear 5.0 xpos -1602
    with dissolve
    pause 4.8

    show cg platonic 
    camera:
        zoom 1.60 xpos 144 ypos 423
        linear 5.0 ypos 792
    with dissolve
    pause 4.8

    show cg platonic 
    camera:
        zoom 0.57 xpos 486 ypos 540
        linear 10.0 zoom 0.5
    with dissolve 

    pause 1.0 
    show screen game_over_neutral_text with Dissolve(2.0) 
    $ persistent.seekLife = True 
    $ _preferences.afm_enable = False

    pause 

    hide screen game_over_neutral_text with dissolve

    scene black 
    camera: 
        subpixel True pos (0,0) zoom 1.0
    with dissolve

    stop music fadeout 3.0 

    pause 4 

    return 



label day5_seekLove_chat: 

    $ chat_message("wnpep: eu diria que é hora de estourar as garrafas proverbiais")

    $ chat_message("elimf: ou as de verdade?? haha imagina")

    $ chat_message("elimf: {image=e_orz}")

    pause 1 

    $ chat_message("elimf: a menos que??",ot="wnpep")

    $ chat_message("wnpep: vou abrir uma cerveja só por você")

    $ chat_message("elimf: teremos um casamento na primavera")

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("wnpep: eu não acho")

    $ chat_message("elimf: deve estar tudo bem pq vc nao é casado né")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: vou pegar aquela cerveja")

    $ chat_message("incri: abandonado antes mesmo de chegar ao altar. BRUTAL")

    $ player_choice(
        [
            ("o clima de festa está ficando meio estranho", "day5_seekLove_1"), 
            ("eu estava prestes a me oferecer para ser o dj do seu casamento", "day5_seekLove_2")
        ]
    )


    #[1] MC: this party vibe is getting kind of weird
label day5_seekLove_1: 

    $ chat_message("elimf: desculpa por não ser bom o suficiente para o pep")

    jump day5_seekLove_3


    #[2] MC: i was just about to offer to be your wedding dj
label day5_seekLove_2: 

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: droga, nós poderíamos ter tido tudo")

    jump day5_seekLove_3


    # end choices
label day5_seekLove_3: 

    $ chat_message("odxny: Ainda temos nossa festa atual.")

    $ chat_message("elimf: o dia foi salvo",ot="wnpep")

    $ chat_message("wnpep: voltei",fastmode=True)

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: ninguém fale com meu ex")

    $ chat_message("incri: rlxa vc pode deixar isso pra trás qnd começar o resto da sua vida triste depois daqui")

    $ chat_message("elimf: essa é a coisa mais legal que vc já me disse",ot="incri")

    $ chat_message("incri: sua vida triste e patética",ot="wnpep")

    $ chat_message("incri: {image=e_pain}",ot="wnpep")

    $ chat_message("wnpep: sempre será um pouco melancólico")

    $ chat_message("wnpep: especialmente quando se trata do meu ex abandonado")

    $ chat_message("elimf: vc ouviu alguma coisa",ot="wnpep")

    $ chat_message("wnpep: que tempos nós tivemos ",ot="incri")

    $ chat_message("incri: AFF",fastmode=True)

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: podemos falar de outra coisa")

    $ chat_message("elimf: depois de todo o nosso trabalho, o incri ainda é alérgico ao amor")

    $ chat_message("wnpep: certamente essa experiência o amoleceu um pouco?")

    $ chat_message("wnpep: sinto que o incri tirou algo disso, mesmo que não admita")

    $ chat_message("incri: eu já sei de tudo")

    $ chat_message("incri: {image=e_letsgo}")

    # dms

    $ chat_message("odxny: Ei.",c="admin")

    $ player_choice(
        [
            ("ei?", "day5_seekLove_4"), 
            ("eiii!!!!", "day5_seekLove_5")
        ]
    )


    #[1] MC: hey?
label day5_seekLove_4: 

    $ chat_message("odxny: Sim. Ei. Por que a confusão?",c="admin")

    #MC: dunno actually. maybe the informality of it
    $ player_choice(
        [
            ("não sei, na verdade. talvez a informalidade", "x")
        ]
    )

    $ chat_message("odxny: Sou capaz de mais de um registro.",c="admin")

    #MC: there really is no end to ur skill
    $ player_choice(
        [
            ("sua habilidade realmente não tem fim", "x")
        ]
    )

    $ chat_message("odxny: Estamos saindo do assunto.",c="admin")

    jump day5_seekLove_6


    #[2] MC: hey!!!!
label day5_seekLove_5: 

    $ chat_message("odxny: Que recepção entusiasmada.",c="admin")

    #MC: i'm just happy to see u!
    $ player_choice(
        [
            ("só estou feliz em te ver!", "x")
        ]
    )

    $ chat_message("odxny: Sou tão emocionante assim?",c="admin")

    #MC: yea!!!
    $ player_choice(
        [
            ("sim!!!", "x")
        ]
    )

    # typing
    pause 2

    $ chat_message("odxny: Interessante.",c="admin")

    $ chat_message("odxny: Mas estamos saindo do assunto.",c="admin")

    jump day5_seekLove_6


    # end choices
label day5_seekLove_6: 

    $ chat_message("odxny: Só estou te enviando algo antes que o programa desligue.",c="admin")

    #MC: oh?
    $ player_choice(
        [
            ("oh?", "x")
        ]
    )

    $ chat_message("odxny: Uma nova função. Vou ativá-la para você logo antes do desligamento",c="admin")

    $ chat_message("odxny: `exec discar()`",c="admin")
    pause 0.2
    $ hack_notes.append("nova função: \ndiscar(numerodetelefone)")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ player_choice(
        [
            ("e o que exatamente eu coloco nesses parênteses desta vez?", "x")
        ]
    )

    $ chat_message("odxny: Ouvi dizer que um número de telefone pode funcionar.",c="admin")

    $ chat_message("odxny: {image=e_orz}",c="admin")

    #MC: hmm. suspicious
    $ player_choice(
        [
            ("hmm. suspeito", "x")
        ]
    )

    $ chat_message("odxny: Oh, agora estamos preocupados com a privacidade.",c="admin")

    #MC: i was joking!!
    $ player_choice(
        [
            ("eu estava brincando!!", "x")
        ]
    )

    $ chat_message("odxny: Mhm.",c="admin")

    #MC: i will call it, promise
    $ player_choice(
        [
            ("eu vou usar, prometo", "x")
        ]
    )

    $ chat_message("odxny: Você é tão confiante.",c="admin")

    $ chat_message("odxny: {image=e_pain}",c="admin")

    #MC: oh my god!! enough!!
    $ player_choice(
        [
            ("ah, meu deus!! chega!!", "x")
        ]
    )

    $ chat_message("odxny: Desculpe, não resisti.",c="admin")

    $ chat_message("odxny: Mas obrigado por prometer.",c="admin")

    #MC: youre WELCOME
    $ player_choice(
        [
            ("de NADA", "x")
        ]
    )

    $ chat_message("odxny: KKKK",c="admin")

    $ player_choice(
        [
            ("mas, espera, eu preciso do seu número!", "x")
        ]
    )

    $ chat_message("odxny: Sim! E, eu deixei para você.",c="admin")

    $ chat_message("odxny: Tenho certeza que você consegue encontrar.",c="admin")

    $ chat_message("odxny: {image=e_orz}",c="admin")

    $ player_choice(
        [
            ("uau.", "x")
        ]
    )

    # general

    $ chat_message("wnpep: suponho que deveríamos botar o bloco na rua")

    $ chat_message("elimf: que coisa de pai")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: não posso negar quem eu sou")

    $ chat_message("incri: é vc ja se entregou ")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: sim, eu lembro, obrigado")

    $ chat_message("incri: como deveria. me agradeça mais")

    $ chat_message("wnpep: obrigado por me fazer sentir um pouco menos de falta disso")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: VCS VAO SENTIR MINHA FALTA E SABEM DISSO")

    $ chat_message("elimf: rlxa todos nós vamos, sempre que o zumbido no ouvido atacar")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("odxny: Vou colocar o cronômetro para 60 segundos para que todos possam se despedir antes de eu apertar o interruptor.")

    $ chat_message("wnpep: justo")

    #wnpep typing
    $ chat_message("wnpep: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",ot="elimf",nooutput=True)

    $ chat_message("elimf: sim, é quase tempo suficiente para um dos seus discursos mais curtos")

    #stops, types again

    pause 1 

    $ chat_message("wnpep: touché")

    $ chat_message("incri: nao tenho nada a dizer pra vcs palhaços")

    $ chat_message("incri: {image=e_letsgo}")

    $ player_choice(
        [
            ("fon fon", "day5_seekLove_7"), 
            ("</3", "day5_seekLove_8")
        ]
    )


    #[1] MC: honk honk
label day5_seekLove_7: 

    $ chat_message("elimf: KKKK",ot="incri")

    $ chat_message("incri: cala a porra da boca")

    $ chat_message("incri: {image=e_letsgo}")

    jump day5_seekLove_9


    #[2] MC: </3
label day5_seekLove_8: 

    $ chat_message("incri: tira isso de perto de mim")

    $ chat_message("incri: {image=e_letsgo}")

    jump day5_seekLove_9


    # end choices
label day5_seekLove_9: 

    # $ chat_message("elimf: has our time frolicking together meant nothing 2 u </3")

    # $ chat_message("incri: wtf")

    $ chat_message("elimf: vc é tão sem coração")

    $ chat_message("incri: vc está abaixo de mim")

    $ chat_message("elimf: eu sou bem versátil :^)")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: AFF",ot="odxny")

    $ chat_message("odxny: Se estivermos prontos, estou iniciando o cronômetro.")

    $ chat_message("wnpep: vou começar dizendo que acho que isso resultou em uma experiência bem ok")

    $ chat_message("wnpep: todos vocês têm pelo menos algumas boas qualidades")

    $ chat_message("elimf: ahhhhh",ot="incri")

    $ chat_message("incri: eca",ot="elimf",fastmode=True)

    $ chat_message("elimf: vc também pep")

    $ chat_message("wnpep: eu tento")

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("elimf: sim, frequentemente")

    $ chat_message("elimf: muito, muito, muito frequentemente")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: certo, já chega",ot="elimf")

    $ chat_message("elimf: em troca, como prova da minha imensa gratidão, vou conceder minha sinceridade a todos vocês")

    #MC: oh???
    $ player_choice(
        [
            ("oh???", "x")
        ]
    )

    $ chat_message("incri: odeio")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: nao quero",ot="elimf")

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("elimf: eu concederei mesmo assim")

    $ chat_message("wnpep: oh dia frabjoso",ot="odxny")

    $ chat_message("odxny: 30 segundos",fastmode=True)

    $ chat_message("elimf: vcs foram pelo menos divertidos ")

    $ chat_message("elimf: não como um filme, mas tipo. um bom episódio de tv ou um especial")

    $ chat_message("elimf: dedicarei a vcs pelo menos uma bongada cada")

    $ chat_message("wnpep: nunca me senti tão honrado",ot="incri")

    $ chat_message("incri: engasga e tosse com isso ",fastmode=True)

    $ chat_message("elimf: no espírito da harmonia, não vou aproveitar a deixa que vc acabou de me dar")

    $ chat_message("odxny: Pela minha parte, direi que gostei um pouco disso. Vocês todos foram certamente interessantes.")

    $ chat_message("wnpep: nós realmente nunca tivemos um momento de tédio")

    $ chat_message("incri: fale por vc, vcs todos foram chatos")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("wnpep: fomos?")

    $ chat_message("incri: vcs todos foram na maior parte chatos",ot="odxny")

    $ chat_message("odxny: 15 segundos.",fastmode=True)

    $ player_choice(
        [
            ("mesmo que nosso tempo tenha sido curto, vou sentir falta de vocês!", "day5_seekLove_10"), 
            ("obrigado por me ensinarem, farei o meu melhor com o que aprendi!", "day5_seekLove_11")
        ]
    )
    

    #[1] MC: even tho our time was short i'll miss u guys!
label day5_seekLove_10: 

    $ chat_message("incri: compreensível mas tente não chorar por mim")

    $ chat_message("wnpep: estou ao mesmo tempo feliz e arrependido por ter causado essa impressão tão rapidamente")

    $ chat_message("wnpep: {image=e_pain}")

    #MC: its ok!! im happy to have been here!
    $ player_choice(
        [
            ("tudo bem!! estou feliz por ter estado aqui!", "x")
        ]
    )

    $ chat_message("odxny: Compartilho do sentimento.")

    $ chat_message("odxny: {image=e_orz}")

    $ chat_message("elimf: ahh vc pegou até o chefe")

    $ chat_message("wnpep: ninguém é imune à sinceridade")

    jump day5_seekLove_12


    #[2] MC: thanks for teaching me, ill do my best w what ive learned!
label day5_seekLove_11: 

    $ chat_message("elimf: vá em frente, bravo guerreiro. eu acredito")

    #MC: thank u for ur support
    $ player_choice(
        [
            ("obrigado pelo seu apoio", "x")
        ]
    )

    $ chat_message("incri: espera qual sua info eu recebo uma parte como seu professor")

    $ chat_message("odxny: Um pouco tarde para isso.")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: NÃO",ot="wnpep")

    $ chat_message("wnpep: bem, boa sorte e vá com deus. só não nos dê crédito se vc for pego pelos federais")

    $ chat_message("incri: amns, d,ml",ot="elimf")

    $ chat_message("elimf: {image=e_crying}",fastmode=True)

    $ chat_message("elimf: KKKK")

    jump day5_seekLove_12


    #end choices
label day5_seekLove_12: 

    $ chat_message("odxny: E com isso, estamos em 5")

    $ chat_message("odxny: 4")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: adeus",ot="odxny")

    $ chat_message("odxny: 3",fastmode=True)

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: adeus e obrigado pelos peixes!")

    $ chat_message("odxny: 2",ot="elimf",fastmode=True)

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: adeus pra sempre :^)")

    $ chat_message("odxny: 1",fastmode=True)

    $ func_access_dial = True 
    $ horn_allowed = False

    # server shut down

    # short credits

    pause 1 

    # shut down server stuff 

    stop music 
    play sound "audio/sfx/data_loaded_001.ogg"
    #$ defenses = True 
    hide screen seekL_ui with Dissolve(0.1)
    pause 0.2
    $ server_kill = True
    $ at_end = True 
    $ player_is_waiting = True 
    $ _preferences.afm_enable = False 

    $ reset_chats() 

    pause 2

    show screen seekL_ui with Dissolve(2.0)
    
    #show screen phonecall_window_real

    #jump day5_seekLove_call

    ## maybe instead of showing the screen, we have the player execute a command 
    ## and that command will let you start up a call if the number works 
    #show screen secure_dial 
    $ renpy.pause(hard=True)