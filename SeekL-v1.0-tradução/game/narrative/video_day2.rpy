label day2_call: 
    show spr o1 smile
    voice "audio/voice/day2/o2-001.ogg"
    o "Sabe, pensando bem, eu deveria estar te agradecendo."

    play music "audio/music/Reflection_in_the_Blank_Screenlooped.ogg" loop fadein 2.0 fadeout 2.0 

    voice "audio/voice/day2/o2-002.ogg"
    o "Ao dar à incri um motivo para se exibir, você deu a eles menos espaço para serem descuidados."
    menu: 
        "Eles... não são bons em hacking?":
            pass

    show spr o1 side neutral
    voice "audio/voice/day2/o2-003.ogg"
    o "Eu não diria que são ruins, mas também não são os melhores. "

    show spr o1 neutral
    voice "audio/voice/day2/o2-004.ogg"
    o "Se eles fossem realmente um caso perdido, eu já os teria expulsado há um tempo."
    menu: 
        "Você avalia os novatos pela habilidade?":
            pass

    show spr o1 happy
    voice "audio/voice/day2/o2-005.ogg"
    o "Mais pelo risco de exposição."

    show spr o1 smile
    voice "audio/voice/day2/o2-006.ogg"
    o "Eu tento ser justo."
    menu: 
        "Que bom que eu passei.":
            pass

    show spr o1 eyes closed
    voice "audio/voice/day2/o2-007.ogg"
    o "Você passou, embora, com base nas suas escolhas de programação, estou te deixando ficar com uma sobrancelha levantada."

    show spr o1 done
    voice "audio/voice/day2/o2-008.ogg"
    o "Tipo, sério, por que ArnoldC? Na verdade, por que qualquer uma das linguagens esotéricas?"
    menu: 
        "Bem, eu não pude resistir à oportunidade de escrever algo baseado no próprio Exterminador do Futuro.":
            pass
    voice "audio/voice/day2/o2-009.ogg"
    o "Na verdade, eu acho que você poderia."
    menu: 
        "Não gosta dos filmes dele?":
            pass

    show spr o1 eyes closed
    voice "audio/voice/day2/o2-010.ogg"
    o "Quer dizer, sim, mas não gosto o suficiente para aprender uma linguagem baseada em citações."

    show spr o1 done
    voice "audio/voice/day2/o2-011.ogg"
    o "Você é realmente tão fã assim?"

    menu: 
        "Ah, com certeza. ":
            #show spr o1 smile
            voice "audio/voice/day2/o2-012.ogg"
            o "Entendi. "
            menu:
                "Mas não é bem por isso que comecei a usar ArnoldC.":
                    pass
        "É, eu acho que sim.":
            show spr o1 neutral
            voice "audio/voice/day2/o2-013.ogg"
            o "Isso é menos entusiasmado do que eu esperava." 
            voice "audio/voice/day2/o2-014.ogg"
            o "Por que essa falta de animação? "
            menu: 
                "Não é bem por isso que comecei a usar ArnoldC.":
                    pass
        "Na verdade, não. ":
            voice "audio/voice/day2/o2-015.ogg"
            o "Confuso, então. "

    menu: 
        "Eu só gosto de aprender linguagens esotéricas porque é divertido, sabe?":
            pass
    show spr o1 done
    voice "audio/voice/day2/o2-016.ogg"
    o "...Aham."
    #show spr o3 neutral
    voice "audio/voice/day2/o2-017.ogg"
    o "Estranho. "
    menu: 
        "Por que estranho?":
            pass
    #show spr o2 side frown 
    voice "audio/voice/day2/o2-018.ogg"
    o "Não sei, é que..."

    show spr o3 neutral
    voice "audio/voice/day2/o2-019.ogg"
    o "É realmente só por amor à arte, hein?"
    #show spr o3 neutral

    menu: 
        "Uhum. Gosto da minha pequena coleção.":
            $ points_seekLove += 2
            #show spr o1 grin 
            voice "audio/voice/day2/o2-020.ogg"
            o "Sua estante de troféus de linguagens ridículas?"
            menu:
                "Espera, uma estante de troféus de verdade seria muito legal.":
                    pass
            show spr o3 eyes closed
            voice "audio/voice/day2/o2-021.ogg"
            o "Isso não era para te incentivar."
            #show spr o3 neutral
            menu:
                "Tarde demais. Já estou procurando as vitrines com as molduras de madeira mais feias que consigo encontrar.":
                    pass
        "Você ri agora, mas um dia minha especialidade pode ser útil.":
            #show spr o1 closed eye grin
            voice "audio/voice/day2/o2-022.ogg"
            o "Sério."
            menu:
                "Seríssimo. ":
                    pass
            #show spr o1 smile
            voice "audio/voice/day2/o2-023.ogg"
            o "Diga um cenário."
            menu:
                "Hum... uh... hm.":
                    pass
            #show spr o3 silly 
            voice "audio/voice/day2/o2-024.ogg"
            o "Sim?"
            menu:
                "Quando eu pensar em uma resposta para isso amanhã, já era para você.":
                    pass

    show spr o1 happy grin
    voice "audio/voice/day2/o2-025.ogg"                
    o "( risos ) "

    show spr o1 smile
    voice "audio/voice/day2/o2-026.ogg"
    o "Você é realmente assim?"
    menu: 
        "O quê, divertido?":
            pass

    show spr o1 side smile
    voice "audio/voice/day2/o2-027.ogg"
    o "Desconcertante."
    menu: 
        "Desconcertante?!":
            pass

    show spr o1 neutral
    voice "audio/voice/day2/o2-028.ogg"
    o "Sim. O jeito que você acha graça em coisas assim."

    show spr o1 side nervous
    voice "audio/voice/day2/o2-029.ogg"
    o "Não é para ser um insulto, eu realmente só estou confuso."
    #show spr o1 neutral
    menu: 
        "Você não se diverte programando?":
            pass

    show spr o1 side neutral 
    voice "audio/voice/day2/o2-030.ogg"
    o "A essa altura, é só um meio para um fim. Assim como a maioria das coisas."
    #show spr o1 neutral 
    menu: 
        "Então o que você faz para se divertir?":
            pass

    show spr o1 closed eye happy
    voice "audio/voice/day2/o2-031.ogg"
    o "Ligo para pessoas estranhas que não se importam com privacidade."
    menu: 
        "Ha. Mas só isso?":
            pass
    pause 2
    show spr o2 side frown
    voice "audio/voice/day2/o2-032.ogg"
    o "Não faço mais muita coisa além disso."


    menu:
        "Isso soa... um pouco solitário.":
            $ points_seekLove += 2
            show spr o2 sad 
            voice "audio/voice/day2/o2-033.ogg"
            o "Talvez. Claro. "
            #show spr o3 eyes closed
            voice "audio/voice/day2/o2-034.ogg"
            o "Mas isso não importa muito agora."
        "Ah, uh. Parece uma vida bem pacífica. ":
            #show spr o1 side neutral
            show spr o2 sad 
            voice "audio/voice/day2/o2-035.ogg"
            o "Diga o que você quer dizer, ha. Eu entendo. "
            #show spr o1 eyes closed
            voice "audio/voice/day2/o2-036.ogg"
            o "Mas não importa mais. "

    show spr o3 neutral
    voice "audio/voice/day2/o2-037.ogg"
    o "Precisar me divertir não é mais importante na minha vida. "

    show spr o3 eyes closed 
    voice "audio/voice/day2/o2-038.ogg"
    o "E, de qualquer forma, vamos nos despedir em breve."

    show spr o3 neutral
    voice "audio/voice/day2/o2-039.ogg"
    o "Então não se preocupe com isso."
    menu: 
        "...Qual é o seu 'fim', exatamente?":
            pass

    show spr o1 side neutral 
    voice "audio/voice/day2/o2-040.ogg"
    o "Simples."
    show spr o1 neutral 
    voice "audio/voice/day2/o2-041.ogg"
    o "Vou sair completamente do mapa em breve. "

    show spr o1 neutral 
    voice "audio/voice/day2/o2-042.ogg"
    o "Eu pego uma parte dos hacks dos outros, e entre os hacks deles e os meus, juntei um fundo para suprimentos."

    show spr o1 eyes closed 
    voice "audio/voice/day2/o2-043.ogg"
    o "Assim que eu fechar o servidor, farei uma última busca por suprimentos e darei minha saída da sociedade."
    #show spr o1 neutral 
    
    
    menu:
        "O que você vai comprar? ":
            show spr o1 eyes closed
            voice "audio/voice/day2/o2-044.ogg"
            o "Eu tenho a maior parte da comida que preciso, então... provavelmente só coisas de última hora. "
            show spr o1 neutral 
            voice "audio/voice/day2/o2-045.ogg"
            o "Uma ou duas jaquetas, alguns suprimentos médicos, o de sempre. "
            voice "audio/voice/day2/o2-046.ogg"
            show spr o1 eyes closed
            o "Aí eu caio fora, o mais rápido possível. "
        "Espera, o quê? Por quê?!":
            $ points_seekLove += 2
            show spr o1 side smile
            voice "audio/voice/day2/o2-047.ogg"
            o "Acha que eu sou louco? "
            #show spr o1 neutral
            menu:
                "Não, só estou confuso.":
                    pass
            show spr o1 eyes closed
            voice "audio/voice/day2/o2-048.ogg"
            o "Quer dizer, não acho que seja difícil de entender. "

    show spr o1 side neutral 
    voice "audio/voice/day2/o2-049.ogg"
    o "Não tenho nenhum motivo para ficar. Eu só estou... cansado. De tudo. "


    menu:
        "Você está de saco cheio das pessoas?":
            show spr o1 eyes closed
            voice "audio/voice/day2/o2-050.ogg"
            o "Não, não há nenhuma frustração real da minha parte. Apenas apatia."
            voice "audio/voice/day2/o2-051.ogg"
            show spr o1 neutral 
            o "Todos com quem eu achava que me importava simplesmente não são mais pessoas na minha vida. Tudo por motivos aleatórios e sem graça. Nada dramático. "
            show spr o1 frown
            voice "audio/voice/day2/o2-052.ogg"
            o "Eu simplesmente acordei um dia e percebi que estava sozinho."
            show spr o1 eyes closed
            voice "audio/voice/day2/o2-053.ogg"
            o "Então, sem essas conexões, não há nada que me prenda aqui."
        "Nenhum motivo? Nada te faz feliz aqui?":
            $ points_seekLove += 2
            #show spr o3 neutral
            voice "audio/voice/day2/o2-054.ogg"
            o "Não há muito tempo."
            #show spr o1 neutral 
            voice "audio/voice/day2/o2-055.ogg"
            o "Eu não sinto muita coisa, na verdade. É o que é. "


    menu: 
        "Isso é...":
            pass
    
    #show spr o1 side neutral
    show spr o3 neutral
    voice "audio/voice/day2/o2-056.ogg"
    o "Não diga."
    show spr o3 eyes closed
    voice "audio/voice/day2/o2-057.ogg"
    o "Desculpe, eu já ouvi isso antes. Não vai mudar minha opinião."
    show spr o1 neutral
    voice "audio/voice/day2/o2-058.ogg"
    o "Nós acabamos de nos conhecer. E seremos estranhos novamente em breve."
    #show spr o1 neutral 
    voice "audio/voice/day2/o2-059.ogg"
    o "Então, não querendo ser frio, mas... você sabe. "
    menu: 
        "...Você tem razão.":
            pass
    show spr o1 eyes closed
    voice "audio/voice/day2/o2-060.ogg"
    o "Sim."
    show spr o1 neutral 
    voice "audio/voice/day2/o2-061.ogg"
    o "E com isso, acho que já chega por hoje."
    menu: 
        "Tudo bem.":
            pass
    show spr o1 side neutral
    voice "audio/voice/day2/o2-062.ogg"
    o "Nós, ah."
    #show spr o1 smile
    voice "audio/voice/day2/o2-063.ogg"
    o "Podemos ligar de novo se a oportunidade surgir."
    #show spr o1 neutral


    menu:
        "Eu gostaria.":
            $ points_seekLove += 2
            show spr o1 smile
            voice "audio/voice/day2/o2-064.ogg"
            o "Vou tentar pensar em um tópico mais interessante da próxima vez."
            menu: 
                "É uma promessa?":
                    pass
            show spr o1 side smile
            voice "audio/voice/day2/o2-065.ogg"
            o "Eu disse que vou tentar."
            menu: 
                "Haha!": 
                    pass
        "É. Parece bom.":
            pass 

    show spr o1 grin
    voice "audio/voice/day2/o2-066.ogg"
    o "Te vejo depois, então."
    #"You too."


    ## must run these two lines to swap to next day 
    $ next_day_number = "3"
    jump day_swap

    $ renpy.pause(hard=True)