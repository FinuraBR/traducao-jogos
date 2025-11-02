label day1_call: 

    voice "audio/voice/day1/o1-001.ogg"
    o "Pronto."

    play music "audio/music/little_hand_on_the_clocklooped.ogg" loop fadein 2.0 fadeout 2.0 

    menu: 
        "Sabe, para alguém preocupado com segurança, essa é uma atitude meio estranha.": 
            pass 

    voice "audio/voice/day1/o1-002.ogg"
    o "O quê, a ligação?"

    show spr o1 eyes closed 
    voice "audio/voice/day1/o1-003.ogg"
    o "Isto é mais seguro que o servidor, e ele já é trancado a sete chaves."
    #show spr o1 neutral 
    menu: 
        "Sua falta de preocupação me deixa apreensivo.": 
            pass

    show spr o1 frown
    voice "audio/voice/day1/o1-004.ogg"
    o "Não tenho medo de uma chamada rápida como esta. E o pequeno risco vale a pena para investigar um maior."

    menu: 
        "Eu estou parecendo um risco maior?": 
            pass 

    show spr o1 neutral 
    voice "audio/voice/day1/o1-005.ogg"
    o "Indeterminado."

    menu: 
        "Eu não sou de ficar falando por aí sobre minhas atividades não tão legais.": 
            pass

    show spr o1 done
    voice "audio/voice/day1/o1-006.ogg"
    o "Entendo."
    #show spr o1 neutral 

    menu: 
        "Então…?": 
            pass 

    show spr o1 done
    voice "audio/voice/day1/o1-007.ogg"
    o "Então nada. Isso foi só para ver quem você é."
    #show spr o1 neutral 

    menu: 
        "Talvez eu devesse ter me arrumado melhor, então.":

            show spr o1 mad 
            voice "audio/voice/day1/o1-008.ogg"
            o "Isso não é uma entrevista de emprego."

            menu:
                "Verdade, mas a regra do \"vista-se para impressionar\" ainda vale.": 
                    pass

            show spr o1 done
            voice "audio/voice/day1/o1-009.ogg"
            o "Talvez fosse bom para você estabelecer metas mais atingíveis."
            #show spr o1 neutral 

        "Qual a sua impressão? Perigoso? Útil? Sedutor?":
            $ points_seekLove += 2

            show spr o1 done frown 
            voice "audio/voice/day1/o1-010.ogg"
            o "Uma dessas opções foi notavelmente diferente."

            menu: 
                "Eu tenho que avaliar todas as possibilidades.": 
                    pass

            show spr o1 done 
            voice "audio/voice/day1/o1-011.ogg"
            o "Note a raiz da palavra \"possível\"."
            #show spr o1 neutral 


    menu:
        "Ai, essa doeu. Anotado.":
            pass

    show spr o1 eyes closed 
    voice "audio/voice/day1/o1-012.ogg"
    o "...Me desculpe. A intenção desta chamada não era te insultar."

    show spr o1 neutral
    voice "audio/voice/day1/o1-013.ogg"
    o "Eu queria mais ouvir sobre seus métodos. Como você trabalha."

    menu: 
        "Eu, uhm. Você não pode rir disso.": 
            pass 

    show spr o1 frown 
    voice "audio/voice/day1/o1-014.ogg"
    o "Muito promissor."

    menu: 
        "Na verdade, eu programo principalmente com linguagens esotéricas.": 
            pass

    show spr o1 done
    voice "audio/voice/day1/o1-015.ogg"
    o "Esotéricas... Não sei o que isso significa." 

    show spr o3 neutral parted 
    voice "audio/voice/day1/o1-016.ogg"
    o "Pesquisando." 
    show spr o3 neutral

    pause 2 

    show spr o3 neutral parted
    voice "audio/voice/day1/o1-017.ogg"
    o "Isso é uma piada?"
    #show spr o1 neutral

    menu: 
        "Estou falando totalmente sério.": 
            pass 

    show spr o3 shocked 
    voice "audio/voice/day1/o1-018.ogg"
    o "...\"projetadas para testar os limites do design de linguagens de programação, como prova de conceito, como arte de software, como uma interface de hacking para outra linguagem, ou como uma piada.\""

    show spr o1 closed eye happy  
    voice "audio/voice/day1/o1-019.ogg"
    o "\"Arte de software.\" Ha. Engraçado."

    show spr o1 happy
    voice "audio/voice/day1/o1-020.ogg"
    o "Qual dessas é a sua razão?" 

    menu: 
        "...Vai ficar óbvio quando eu disser a linguagem que eu uso.": 
            pass 

    show spr o1 neutral 
    voice "audio/voice/day1/o1-021.ogg"
    o "Que é...?" 

    menu: 
        "ArnoldC, ultimamente.": 
            pass 

    show spr o1 done
    voice "audio/voice/day1/o1-022.ogg"
    o "O que ela tem de especial?" 


    menu: 
        "...Ela é construída em torno das frases de efeito do Arnold Schwarzenegger.": 
            pass 
    
    pause 1

    show spr o1 closed eye grin
    voice "audio/voice/day1/o1-023.ogg"
    o "Ah, meu Deus."
    show spr o1 happy

    menu: 
        "Sem risadas. Isso é coisa séria.": 
            show spr o1 happy
            voice "audio/voice/day1/o1-024.ogg"
            o "Eu não estou... bom, um pouco. Mas estou mais fascinado do que qualquer outra coisa. Sério?" 
            menu: 
                "Sim!": 
                    pass 
        "Eu sei. Avançado. Já está intimidado?": 
            $ points_seekLove += 2
            show spr o1 happy
            voice "audio/voice/day1/o1-025.ogg"
            o "Um pouco. Mais ainda pela naturalidade com que você admitiu isso." 
            voice "audio/voice/day1/o1-026.ogg"
            o "Como foi que logo você encontrou este servidor mesmo?" 
            menu: 
                "Eu sou, tipo, o melhor em ArnoldC.": 
                    pass 
            voice "audio/voice/day1/o1-027.ogg"
            o "Aham." 

    show spr o1 happy grin
    voice "audio/voice/day1/o1-028.ogg"
    o "Vai ser interessante observar você interagindo com todo mundo."
    show spr o1 happy
    menu: 
        "Bom, agora eu fiquei nervoso.": 
            pass 

    show spr o1 eyes closed
    voice "audio/voice/day1/o1-029.ogg"
    o "Não fique."

    menu: 
        "Vou tentar.":
            $ points_seekLove += 2

            show spr o1 neutral
            voice "audio/voice/day1/o1-030.ogg"
            o "Já é o suficiente. Continue assim."

        "Os outros não ajudam muito.": 

            voice "audio/voice/day1/o1-031.ogg"
            o "Eles são assim mesmo. Não dê muita bola para eles."

    # end choices

    #show spr o2 side frown 
    show spr o3 neutral 
    voice "audio/voice/day1/o1-032.ogg"
    o "E com isso, estamos acertados. Te vejo por aí no servidor."
    #show spr o3 neutral
    menu: 
        "Isso foi rápido. Quer dizer que agora você confia em mim?": 
            pass 
    
    #show spr o3 eyes closed
    voice "audio/voice/day1/o1-033.ogg"
    o "O suficiente para manter você por perto."
    #show spr o3 neutral 
    voice "audio/voice/day1/o1-034.ogg"
    o "Até mais."

    menu: 
        "Até.": 
            pass

    ## must run these two lines to swap to next day 
    $ next_day_number = "2"
    jump day_swap