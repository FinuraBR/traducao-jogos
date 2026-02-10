################################################################################
##
## Extended Music Room for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
##
################################################################################
## This file contains code for a music room in Ren'Py. It is designed
## as a wrapper to the built-in music room system, so many of the methods and
## functions used there will also work with this music room.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## If you'd like to see how to use this tool, check the other file,
## music_room.rpy! This is just the backend; you don't need to understand
## everything in this file.
##
## Leave a comment on the tool page on itch.io or an issue on the GitHub
## if you run into any issues.
################################################################################
python early:

    class AudioBar(renpy.display.behavior.Bar):
        """
        Um tipo especial de barra que permite ao usuário ajustar a posição
        do áudio que está tocando ao soltá-la. É configurada automaticamente para
        usar o valor correto e pode ser estilizada como qualquer outra barra. Você pode
        fornecer uma propriedade "room" para a barra, que deve ser um objeto
        MusicRoom (como o ExtendedMusicRoom incluído nestes arquivos). Se for o caso,
        ela funcionará automaticamente com os recursos de playlist e looping
        da sala. Caso contrário, você pode fornecer uma propriedade "channel", que deve
        ser uma string. A música será tocada nesse canal quando reiniciada.
        """

        def __init__(self, **kwargs):
            self.musicroom = kwargs.get('room', None)
            if self.musicroom:
                kwargs['channel'] = self.musicroom.channel
            kwargs['value'] = AudioAdjustmentValue(kwargs.get('channel', 'music'),
                kwargs.get('update_interval', 0.1))
            super(AudioBar, self).__init__(**kwargs)
            self.channel = kwargs.get('channel', 'music')
            self.released_fn = adjust_music_released
            self.released = self.pass_value_released

        def pass_value_released(self):
            return self.released_fn(self.adjustment.value,
                self.musicroom or self.channel)

    ## Create a special music bar screen language statement which uses the
    ## AudioBar class.
    renpy.register_sl_displayable("music_bar", AudioBar, "bar", 0, replaces=True,
        pass_context=True
        ).add_property("hovered"
        ).add_property("unhovered"
        ).add_property("channel"
        ).add_property("room"
        ).add_property("update_interval"
        ).add_property_group("bar")

init python:

    def adjust_music_released(value, musicroom):
        """
        Toca uma faixa começando na posição fornecida por 'value', em segundos,
        no canal fornecido. 'musicroom' deve ser um objeto MusicRoom
        ou o nome de um canal. Se for o primeiro, funcionará
        com os recursos de looping e playlist da sala. Caso contrário,
        apenas tocará a faixa no canal.
        """
        next_songs = None

        try:
            channel = musicroom.channel
            loop = musicroom.loop or musicroom.single_track
            fadeout = musicroom.fadeout
            fadein = musicroom.fadein
        except:
            channel = musicroom
            loop = renpy.music.get_loop(channel)
            fadeout = 0.0
            fadein = 0.0
            if loop:
                next_songs = list(loop)
                next_songs.pop(0)
                loop = True

        track = renpy.music.get_playing(channel)
        if not track:
            return

        # Strip out any existing <> information
        track = strip_playback(track)

        duration = renpy.music.get_duration(channel)
        if not duration:
            return

        new_t = max(value, 0)
        new_t = min(new_t, duration)

        file = "<from {} loop 0.0>{}".format(new_t, track)

        try:
            musicroom.play(file)
        except:
            renpy.music.play(file, channel=channel, loop=loop,
                fadeout=fadeout, fadein=fadein)
            if next_songs:
                renpy.music.queue(next_songs, channel=channel, clear_queue=True,
                    loop=loop)

    class AudioAdjustmentValue(AudioPositionValue):
        """
        Um valor de barra AudioPositionValue que dá um pouco mais de
        folga para não pular a posição para 0. Tem um valor ajustável
        que pode ser alterado ao soltar usando a classe AudioBar.
        """
        def __init__(self, *args, **kwargs):
            super(AudioAdjustmentValue, self).__init__(*args, **kwargs)
            self.last_nonzero_pos = 0
            self.last_duration = 1.0
            self.last_zero = 0

        def get_pos_duration(self):
            """
            Retorna a posição e a duração da faixa atualmente em reprodução.
            Se nenhuma faixa for detectada, e alguma informação estiver salva, ela
            continuará mostrando a informação salva por um curto período para evitar
            que a barra pule para 0.
            """
            pos = renpy.music.get_pos(self.channel) or self.last_nonzero_pos
            duration = renpy.music.get_duration(self.channel) or self.last_duration

            if pos > self.update_interval:
                self.last_nonzero_pos = pos
                self.last_duration = duration
                self.last_zero = 0
            else:
                self.last_zero += 1

            if self.last_zero > 10:
                return pos, duration
            else:
                return self.last_nonzero_pos, self.last_duration

        def get_adjustment(self):
            """
            Obtém o valor atual do ajuste para esta barra, com base na
            posição e duração da música atualmente em reprodução.
            """
            pos, duration = self.get_pos_duration()
            self.adjustment = ui.adjustment(value=pos, range=duration,
                adjustable=True)
            return self.adjustment

init -50 python:

    class MusicInfo():
        """
        Uma classe com informações sobre uma faixa que pode ser tocada na sala
        de música.

        Atributos:
        -----------
        name : string
            O nome da faixa.
        path : string
            O caminho do arquivo para a faixa.
        artist : string
            O artista da faixa.
        art : Displayable
            A arte a ser exibida para a faixa.
        description : string
            Uma descrição opcional da faixa (pode ser usada para informações
            extras, quando a faixa toca no jogo, a duração da
            faixa a ser exibida na lista de faixas, etc.).
        unlock_condition : string
            A condição para desbloquear a faixa. Esta é uma string que pode ser
            avaliada como um booleano. Se for avaliada como True, a faixa é
            desbloqueada. Se for avaliada como False, a faixa está bloqueada. Por padrão,
            uma faixa é desbloqueada se já foi vista no jogo.
        """
        ALL_MUSIC_FILES = [ ]
        PATH_TO_INFO = dict()
        def __init__(self, name, path, artist=None, art=None, description=None,
                    unlock_condition=None):
            self.name = name
            self.path = path
            self.artist = artist
            self.art = art
            self.description = description

            if unlock_condition is None:
                self.unlock_condition = "renpy.seen_audio('{}')".format(path)
            else:
                self.unlock_condition = unlock_condition

            MusicInfo.ALL_MUSIC_FILES.append(self)
            MusicInfo.PATH_TO_INFO[path] = self

        @property
        def locked(self):
            try:
                return not eval(self.unlock_condition)
            except:
                return True

        def __str__(self):
            return "<MusicInfo: {} : {} : {}>".format(self.name, self.path,
                "locked" if self.locked else "unlocked")


    def strip_playback(filename):
        """
        Remove qualquer informação de reprodução <> existente de um nome de arquivo.
        """
        if filename and filename.startswith("<"):
            return '>'.join(filename.split(">")[1:])
        else:
            return filename


    @renpy.pure
    class CustomMusicRoomPlay(Action, FieldEquality):
        """
        A ação retornada por MusicRoom.Play quando chamada com um arquivo.
        É o mesmo que __MusicRoomPlay na engine, mas com um método `get_selected`
        mais tolerante para levar em conta a reprodução parcial.
        """
        identity_fields = [ "mr" ]
        equality_fields = [ "filename" ]

        def __init__(self, mr, filename):
            self.mr = mr
            self.filename = filename
            self.selected = self.get_selected()

        def __call__(self):

            renpy.restart_interaction()
            playing = renpy.music.get_playing(self.mr.channel)
            playing = strip_playback(playing) if playing else None

            if playing == self.filename:
                if renpy.music.get_pause(self.mr.channel):
                    renpy.music.set_pause(False, self.mr.channel)
                    return
            self.mr.play(self.filename, 0)

        def get_sensitive(self):
            return self.mr.is_unlocked(self.filename)

        def get_selected(self):
            song = renpy.music.get_playing(self.mr.channel)
            if song:
                song = strip_playback(song)
            return song == self.filename

        def periodic(self, st):
            if self.selected != self.get_selected():
                self.selected = self.get_selected()
                renpy.restart_interaction()

            self.mr.periodic(st)

            return .1


    class ExtendedMusicRoom(MusicRoom):
        """
        Uma classe que estende a sala de música embutida para permitir maior
        compatibilidade com a reprodução parcial.

        Atributos específicos de ExtendedMusicRoom:
        --------------------------------------
        alphabetical : bool
            Se True, a sala de música será ordenada alfabeticamente. Se False,
            a sala de música será ordenada pela ordem em que as faixas
            foram adicionadas à sala de música. O padrão é False.
        default_art : Displayable
            Um displayable para usar como a arte padrão para as faixas, a menos que
            uma arte mais específica seja fornecida.
        saved_pos : string
            A última posição salva da faixa atualmente em reprodução. Salvo para
            evitar oscilações na exibição devido a uma pausa ao iniciar uma faixa
            novamente usando a reprodução parcial.
        saved_duration : string
            A última duração salva da faixa atualmente em reprodução. Salvo para
            evitar oscilações na exibição devido a uma pausa ao iniciar uma faixa
            novamente usando a reprodução parcial.
        last_zero : int
            O número de vezes que a posição da faixa atualmente em reprodução
            foi None. Usado para evitar oscilações na exibição devido a uma pausa
            ao iniciar uma faixa novamente usando a reprodução parcial.
        last_song : string
            O caminho da música que é a última na fila antes
            que ela precise ser reembaralhada. Usado para identificar quando a fila precisa
            ser reembaralhada.
        old_shuffle : bool
            O valor de shuffle, sem levar em conta o valor atual
            de single_track. Usado para lembrar o valor de shuffle quando a
            faixa única é ativada.
        music_dictionary : dict
            Um dicionário de objetos path : MusicInfo para todas as faixas na
            sala de música.
        """
        ## The grace period for the position of the currently playing track
        ## to not be reset to 0. Mostly prevents the bar from jumping to zero
        ## when we're starting partial playback in a new position.
        ZERO_THRESHOLD = 10
        def __init__(self, *args, **kwargs):
            """
            Argumentos específicos de ExtendedMusicRoom:
            -------------------------------------
            alphabetical : bool
                Se True, a sala de música será ordenada alfabeticamente. Se False,
                a sala de música será ordenada pela ordem em que as faixas
                foram adicionadas à sala de música. O padrão é False.
            default_art : Displayable
                Um displayable para usar como a arte padrão para as faixas, a menos que
                uma arte mais específica seja fornecida.
            """
            self.alphabetical = kwargs.pop("alphabetical", False)
            stop_action = kwargs.pop("stop_action", None)
            if stop_action and not isinstance(stop_action, list):
                stop_action = [ stop_action ]
            else:
                stop_action = [ ]
            stop_action.append(SetScreenVariable("current_track", None))
            kwargs['stop_action'] = stop_action
            if kwargs['single_track']:
                kwargs['loop'] = True
            super(ExtendedMusicRoom, self).__init__(*args, **kwargs)
            self.default_art = kwargs.pop('default_art', Null())
            self.saved_pos = "--:--"
            self.saved_duration = "--:--"
            self.last_zero = 0
            self.last_song = None
            self.old_shuffle = self.shuffle
            self.music_dictionary = dict()

        def add(self, name, path, artist=None, art=None, description=None,
                    unlock_condition=None):
            """
            Cria um objeto MusicInfo que adiciona música a esta sala de música.
            Veja a classe MusicInfo para informações sobre esses campos.
            """
            track = MusicInfo(name, path, artist, art or self.default_art,
                description, unlock_condition)

            super(ExtendedMusicRoom, self).add(track.path,
                always_unlocked=track.unlock_condition=="True",
                action=SetScreenVariable('current_track', track))

            self.music_dictionary[track.path] = track

            if self.alphabetical:
                self.playlist.sort(key=lambda x: self.music_dictionary[x].name)

        def is_unlocked(self, filename):
            """
            Retorna True se o nome do arquivo foi desbloqueado (ou está sempre
            desbloqueado), e False se ainda estiver bloqueado.
            """
            track = self.music_dictionary.get(filename)

            if filename in self.always_unlocked:
                return True

            ## Allow for all songs in developer mode with the correct
            ## config value. Otherwise, use only unlocked songs.
            if config.developer and myconfig.UNLOCK_TRACKS_FOR_DEVELOPMENT:
                return True

            return (not track.locked)

        def periodic(self, st):
            """
            Uma função que é chamada periodicamente. Usada para garantir que as
            ações sejam chamadas quando a sala de música muda de música para
            atualizar as informações da música e possivelmente reembaralhar a fila.
            """

            if st == self.st:
                return
            elif st < self.st:
                self.last_playing = None

            self.st = st

            current_playing = renpy.music.get_playing(self.channel)
            if current_playing is None:
                current_playing = ""
            else:
                current_playing = strip_playback(current_playing)

            if self.last_playing != current_playing:
                action = self.action.get(current_playing, None)
                renpy.run_action(action)
                ## Check if we're at the last song of the shuffle queue.
                if (self.last_song is not None
                        and current_playing == self.last_song):
                    self.last_song = None
                    self.shuffled = None
                    ## Shuffle the playlist again to queue up in a new order.
                    self.play(None, 0, queue=True)

                self.last_playing = current_playing

        def pos_dd(self, st, at, style="music_room_pos"):
            """
            Uma função DynamicDisplayable para a posição da faixa atualmente
            em reprodução.
            """
            x = renpy.music.get_pos(channel=self.channel)
            if x is None:
                txt = "--:--"
                self.last_zero += 1
            else:
                ## Format it in 00:00 style
                txt = "{:02}:{:02}".format(int(x/60), int(x%60))
                self.saved_pos = txt
                self.last_zero = 0

            ## Use the saved value if it's been temporarily at zero.
            if self.last_zero < self.ZERO_THRESHOLD:
                txt = self.saved_pos
            ## Make sure this is updated at least every second
            return Text(txt, style=style), 0.2

        def duration_dd(self, st, at, style="music_room_duration"):
            """
            Uma função DynamicDisplayable para a duração da faixa atualmente
            em reprodução.
            """
            x = renpy.music.get_duration(channel=self.channel)
            if not x:
                txt = "--:--"
            else:
                ## format it in 00:00 style
                txt = "{:02}:{:02}".format(int(x/60), int(x%60))
                self.saved_duration = txt
            if self.last_zero < self.ZERO_THRESHOLD:
                txt = self.saved_duration
            ## This only needs to be updated when the song changes instead
            ## of every second.
            return Text(txt, style=style), None

        def get_current_song(self):
            """
            Retorna o objeto MusicInfo da música atualmente em reprodução.
            """
            filename = renpy.music.get_playing(channel=self.channel)
            if filename is None:
                return None
            else:
                return self.music_dictionary.get(strip_playback(filename))

        def get_pos(self, style="music_room_text"):
            """
            Retorna a posição da faixa atualmente em reprodução, em segundos.
            """
            return DynamicDisplayable(self.pos_dd, style=style)

        def get_duration(self, style="music_room_text"):
            """
            Retorna a duração da faixa atualmente em reprodução, em segundos.
            """
            return DynamicDisplayable(self.duration_dd, style=style)

        def play(self, filename=None, offset=0, queue=False, strip=False):
            """
            Inicia a reprodução na sala de música. O arquivo que começamos a tocar é
            selecionado em duas etapas.

            Se `filename` for um arquivo desbloqueado, começamos tocando-o.
            Caso contrário, começamos tocando o arquivo atualmente em reprodução, e se
            esse não existir ou não estiver desbloqueado, começamos com o primeiro arquivo.

            Em seguida, aplicamos `offset`. Se `offset` for positivo, avançamos esse
            número de arquivos, caso contrário, retrocedemos esse número de arquivos.

            Se `queue` for verdadeiro, a música é enfileirada. Caso contrário, é tocada
            imediatamente.

            `strip` garante que a música que está configurada para ser tocada
            não tenha informações de reprodução parcial.
            """

            playlist = self.unlocked_playlist(filename)

            if not playlist:
                return

            if filename is None:
                filename = renpy.music.get_playing(channel=self.channel)
            ## Strip out any existing <> information. This ensures the
            ## music room can find songs played via partial playback.
            if filename:
                find_filename = strip_playback(filename)
            else:
                find_filename = None

            try:
                idx = playlist.index(find_filename)
                has_filename = True
            except ValueError:
                has_filename = False
                idx = 0

            idx = (idx + offset) % len(playlist)

            if self.single_track:
                playlist = [ playlist[idx] ]
            elif self.loop:
                playlist = playlist[idx:] + playlist[:idx]
            else:
                playlist = playlist[idx:]

            if self.shuffle and self.loop and self.last_song is None and self.shuffled:
                self.last_song = playlist[idx:][-1]

            if (has_filename and playlist and playlist[0] == find_filename
                    and not queue and not strip):
                # Play the partial playback version of the song.
                playlist.pop(0)
                playlist.insert(0, filename)

            if queue:
                renpy.music.queue(playlist, channel=self.channel, loop=self.loop)
            else:
                renpy.music.play(playlist, channel=self.channel,
                    fadeout=self.fadeout, fadein=self.fadein, loop=self.loop)
            renpy.restart_interaction()

        def next(self):
            """
            Toca o próximo arquivo na playlist.
            """

            filename = renpy.music.get_playing(channel=self.channel)
            if filename is None:
                return self.play(None, 0)
            else:
                ## Turn off single track playback and toggle regular looping
                if self.single_track:
                    self.single_track = False
                    self.loop = True
                    ## Reset shuffle if necessary
                    self.shuffle = self.old_shuffle
                return self.play(None, 1)

        def previous(self):
            """
            Toca o arquivo anterior na playlist.
            """
            pos = renpy.music.get_pos(channel=self.channel)
            if pos > 2 or self.single_track:
                ## This starts the current song over again if it's been
                ## playing for more than 2 seconds.
                return self.play(None, 0, strip=True)
            else:
                ## Turn off single track playback and toggle regular looping.
                if self.single_track:
                    self.single_track = False
                    ## Reset shuffle if necessary
                    self.shuffle = self.old_shuffle
                    self.loop = True
                return self.play(None, -1)

        def get_tracklist(self, all_tracks=False):
            """
            Obtém as faixas desbloqueadas desta lista de faixas, ou todas as faixas se
            all_tracks for True. Retorna objetos MusicInfo em vez de
            nomes de arquivos.
            """
            return [self.music_dictionary.get(x) for x in self.playlist
                if all_tracks or self.is_unlocked(x)]

        def unlocked_playlist(self, filename=None):
            """
            Retorna uma lista de nomes de arquivos na playlist que foram
            desbloqueados.
            """

            if self.shuffle:
                ## Create the shuffle order if it doesn't yet exist, or if
                ## we're starting to shuffle from a new track.
                if self.shuffled is None or (filename
                        and self.shuffled[0] != filename):
                    import random
                    self.shuffled = list(self.playlist)
                    random.shuffle(self.shuffled)

                    if filename in self.shuffled:
                        self.shuffled.remove(filename)
                        self.shuffled.insert(0, filename)

                playlist = self.shuffled

            else:
                self.shuffled = None
                playlist = self.playlist

            return [ i for i in playlist if self.is_unlocked(i) ]

        def Play(self, filename=None):
            """
            :doc: music_room method

            Esta ação faz com que a sala de música comece a tocar. Se `filename`
            for fornecido, esse arquivo começa a tocar. Caso contrário, o arquivo
            atualmente em reprodução recomeça (se estiver desbloqueado), ou o primeiro
            arquivo começa a tocar.

            Se `filename` for fornecido, os botões com esta ação ficarão insensíveis
            enquanto `filename` estiver bloqueado, e serão selecionados quando `filename`
            estiver tocando.
            """

            if filename is None:
                return self.play

            if filename not in self.filenames:
                raise Exception("{0!r} is not a filename registered with this music room.".format(filename))

            return CustomMusicRoomPlay(self, filename)

        def PlayAction(self):
            """
            Uma ação de conveniência para determinar qual ação deve ser tomada
            quando o botão Play/Pause é pressionado para a sala de música.
            """
            if not (renpy.music.is_playing(channel=self.channel)):
                if self.shuffle:
                    return [SelectedIf(True), self.RandomPlay()]
                else:
                    return [SelectedIf(True), self.Play()]
            else:
                return [SelectedIf(renpy.music.get_pause(channel=self.channel)),
                    self.TogglePause()]

        def CycleLoop(self):
            """
            Uma ação de conveniência para alternar entre as 3 opções de loop:
                sem loop, loop e repetir uma.
            """
            if not self.loop:
                ## Not looping; turn on loop.
                return [SelectedIf(False), self.SetLoop(True)]
            elif not self.single_track:
                ## Looping; toggle repeat one
                return [SelectedIf(True), self.SetSingleTrack(True)]
            else:
                ## Repeat one; turn off loop.
                return [SelectedIf(True), self.SetSingleTrack(False),
                    self.SetLoop(False)]

        def AdjustTrackPos(self, seconds):
            """
            Uma função que pula `seconds` segundos na faixa atualmente em
            reprodução.
            """
            return AdjustTrackPos(seconds, self)

        def SetSingleTrack(self, value):
            """
            Esta ação define o valor da propriedade single_track.
            """
            if value:
                act = [SelectedIf(self.single_track)]
            else:
                act = [SelectedIf(not self.single_track)]

            ## Have to remember the old value of shuffle if we're toggling
            ## single track on.
            if value:
                act.append(SetField(self, "old_shuffle", self.shuffle))
                act.append(SetField(self, "shuffle", False))
            else:
                act.append(SetField(self, "shuffle", self.old_shuffle))
            act.append(SetField(self, "single_track", value))
            act.append(self.queue_if_playing)
            return act

        def SetShuffle(self, value):
            """
            Esta ação define o valor da propriedade shuffle.
            """
            if value:
                act = [SelectedIf(self.old_shuffle)]
            else:
                act = [SelectedIf(not self.old_shuffle)]

            if self.single_track:
                ## Can't *really* toggle shuffle if single track is on,
                ## but we can prep it to be the right value later
                act.append(SetField(self, "old_shuffle", value))
                ## Turn off shuffle if it's not already off
                act.append(SetField(self, "shuffle", False))
            else:
                ## Otherwise, set both to the new value
                act.append(SetField(self, "shuffle", value))
                act.append(SetField(self, "old_shuffle", value))
            ## And queue the music if it's playing
            act.append(self.queue_if_playing)
            return act

        def ToggleShuffle(self):
            """
            Esta ação alterna o valor da propriedade shuffle.
            """
            if self.old_shuffle:
                act = self.SetShuffle(False)
            else:
                act = self.SetShuffle(True)
            act.pop(0)
            act.insert(0, SelectedIf(self.old_shuffle))
            return act


    def adjust_track_pos(seconds, musicroom):
        """
        Uma função que pula `seconds` segundos na faixa atualmente em reprodução.
        Se musicroom for uma Music Room, usará o canal e as informações
        de loop apropriados. Caso contrário, deve ser um nome de canal como "music".
        """
        try:
            channel = musicroom.channel
        except:
            channel = musicroom

        track = renpy.music.get_playing(channel)
        if not track:
            return

        # Strip out any existing <> information
        track = strip_playback(track)

        duration = renpy.music.get_duration(channel)
        if not duration:
            return

        t = renpy.music.get_pos(channel)
        if not t:
            return

        new_t = max(t+seconds, 0)
        new_t = min(new_t, duration)

        adjust_music_released(new_t, musicroom)


    class AdjustTrackPos(Action):
        """
        Uma ação personalizada que usa a reprodução parcial para iniciar a
        reprodução no argumento de segundos fornecido. 'musicroom' deve ser um
        objeto Music Room ou o nome do canal em que a música está sendo tocada.
        """
        def __init__(self, seconds, musicroom):
            self.seconds = seconds
            self.musicroom = musicroom
            try:
                self.channel = musicroom.channel
            except:
                self.channel = musicroom
        def get_sensitive(self):
            return (renpy.music.is_playing(channel=self.channel)
                and not preferences.get_mute(self.channel)
                and preferences.get_volume(self.channel))
        def __call__(self):
            adjust_track_pos(self.seconds, self.musicroom)
            renpy.restart_interaction()


init -100 python in myconfig:
    _constant = True

    ## True if all tracks in the music room should be automatically unlocked
    ## during development. In a release build, tracks will automatically
    ## enforce the unlock condition regardless of the value of this variable,
    ## which only affects development.
    UNLOCK_TRACKS_FOR_DEVELOPMENT = True