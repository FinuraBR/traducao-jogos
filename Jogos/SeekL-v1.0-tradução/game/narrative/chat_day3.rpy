## INSERT SIDE WORD GAME WITH ODXNY STARTING THIS DAY 

label day3_start: 

    #play music "audio/music/server_room_chiller_version.mp3" loop fadein 2.0 fadeout 2.0 
    play music "audio/music/little_hand_on_the_clocklooped.ogg" loop fadein 2.0 fadeout 2.0 

    $ chat_message("elimf: certo uhhh hh h")

    $ chat_message("elimf: espera aí, eu tinha")

    $ chat_message("elimf: eu tinha algo em mente")

    $ chat_message("wnpep: bom, desembucha então",ot="elimf")

    $ chat_message("elimf: já vai vir")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("wnpep: vai nessa")

    $ chat_message("wnpep: tô voltando ao trabalho")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("wnpep: {image=e_serious}")

    # MC: what are you working on wnpep?
    $ player_choice(
        [
            ("no que você está trabalhando, wnpep?", "x")
        ]
    )

    $ chat_message("wnpep: só coletando dados pro meu hack final. um negócio bem simples, mas tem que ser feito")

    $ chat_message("wnpep: acho que isso significa que é minha vez de te usar?")

    $ player_choice(
        [
            ("errrr, não sei não, hein", "day3_1"),
            ("oh. ousado", "day3_2"),
            ("finalmente eu tenho um propósito", "day3_3")
        ]
    )


    # [1] MC: errrr I don't know about that
label day3_1: 
    $ chat_message("wnpep: foi uma piada! eu só queria ver se você gostaria de acompanhar e receber umas dicas")

    $ chat_message("incri: ah meu deus é a porra da teresa")

    $ chat_message("elimf: *teresa")

    $ chat_message("incri: cala a boca")

    jump day3_4 


    # [2] MC: oh. saucy
label day3_2: 
    $ points_seekLove += 1

    # wnpep typing a while

    $ chat_message("incri: {image=e_crying}")

    $ chat_message("incri: ROLANDO DE RIR")

    $ chat_message("incri: KKKKKKKKKKKKKKKK",ot="wnpep")

    $ chat_message("wnpep: muito engraçado, mas todos nós sabemos que não foi isso que eu quis dizer")

    $ chat_message("elimf: será?????")

    # MC: i just can't be sure
    $ player_choice(
        [
            ("eu só não tenho certeza", "x")
        ]
    )

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: seu velho tarado nojento")
    
    jump day3_4


    # [3] MC: finally i have a purpose
label day3_3: 
    $ points_seekLove += 1

    $ chat_message("odxny: HA",ot="elimf")

    $ chat_message("elimf: pfv",fastmode=True)

    $ chat_message("elimf: retiro tudo que disse, vc não é mais inútil")

    $ chat_message("elimf: vc é tipo um liquidificador ou um sofá")

    $ chat_message("incri: nossa, essas são boas")

    # MC: uh. thanks
    $ player_choice(
        [
            ("uh. valeu", "x")
        ]
    )

    jump day3_4



    # end choices
label day3_4: 

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: estamos nos desviando do assunto. o ponto é que, se você quiser participar, eu posso te dar umas dicas em troca")

    $ chat_message("odxny: Uma troca justa.",ot="incri")

    $ chat_message("incri: como se vc pudesse superar minhas habilidades de ensino. otário")

    $ chat_message("elimf: eu sinto que não rolou muito ensino da sua parte")

    $ chat_message("incri: não é verdade",ot="wnpep")

    $ chat_message("wnpep: não querendo usar a carteirada da idade, mas eu tenho experiência pra dizer o contrário")

    $ chat_message("wnpep: na verdade, acho que eu poderia dar uns conselhos muito bons")

    $ chat_message("odxny: Ele tem seus momentos.",ot="incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: só tô ouvindo desculpinha")

    $ chat_message("wnpep: você saberia disso se algum dia aceitasse meu conselho")

    $ chat_message("incri: não precisei. tanto faz")

    $ chat_message("incri: vc também só tá se aproveitando delu")

    $ chat_message("elimf: incri, eu pensei que vc tinha ensinado elu por causa do seu coração de ouro ou algo assim kkk")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: é DIFERENTE",ot="wnpep")

    $ chat_message("wnpep: nós dois podemos estar nos beneficiando, mas é aí que as semelhanças acabam")

    $ chat_message("wnpep: estou entrando nisso com uma mentalidade diferente e muito mais paciência")

    $ chat_message("elimf: ele tem a atenção plena do lado dele")

    $ chat_message("incri: {image=e_serious}")

    $ chat_message("incri: que tédio")

    $ chat_message("wnpep: não é a coisa mais empolgante, mas é importante")

    $ chat_message("incri: CRINGE")

    $ chat_message("wnpep: a gente tá no primário agora?")

    $ chat_message("incri: suas habilidades tão")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: certo, bom, eu tenho um hack pra rodar")

    $ chat_message("wnpep: thrim, se vc quiser ajudar, minha oferta ainda tá de pé")

    # MC: oh yeah lets do it
    $ player_choice(
        [
            ("ah, claro, vamos nessa", "x")
        ]
    )

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: excelente")

    $ chat_message("wnpep: deixa eu carregar tudo aqui",ot="elimf")

    $ chat_message("elimf: incri, qual a sensação de ser trocada")

    $ chat_message("incri: eu que saí primeiro, idiota")

    $ chat_message("elimf: oo foi mal, erro meu")

    $ chat_message("odxny: Sua habilidade de criar drama em tão pouco tempo é impressionante.")

    $ chat_message("incri: foi mal por fazer todo mundo ficar obcecado por mim")

    $ chat_message("incri: {image=e_orz}")

    #$ chat_message("odxny: All is forgiven.")

    $ chat_message("wnpep: beleza, tá tudo pronto")

    $ chat_message("wnpep: vamos ao que interessa")

    $ chat_message("wnpep: {image=e_sparkle}")

    jump day3_5


## SEEKL SEGMENT 
label day3_5: 

    # MC: sweet!
    $ player_choice(
        [
            ("demorou!", "x")
        ]
    )

    $ chat_message("wnpep: dei uma fuçada mais cedo assim que tivemos aquela grande revelação de dados do irs")

    $ chat_message("elimf: que adição de última hora foda, od")

    $ chat_message("incri: teria sido mais foda ter isso tipo. esse tempo todo",ot="wnpep")

    $ chat_message("odxny: Kkkk.",ot="wnpep")

    $ chat_message("wnpep: e acho que temos exatamente a tabela que eu preciso",fastmode=True)

    $ chat_message("wnpep: {color="+color_help+"}você pode dar uma olhada nisso, thrim?{/color}")

    $ chat_message("wnpep: `select * \nfrom azgov.insurance` ")
    pause 0.5
    $ tables_seen.append("azgov.insurance")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.insurance"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_8"

    $ chat_message("odxny: Seguro?")

    $ chat_message("elimf: arizona de novo não")

    $ player_choice(
        [
            ("claro, um momento", "day3_6"), 
            ("a gente tá atrás de uma seguradora?", "day3_7")
        ]
    )


    # [1] MC: sure, one moment 
label day3_6:

    $ chat_message("wnpep: vlw. eu explico em um segundo")

    jump wait_start


    # [2] MC: are we chasing an insurance company? 
label day3_7:
    $ points_seekLove += 1

    $ chat_message("wnpep: não exatamente, mas quase isso")

    $ chat_message("wnpep: dê uma olhada primeiro, por favor")

    jump wait_start


    # complete the query 
label day3_8: 

    $ chat_message("wnpep: tá vendo?")

    # MC: yes -- looks like a list of insurance companies 
    $ player_choice(
        [
            ("sim -- parece uma lista de seguradoras", "x")
        ]
    )

    $ chat_message("elimf: boraaaaa",ot="wnpep")

    $ chat_message("wnpep: bom. agora...")

    $ chat_message("wnpep: Preciso que você encontre uma empresa aí que corresponda aos dois seguintes critérios -")

    $ chat_message("wnpep: {color="+color_help+"}1) tenha INS_TYPE = 'medical'{/color}, e")

    $ chat_message("wnpep: {color="+color_help+"}2) tenha INS_HSP_PARTNERS = 1{/color}")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["ins_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.insurance"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("ins_id", "INS91983-AZ")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_12"

    $ player_choice(
        [
            ("ok, já sei o que fazer.", "day3_9"),
            ("com uma cláusula where de novo?", "day3_10")
        ]
    )


    # [1] MC: okay, i know what to do. 
label day3_9:
    $ points_seekLove += 1

    $ chat_message("incri: vamos ver isso aí")

    $ chat_message("elimf: elu se saiu bem ontem, como assim")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: \"se saiu bem\" vc é idiota")

    $ chat_message("incri: que parte daquilo foi bem")

    $ chat_message("odxny: Pra mim pareceu bem.")

    $ chat_message("odxny: Não que você estivesse fazendo um hack complicado, de qualquer forma.")

    $ chat_message("incri: q porra é essa")

    jump day3_11 


    # [2] MC: with a where clause again? 
label day3_10:

    $ chat_message("wnpep: sim! exatamente",ot="elimf")

    $ chat_message("elimf: {color="+color_help+"}em vez de usar \"OR\" como antes, você pode usar \"AND\"{/color}")

    # in dms 

    $ chat_message("odxny: Precisa da resposta?",c="admin")

    $ player_choice(
        [
            ("ah, não, mas obrigado", "day3_10A"),
            ("talvez... por favor?", "day3_10B")
        ]
    )


    # [2-A] MC: oh, no, but thanks 
label day3_10A:

    $ chat_message("odxny: D boa",c="admin")

    $ chat_message("odxny: Boa sorte",c="admin")

    $ chat_message("odxny: {image=e_wink}",c="admin")

    jump day3_11


    # [2-B] MC: maybe... please? 
label day3_10B:

    $ chat_message("odxny: Claro.",c="admin")

    $ chat_message("odxny: `select ins_name \nfrom azgov.insurance \nwhere ins_type = 'medical' \n   and ins_hsp_partners = 1`",c="admin")

    jump day3_11 


    # exit bronches
label day3_11: 

    $ chat_message("wnpep: vai em frente e tenta aí, thrim")

    # MC: can i ask why we're looking this up? 
    $ player_choice(
        [
            ("posso perguntar por que estamos procurando isso?", "x")
        ]
    )

    $ chat_message("wnpep: ah, claro, sim")

    $ chat_message("wnpep: estou procurando a confirmação de algo que suspeito há um tempo")

    $ chat_message("wnpep: rumores de um golpe entre seguradora e hospital. pedindo procedimentos desnecessários e pagando um extra por fora pro médico fazer")

    $ chat_message("elimf: algum motivo pra ir atrás disso?")

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("wnpep: não é do nosso interesse fazer o bem ao próximo?")

    $ chat_message("incri: deixa eles se preocuparem com eles mesmos")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: quem deixou a ayn rand entrar aqui")

    $ chat_message("incri: cala a boca porra")

    $ chat_message("incri: o que isso significa")

    $ chat_message("elimf: te conto quando vc crescer",ot="odxny")

    $ chat_message("odxny: O hack final de todo mundo é relacionado a vingança?")

    $ chat_message("wnpep: opa opa opa")

    $ chat_message("wnpep: eu não sou vingativo")

    $ chat_message("wnpep: eu estou moralmente certo.")

    $ chat_message("wnpep: {image=e_serious}")

    $ chat_message("elimf: interessante",ot="incri")

    $ chat_message("incri: eu também estava")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: você e eu não somos iguais")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: sim, graças a deus")

    $ chat_message("wnpep: enfim. vá em frente e tente achar o nome daquele hospital, thrim")

    $ chat_message("wnpep: {color="+color_help+"}1) tenha INS_TYPE = 'medical'{/color}, e")

    $ chat_message("wnpep: {color="+color_help+"}2) tenha INS_HSP_PARTNERS = 1{/color}")

    jump wait_start


    # query runs 
label day3_12:

    $ chat_message("wnpep: alguma correspondência?")

    $ chat_message("wnpep: para conseguir aplicar um golpe dessa magnitude, provavelmente tem que ser um hospital e uma seguradora em conluio")

    $ chat_message("incri: \"conluio\"")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: vc é velho pra caralho")

    # MC: i did find a match. 
    $ player_choice(
        [
            ("eu achei uma correspondência.", "x")
        ]
    )

    # MC: one name -- "Gered Group" 
    $ player_choice(
        [
            ("um nome -- \"Gered Group\"", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("insurance: \nGered Group")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("wnpep: só esse?")

    $ player_choice(
        [
            ("só esse", "day3_13"),
            ("talvez.", "day3_14")
        ]
    )



    # [1] MC: just the one 
label day3_13:

    $ chat_message("wnpep: ok, obrigado.")

    jump day3_15


    # [2] MC: maybe. 
label day3_14:
    $ points_seekLove += 1

    $ chat_message("elimf: talvez?",ot="wnpep")

    $ chat_message("wnpep: por favor.")

    # MC: yes, one. sorry
    $ player_choice(
        [
            ("sim, um. foi mal", "x")
        ]
    )

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: ok")

    jump day3_15


label day3_15: 

    $ chat_message("odxny: Então, você tem certeza que esse é o do golpe?")

    $ chat_message("wnpep: {image=e_serious}")

    $ chat_message("wnpep: não diria 100% de certeza, mas perto o suficiente")

    $ chat_message("wnpep: tipo 98%",ot="elimf")

    $ chat_message("elimf: quer dizer, não é tudo golpe?")

    $ chat_message("elimf: no esquema das coisas. o mundo das paradas")

    $ chat_message("incri: a vida é um golpe do caralho.")

    $ chat_message("elimf: ^ o coringa")

    $ chat_message("elimf: {image=e_pain}",ot="incri")

    $ chat_message("incri: CALA A BOCA")

    $ chat_message("incri: sua vida é um golpe")

    $ chat_message("elimf: essa também foi fácil demais")

    $ chat_message("wnpep: podemos focar, por favor")

    $ chat_message("elimf: certo")

    $ chat_message("elimf: não podemos esquecer o verdadeiro golpe",ot="odxny")

    $ chat_message("odxny: Só continue, pep.")

    $ chat_message("wnpep: próximo passo -- precisamos identificar o hospital que trabalha com eles")

    $ chat_message("wnpep: você pode pegar isso aqui: #azgov.hospitals#")
    pause 0.5
    $ tables_seen.append("azgov.hospitals")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["hsp_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["azgov.hospitals"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("hsp_id", "H5212-03")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_16"

    $ chat_message("elimf: cê tá de sacanagem")

    #$ chat_message("odxny: LMAO")

    $ chat_message("elimf: por que é sempre tão direto")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("wnpep: olha o chefão, não sou eu que mando")

    $ chat_message("odxny: O programa do back-end faz um bom trabalho às vezes montando dados assim.")

    $ chat_message("elimf: doideira")

    $ chat_message("wnpep: vá dar uma espiada naquela tabela e {color="+color_help+"}veja se consegue descobrir qual deles trabalha com aquela seguradora{/color}")

    jump wait_start


    # query runs 
label day3_16:

    # MC: i think i got it? 
    $ player_choice(
        [
            ("acho que consegui?", "x")
        ]
    )

    $ chat_message("odxny: E?") 

    # MC: "PRIDE" 
    $ player_choice(
        [
            ("\"PRIDE\"", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("hospital: \nPRIDE")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    pause 2 

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: ....sério?") 

    $ chat_message("odxny: ?") 

    # MC: why surprised? 
    $ player_choice(
        [
            ("por que a surpresa?", "x")
        ]
    )

    pause 1 

    $ chat_message("wnpep: não faz sentido")

    $ chat_message("wnpep: pensando")

    pause 3  

    $ chat_message("wnpep: não tem nenhuma outra seguradora listada com aquele hospital? achei que eu tinha checado essa")

    $ chat_message("wnpep: talvez ins_define? está definido como true?")

    $ chat_message("odxny: Sim, está.")

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: q porra é essa")

    $ chat_message("wnpep: mas a gered só trabalha com a PRIDE?")

    $ chat_message("odxny: Pep, se você voltar para #azgov.insurance#, dê uma olhada na coluna ins_alias da linha do Gered Group.")

    $ chat_message("wnpep: olhando") 

    pause 3 

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: \"Define\". meu deus")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("elimf: não entendi. por favor, explique com palavras simples")

    $ chat_message("wnpep: A PRIDE parece aceitar duas seguradoras, Define e Gered -- mas elas são a mesma empresa.")

    $ chat_message("odxny: Meio sorrateiro.")

    # MC: what's the point of doing that? 
    $ player_choice(
        [
            ("qual o sentido de fazer isso?", "x")
        ]
    )

    $ chat_message("odxny: Para não parecerem suspeitos, ha.",ot="wnpep")

    $ chat_message("wnpep: deveria ter ligado os pontos. não sei como deixei passar")

    $ chat_message("wnpep: minha filha anda dizendo que preciso de óculos novos")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: uma filha",ot="odxny")

    $ chat_message("odxny: Faz sentido você ser pai.")

    $ chat_message("elimf: é, nem consigo ficar bravo com essa. seria estranho se vc não fosse, pra ser sincero")

    $ chat_message("wnpep: kkk")

    $ chat_message("wnpep: desculpa, eu continuo deixando as coisas escaparem de alguma forma")

    $ chat_message("wnpep: deve ser meu amor e carinho por todos vocês me permitindo me abrir mais livremente")

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("elimf: vai se foder",ot="incri")

    $ chat_message("incri: é a porra do thrim",fastmode=True)

    # MC: i didn't do shit 
    $ player_choice(
        [
            ("eu não fiz porra nenhuma", "day3_17"), 
            ("não, é o amor e o carinho com certeza", "day3_18")
        ]
    )

label day3_17: 

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: nos contaminou")

    $ chat_message("odxny: Eu não diria contaminou.")

    $ chat_message("odxny: Thrim trouxe um pouco de vida de volta a este servidor.")

    # MC: aw. 
    $ player_choice(
        [
            ("own. vc tá falando sério", "x")
        ]
    )

    $ chat_message("odxny: Claro.")

    $ chat_message("elimf: kkkk um sopro de vida antes do fim")

    $ chat_message("elimf: tem um poema aí em algum lugar")

    jump day3_odm_1


label day3_18: 
    $ points_seekLove += 1

    $ chat_message("elimf: UUUUUUUUUUUUUUUUUU",ot="incri")

    $ chat_message("incri: UUUUUUUUUUUUUUUUUUUUUUUUUUUU",fastmode=True)

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: IDEIA DE MERDA",ot="elimf")

    $ chat_message("elimf: SAI DO PALCO",fastmode=True)

    $ player_choice(
        [
            ("nossa. od, vc tá vendo isso", "x")
        ]
    )

    $ chat_message("odxny: KKKKK")

    jump day3_odm_1


label day3_odm_1: 

    $ chat_message("odxny: Parece que você está se divertindo mais aprendendo com o pep.", c="admin")

    $ player_choice(
        [
            ("estou! ele tem sido muito legal", "day3_odm_2"), 
            ("bem.........", "day3_odm_5"), 
            ("e se eu precisar da ameaça de violência pra aprender", "day3_odm_6")
        ]
    )


    # [1] MC: i am! hes been really nice
label day3_odm_2: 

    $ chat_message("odxny: Não sei se eu o elogiaria tanto assim.", c="admin")

    $ player_choice(
        [
            ("quer dizer, comparado com a incri...", "day3_odm_3"), 
            ("retiro tudo. ele é uma ameaça", "day3_odm_4")
        ]
    )


    # [1-1] MC: i mean, compared to incri…
label day3_odm_3: 

    $ chat_message("odxny: {image=e_pain}", c="admin")

    $ chat_message("odxny: Tenho certeza que ele ficaria lisonjeado em saber que passou no sarrafo mais baixo possível.", c="admin")

    #MC: really? lemme tell him rn
    $ player_choice(
        [
            ("sério? deixa eu contar pra ele agora", "x")
        ]
    )

    $ chat_message("odxny: Por que você sempre faz coisas horríveis com a minha pressão arterial.", c="admin")

    #MC: HAHAHA
    $ player_choice(
        [
            ("HAHAHA", "x")
        ]
    )

    $ chat_message("odxny: Acho que teremos que parar por aqui. Ordens médicas.", c="admin")

    #MC: WAIT NO
    $ player_choice(
        [
            ("ESPERA NÃO", "x")
        ]
    )

    $ chat_message("odxny: Desculpe, thrim. Simplesmente não há nada que eu possa fazer.", c="admin")

    jump day3_odm_cont  



    #[1-2] MC: i take it all back. he's a menace
label day3_odm_4: 
    $ points_seekLove += 1

    $ chat_message("odxny: {image=e_baby}", c="admin")

    $ chat_message("odxny: Você talvez seja a pessoa mais do contra do mundo.", c="admin")

    #MC: i havent even begun to contradict
    $ player_choice(
        [
            ("eu nem comecei a contrariar ainda", "x")
        ]
    )

    $ chat_message("odxny: Você está fazendo isso de novo.", c="admin")

    #MC: i………….may be
    $ player_choice(
        [
            ("eu..........talvez esteja", "x")
        ]
    )

    $ chat_message("odxny: Você terá que admitir ou provar que estou certo.", c="admin")

    jump day3_odm_cont  



    #[2] MC: well……….
label day3_odm_5: 

    $ chat_message("odxny: Sério? Eu achei que ele estava fazendo um bom trabalho.", c="admin")

    #MC: i might just be a little hopeless
    $ player_choice(
        [
            ("eu talvez seja um pouco sem esperança", "x")
        ]
    )

    $ chat_message("odxny: {image=e_baby}", c="admin")

    $ chat_message("odxny: Bem", c="admin")

    #MC: CMON
    $ player_choice(
        [
            ("QUAL É", "x")
        ]
    )

    $ chat_message("odxny: Você tem que admitir, dominar ArnoldC mas considerar SQL simplificado um passo grande demais é meio engraçado.", c="admin")

    #MC: it's not!!!!
    $ player_choice(
        [
            ("não é!!!!", "x")
        ]
    )

    $ chat_message("odxny: Meio que é.", c="admin")

    jump day3_odm_cont 



    #[3] MC: what if I need the threat of violence to learn
label day3_odm_6: 
    $ points_seekLove += 1

    $ chat_message("odxny: {image=e_pain}", c="admin")

    $ chat_message("odxny: Você alguma vez escuta as palavras que está digitando ou dizendo?", c="admin")

    $ player_choice(
        [
            ("sim sempre", "day3_odm_7"), 
            ("não nunca", "day3_odm_8"), 
            ("hã o quê???", "day3_odm_9")
        ]
    )

    #[3-1] MC: yes always

    #[3-3] MC: no never

    #[3-4] MC: huh whuh???

label day3_odm_7: 

    $ chat_message("odxny: Eu não deveria ter perguntado.", c="admin")

    jump day3_odm_10 

label day3_odm_8: 

    $ chat_message("odxny: Eu não deveria ter perguntado.", c="admin")

    jump day3_odm_10 

label day3_odm_9: 

    $ chat_message("odxny: Eu não deveria ter perguntado.", c="admin")

    jump day3_odm_10 

label day3_odm_10: 

    #MC: aww
    $ player_choice(
        [
            ("aww", "x")
        ]
    )

    $ chat_message("odxny: Enfim. Certamente existem motivadores melhores.", c="admin")

    pause 1

    $ chat_message("odxny: Não me diga que você tem aprendido linguagens esotéricas dessa forma.", c="admin")

    #MC: absolutely not
    $ player_choice(
        [
            ("claro que não", "x")
        ]
    )

    $ chat_message("odxny: Estágio 1: Negação", c="admin")

    #MC: for real!!! i'm not!!!
    $ player_choice(
        [
            ("é sério!!! eu não sou!!!", "x")
        ]
    )

    $ chat_message("odxny: Estágio 2: Raiva", c="admin")

    jump day3_odm_cont 


    # end choices
label day3_odm_cont: 

    #MC: AAAAAAAAAAA
    $ player_choice(
        [
            ("AAAAAAAAAAA", "x")
        ]
    )

    $ chat_message("odxny: KKKKK", c="admin")

    $ chat_message("odxny: Desculpa, não resisti.", c="admin")

    #MC: could you??
    $ player_choice(
        [
            ("poderia??", "x")
        ]
    )

    $ chat_message("odxny: Alguma das respostas ajudaria?", c="admin")

    #MC: ……no……..
    $ player_choice(
        [
            (".....não......", "x")
        ]
    )

    $ chat_message("odxny: Lamento desapontar.", c="admin")

    $ chat_message("odxny: E por te irritar.", c="admin")

    pause 1 

    $ chat_message("odxny: Um pouco.", c="admin")

    #MC: utterly unrepentant
    $ player_choice(
        [
            ("totalmente sem remorso", "x")
        ]
    )

    $ chat_message("odxny: Eu disse um pouco.", c="admin")

    #MC: completely w/o shame
    $ player_choice(
        [
            ("completamente sem vergonha", "x")
        ]
    )

    $ chat_message("odxny: //Um pouco.//", c="admin")

    #MC: totally heedless
    $ player_choice(
        [
            ("totalmente imprudente", "x")
        ]
    )

    $ chat_message("odxny: Thrim.", c="admin")

    #MC: got you
    $ player_choice(
        [
            ("te peguei", "x")
        ]
    )

    $ chat_message("odxny: ...", c="admin")

    $ chat_message("odxny: Estou fechando esta DM.", c="admin")

    #MC: LMAO
    $ player_choice(
        [
            ("KKKKK", "x")
        ]
    )

    jump day3_19




label day3_19:

    $ chat_message("wnpep: ok. hora de focar")

    $ chat_message("wnpep: vamos descobrir quem está registrando os pedidos aqui")

    $ chat_message("wnpep: #pride.claims#")
    pause 0.5
    $ tables_seen.append("pride.claims")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["claim_doctor"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["pride.claims"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_20"

    $ chat_message("wnpep: se você verificar essa tabela, verá algumas informações sobre os procedimentos hospitalares e qual médico solicitou cada um")

    $ chat_message("wnpep: {color="+color_help+"}pode dar uma olhada nessa tabela?{/color}")

    # MC: sure, one moment 
    $ player_choice(
        [
            ("claro", "x")
        ]
    )

    jump wait_start 


    # query runs 
label day3_20: 

    # MC: I see two names in here 
    $ player_choice(
        [
            ("Vejo dois nomes aqui. Bailey Yang, Adriel Humphrey", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("name 1: \nBailey Yang")
    $ hack_notes.append("name 2: \nAdriel Humphrey")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("elimf: que hospitalzinho de merda kkkk")

    $ chat_message("odxny: Profissionais em passar despercebidos. Como nós.",ot="wnpep")

    $ chat_message("wnpep: ótimo! e os valores dos pedidos?")

    # MC: not in here, unfortunately 
    $ player_choice(
        [
            ("não estão aqui, infelizmente", "x")
        ]
    )

    $ chat_message("wnpep: {image=e_baby}")

    $ chat_message("wnpep: hã? o quê? sério?")

    # MC: why?
    $ player_choice(
        [
            ("por quê?", "x")
        ]
    )

    $ chat_message("wnpep: bem... achei que precisávamos ver quem está registrando a maioria das coisas caras")

    $ chat_message("elimf: não são só os dois?")

    $ chat_message("wnpep: poderia ser... mas prefiro ter certeza. hm")

    $ chat_message("wnpep: como confirmar...")

    $ chat_message("odxny: O que você acha que deveríamos fazer, thrim?")

    python:
        if has_sql_knowledge: 
            renpy.jump("day3_20_SQL") 
        else: 
            renpy.jump("day3_20_cont")


    # if stated sql knowledge
    # [1] MC: can't we just use a group by or something to see who has which type of claims most often? 
label day3_20_SQL:

    $ player_choice(
        [
            ("não podemos simplesmente usar um group by ou algo assim para ver quem tem qual tipo de pedido com mais frequência?", "x")
        ]
    )

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: KKKKKKKKK")

    $ chat_message("elimf: é od, cadê a porra do group by")

    $ chat_message("odxny: Desculpe. O SeekL não é perfeito.")

    $ chat_message("odxny: Não dá pra fazer muitas daquele tipo de consulta.")

    $ chat_message("elimf: ainda assim, que doideira")

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: Olha.")

    jump day3_20_cont


label day3_20_cont: 

    $ player_choice(
        [
            ("podemos simplesmente ameaçar os dois?", "day3_21"), 
            ("você não disse que um dos médicos estava embolsando dinheiro extra? podemos rastrear isso?", "day3_22")
        ]
    )

    # [2] MC: can we just threaten both of them? 
label day3_21: 

    $ chat_message("incri: é a estratégi a mais eficien te")

    #$ chat_message("elimf: incri stop ruining the new persson ",ot="wnpep")

    $ chat_message("wnpep: kkk. prefiro evitar chantagear um inocente se puder")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: que tédio",ot="odxny")

    $ chat_message("odxny: Que tal holerites? Vamos rastrear o dinheiro.")

    $ chat_message("wnpep: ah, certo. isso faria sentido")

    jump day3_23


    # [3] MC: didn't you say one of the doctors was pocketing extra money? can we track that? 
label day3_22: 
    $ points_seekLove += 1

    $ chat_message("wnpep: excelente raciocínio, thrim. e nós podemos, de fato")

    $ chat_message("wnpep: agora que temos o maravilhoso mundo dos dados do irs")

    $ chat_message("elimf: CA-CHING")

    $ chat_message("elimf: {image=e_sparkle}")

    jump day3_23


label day3_23: 

    $ chat_message("wnpep: para isso, {color="+color_help+"}vamos comparar o resultado de duas tabelas{/color}")

    $ chat_message("wnpep: tabela 1 - #pride.paystubs23#")

    pause 0.5
    $ tables_seen.append("pride.paystubs23")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")

    $ chat_message("wnpep: tabela 2 - #irs.income23#")

    pause 0.5
    $ tables_seen.append("irs.income23")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["pay_total", "irs_total", "full_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["pride.paystubs23", "irs.income23"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [
            ("pay_no", "P3406"), ("pay_no", "P1282"), 
            ("pstb_no", "P73604-437"), ("pstb_no", "P24992-474")
            ]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_27"


    $ chat_message("wnpep: podemos comparar o quanto cada pessoa ganhou de acordo com cada uma") 

    # MC: ohh so... 
    $ player_choice(
        [
            ("ahh então...", "x")
        ]
    )

    # MC: the one who is pocketing extra cash should have reported less to the irs 
    $ player_choice(
        [
            ("aquele que está embolsando dinheiro extra deve ter declarado menos ao irs", "x")
        ]
    )

    $ chat_message("elimf: na mosca",ot="wnpep")

    $ chat_message("wnpep: este pode ser um ótimo momento para te mostrar uma nova função do seekL -- {color="+color_help+"}JOIN{/color}")

    $ chat_message("wnpep: {color="+color_help+"}você já sabe como natural joins funcionam?{/color}")

    $ player_choice(
        [
            ("ah sim, tô de boa!", "day3_24"), 
            ("não (tutorial)", "day3_25")
        ]
    )



    # [1] MC: oh yeah, i'm good! 
label day3_24:

    $ chat_message("wnpep: ok")

    $ chat_message("wnpep: use-o neste exercício")

    jump day3_26 


    # [2] MC: no (tutorial)
label day3_25: 

    $ chat_message("wnpep: sem problemas! vamos sentar e aprender")

    $ chat_message("elimf: vc não tá sentado wn")

    $ chat_message("wnpep: estou sentado.")

    $ chat_message("elimf: confuso")

    $ chat_message("incri: é uma figura de linguagem, idiota")

    $ chat_message("elimf: eu não sou idiota")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: idiota",ot="odxny")

    $ chat_message("odxny: Eu posso ajudar aqui.")

    $ chat_message("odxny: Um {color="+color_syntax+"}JOIN{/color} pode ser usado para combinar as colunas de duas tabelas.")

    $ chat_message("odxny: {color="+color_help+"}Ele procurará por uma coluna em comum entre as duas tabelas e, se uma existir, ele retornará essas duas tabelas combinadas.{/color}")

    $ chat_message("odxny: Então, se você quiser obter informações sobre alguém de duas tabelas diferentes, execute com um {color="+color_syntax+"}JOIN{/color} e você pode ter uma visão limpa de tudo que precisa.")

    $ chat_message("odxny: Aqui está um exemplo. Lembra do \"OfficerOral\"?")

    # MC: how could i forget 
    $ player_choice(
        [
            ("como eu poderia esquecer", "x")
        ]
    )

    $ chat_message("odxny: Tão, tão verdade.")

    $ chat_message("odxny: `SELECT ss_alias \nFROM irs.contacts \nJOIN secretsmooch.users \nWHERE full_name = 'bruce johnson'`")

    $ chat_message("odxny: (Se você rodar isso, vai te ajudar a entender o que vou dizer a seguir.)")

    $ chat_message("odxny: Você chegou naquele apelido ontem através de cláusulas where e olhando entre tabelas, mas você também poderia ter chegado lá apenas rodando isso diretamente.")

    $ chat_message("odxny: #irs.contacts# e #secretsmooch.users# ambas {color="+color_help+"}compartilham a coluna \"email\", o que permite que você junte essas tabelas{/color} e dê uma olhada no apelido do Bruce lá.")

    $ chat_message("odxny: note também como {color="+color_help+"}qualquer coluna que é usada na junção também é impressa{/color}, mesmo que você não a liste especificamente na sua declaração {color="+color_syntax+"}SELECT{/color}. O mesmo para a coluna na cláusula {color="+color_syntax+"}WHERE{/color}.")

    $ chat_message("odxny: Ajuda a manter o controle das coisas.")

    $ chat_message("wnpep: uau. um professor nato")

    $ chat_message("elimf: por que a gente ainda precisa do wnpep")

    $ chat_message("wnpep: verdade",ot="odxny")

    $ chat_message("odxny: Cala a boca kkk")

    $ chat_message("wnpep: tudo isso fez sentido, thrim?")

    $ player_choice(
        [
            ("acho que sim", "day3_25A"), 
            ("vc é tipo. bem prolixo", "day3_25B")
        ]
    )


    # [2-A] MC: i think so 
label day3_25A: 
    $ points_seekLove += 1

    $ chat_message("wnpep: bom trabalho od")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("odxny: Obrigado, obrigado. Mais elogios, por favor.") 

    $ chat_message("incri: sua máscara é só levemente cringe")

    $ chat_message("elimf: eu acho sua máscara muito legal od")

    $ chat_message("odxny: {image=e_pain}") 

    $ chat_message("odxny: Ok. Chega de elogios, por favor.")
    
    jump day3_26


    # [2-B] MC: ur like. rly wordy 
label day3_25B:

    $ chat_message("elimf: retiro o que disse. vc é um saco, od")

    $ chat_message("odxny: {image=e_pain}")

    #$ chat_message("odxny: ...",ot="wnpep")

    $ chat_message("wnpep: eli")

    $ chat_message("elimf: ?")

    jump day3_26


    # exit bronches
label day3_26:

    $ chat_message("wnpep: thrim, se você precisar de lembretes sobre como as coisas funcionam, {color="+color_help+"}você sempre pode verificar a aba do guia seekL{/color}")

    $ chat_message("wnpep: então, {color="+color_help+"}vá em frente e veja se consegue dizer quem tem registros divergentes entre #pride.paystubs23# e #irs.income23# apenas entre aqueles dois nomes na tabela de pedidos{/color}")

    $ chat_message("wnpep: {color="+color_help+"}você vai querer utilizar um JOIN e uma cláusula WHERE para obter a informação que precisamos.{/color}")

    $ chat_message("wnpep: {color="+color_help+"}por favor, puxe essas duas pessoas ao mesmo tempo!{/color}")

    # MC: u got it 
    $ player_choice(
        [
            ("pode deixar", "x")
        ]
    )

    jump wait_start


    # query wait 
label day3_27: 

    # MC: i am so skilled. i got it 
    $ player_choice(
        [
            ("eu sou tão habilidoso. consegui", "x")
        ]
    )

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: esse é o espírito! claro que você é!",ot="odxny")

    $ chat_message("odxny: Bom trabalho.",ot="wnpep")

    $ chat_message("wnpep: então, quem é? {color="+color_help+"}quais totais de holerite não batem para 2023?{/color}")

    $ player_choice(
        [
            ("Bailey Yang", "day3_28"), 
            ("Adriel Humphrey", "day3_29")
        ]
    )


    # [1] MC: Bailey Yang 
label day3_28: 
    $ points_seekLove += 1

    # MC: PRIDE has them down as making 190k, irs as 120k 
    $ player_choice(
        [
            ("A PRIDE registrou elu ganhando 190k, o irs 120k", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("fraudster: \nBailey Yang")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("elimf: eu amo como vc é habilidoso em afirmar fatos básicos")

    $ chat_message("elimf: vc é deslumbrante, thrim")

    # MC: omg thank u 
    $ player_choice(
        [
            ("meu deus, obrigado", "x")
        ]
    )

    jump day3_30


    # [2] MC: Adriel Humphrey 
label day3_29: 

    $ chat_message("incri: compará um numerozinho foi muito difíciu pra vc?")

    $ chat_message("incri: o bebezinho precisa que segurem a mãozinha dele?")

    # MC: ????? am i wrong? 
    $ player_choice(
        [
            ("????? eu estou errado?", "x")
        ]
    )

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: sim, vc tá errado pra caralho, IDIOTA")

    # MC: omg... 
    $ player_choice(
        [
            ("meu deus...", "x")
        ]
    )

    $ chat_message("odxny: Relaxa. É o outro. Bailey Yang.")

    $ chat_message("odxny: Os valores dos pagamentos não batem.")

    pause 0.2
    $ hack_notes.append("fraudster: \nBailey Yang")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    jump day3_30



    # end choices
label day3_30: 

    $ chat_message("odxny: Isso é confirmação suficiente de que este é o médico?")

    $ chat_message("wnpep: para mim? sim")

    $ chat_message("wnpep: geralmente eu seria mais minucioso, mas")

    $ chat_message("wnpep: dadas as minhas informações, isso parece bem direto")

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("wnpep: {color="+color_help+"}se importa de pegar o e-mail de Bailey Yang em {/color}#irs.contacts#, thrim?")

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I93999-218")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day3_33"

    $ player_choice(
        [
            ("eu só estou aqui para fazer trabalho insignificante para vocês", "day3_31"), 
            ("claro, um momento", "day3_32")
        ]
    )


    # [1] MC: am i just here to do petty work for you all 
label day3_31: 
    $ points_seekLove += 1

    $ chat_message("incri: sim")

    $ chat_message("elimf: KKK",ot="wnpep")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("wnpep: estamos todos aprendendo juntos!")

    # MC: are we? 
    $ player_choice(
        [
            ("estamos?", "x")
        ]
    )


    $ chat_message("wnpep: talvez!")

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("wnpep: por favor, pegue")

    # MC: fine, fine 
    $ player_choice(
        [
            ("tá bom, tá bom", "x")
        ]
    )

    jump day3_32


    # [2] MC: sure thing, one moment 
label day3_32: 

    $ chat_message("wnpep: valeu, campeão!")

    jump wait_start 


    # query wait 
label day3_33: 

    # MC: itsssbaeley@baver.net
    $ player_choice(
        [
            ("itsssbaeley@baver.net", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("email: \nitsssbaeley@baver.net")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("wnpep: maravilhoso")

    $ chat_message("wnpep: ah",ot="elimf")

    $ chat_message("elimf: o momento que todos estávamos esperando",ot="incri")

    $ chat_message("incri: CHANTAGEM CHANTAGEM CHANTAGEM",fastmode=True)

    $ chat_message("wnpep: {image=e_serious}")

    $ chat_message("wnpep: um momento, preciso aperfeiçoar isso")

    $ chat_message("odxny: Certo.",ot="elimf")

    $ chat_message("elimf: pensei que ele já teria isso pronto")

    $ chat_message("incri: às vezes vc precisa tipo")

    $ chat_message("incri: sentir")

    $ chat_message("incri: no momento")

    $ chat_message("incri: {image=e_orz}")

    $ chat_message("elimf: uh huh")

    pause 1.0

    $ chat_message("SYSTEM: EXTORSÃO ENVIADA -- ITSSSBAELEY@BAVER.NET")

    $ chat_message("odxny: Boa.")

    $ chat_message("wnpep: este provavelmente vai demorar um pouco. podemos verificar amanhã")

    # MC: why? 
    $ player_choice(
        [
            ("por que vai demorar?", "x")
        ]
    )

    $ chat_message("wnpep: pq isso envolve um golpe gigante sendo exposto kkk")

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("elimf: KKKK",ot="odxny")

    $ chat_message("odxny: Eles vão criar uma estratégia do lado deles.")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("wnpep: último... tudo pronto. huh")


    ## WRAP UP 

    $ chat_message("elimf: é isso pessoal, aplausos")

    $ chat_message("elimf: e rima. na hora",ot="incri")

    $ chat_message("incri: eu terminei o meu mais rápido")

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: eu disse aplausos",ot="odxny")

    $ chat_message("odxny: Bom trabalho, como sempre.")

    $ chat_message("wnpep: valeu")

    # MC: how do u feel?
    $ player_choice(
        [
            ("como você se sente?", "x")
        ]
    )

    pause 1 

    $ chat_message("wnpep: não estou me sentindo exatamente feliz, por assim dizer, mais tipo")

    pause 2 

    $ chat_message("wnpep: tentando pensar numa boa palavra pra isso")

    # MC: satisfied?
    $ player_choice(
        [
            ("satisfeito?", "x")
        ]
    )

    $ chat_message("wnpep: de certa forma",ot="elimf")

    $ chat_message("elimf: wnpep está sem o pep")

    $ chat_message("incri: para de rimar, idiota")

    $ chat_message("elimf: minha fantasia :^(",ot="odxny")

    $ chat_message("odxny: Tenho certeza que é um pouco estranho finalmente ter acabado.")

    $ chat_message("wnpep: suponho que isso faça parte")

    $ chat_message("wnpep: {image=e_baby}")

    $ player_choice(
        [
            ("vai vir com o tempo!", "day3_34"), 
            ("pensou que seria melhor?", "day3_35")
        ]
    )


    # [1] MC: it'll come in time!
label day3_34: 

    pause 1 

    $ chat_message("wnpep: mm")

    $ chat_message("wnpep: talvez")

    pause 1 

    jump day3_36


    # [2] MC: thought it would feel better?
label day3_35: 
    $ points_seekLove += 1

    $ chat_message("wnpep: talvez um pouco")

    $ chat_message("wnpep: a culpa é minha por não gerenciar minhas expectativas")

    jump day3_36


    # end choices
label day3_36: 

    $ chat_message("odxny: Ajudaria se tomássemos um shot da vitória? Acho que tenho algo que posso usar.")

    $ chat_message("wnpep: agradeço a intenção, mas não, obrigado")

    $ chat_message("wnpep: acho que vou só pegar uma cerveja e sentar um pouco")

    $ chat_message("odxny: Tudo bem.")

    $ chat_message("wnpep: se cuida")

    $ chat_message("wnpep: {image=e_wink}")

    # wnpep offline
    pause 2.0

    $ chat_message("SYSTEM: WNPEP offline") 
    $ wnpep_online = False

    $ chat_message("incri: vc não me ofereceu um shot comemorativo")

    $ chat_message("odxny: Desculpe pelo descuido.")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: mentiroso")

    pause 2 

    $ chat_message("odxny: Você me desvendou.")

    $ chat_message("elimf: jogada de mestre",ot="incri")

    $ chat_message("incri: foda-se vocês todos, vou pegar meu próprio shot")

    $ chat_message("elimf: eu tomo um shot com vc")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: não vou te ajudar a ficar chapado e bêbado")

    $ chat_message("elimf: todos os dias eu sofro um milhão de torturas")

    $ chat_message("odxny: Que vida você leva.")

    $ chat_message("elimf: pois é")

    # dms

    $ chat_message("odxny: Já que o wnpep não está a fim, gostaria de fazer uma chamada? Nenhum shot é necessário.",c="admin")

    $ chat_message("odxny: Podemos comemorar sua participação em dois hacks bem-sucedidos.",c="admin")

    $ player_choice(
        [
            ("topo um brinde!", "day3_37"), 
            ("claro, podemos fazer isso", "day3_38")
        ]
    )


    # [1] MC: id be up for a toast!
label day3_37: 
    $ points_seekLove += 1

    $ chat_message("odxny: Vamos tirar um minuto para pegar nossas bebidas de escolha, então.",c="admin")

    $ chat_message("odxny: Eu ligo assim que encontrar a minha.",c="admin")

    jump day3_39 


    # [2] MC: sure we can do that
label day3_38: 

    $ chat_message("odxny: Certo, deixa eu pegar uma bebida.",c="admin")
    
    jump day3_39


label day3_39: 

    $ chat_message("odxny: Um sexo",c="admin")

    $ player_choice(
        [
            ("caramba. já?", "day3_40"), 
            ("kk", "day3_41")
        ]
    )


label day3_40: 
    $ points_seekLove += 1

    $ chat_message("odxny: O quê?",c="admin") 

    $ player_choice(
        [
            ("poderia, tipo, pelo menos me cobrir de elogios primeiro", "day3_40A"), 
            ("deixa pra lá", "day3_40B")
        ]
    )


label day3_40A: 
    $ points_seekLove += 1

    pause 2 

    $ chat_message("odxny: {image=e_pain}",c="admin")

    $ chat_message("odxny: Um seg*",c="admin") 

    $ chat_message("odxny: Vai se foder kkk",c="admin") 

    $ player_choice(
        [
            ("KKK", "x")
        ]
    )

    jump day3_41


label day3_40B: 

    pause 2 

    $ chat_message("odxny: k",c="admin") 

    jump day3_41


label day3_41: 
    $ wnpep_online = True 

    ## call time 
    jump go_to_call

    $ renpy.pause(hard=True)