label day4_start: 

    play music "audio/music/cracking_the_codelooped.ogg" loop fadein 2.0 fadeout 2.0 

    $ chat_message("wnpep: hmm")

    $ chat_message("elimf: ?")

    $ chat_message("wnpep: {image=e_serious}")

    $ chat_message("wnpep: nenhuma resposta ainda")

    $ chat_message("odxny: Tenho certeza que virá em breve. Impossível o time jurídico deles não ter virado a noite.")

    $ chat_message("wnpep: ha. verdade")

    $ player_choice(
        [
            ("acha que eles vão ceder?", "day4_1"), 
            ("de certa forma é uma vantagem - vc sabe que tá fazendo eles suarem", "day4_2")
        ]
    )

    # [1] MC: think theyll cave?
label day4_1: 

    $ chat_message("wnpep: improvável")

    $ chat_message("wnpep: com o dinheiro que eles têm, vão tentar se safar ou ameaçar primeiro")

    $ chat_message("odxny: Provavelmente uma mistura dos dois.")

    jump day4_3 


    # [2] MC: thats a plus in a way- u know youre making em sweat
label day4_2: 
    $ points_seekLove += 1

    $ chat_message("wnpep: {image=e_pain}")

    $ chat_message("wnpep: eu realmente gosto de saber que tô acumulando horas faturáveis pra eles")

    $ chat_message("odxny: Sem falar nas horas extras.")

    $ chat_message("wnpep: quase o suficiente pra compensar o que eles estão fazendo")

    jump day4_3 


    # end choices
label day4_3: 

    $ chat_message("wnpep: se ao menos isso tornasse a espera menos entediante")

    $ chat_message("elimf: a gente sempre pode jogar algo enquanto isso")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("incri: pode apostar tudo que vc tem")

    $ chat_message("incri: eu acabo com a sua raça em qualquer jogo")

    $ chat_message("wnpep: um começo promissor")

    $ chat_message("elimf: que audácia inc :^)")

    $ chat_message("incri: vem")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: cagão")

    pause 0.5

    $ chat_message("SYSTEM: RESPOSTA - ITSSSBAELEY - Não seremos intimidados por ameaças de extorsão. Cessem e desistam, ou esperem uma resposta das autoridades.")

    $ chat_message("elimf: péssima hora incri pois hoje os covardes fazem a festa")

    $ chat_message("wnpep: você não vai ganhar uma parte elimf")

    $ chat_message("elimf: ahh",ot="odxny")

    $ chat_message("odxny: Parece que você vai ter que trabalhar pelo seu jantar, pep.")

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("wnpep: nem ligo. eu esperava resistência")

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("wnpep: então vamos só enviar isso")

    pause 0.5

    $ chat_message("SYSTEM: EXTORSÃO ENVIADA -- ITSSSBAELEY@BAVER.NET")

    $ chat_message("odxny: Acabei de ver. Bela jogada.")

    $ chat_message("wnpep: eles provavelmente vão tentar nos abrir primeiro. uma operação um pouco mais bem financiada que a do bruce")

    $ chat_message("odxny: Justo, vou levantar uma proteção por precaução.")

    pause 1.0

    $ chat_message("SYSTEM: DEFESAS SUPLEMENTARES ATIVADAS")
    $ defenses = True 

    # $ player_choice(
    #     [
    #         ("what just happened??", "x")
    #     ]
    # )

    # $ chat_message("odxny: They're pissed lol. They're trying to attack us back.")

    $ chat_message("elimf: \"defesas suplementares\" o que é isso, o exército")

    $ chat_message("incri: elimf nos EUA")

    $ chat_message("elimf: ???")

    $ chat_message("odxny: Você pode inventar nomes divertidos quando fizer seu próprio servidor.")

    $ chat_message("elimf: vc se convenceria com ARMADURA ANTI-HACK ou TURBOESCUDO")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("odxny: Não.",ot="elimf")

    $ chat_message("elimf: MURALHA MÁGICA DO FODA-SE")

    $ chat_message("incri: gostei dess a")

    $ chat_message("incri: {image=e_letsgo}")

    pause 1.0

    $ chat_message("SYSTEM: RESPOSTA - ITSSSBAELEY - Transferiremos os fundos conforme o acordo estabelecido. Considere este assunto encerrado.")

    play chat "audio/sfx/Casino_Jackpot_001.ogg" loop fadeout 0.2

    # make it rain money??  
    show money_rain onlayer screens
    $ force_scroll_down()

    pause 0.5

    $ chat_message("SYSTEM: PLANO DE PAGAMENTO INICIADO PARA - $ 1.000.000")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("wnpep: agora sim")

    $ chat_message("odxny: Bom trabalho, pep.")

    pause 0.2

    hide money_rain onlayer screens with Dissolve(0.5)
    stop chat fadeout 0.5
    $ force_scroll_down()

    pause 0.5 

    $ defenses = False
    $ defenses_off = True 

    pause 0.5

    $ chat_message("SYSTEM: DEFESAS SUPLEMENTARES DESATIVADAS")
    

    $ chat_message("incri: eu quero uma parte")

    $ chat_message("wnpep: você também não vai ganhar uma parte, inc")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: palhaçada")

    $ chat_message("incri: eu treinei o thrim que te ajudou")

    $ chat_message("odxny: Forçou a barra.")

    $ chat_message("incri: ah qualéee")

    pause 1 

    $ chat_message("elimf:  bem")
    $ defenses_off = False 

    $ chat_message("elimf: é a minha vez de terminar, hein")

    $ chat_message("odxny: Você precisa se apressar em algum momento.")

    $ chat_message("wnpep: ainda dá tempo pra um respeitável terceiro lugar")

    $ chat_message("elimf: ainda no pódio, irado")

    $ chat_message("incri: é o que os perdedores que não ganham ouro dizem")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("elimf: eu tava ocupado")

    $ chat_message("incri: ficar chapado demais pra se mover não conta")

    $ chat_message("elimf: {image=e_baby}")

    $ chat_message("elimf: ok olha",ot="wnpep")

    $ chat_message("wnpep: essa vai ser boa")

    $ chat_message("elimf: eu jurei ficar sóbrio até meu hack terminar")

    $ chat_message("odxny: Muito admirável.",ot="wnpep")

    $ chat_message("wnpep: e quando foi a última vez que você usou, mesmo?")

    $ chat_message("elimf: isso não é importante")

    $ chat_message("elimf: de agora em diante, me absterei da erva do diabo até que esteja feito")

    $ chat_message("elimf: assim digo eu-eth")

    $ chat_message("incri: é assim que vc fica quando não fuma")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: eu odeio")

    $ chat_message("elimf: vc não tá ajudando com a minha sobriedade")

    $ chat_message("wnpep: nada a ver com o assunto, mas eu iniciei um cronômetro")

    $ chat_message("wnpep: {image=e_orz}")

    $ chat_message("elimf: et tu pep")

    $ chat_message("wnpep: não se preocupe, não estarei por perto para cobrar")

    $ chat_message("wnpep: vou sair com a minha filha como prometido")

    $ chat_message("elimf: buuu")

    $ chat_message("elimf: o que eu vou fazer então")

    $ chat_message("wnpep: ensinar algo pro thrim? todo mundo tá fazendo isso")

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: eu não sou do tipo mentor")

    $ player_choice(
        [
            ("por que não acaba com a raça do incri no ensino?", "day4_4"), 
            ("sem pressão!", "day4_5")
        ]
    )


    # [1] MC: why not kick incri's ass at teaching?
label day4_4: 
    $ points_seekLove += 1

    $ chat_message("elimf: ohohoho",ot="incri")

    $ chat_message("incri: até pareceeeeee",ot="elimf",fastmode=True)

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("elimf: isso fica mais tentador a cada segundo")

    jump day4_6


    # [2] MC: no pressure tho!
label day4_5: 

    $ chat_message("elimf: isso parece pressão")

    $ chat_message("elimf: {image=e_serious}")

    # MC: i'm being sincere!!!
    $ player_choice(
        [
            ("estou sendo sincero!!!", "x")
        ]
    )

    $ chat_message("elimf: hmmmmmmmm")

    jump day4_6


    # end choices
label day4_6:

    $ chat_message("wnpep: considere também poder usar o thrim como mão de obra gratuita")

    $ chat_message("elimf: atraente, atraente")

    # MC: i never get a break do i
    $ player_choice(
        [
            ("espera. não desse jeito", "x")
        ]
    )

    $ chat_message("elimf: não se preocupa com pep")

    $ chat_message("elimf: mudando de assunto ")

    $ chat_message("elimf: quer aprender mais um pouco de seekL hoje")

    $ chat_message("elimf: {image=e_heart}")

    # MC: i knew it
    $ player_choice(
        [
            ("eu sabia", "x")
        ]
    )

    $ chat_message("wnpep: acho que vamos ter você pagando suas dívidas até o fim",ot="odxny")

    $ chat_message("odxny: Elimf ensinando? Essa vai ser boa.")

    $ chat_message("elimf: relaxa, tô sóbrio hoje, vai ser moleza")

    $ chat_message("elimf: se você confiar menos em mim do que no incri nisso, acho que vou ter que jogar a toalha")

    # MC: ok fair
    $ player_choice(
        [
            ("eu confio em você. um pouco mais", "x")
        ]
    )


    $ chat_message("incri: o que eu fiz pra merecer isso")

    $ chat_message("elimf: uhhhhhhhhhhhhhhhhh")

    $ chat_message("wnpep: eu adoraria fazer uma lista, mas eu realmente preciso ir agora")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: COVARDE",ot="odxny")

    $ chat_message("odxny: Até mais, pep.")

    $ chat_message("wnpep: boa sorte, thrim")

    $ chat_message("wnpep: {image=e_wink}")

    # MC: uhh thanks!
    $ player_choice(
        [
            ("uhh, valeu!", "x")
        ]
    )

    $ chat_message("elimf: confia em mim pep")

    pause 0.5

    $ chat_message("SYSTEM: WNPEP offline")
    $ wnpep_online = False

    $ chat_message("elimf: isso vai ser ótimo")

    $ chat_message("odxny: Talvez devesse elaborar o que é \"isso\".")

    $ chat_message("elimf: ah sim, claro")


    ## seekl segment 

    $ chat_message("elimf: hoje nós ")

    $ chat_message("elimf: desbravamos as águas úmidas e fedorentas ")

    $ chat_message("elimf: do passado ")

    $ chat_message("odxny: Interessante.")

    $ player_choice(
        [
            ("seu passado? ", "day4_7"), 
            ("por que não o futuro ", "day4_8")
        ]
    )


    # [1] MC: your past? 
label day4_7: 

    $ chat_message("elimf: quem sabe ")

    jump day4_9 


    # [2] MC: why not the future 
label day4_8: 
    $ points_seekLove += 1

    $ chat_message("elimf: deus ")

    $ chat_message("elimf: um passo de cada vez, por favor ")

    jump day4_9 


    # end choices
label day4_9: 

    $ chat_message("incri: onde")

    $ chat_message("elimf: temos que encontrar um garoto muito estúpido, estúpido, estúpido")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: vc está pronto para ser útil de novo, thrim ")

    $ player_choice(
        [
            ("eu não quero muito fazer isso", "day4_10"), 
            ("com certeza, capitão!", "day4_11")
        ]
    )


    # [1] MC: i don't really want to do this 
label day4_10: 

    $ chat_message("elimf: que pena ahaaaaa")

    $ chat_message("incri: vai trabalhar, porra ")

    $ chat_message("incri: {image=e_letsgo}")

    # MC: y'all are so mean to me 
    $ player_choice(
        [
            ("vocês são tão maus comigo", "x")
        ]
    )

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: buá buá buá buá buá ")

    jump day4_12 


    # [2] MC: absolutely captain! 
label day4_11: 
    $ points_seekLove += 1

    $ chat_message("elimf: oooooooo! ",ot="odxny")

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: Quem é o capitão? ")

    $ chat_message("incri: nenhum de vcs é qualificado ")

    $ chat_message("odxny: Ah")

    $ chat_message("elimf: acho que vc é qualificado pra ser capitão, od ")

    $ chat_message("elimf: mas eu sou o capitão agora.")

    $ chat_message("odxny: Não tenho certeza disso. ")

    jump day4_12 


    # end choices
label day4_12:

    $ chat_message("elimf: ok, agora. escutem, crianças ")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: era uma vez um jovem garoto com o rosto sardento")

    $ chat_message("elimf: que desapareceu da terra sem deixar vestígios",ot="incri")

    $ chat_message("incri: {image=e_pain}",ot="elimf")

    $ chat_message("incri: para com isso ",ot="elimf",fastmode=True)

    $ chat_message("elimf: apesar de uma longa caçada")

    $ chat_message("elimf: que não foi tão divertida ")

    $ chat_message("elimf: o mistério continua a ser irritante ")

    pause 1 

    $ chat_message("odxny: Isso não rima. ")

    $ chat_message("elimf: o que ")

    $ chat_message("elimf: eu não estava rimando ")

    pause 1 

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: O que ")

    $ chat_message("elimf: thrim, procure em #irs.contacts# por {color="+color_help+"}\"Darren Horton\"{/color}")
    pause 0.2
    $ hack_notes.append("name: \nDarren Horton")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I23066-809")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_13"

    $ chat_message("elimf: vc vai. entender ")

    # MC: ....ok 
    $ player_choice(
        [
            ("....ok", "x")
        ]
    )

    jump wait_start

    # wait for code 


label day4_13: 
    # MC: why is it all \"NULL\"? 
    $ player_choice(
        [
            ("por que está tudo \"NULO\"? ", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("contact info: \nmissing")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("odxny: Está?? ")

    $ chat_message("odxny: Isso não deveria ser possível. ",ot="elimf")

    $ chat_message("elimf: infelizmente ")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: ainda vagamos pela névoa... ")

    $ chat_message("incri: ah meu deus cala a porra da boca ")

    $ chat_message("incri: você checou as tabelas de óbitos?? ")

    $ chat_message("elimf: claro que chequei as tabelas de óbitos, imbecil ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: duvido ",ot="odxny")

    $ chat_message("odxny: Se ele estivesse nas tabelas de óbitos, ainda estaria nas tabelas de contatos.")

    $ chat_message("odxny: Devem ter tido o registro apagado de alguma forma.")

    # MC: death tables?? 
    $ player_choice(
        [
            ("tabelas de óbitos??", "x")
        ]
    )

    $ chat_message("odxny: Tem muitos dados da Receita Federal aqui agora. Incluindo alguns dados de óbitos.")

    $ chat_message("odxny: Por que não dá uma olhada se estiver curioso? {color="+color_help+"}Procure por \"Darren Horton\" em {/color}#irs.death#")
    pause 0.5
    $ tables_seen.append("irs.death")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")

    $ chat_message("elimf: E AINDA ASSIM VOCÊ NÃO ENCONTRARÁ REGISTRO...")

    $ chat_message("odxny: Kkkk. ")

    # MC: if there's no record... where is this guy? 
    $ player_choice(
        [
            ("não sei. talvez depois", "day4_14"), 
            ("se não há registro... onde está esse cara?", "day4_15")
        ]
    )


label day4_14: 

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: preguiçoso pra caralho")

    $ chat_message("odxny: Quer dizer. Se o elimf já checou...")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: PREGUIÇOSO PRA CARALHO")

    jump day4_16 


label day4_15: 
    $ points_seekLove += 1

    $ chat_message("elimf: não sei...")

    $ chat_message("elimf: mas a caçada continua... devemos continuar caçando...")

    $ chat_message("elimf: {image=e_serious}")

    jump day4_16 


label day4_16:

    $ chat_message("odxny: Você se lembra de mais alguma coisa sobre ele? ")

    $ chat_message("elimf: eu nunca disse que lembrava dessa pessoa ")

    $ chat_message("elimf: ele é simplesmente ")

    $ chat_message("elimf: o passado ",ot="incri")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: não vou ler essa merda agora ")

    pause 0.5

    $ chat_message("SYSTEM: INCRI offline")
    $ incri_online = False

    $ chat_message("elimf: uau")

    $ chat_message("odxny: Ignore, vamos focar. ")

    $ chat_message("elimf: mandão, mandão ")

    $ chat_message("elimf: qual é a pressa ")

    $ chat_message("odxny: Ha ha. ")

    $ player_choice(
        [
            ("tão ansioso pra acabar logo com isso, hein?", "day4_17"), 
            ("escuta o chefe, elimf", "day4_18")
        ]
    )


    # [1] MC: that eager to get this all over with, huh? 
label day4_17: 
    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: Não é isso. ")

    # MC: oh? 
    $ player_choice(
        [
            ("ah é?", "x")
        ]
    )

    $ chat_message("odxny: E também não é isso. ")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: tipo o que")

    $ chat_message("odxny: Nada ")

    jump day4_19 



    # [2] MC: listen to the boss elimf
label day4_18: 
    $ points_seekLove += 1

    $ chat_message("elimf: uau ")

    $ chat_message("elimf: exigente ")

    pause 2

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: seja exigente de novo")

    $ chat_message("odxny: Foco. ")

    $ chat_message("elimf: mds ")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: tô sentindo uma coisa ")

    $ chat_message("odxny: Não, não está. ")

    $ chat_message("elimf: KKK ")

    jump day4_19 



    # end choices
label day4_19: 

    $ chat_message("elimf: agora ")

    $ chat_message("elimf: tem outro fato que sei sobre ele")

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("elimf: ele esteve no sistema de adoção ")

    $ chat_message("elimf: e eu acho que talvez a gente consiga ")

    $ chat_message("elimf: chegar nele por lá ")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: ELIMF MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

    $ chat_message("elimf: #txgov.foster_parents#")
    pause 0.5
    $ tables_seen.append("txgov.foster_parents")
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
        required_runs["idx"] = [("irs_id", "I85863-307")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_23"

    $ chat_message("odxny: Não no Arizona? ")

    $ chat_message("elimf: é, não, eu moro no t")

    pause 2 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: ahhhahahahahahaha")

    $ chat_message("elimf: AHAHAHAAHAHHAHAAAAA HAAAA")

    $ chat_message("elimf: GRRRAAAAAUUUUUGGGGHHHHHHHHHHHHHHHH")

    $ chat_message("odxny: o ",ot="elimf")

    $ chat_message("elimf: RRRRRAAAAAUUUUUGGGHGHGHGHHHGHHHGHGHGHHHHHHHHHH",fastmode=True)

    $ player_choice(
        [
            ("comportamento normal de um texano ", "day4_20"), 
            ("que porra vc tá fazendo ", "day4_21")
        ]
    )


    # [1] MC: normal texan behavior 
label day4_20: 
    $ points_seekLove += 1

    $ chat_message("odxny: KKKKK ",ot="elimf")

    $ chat_message("elimf: EU VOUUUUUUUUUUUUU GGGGRRRARUAUAUAUUAUUGHGGHHHHHHGHH")

    $ chat_message("elimf: RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")

    $ chat_message("elimf: {image=e_letsgo}")

    jump day4_odm_1 


    # [2] MC: tf r you doing 
label day4_21: 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: a futilidade de. tudo ")

    $ chat_message("elimf: tudo que temos de mais precioso")

    $ chat_message("elimf: desaparece ")

    $ chat_message("elimf: apesar de como nós")

    $ chat_message("elimf: seguramos loucamente")

    pause 1 

    # MC: what 
    $ player_choice(
        [
            ("o que", "x")
        ]
    )

    jump day4_odm_1 

label day4_odm_1: 

    $ chat_message("odxny: Bem, isso está se tornando uma aventura.", c="admin")

    $ chat_message("odxny: elimf foi só metade disso de irritante nos outros hacks.", c="admin")

    $ chat_message("odxny: {image=e_pain}", c="admin")

    #MC: looks like this is smth personal for them
    $ player_choice(
        [
            ("parece que isso é algo pessoal pra ele", "x")
        ]
    )

    $ chat_message("odxny: Muito provável. A tendência de hacks de vingança parece continuar também.", c="admin")

    $ player_choice(
        [
            ("seu último hack também vai ser uma coisa de vingança?", "day4_odm_2"), 
            ("vocês todos entraram no hacking por motivos pessoais?", "day4_odm_3")
        ]
    )


    #[1] MC: is your last hack also going to be a revenge thing?
label day4_odm_2: 

    $ chat_message("odxny: Não, nada disso kkkk.", c="admin")

    $ chat_message("odxny: Tenho certeza que vão me vaiar por quebrar a sequência.", c="admin")

    jump day4_odm_4


    #[2] MC: did you guys all get into hacking for personal reasons?
label day4_odm_3:
    $ points_seekLove += 1

    $ chat_message("odxny: Não sei os motivos de todo mundo. Poderia adivinhar se tivesse que pensar sobre isso.", c="admin")

    $ chat_message("odxny: O do Incri parece o mais transparente - vingança mesquinha, possivelmente tédio.", c="admin")

    jump day4_odm_4


    # end choices
label day4_odm_4: 

    #MC: what are your reasons for getting into hacking then?
    $ player_choice(
        [
            ("quais são os seus motivos para entrar no hacking, então?", "x")
        ]
    )

    $ chat_message("odxny: Ah. Isso.", c="admin")

    $ chat_message("odxny: {image=e_serious}", c="admin")

    $ chat_message("odxny: Eu encontrei alguns fóruns de hacking no início dos meus dias de programação, e meio que caí de paraquedas nisso.", c="admin")

    $ chat_message("odxny: Era principalmente exercícios e hackathons. Depois se provou útil para o fundo.", c="admin")

    #MC: That's practical.
    $ player_choice(
        [
            ("Isso é prático.", "x")
        ]
    )

    $ chat_message("odxny: E sem surpresas, imagino.", c="admin")

    $ chat_message("odxny: Vamos voltar ao assunto. Sem a gente, o elimf vai despencar de um penhasco.", c="admin")

    jump day4_22



    # end choices
label day4_22: 

    pause 2 

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("elimf: ok, voltei à forma humana")

    $ chat_message("odxny: Bem-vindo de volta. ",ot="elimf")

    $ chat_message("elimf: por favor, {color="+color_help+"}dê uma olhada na tabela de adoção para nosso jovem adotado{/color} ")

    $ chat_message("elimf: e {color="+color_help+"}me traga o email do responsável{/color}... por favor.... da nossa tabela de contatos favorita....") 

    $ chat_message("elimf: {image=e_serious}")

    $ chat_message("odxny: Você pode resolver isso com {color="+color_help+"}um join ou uma cláusula where{/color}. Você que sabe.")

    $ chat_message("elimf: VAI") 

    # wait for code

    jump wait_start 


label day4_23: 

    # MC: I've got it -- kenneth.stafford@copmail.com, fostered Darren in 2002 
    $ player_choice(
        [
            ("Achei -- kenneth.stafford@copmail.com, foi pai adotivo do Darren em 2002", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("foster parent: \nKenneth Stafford")
    $ hack_notes.append("foster email: \nkenneth.stafford\n@copmail.com")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("odxny: Mirando muito na polícia ultimamente.")

    # MC: is that a bad thing? 
    $ player_choice(
        [
            ("isso é ruim?", "x")
        ]
    )
    $ chat_message("odxny: {image=e_baby}")

    $ chat_message("odxny: Não.... mas isso atrai mais atenção pra gente. ")

    # MC: oh. that's probably not good 
    $ player_choice(
        [
            ("ah. isso provavelmente não é bom", "x")
        ]
    )

    $ chat_message("elimf: relaxa, a gente já tá quase acabando com isso tudo mesmo, né ")

    $ chat_message("odxny: Verdade. ")

    $ chat_message("elimf: ok hora de PEGAR ")

    $ chat_message("elimf: UMA INFO ")

    $ chat_message("elimf: {image=e_letsgo}")

    pause 0.5

    $ chat_message("SYSTEM: EXTORSÃO ENVIADA - KENNETH.STAFFORD@COPMAIL.COM ")

    $ chat_message("elimf: OHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH ")

    pause 0.5

    $ chat_message("SYSTEM: FALHA NA EXTORSÃO - CONTATO INVÁLIDO ")

    $ chat_message("elimf: O QUE ")

    $ chat_message("elimf: {image=e_crying}")

    $ chat_message("elimf: MSUJGHUIHUOH???? ",ot="odxny")

    $ chat_message("odxny: ....Não estou acostumado com os dados da Receita Federal estarem tão errados. ")

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: Tem certeza que esse era o email certo, thrim? ")

    $ player_choice(
        [
            ("era o único email que tinha lá", "day4_24"), 
            ("quer dizer... não tenho certeza. acho que era esse ", "day4_25")
        ]
    )


    #$ [1] MC: that was the only email there 
label day4_24: 
    $ points_seekLove += 1

    $ chat_message("odxny: Entendi.") 

    jump day4_26


    # [2] MC: i mean... i'm not sure. i think that was it 
label day4_25: 

    $ chat_message("odxny: Hm.") 
    
    jump day4_26


    # end choices 
label day4_26:

    # MC: maybe they're dead...? 
    $ player_choice(
        [
            ("talvez ele esteja morto...?", "x")
        ]
    )

    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["full_name"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.death"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("d_no", "D68141-771")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_27"

    $ chat_message("odxny: O Kenneth? ")

    $ chat_message("odxny: Vale a pena checar, eu acho. ",ot="elimf")

    $ chat_message("elimf: devastador se for verdade..... ")

    $ chat_message("elimf: {image=e_baby}")

    $ chat_message("elimf: thrim... você pode.... {color="+color_help+"}por favor, procurar pelo kenneth{/color}.... ")

    $ chat_message("elimf: #irs.death#.......... ")

    # MC: lol ok 
    $ player_choice(
        [
            ("lol ok", "x")
        ]
    )

    jump wait_start 
    

    # wait for code 


label day4_27:
    pause 0.2
    $ hack_notes.append("kenneth status: \ndead af")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    # MC: .......... uh. Kenneth is in here. 
    $ player_choice(
        [
            (".......... uh. O Kenneth está aqui.", "day4_28"), 
            ("boas notícias! o kenneth vive", "day4_29")
        ]
    )


label day4_28: 

    pause 1 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: por favor me imagine caído sobre minhas delicadas mãos e joelhos")

    $ chat_message("elimf: uma lágrima pingando no chão ")

    jump day4_30 


label day4_29: 
    $ points_seekLove += 1

    $ chat_message("odxny: ?? Isso não é...",ot="elimf")

    $ chat_message("elimf: oh UFA",fastmode=True)

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: ok, posso respirar de novo")

    $ player_choice(
        [
            ("vive na vida após a morte", "x")
        ]
    )

    pause 2

    $ chat_message("elimf: {image=e_pain}") 

    $ chat_message("elimf: HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")

    $ chat_message("odxny: Esperto.")

    jump day4_30



label day4_30: 

    # MC: but there is a living contact listed here. Elsie Patrick
    $ player_choice(
        [
            ("mas tem um contato vivo listado aqui. Elsie Patrick", "x")
        ]
    )
    pause 0.2
    $ hack_notes.append("death contact: \nElsie Patrick")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("elimf: VIVA")

    pause 2 

    $ chat_message("elimf: PORRA EU BATI MINHA CABEÇA ")

    $ chat_message("odxny: KKKKK")

    pause 0.5

    $ chat_message("SYSTEM: INCRI online") 
    $ incri_online = True

    $ chat_message("incri: sinto que alguém tá se ferrando ")

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: quem ")

    $ chat_message("odxny: elimf com certeza ")

    $ chat_message("incri: bom ",ot="elimf")

    $ chat_message("elimf: pare")

    $ chat_message("elimf: thrim")

    $ chat_message("elimf: {color="+color_help+"}por favor, me arranja o email daquele contato{/color}")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = ["email"]
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["irs.contacts"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("irs_id", "I73094-157")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_31"

    $ chat_message("incri: lol thrim vc ainda tá sendo o cachorrinho desse idiota ")

    $ chat_message("odxny: O Thrim ajuda muito, sabe.")

    $ chat_message("incri: vergonha alheia")

    jump day4_odm2_1


    ## odm part 2 
label day4_odm2_1: 

    $ chat_message("odxny: Alinhei minha lista de compras para amanhã, mas sinto que estou esquecendo algo.",c="admin")

    #MC: like what?
    $ player_choice(
        [
            ("tipo o que?", "x")
        ]
    )

    $ chat_message("odxny: Não sei. Verifiquei meus suprimentos três vezes.",c="admin")

    $ chat_message("odxny: É só uma sensação vaga e incômoda. ",c="admin")

    $ player_choice(
        [
            ("está com dúvidas?", "day4_odm2_2"), 
            ("talvez vc precise de algo divertido?", "day4_odm2_3")
        ]
    )


    #[1] MC: having second thoughts?
label day4_odm2_2: 
    $ points_seekLove += 1

    $ chat_message("odxny: Não. Nada disso.",c="admin")

    #MC: okay
    $ player_choice(
        [
            ("ok", "x")
        ]
    )

    $ chat_message("odxny: Vai acontecer.",c="admin")

    jump day4_odm2_4


    #[2] MC: maybe u need something fun?
label day4_odm2_3: 

    $ chat_message("odxny: O quê?",c="admin")

    #MC: u know, to keep u entertained
    $ player_choice(
        [
            ("sabe, pra te manter entretido", "x")
        ]
    )

    $ chat_message("odxny: Eu já vou estar bem ocupado. Dá muito trabalho viver fora da civilização.",c="admin")

    jump day4_odm2_4


    # end choices
label day4_odm2_4:

    $ chat_message("odxny: Isso não está ajudando. Preciso revisar tudo de novo.",c="admin")

    #MC: then why message me?
    $ player_choice(
        [
            ("então por que me mandou mensagem?", "x")
        ]
    )

    $ chat_message("odxny: Porque",c="admin")

    pause 2

    $ chat_message("odxny: Eu não sei.",c="admin")

    $ chat_message("odxny: Força do hábito?",c="admin")

    pause 2

    $ chat_message("odxny: Eu não sei.",c="admin")

    #MC: are you ... sure you want to do this?
    $ player_choice(
        [
            ("você tem... certeza que quer fazer isso?", "x")
        ]
    )

    $ chat_message("odxny: Sim. Talvez. Sim.",c="admin")

    $ chat_message("odxny: É só nervosismo de última hora. Ansiedade de viagem.",c="admin")

    #$ chat_message("odxny: Dealing with the finality.",c="admin")

    #MC: u dont sound convinced
    $ player_choice(
        [
            ("você não parece convencido", "x")
        ]
    )

    $ chat_message("odxny: Eu estou. Provavelmente só preciso dormir um pouco para pensar melhor.",c="admin")

    #MC: i suppose so
    $ player_choice(
        [
            ("acho que sim", "x")
        ]
    )

    $ chat_message("odxny: Agora você não está convencido.",c="admin")

    #MC: i cant claim to be
    $ player_choice(
        [
            ("não posso dizer que estou", "x")
        ]
    )

    $ chat_message("odxny: Acho que não posso discordar disso.",c="admin")

    $ chat_message("odxny: Vou pensar sobre isso. Temos um pouco mais de tempo - ainda falta terminar o meu hack.",c="admin")

    #MC: i'll be here
    $ player_choice(
        [
            ("estarei aqui", "x")
        ]
    )

    $ chat_message("odxny: Supondo que o elimf não enlouqueça de esperar e te mate.",c="admin")

    #MC: LOL
    $ player_choice(
        [
            ("KKK", "x")
        ]
    )


    $ chat_message("elimf: por favor, thrim. {color="+color_help+"}por favor, encontre o email da elsie patrick para mim{/color}")

    # wait for code 

    jump wait_start 


label day4_31: 

    # MC: here you go -- elsie.patrick@copmail.com
    $ player_choice(
        [
            ("aqui está -- elsie.patrick@copmail.com", "x")
        ]
    )

    pause 0.2
    $ hack_notes.append("elsie email: \nelsie.patrick\n@copmail.com")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ chat_message("odxny: Ainda outro policial. ")

    $ chat_message("elimf: ei, pelo menos o último estava morto ")

    $ chat_message("incri: {image=e_letsgo}")

    $ chat_message("incri: policiais mortos???? ",ot="elimf")

    $ chat_message("elimf: HORA DO EMAIL ")

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: OHHHHHHHHHHHHHHHHH")

    pause 0.5

    $ chat_message("SYSTEM: EXTORSÃO ENVIADA - ELSIE.PATRICK@COPMAIL.COM ")

    # MC: are u actually like extorting all these people lol 
    $ player_choice(
        [
            ("vocês estão mesmo extorquindo toda essa gente lol ", "x")
        ]
    )

    $ chat_message("elimf: não não não")

    $ chat_message("elimf: só envia isso sempre que mandamos emails desse serviço lol ")

    $ chat_message("elimf: quer tentar enviar algo? ")

    $ chat_message("elimf: {image=e_orz}")

    # MC: oh? 
    $ player_choice(
        [
            ("oh? ", "x")
        ]
    )

    $ chat_message("elimf: rode isso no seu console ")

    $ chat_message("elimf: `exec out('elsie.patrick@copmail.com')`")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # IF EXEC, WHAT NEEDS TO BE EXEC 
        exec_needed = ["out", "elsie.patrick@copmail.com"]
        exec_condition = ["day4_32", "day4_33"]
        # WHAT COLUMNS THEY NEED TO SEE
        required_runs["columns"] = None 
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = None
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = None
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_32"

        # make it jump this time to a diff new label depending on if you sent it to the right email or not 

    pause 0.2
    $ hack_notes.append("new function: \nout('email')")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    $ func_access_email = True 

    $ chat_message("odxny: ...Concedi a você acesso à função, Thrim.")

    $ chat_message("elimf: {color="+color_syntax+"}EXEC{/color} executa uma função pré-construída específica, e a função que estamos usando hoje se chama \"out\"")

    $ chat_message("elimf: essa função apenas envia tipo. uma mensagem assustadora padrão para qualquer email que você colocar aí")

    $ chat_message("odxny: Sinto que uma mensagem adicional vai diminuir o impacto do que você acabou de enviar. ")

    $ chat_message("elimf: eu acho que vai realçar ")

    $ chat_message("elimf: {image=e_orz}")

    $ player_choice(
        [
            ("se o od acha que é uma má ideia... ", "day4_31_A"), 
            ("relaxa od. vc tá pensando demais", "day4_31_B")
        ]
    )


label day4_31_A: 
    $ points_seekLove += 1

    $ chat_message("odxny: Quer dizer, você pode... não sei. Depende do elimf. O hack é dele.")

    $ chat_message("elimf: vlw. vc provs tá certo mas. KKKK")

    $ chat_message("odxny: Kkkk",ot="elimf")

    $ chat_message("elimf: {color="+color_help+"}manda ver, thrimmy{/color}")

    jump wait_start


label day4_31_B: 

    $ chat_message("odxny: k",ot="elimf")

    $ chat_message("elimf: vai lá, thrim, {color="+color_help+"}MANDA VER{/color}")

    # wait for code 

    jump wait_start


label day4_32: 

    $ chat_message("odxny: Que loucura kkkk ",ot="incri")

    $ chat_message("incri: vc faz parte disso agora")

    $ chat_message("incri: chantagista ")

    $ chat_message("incri: {image=e_crying}")

    # MC: omg does this mean u accept me 
    $ player_choice(
        [
            ("mds isso significa que vc me aceita ", "x")
        ]
    )

    $ chat_message("incri: {image=e_pain}")

    $ chat_message("incri: até parece ")

    jump day4_34 


label day4_33: 

    $ chat_message("odxny: Espera, qual foi aquele email?",ot="incri,elimf")

    $ chat_message("incri: KKKK??? THRIM???",ot="elimf",fastmode=True)

    $ chat_message("elimf: mds thrim o que você fez",fastmode=True)

    # MC: I THOUGHT YOU SAID IT WAS JUST A GENERIC EMAIL 
    $ player_choice(
        [
            ("EU PENSEI QUE VOCÊ TINHA DITO QUE ERA SÓ UM EMAIL GENÉRICO", "x")
        ]
    )

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: um email genérico muito ASSUSTADOR",ot="incri")

    $ chat_message("incri: HAHAHAHAHAHA",ot="odxny",fastmode=True)

    $ chat_message("odxny: Thrim...")

    $ chat_message("odxny: {image=e_baby}")

    jump day4_34 


label day4_34: 

    pause 0.5

    $ chat_message("SYSTEM: RESPOSTA - ELSIE.PATRICK - ??? Nunca ouvi falar de Darren. Kenneth não adotou ninguém. Vão embora. ")

    $ chat_message("elimf: MENTIROSA VOCÊ ESTÁ MENTINDOOOO MENTIROSA MENTIROSA ")

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: HORA DE USAR A ARTILHARIA PESADA ")

    # MC: ? 
    $ player_choice(
        [
            ("?", "x")
        ]
    )

    $ chat_message("elimf: o arquivo de emails") 

    $ chat_message("odxny: Ohhhhh")

    # MC: what's the email archive 
    $ player_choice(
        [
            ("o que é o arquivo de emails?", "x")
        ]
    )

    $ chat_message("odxny: Às vezes conseguimos pequenas janelas de acesso a bancos de dados enormes cheios de emails enviados e recebidos ")

    $ chat_message("odxny: Usamos isso para dar uma olhada e pegar o máximo de emails que conseguimos, mas ")

    $ chat_message("odxny: É um pouco limitado. ",ot="elimf")

    $ chat_message("elimf: bem-vindo ao glorioso mundo de #emails.content#")

    $ chat_message("elimf: {image=e_sparkle}")

    pause 0.5
    $ tables_seen.append("emails.content")
    play sound "audio/sfx/message_notification_01_002 new table.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_table_pos
    $ renpy.notify("LISTA DE TABELAS ATUALIZADA")
    ## SET REQUIREMENTS TO PROGRESS 
    python: 
        # WHAT COLUMNS THEY NEED TO SEE
        exec_needed = None 
        required_runs["columns"] = None
        # WHAT TABLES THEY NEED TO ENTER 
        required_runs["tables"] = ["emails.content"]
        # WHAT IDS MUST APPEAR 
        required_runs["idx"] = [("email_id", "X66352")]
        # STOP THEM BEFORE THEY GET TOO FAR 
        player_can_pass = False 
        waiting_label = "day4_35"

    $ chat_message("elimf: sinto cheiro de sorte hoje à noite ")

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: procure, thrim, procure ")

    $ chat_message("elimf: {color="+color_help+"}procure o email da elsie aí!!!!!!{/color}")

    $ chat_message("odxny: {color="+color_help+"}A coluna de email não se chama 'email' desta vez{/color}, então você não conseguirá usar join. Use um {color="+color_syntax+"}WHERE{/color} sozinho.")

    $ chat_message("odxny: Só um aviso. Desculpe.")

    $ chat_message("odxny: Essa tabela se fodeu de alguma forma na varredura.")

    # wait for code 

    jump wait_start


label day4_35: 

    $ chat_message("odxny: KKKK como você é tão sortudo, eli")

    
    $ player_choice(
        [
            ("sortudo como??", "day4_36"), 
            ("vc também tá vendo isso lol?", "day4_37")
        ]
    )


label day4_36: 

    $ chat_message("odxny: Olha a coluna de conteúdo lol ")

    jump day4_38 


label day4_37: 
    $ points_seekLove += 1

    $ chat_message("odxny: Sim lol. ")

    $ chat_message("odxny: {image=e_pain}")

    $ chat_message("odxny: Tão estúpido pra caralho lol ")

    jump day4_38 

 
label day4_38: 

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: SIM? ")

    $ chat_message("odxny: Muitos emails com o assunto \"RE: DARREN HORTON\" ")

    $ chat_message("elimf: E? ")

    $ chat_message("odxny: Quer deixar pro thrim? ")

    $ player_choice(
        [
            ("ah não, manda ver!", "day4_39"), 
            ("se você não se importa", "day4_40")
        ]
    )


    # [1] MC: oh no, go for it! 
label day4_39: 
    $ points_seekLove += 1

    $ chat_message("odxny: Valeu.")

    # MC: having fun, huh?
    $ player_choice(
        [
            ("se divertindo, hein?", "x")
        ]
    )

    $ chat_message("odxny: Você é engraçado. ") 

    $ chat_message("odxny: É \"fdhj398fh@notmail.com\" ") 

    jump day4_41


    # [2] MC: if u don't mind
label day4_40: 

    $ chat_message("odxny: O palco é seu. ") 

    # MC: "fdhj398fh@notmail.com" 
    $ player_choice(
        [
            ("\"fdhj398fh@notmail.com\"", "x")
        ]
    )

    jump day4_41


    # end choices 
label day4_41: 
    pause 0.2
    $ hack_notes.append("darren email: \nfdhj398fh\n@notmail.com")
    play sound "audio/sfx/message_notification_01_003 new info.ogg"
    # show highlight_small onlayer screens: 
    #     pos highlight_tab_info_pos
    $ renpy.notify("ABA DE INFORMAÇÕES ATUALIZADA")
    pause 0.5

    pause 2 

    $ chat_message("elimf: todo esse tempo... ele esteve se escondendo do mundo...") 

    $ chat_message("elimf: este jovem garoto... finalmente encontrado... deus abençoe... deus abençoe.... ")

    $ chat_message("odxny: E você disse que não conhecia essa pessoa? ")

    $ chat_message("elimf: bem, eu conheço ")

    $ chat_message("elimf: algo que ele já foi ")

    $ chat_message("elimf: um jovem em um parque ")

    $ chat_message("elimf: sorrindo ")

    $ chat_message("elimf: transbordando de ")

    $ chat_message("elimf: esperança ",ot="incri")

    $ chat_message("incri: vou sair de novo, juro por deus ",ot="elimf")

    $ chat_message("elimf: um jovem que ",fastmode=True)

    $ chat_message("elimf: que por acaso perdeu ")

    $ chat_message("elimf: uma aposta ")

    $ chat_message("elimf: e essa aposta tinha ")

    $ chat_message("elimf: JUROS INCLUÍDOS",ot="incri")

    $ chat_message("elimf: {image=e_letsgo}",ot="incri")

    $ chat_message("incri: espera KKKK",ot="elimf")

    $ chat_message("elimf: E EMBORA ELE ESTEJA TENTANDO SE ESCONDER ")

    $ chat_message("elimf: ELE NÃO PODE SE ESCONDER DO OLHO QUE TUDO VÊ DA ")

    $ chat_message("elimf: GANÂNCIA MESQUINHA ")

    pause 0.5

    $ chat_message("SYSTEM: EXTORSÃO ENVIADA - FDHJ398FH@NOTMAIL.COM ")

    $ player_choice(
        [
            ("mds você acabou de extorquir alguém por causa de uma aposta de infância", "day4_42"), 
            ("ele estava se escondendo??? de você?????", "day4_43")
        ]
    )

    
    # [1] MC: omg did you just extort someone over a childhood bet 
label day4_42: 
    $ points_seekLove += 1

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: ELES PODEM CORRER, MAS NÃO PODEM SE ESCONDER ",ot="odxny")

    $ chat_message("odxny: Vejo que a amizade significava muito pra você.") 

    $ chat_message("elimf: não somos nada sem nossos princípios ")

    $ chat_message("elimf: {image=e_orz}")

    $ chat_message("elimf: deus, onde caralhos está o wnpep quando eu preciso dele ")

    jump day4_44 


    # [2] MC: they were in hiding??? from you????? 
label day4_43: 

    $ chat_message("elimf: uma perda de tempo, CONCORDO ")

    $ chat_message("elimf: isso era inevitável ",ot="incri")

    $ chat_message("incri: puta merda VAMOOOOOOOOOOOOOOOO")

    $ chat_message("incri: FINAL DO CARALHO, ELI ")

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("elimf: obrigado inc <3 ")

    python: 
        renpy.pause(0.5)
        chat_message("SYSTEM: INCRI MANDA A BUZINA")
        renpy.play(horn_sound, channel="honk")
        renpy.pause(0.5)

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

    jump day4_44 


    # end choices 
label day4_44: 

    pause 0.5

    $ chat_message("SYSTEM: WNPEP online")
    $ wnpep_online = True

    $ chat_message("wnpep: beleza! estou de volta! ")

    $ chat_message("wnpep: {image=e_wink}")

    $ chat_message("wnpep: como foi? ")

    # MC: um. elimf had a productive extortion 
    $ player_choice(
        [
            ("hum. o elimf teve uma extorsão produtiva ", "x")
        ]
    )

    $ chat_message("elimf: estou tão zen agora ")

    $ chat_message("elimf: vou. forrar a grana")

    pause 1.0

    $ chat_message("SYSTEM: RESPOSTA - Ok. Foda-se você. Eu te odeio pra caralho. Eu vou te achar, seu monte de merda. Pega a porra do seu dinheiro. Cansei de lidar com você. ")

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("elimf: WOOOOOOO ",ot="wnpep")

    $ chat_message("wnpep: que porra é essa ")

    play chat "audio/sfx/Casino_Jackpot_001.ogg" loop fadeout 0.2

    # make it rain money??  
    show money_rain onlayer screens
    $ force_scroll_down()

    pause 0.5

    $ chat_message("SYSTEM: PLANO DE PAGAMENTO INICIADO PARA - $ 1.253.390 ")

    $ chat_message("incri: QUE PORRA É ISSO, É TUDO JUROS??? ")

    $ chat_message("incri: {image=e_crying}")

    $ chat_message("elimf: eu sou ")

    $ chat_message("elimf: o melhor em fazer acordos ")

    pause 0.2

    hide money_rain onlayer screens with Dissolve(0.5)
    stop chat fadeout 0.5
    $ force_scroll_down()

    pause 0.5 

    $ chat_message("wnpep: caramba ",ot="odxny")

    $ chat_message("odxny: Uma parte? ")

    $ chat_message("elimf: merda, pode ficar com tipo")

    $ chat_message("elimf: metade ")

    $ chat_message("odxny: Tem certeza?? ")

    $ chat_message("elimf: cara, a vitória moral foi tipo. a coisa mais importante ")

    $ chat_message("elimf: obrigado, thrim. não conseguiria ter feito isso sem você. ")

    $ chat_message("elimf: {image=e_orz}")

    # MC: ur welcome????? omg
    $ player_choice(
        [
            ("de nada????? mds", "x")
        ]
    )


    $ chat_message("elimf: excelente")

    $ chat_message("elimf: isso pede um baseado da vitória")

    $ chat_message("elimf: {image=e_heart}")

    $ chat_message("wnpep: não aguentou um dia de sobriedade?")

    $ chat_message("elimf: eu só estava surfando em uma onda diferente")

    $ chat_message("elimf: de vingança justa")

    $ chat_message("elimf: de VITÓRIA IMINENTE",ot="wnpep")

    $ chat_message("elimf: {image=e_letsgo}")

    $ chat_message("wnpep: tá bom, tá bom",ot="odxny")

    $ chat_message("odxny: Eu diria que você mereceu seu baseado.")

    $ chat_message("elimf: com certeza")

    # MC: what a texan thing to say
    $ player_choice(
        [
            ("que coisa bem texana de se dizer", "x")
        ]
    )

    pause 1 

    $ chat_message("elimf: {image=e_pain}")

    $ chat_message("elimf: UUUUUUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") 

    pause 0.5

    $ chat_message("SYSTEM: ELIMF offline")
    $ elimf_online = False

    $ chat_message("wnpep: ???????")

    $ chat_message("odxny: Não se preocupe com isso.")

    $ chat_message("odxny: Topa uma chamada agora?",c="admin")

    # MC: o sure, go ahead
    $ player_choice(
        [
            ("ah claro, pode ligar", "x")
        ]
    )

    ## call time 
    $ elimf_online = True
    jump go_to_call

    $ renpy.pause(hard=True)