label day3_call: 

    show spr o1 eyes closed
    voice "audio/voice/day3/o3-001.ogg"
    o "Bem, aqui estamos. Dois hacks concluídos, faltam dois."

    play music "audio/music/Digital_Dreamlooped.ogg" loop fadein 2.0 fadeout 2.0 

    show spr o1 neutral 
    voice "audio/voice/day3/o3-002.ogg"
    o "Ainda tenho algumas coisas para terminar, então o elimf provavelmente vai acabar antes de mim."
    menu: 
        "O melhor fica para o final, certo?": 
            pass 

    show spr o1 smile
    voice "audio/voice/day3/o3-003.ogg"
    o "Ha. Pode ser."

    #show spr o1 neutral 
    voice "audio/voice/day3/o3-004.ogg"
    o "Sente que está se acostumando com tudo?"

    menu: 
        "Veremos quando o 'melhor para o final' decidir me dar umas dicas.":
            show spr o1 eyes closed
            voice "audio/voice/day3/o3-005.ogg"
            o "Você está presumindo que eu vou te ensinar alguma coisa."
            menu: 
                "E você vai me deixar sair só com o que o incri me ensinou?":
                    pass
            show spr o1 done
            voice "audio/voice/day3/o3-006.ogg"
            o "...Talvez eu não devesse soltar isso no mundo."
        "Diria que sim. Pena que não vou poder testar tudo com vocês.":
            $ points_seekLove += 2
            show spr o1 smile 
            voice "audio/voice/day3/o3-007.ogg"
            o "Você sobrevive. Já a sua opsec, não tenho certeza."
            show spr o1 closed eye happy 
            voice "audio/voice/day3/o3-008.ogg"
            o "Vou ficar de olho em você no noticiário."
            show spr o1 smile
            menu: 
                "Tão pouca fé em mim.":
                    pass 
            show spr o1 done
            voice "audio/voice/day3/o3-009.ogg"
            o "Diz a pessoa que teve o IP encontrado por todo mundo em menos de uma hora depois de entrar."
            show spr o1 side nervous
            voice "audio/voice/day3/o3-010.ogg"
            o "Desculpa, isso foi meio rude. Desculpa."
            menu: 
                "E agora você está me zoando??": 
                    pass 
            show spr o1 grin 
            voice "audio/voice/day3/o3-011.ogg"
            o "Eu pedi desculpa!"
            show spr o1 smile 

    menu: 
        "Acho que consigo fazer algo bom, com o tempo. Que tal ficar por aqui para ver?":
            pass 
    show spr o1 frown
    voice "audio/voice/day3/o3-012.ogg"
    o "Mm. Eu devia saber que o assunto voltaria para isso."
    
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-013.ogg"
    o "Por que você se importa com o que eu escolho fazer da minha vida?"
    menu: 
        "Eu não posso me importar com outra pessoa?":
            pass 

    show spr o1 side frown 
    voice "audio/voice/day3/o3-014.ogg"
    o "Pode, mas... eu não sou mais bem uma pessoa."

    menu: 
        "Como assim?":   
            $ points_seekLove += 2
            #show spr o1 eyes closed  
            show spr o2 side frown
            voice "audio/voice/day3/o3-015.ogg"
            o "Eu não sou ninguém. E vou me tornar ninguém. Você tem outras coisas para preencher sua vida."
            #show spr o1 neutral 
            menu: 
                "Tenho. Mas eu consigo me importar com várias coisas ao mesmo tempo.": 
                    pass 
            #show spr o1 done frown 
            show spr o2 sad
            voice "audio/voice/day3/o3-016.ogg"
            o "Isso parece um fardo."

            #show spr o1 side frown
            voice "audio/voice/day3/o3-017.ogg"
            o "Não é exaustivo?"
            menu: 
                "Às vezes. Mas vale a pena o esforço.":
                    pass
            #show spr o2 side frown
            voice "audio/voice/day3/o3-018.ogg"
            o "Por quê?"
            menu: 
                "Porque eu gosto da sua companhia.": 
                    pass 
        "Você ainda parece uma pessoa.":
            show spr o1 done frown
            voice "audio/voice/day3/o3-019.ogg"
            o "Você sabe o que eu quero dizer."
            menu: 
                "Sei que estou discutindo o significado das palavras. Mas você ainda está aqui, não está?": 
                    pass 
            show spr o2 side frown
            voice "audio/voice/day3/o3-020.ogg"
            o "Nunca esteve numa situação em que quis desaparecer?"
            menu: 
                "Não disse isso.": 
                    pass 
            menu: 
                "Mas eu nunca fui até o fim.":
                    pass 
            show spr o2 scowl
            voice "audio/voice/day3/o3-021.ogg"
            o "Então você não sentiu o que eu sinto."

            show spr o2 sad
            voice "audio/voice/day3/o3-022.ogg"
            o "Senão, você teria ido."
            menu: 
                "Não é verdade. Eu só lidei com o sentimento.": 
                    pass 

    show spr o2 scowl
    voice "audio/voice/day3/o3-023.ogg"
    o "Não pode ser tão simples."
    #show spr o3 neutral
    menu: 
        "Por que não?": 
            pass 
    show spr o2 side frown
    voice "audio/voice/day3/o3-024.ogg"
    o "Se fosse tão simples, então–"
    pause 1
    show spr o2 sad
    voice "audio/voice/day3/o3-025.ogg"
    o "Não sei por que estou me dando ao trabalho de discutir."
    show spr o2 side frown
    voice "audio/voice/day3/o3-026.ogg"
    o "Por que sinto que preciso provar isso para você?"
    menu: 
        "Tem certeza que é para mim?": 
            pass 
    #show spr o3 shocked
    pause 3
    show spr o2 sad
    voice "audio/voice/day3/o3-027.ogg"
    o "Não. Não, não. Não. Não."
    show spr o3 eyes closed 
    voice "audio/voice/day3/o3-028.ogg"
    o "Acho que já chega por hoje."
    show spr o3 neutral 
    voice "audio/voice/day3/o3-029.ogg"
    o "Vamos falar de outra coisa."
    pause 3
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-030.ogg"
    o "Desculpa. Vou pensar em algo."
    show spr o1 side nervous 
    voice "audio/voice/day3/o3-031.ogg"
    o "O que, uhm, o que mais você faz? Além de coisas relacionadas a programação."
    #show spr o1 neutral 

    menu: 
        "Procurando uma desculpa para criticar minha opsec de novo?":
            show spr o1 done 
            voice "audio/voice/day3/o3-032.ogg"
            o "Quer dizer, se você responder com algo que te identifique–"
            menu:
                "Entendi, entendi! Umm. Certo.": 
                    pass 
        "Ora, ora, ora. Olha só quem está se importando agora.":
            $ points_seekLove += 2
            show spr o1 done
            voice "audio/voice/day3/o3-033.ogg"
            o "Estou com o mouse em cima do botão 'encerrar chamada' neste exato momento."
            menu: 
                "Tá bom, tá bom, eu respondo!": 
                    pass 

    pause 1

    menu: 
        "Eu gosto de provar o hambúrguer ou sanduíche com o nome mais idiota do cardápio dos restaurantes.":
            show spr o1 neutral 
            voice "audio/voice/day3/o3-034.ogg"
            o "O nome ou os ingredientes mais idiotas?"
            menu: 
                "O que me chamar mais atenção. Às vezes acho um que tem os dois.": 
                    pass 
            show spr o1 done 
            voice "audio/voice/day3/o3-035.ogg"
            o "Tipo...?"
            menu: 
                "O hambúrguer 'Absurdo de PB&J' – tipo, pasta de amendoim e geleia de jalapeño.": 
                    pass 
            show spr o1 done frown 
            voice "audio/voice/day3/o3-036.ogg"
            o "Isso parece... desagradável."
            #show spr o1 neutral 
            menu: 
                "Não foi o pior de todos!": 
                    pass 
            show spr o1 smile
            voice "audio/voice/day3/o3-037.ogg"
            o "Vou acreditar na sua palavra."
            show spr o1 eyes closed
            voice "audio/voice/day3/o3-038.ogg"
            o "Ugh. Agora isso vai ficar na minha cabeça."
            menu: 
                "Desculpa!":
                    pass 
            show spr o1 smile
            voice "audio/voice/day3/o3-039.ogg"
            o "Eu me recupero. Eventualmente."
            show spr o3 shocked 
            voice "audio/voice/day3/o3-040.ogg"
            o "...É estranho que uma parte doentia de mim queira provar?"
            #show spr o3 neutral 
        "Gosto de navegar em fóruns de nicho e tentar me infiltrar.":
            show spr o1 smile 
            voice "audio/voice/day3/o3-041.ogg"
            o "O quê, tipo Reddit?"

            show spr o1 closed eye happy 
            voice "audio/voice/day3/o3-042.ogg"
            o "Dificilmente um nicho."
            #show spr o1 smile 
            menu: 
                "Não, não. Estou falando de grupos de Facebook.": 
                    pass 
            show spr o1 done frown
            voice "audio/voice/day3/o3-043.ogg"
            o "Hã?"
            menu: 
                "Tipo grupos de bairro de lugares que eu moro a pelo menos mil e quinhentos quilômetros de distância.": 
                    pass 
            show spr o1 mad 
            voice "audio/voice/day3/o3-044.ogg"
            o "O quê? Por quê? Qual é o seu problema?"
            menu: 
                "Para sentir o gostinho da treta sem ser afetado por ela.": 
                    pass 
            show spr o1 done frown 
            voice "audio/voice/day3/o3-045.ogg"
            o "Quem gosta de ir atrás de treta?"
            #show spr o1 side frown 
            show spr o3 silly 
            voice "audio/voice/day3/o3-046.ogg"
            o "Mas, não acredito que agora estou curioso."
            #show spr o1 grin 
            voice "audio/voice/day3/o3-047.ogg"
            o "Será que estou perdendo algo? Eu deveria ir procurar umas tretas de subúrbio?"
            #show spr o1 smile 

    menu: 
        "Deveria. É um gosto que se adquire, mas quando você menos esperar, {i}você vai voltar.{/i}":
            pass
    #show spr o3 silly 
    pause 2
    show spr o1 done 
    voice "audio/voice/day3/o3-048.ogg"
    o "Isso foi uma tentativa de imitar o Exterminador do Futuro?"
    menu: 
        "Eu sei que é horrível! Eu sei!":
            pass
    #show spr o1 eyes closed
    voice "audio/voice/day3/o3-049.ogg"
    o "Essa foi a pior preparação e imitação que eu já ouvi."
    #show spr o1 smile 
    menu: 
        "Você gostou. Olha, aqui vai outra–":
            pass
    show spr o3 shocked
    voice "audio/voice/day3/o3-050.ogg"
    o "Larga o livro de citações! Agora!"
    menu: 
        "...":
            pass
    voice "audio/voice/day3/o3-051.ogg"
    show spr o1 side nervous
    o "Olha–"
    menu: 
        "Essa foi ainda pior!":
            pass
    show spr o1 mad 
    voice "audio/voice/day3/o3-052.ogg"
    o "Para de ficar tão feliz com isso!"
    menu: 
        "Foi muito ruim!":
            pass
    show spr o1 happy grin 
    voice "audio/voice/day3/o3-053.ogg"
    o "Foi um lapso de julgamento."
    voice "audio/voice/day3/o3-054.ogg"
    o "( rindo )"

    menu: 
        "Vou me lembrar deste dia para sempre.":
            show spr o1 grin 
            voice "audio/voice/day3/o3-055.ogg"
            o "Vai mesmo?"
            show spr o1 smile 
            menu: 
                "Não posso prever todas as contingências. Mas posso tentar.": 
                    pass 
            show spr o1 closed eye happy 
            voice "audio/voice/day3/o3-056.ogg"
            o "Aceito isso."
        "A propósito, eu gosto da sua risada.":
            $ points_seekLove += 2
            show spr o3 silly 
            voice "audio/voice/day3/o3-057.ogg"
            o "Ah, minha risada?"
            show spr o1 side nervous
            voice "audio/voice/day3/o3-058.ogg"
            o "Uhm... obrigado. Hm."
            show spr o1 side smile 
            voice "audio/voice/day3/o3-059.ogg"
            o "Tenho rido bastante, não é?"
            menu: 
                "Com certeza.": 
                    pass 
            show spr o1 side nervous 
            voice "audio/voice/day3/o3-060.ogg"
            o "Ha... estranho."

    pause 2
    show spr o1 frown 
    voice "audio/voice/day3/o3-061.ogg"
    o "Eu gosto da sua risada, eu acho."
    menu: 
        "Você acha???":
            pass
    show spr o1 eyes closed
    voice "audio/voice/day3/o3-062.ogg"
    o "É... eu acho."
    show spr frown
    voice "audio/voice/day3/o3-063.ogg"
    o "Ria de novo."
    #show spr o1 smile
    menu: 
        "Não, não, você tem que merecer. Me faça rir.":
            pass
    show spr o1 done
    voice "audio/voice/day3/o3-064.ogg"
    o "Deixa pra lá, cala a boca."
    menu: 
        "( Rir )" :
            pass
    show spr o1 grin 
    voice "audio/voice/day3/o3-065.ogg"
    o "E agora você ri?? De mim?? ( rindo )"
    show spr o1 side smile 
    voice "audio/voice/day3/o3-066.ogg"
    o "Inacreditável..."
    pause 1
    show spr o1 smile 
    menu: 
        "Posso perguntar só uma coisa sobre você?":
            pass
    show spr o1 neutral 
    voice "audio/voice/day3/o3-067.ogg"
    o "Claro. Manda."
    menu: 
        "Qual foi sua primeira linguagem de programação?":
            pass
    voice "audio/voice/day3/o3-068.ogg"
    o "Por que você quer saber disso?"
    menu: 
        "Nenhum motivo. Só curiosidade.":
            pass
    voice "audio/voice/day3/o3-069.ogg"
    o "Foi Python."
    
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-070.ogg"
    o "Eu tinha doze anos e encontrei um site dedicado a exercícios divertidos usando Python."

    show spr o1 neutral 
    voice "audio/voice/day3/o3-071.ogg"
    o "Jogo da cobrinha, Torre de Hanói... coisas bobas."
    pause 2

    show spr o1 side frown 
    voice "audio/voice/day3/o3-072.ogg"
    o "Eu gostava muito daquela linguagem."
    menu: 
        "Você não usa mais?":
            pass
    show spr o3 eyes closed 
    voice "audio/voice/day3/o3-073.ogg"
    o "Não, Python não consegue cobrir tudo que eu preciso fazer neste servidor."
    show spr o3 neutral 
    voice "audio/voice/day3/o3-074.ogg"
    o "Mas era amigável para iniciantes. Muito fácil de ler e entender, sabe?"
    show spr o1 eyes closed 
    voice "audio/voice/day3/o3-075.ogg"
    o "Sou grato por ter encontrado essa linguagem primeiro."
    show spr o1 neutral 
    voice "audio/voice/day3/o3-076.ogg"
    o "Talvez eu não tivesse entrado na programação sem ela."
    menu: 
        "Então você gosta de programar.":
            pass
    show spr o1 side smile 
    voice "audio/voice/day3/o3-077.ogg"
    o "Ha."
    show spr o1 happy
    voice "audio/voice/day3/o3-078.ogg"
    o "Talvez um pouco."
    #show spr o1 side smile 
    voice "audio/voice/day3/o3-079.ogg"
    o "Você se lembra de coisas demais que eu digo."
    pause 1
    show spr o1 side smile 
    voice "audio/voice/day3/o3-080.ogg"
    o "Obrigado por conversar comigo nestes últimos dias."
    voice "audio/voice/day3/o3-081.ogg"
    show spr o1 happy
    o "Tem sido legal."
    menu: 
        "Sempre podemos conversar por muitos outros dias, se você quiser.":
            pass
    show spr o1 closed eye happy
    voice "audio/voice/day3/o3-082.ogg"
    o "Atrevido."
    show spr o1 happy
    voice "audio/voice/day3/o3-083.ogg"
    o "Não sei quanto a isso, Thrim."
    menu: 
        "Valia a tentativa.":
            pass
    show spr o1 side smile
    voice "audio/voice/day3/o3-084.ogg"
    o "Você realmente achou que ia funcionar?"
    menu: 
        "Na verdade não. Mas a esperança é a última que morre.":
            pass
    voice "audio/voice/day3/o3-085.ogg"
    show spr o1 closed eye happy
    o "Ha."
    voice "audio/voice/day3/o3-086.ogg"
    show spr o1 neutral
    o "Enfim, está tarde. Hora de eu ir."
    voice "audio/voice/day3/o3-087.ogg"
    o "Presumo que você vai estar online amanhã?"
    menu: 
        "Com certeza.":
            pass
    show spr o1 eyes closed
    voice "audio/voice/day3/o3-088.ogg"
    o "Até lá, então."

    ## must run these two lines to swap to next day 
    $ next_day_number = "4"
    jump day_swap

    $ renpy.pause(hard=True)