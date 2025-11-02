label day4_call: 
    $ first_line = True 
    menu: 
        "Hm? O que foi?":
            pass 
    $ first_line = False 
    pause 1
    show spr o1 side neutral 
    voice "audio/voice/day4/o4-001.ogg"
    o "Desta vez não tem um motivo de verdade. Só senti vontade de ligar."
    show spr o1 neutral 

    play music "audio/music/Reflection_in_the_Blank_Screenlooped.ogg" loop fadein 2.0 fadeout 2.0 
    
    show spr o1 grin 
    voice "audio/voice/day4/o4-002.ogg"
    o "E por que não manter a sequência?"
    show spr o1 smile 

    menu: 
        "Estranho para alguém tão ansioso para ir embora logo. ":
            show spr o1 done 
            voice "audio/voice/day4/o4-003.ogg"
            o "Não force a sorte. "
            show spr o1 eyes closed 
            voice "audio/voice/day4/o4-004.ogg"
            o "Nada mudou. "
            #show spr o1 neutral 
            menu:
                "Certo.":
                    pass
        "Bom ponto. Quer conversar sobre algo, então?":
            $ points_seekLove += 2
            show spr o1 neutral 
            voice "audio/voice/day4/o4-005.ogg"
            o "Ainda não pensei em nada."
            menu: 
                "Então diz a primeira coisa que vier à mente.":
                    pass
    show spr o1 side frown
    voice "audio/voice/day4/o4-006.ogg"
    o "Uhh. Hm."
    show spr o1 neutral 
    voice "audio/voice/day4/o4-007.ogg"
    o "Você fuma?"
    show spr o1 side nervous 
    voice "audio/voice/day4/o4-008.ogg"
    o "Desculpa, a primeira coisa que veio à mente foi o beck da vitória do elimf."
    show spr o1 frown

    menu: 
        "Sim, eu curto de vez em quando.":
            show spr o1 smile 
            voice "audio/voice/day4/o4-009.ogg"
            o "É um jeito divertido de dizer."
            pause 1
            #show spr o1 neutral 
            voice "audio/voice/day4/o4-010.ogg"
            o "Você estava curtindo quando entrou no servidor–"
            menu: 
                "Não.": 
                    pass 
            show spr o1 grin 
            voice "audio/voice/day4/o4-011.ogg"
            o "Desculpa. Tinha que perguntar."
            show spr o1 smile 
            #show spr o1 neutral 
        "Não, não é pra mim.":
            show spr o1 eyes closed
            voice "audio/voice/day4/o4-012.ogg"
            o "Tudo bem. Não é pra todo mundo."
            #show spr o1 neutral 
        "Eu sou mais de comestíveis.":
            voice "audio/voice/day4/o4-013.ogg"
            o "Ah, faz tanta diferença assim?"
            menu: 
                "Sim, não curto a fumaça nem a bagunça.":
                    pass
            show spr o1 eyes closed 
            voice "audio/voice/day4/o4-014.ogg"
            o "Isso é bem prático."
            #show spr o1 neutral 

    menu:
        "E você?":
            pass 
    show spr o1 side frown 
    voice "audio/voice/day4/o4-015.ogg"
    o "Não, eu não fumo. Tentei uma vez e não acrescentou nada."
    show spr o1 eyes closed 
    voice "audio/voice/day4/o4-016.ogg"
    o "O que foi, na verdade, incrivelmente decepcionante. "
    show spr o1 eyes closed 
    voice "audio/voice/day4/o4-017.ogg"
    o "Todos ao meu redor pareciam flutuar facilmente para seus próprios mundinhos. "
    show spr o1 side frown 
    voice "audio/voice/day4/o4-018.ogg"
    o "E lá estava eu. Encarando a parede. "
    menu:
        "Tinha algo de interessante na parede?":
            pass
    show spr o3 neutral 
    voice "audio/voice/day4/o4-019.ogg"
    o "Não. O quê? "
    menu:
        "Sei lá. Tipo uma mancha ou algo assim. ":
            pass
    show spr o3 shocked 
    voice "audio/voice/day4/o4-020.ogg"
    o "Por que diabos isso seria interessante? "
    menu:
        "Você não tem curiosidade por manchas estranhas? ":
            pass
    show spr o1 closed eye happy 
    voice "audio/voice/day4/o4-021.ogg"
    o "Idiota, ha. "
    show spr o1 neutral 
    voice "audio/voice/day4/o4-022.ogg"
    o "Mas, enfim, é mais fácil pra minha carteira não entrar nisso. Sobra mais para o fundo. "
    pause 1
    menu:
        "É... aquele fundo.":
            pass
    voice "audio/voice/day4/o4-023.ogg"
    o "Nós já falamos sobre isso. "
    show spr o1 frown 
    voice "audio/voice/day4/o4-024.ogg"
    o "Eu nem entendo por que você se importa tanto com isso, pra começo de conversa."
    show spr o1 neutral 
    menu:
        "É difícil de acreditar que eu passei a gostar de você em poucos dias?":
            pass
    show spr o1 mad 
    voice "audio/voice/day4/o4-025.ogg"
    o "De um jeito que importe, sim."
    show spr o1 side frown 
    voice "audio/voice/day4/o4-026.ogg"
    o "A gente se diverte, mas não é... sabe..."
    #show spr o1 neutral 
    voice "audio/voice/day4/o4-027.ogg"
    o "Isso deveria ser como nunca mais ver um conhecido querido. Ficar triste por um minuto antes de passar."
    menu: 
        "Eu não penso tão pouco de você.":
            pass 
    show spr o1 mad 
    voice "audio/voice/day4/o4-028.ogg"
    o "Bem- eu não- isso-"
    show spr o2 side scowl 
    voice "audio/voice/day4/o4-029.ogg"
    o "Gah."
    show spr o2 side frown 
    voice "audio/voice/day4/o4-030.ogg"
    o "Eu– não é uma questão de pensar pouco de mim. É apenas um fato."
    show spr o2 sad 
    voice "audio/voice/day4/o4-031.ogg"
    o "É a vida. É normal. Pessoas vêm, pessoas vão."

    menu:
        "Não pra mim. Eu não consigo te esquecer tão facilmente.":
            $ points_seekLove += 2
            show spr o2 scowl 
            voice "audio/voice/day4/o4-032.ogg"
            o "Então–tente!"
            voice "audio/voice/day4/o4-033.ogg"
            o "Você está se sobrecarregando tanto, e pra quê?"
            show spr o2 upset
            voice "audio/voice/day4/o4-034.ogg"
            o "Você não tem nada a ganhar com isso."
            menu:
                "Paz de espírito. Saber que você ainda está por aí.":
                    pass
            #show spr o3 neutral
            voice "audio/voice/day4/o4-035.ogg"
            o "Eu vou viver fora da sociedade, não–"
            show spr o2 sad 
            pause 2
            #show spr o2 sad 
            voice "audio/voice/day4/o4-036.ogg"
            o "Eu não conseguiria ir tão longe. "
            #show spr o1 frown 
        "Pensei que você tinha dito que não era mais uma pessoa. ":
            show spr o2 upset
            pause 1
            #show spr o1 neutral 
            show spr o2 scowl 
            voice "audio/voice/day4/o4-037.ogg"
            o "Você tem razão. Desculpas. Ato falho. "
            show spr o2 side scowl
            voice "audio/voice/day4/o4-038.ogg"
            o "\"Não sou uma pessoa\". Esse sou eu. "
            #show spr o1 neutral 
            voice "audio/voice/day4/o4-039.ogg"
            o "Desperdiçando espaço que seria melhor ocupado por uma pessoa de verdade. "
            #show spr o1 side frown 
            #show spr o2 scowl 
            voice "audio/voice/day4/o4-040.ogg"
            o "Alguém que não pensou o quão melhor tudo seria se simplesmente acabasse."
            #show spr o3 shocked
            voice "audio/voice/day4/o4-041.ogg"
            o "Se eu simplesmente–"
            #show spr o2 sad 
            pause 1
            show spr o2 sad 
            pause 1
            voice "audio/voice/day4/o4-042.ogg"
            o "Mas eu não conseguiria... não faria isso. "

    menu:
        "Você... parece que já pensou nisso.":
            pass
    show spr o2 side frown
    voice "audio/voice/day4/o4-043.ogg"
    o "...Já pensei. Mas não é algo que eu considere mais."
    menu:
        "O que mudou?":
            pass
    pause 2
    #show spr o3 neutral
    show spr o2 sad 
    voice "audio/voice/day4/o4-044.ogg"
    o "Nada. "
    voice "audio/voice/day4/o4-045.ogg"
    o "Absolutamente nada mudou. "
    #show spr o3 eyes closed 
    voice "audio/voice/day4/o4-046.ogg"
    o "Foi só nisso que minha mente se decidiu. "

    menu:
        "Você estava com medo?":
            #show spr o2 side frown 
            show spr o3 eyes closed 
            voice "audio/voice/day4/o4-047.ogg"
            o "Não estava. Isso foi mais prático. "
            show spr o3 shocked
            voice "audio/voice/day4/o4-048.ogg"
            o "Eu não tenho medo de não existir. Não tenho. "
            #show spr o2 upset 
            voice "audio/voice/day4/o4-049.ogg"
            o "Por que eu deveria ter? "
            menu:
                "Ok. ":
                    pass
            #show spr o3 neutral 
            show spr o1 side frown
            voice "audio/voice/day4/o4-050.ogg"
            o "Não tenho. "
        "Por quê?":
            $ points_seekLove += 2
            show spr o2 side frown 
            voice "audio/voice/day4/o4-051.ogg"
            o "Como diabos eu vou saber? "
            voice "audio/voice/day4/o4-052.ogg"
            o "Nada parece fazer sentido mais. "
            show spr o2 upset 
            voice "audio/voice/day4/o4-053.ogg"
            o "Tudo costumava ser tão certo e agora..."
            show spr o2 sad 
            voice "audio/voice/day4/o4-054.ogg"
            o "...Agora eu só estou..."

    pause 2
    show spr o3 neutral 
    #show spr o1 side frown
    voice "audio/voice/day4/o4-055.ogg"
    o "Não interprete mal o que vou dizer, ok?"
    menu:
        "Claro. ":
            pass
    pause 1
    show spr o1 side frown
    pause 1 
    voice "audio/voice/day4/o4-056.ogg"
    o "Como é que alguém consegue recomeçar? "
    voice "audio/voice/day4/o4-057.ogg"
    o "Tudo se foi. Agora sou só eu. Sozinho."
    #show spr o1 side frown 
    voice "audio/voice/day4/o4-058.ogg"
    o "E eu não entendo como isso aconteceu."
    #show spr o1 frown 
    voice "audio/voice/day4/o4-059.ogg"
    o "É como se eu estivesse sufocando enquanto assisto todo mundo respirar ar puro facilmente."
    show spr o1 mad 
    voice "audio/voice/day4/o4-060.ogg"
    o "Então, ou eu posso deixar tudo para trás e aceitar este novo normal, ou... o quê?"
    show spr o1 side frown 
    voice "audio/voice/day4/o4-061.ogg"
    o "Como se faz conexões de verdade? Eu não entendo mais."
    #show spr o1 neutral 

    menu:
        "Não tenho certeza, mas... eu acho que sinto uma conexão com você.":
            $ points_seekLove += 2
            show spr o1 mad 
            voice "audio/voice/day4/o4-062.ogg"
            o "Pare com isso. "
            #show spr o1 neutral 
            voice "audio/voice/day4/o4-063.ogg"
            o "Você sente pena, é isso que você sente."
            menu:
                "Eu me conheço. ":
                    pass
        "Acho que você só tem que tentar. Sair, conversar com as pessoas, tudo isso.":
            show spr o1 mad 
            voice "audio/voice/day4/o4-064.ogg"
            o "\"Sair?\" Você tá falando sério? "
            voice "audio/voice/day4/o4-065.ogg"
            o "Você acha que eu não tentei isso?"
            menu:
                "Não? ":
                    pass

    pause 1
    menu:
        "E aqueles amigos que você mencionou? ":
            pass
    show spr o1 neutral 
    voice "audio/voice/day4/o4-066.ogg"
    o "Que amigos? "
    menu:
        "Aqueles com quem você fumou. ":
            pass
    show spr o1 mad 
    voice "audio/voice/day4/o4-067.ogg"
    o "Eu te disse. Todos se foram. "
    show spr o1 side frown 
    voice "audio/voice/day4/o4-068.ogg"
    o "Eu nem me lembro direito o que aconteceu com eles. "
    #show spr o1 neutral 
    voice "audio/voice/day4/o4-069.ogg"
    o "Não nos falamos há anos. "
    menu:
        "Talvez mandar uma mensagem?":
            pass
    voice "audio/voice/day4/o4-070.ogg"
    show spr o1 mad 
    o "E dizer o quê, exatamente? "
    #show spr o1 eyes closed 
    voice "audio/voice/day4/o4-071.ogg"
    o "Faz anos. Não faria sentido. "
    pause 2
    show spr o1 side frown
    pause 2 
    #show spr o1 neutral 
    voice "audio/voice/day4/o4-073.ogg"
    o "É realmente tão fácil assim para você? "
    menu:
        "Não é. Mas eu ainda tenho que tentar.":
            pass
    show spr o3 shocked 
    voice "audio/voice/day4/o4-074.ogg"
    o "É isso que você está fazendo comigo?"
    menu:
        "O quê?":
            pass
    voice "audio/voice/day4/o4-075.ogg"
    o "Isso é..."
    pause 2
    show spr o3 neutral 
    voice "audio/voice/day4/o4-076.ogg"
    o "Eu tenho trabalho a fazer. "
    show spr o3 eyes closed 
    voice "audio/voice/day4/o4-077.ogg"
    o "Te vejo amanhã. "
    menu:
        "Espera!":
            pass

    ## must run these two lines to swap to next day 
    $ next_day_number = "5"
    jump day_swap

    $ renpy.pause(hard=True)