# Flor de Neve

init python:
    
    import random
    
    random.seed()
    
    #################################################################
    # Partículas de neve
    # ----------------
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        Esta função cria o efeito de neve. Você deve usá-la em vez de instanciar
        a SnowFactory diretamente (bem, na verdade não importa, mas economiza digitação se você
        estiver usando os valores padrão =D)
        
        @param {image} image:
            A imagem usada como flocos de neve. Deve ser sempre um arquivo de imagem ou um objeto im,
            já que aplicaremos transformações de imagem nela.
        
        @param {int} max_particles:
            O número máximo de partículas simultaneamente na tela.
            
        @param {float} speed:
            A velocidade vertical base das partículas. Quanto maior o valor, mais rápido as partículas cairão.
            Valores abaixo de 1 serão alterados para 1.
            
        @param {float} wind:
            A força máxima do vento que será aplicada às partículas.
            
        @param {Tuple ({int} min, {int} max)} xborder:
            O alcance da borda horizontal. Um valor aleatório entre esses dois será aplicado ao criar as partículas.
            
        @param {Tuple ({int} min, {int} max)} yborder:
            O alcance da borda vertical. Um valor aleatório entre esses dois será aplicado ao criar as partículas.
            Quanto maiores os valores, mais longe da tela elas serão criadas.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    # ---------------------------------------------------------------
    class SnowFactory(object):
        """
        A fábrica que cria as partículas que usamos no efeito de neve.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Inicializa a fábrica. Os parâmetros são os mesmos da função Snow.
            """            
            self.max_particles = max_particles
            
            self.speed = speed
            
            self.wind = wind
            
            self.xborder = xborder
            self.yborder = yborder
            
            self.depth = kwargs.get("depth", 10)
            
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            """
            Esta função é chamada internamente a cada quadro pelo objeto Particles para criar novas partículas.
            Nós só criaremos novas partículas se o número de partículas na tela for
            menor que o número máximo de partículas que podemos ter.
            """
            if particles is None or len(particles) < self.max_particles:
                
                depth = random.randint(1, self.depth)
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # a imagem usada pela partícula 
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # força do vento
                                      self.speed*depth_speed,  # a velocidade vertical da partícula
                                      random.randint(self.xborder[0], self.xborder[1]), # borda horizontal
                                      random.randint(self.yborder[0], self.yborder[1]), # borda vertical
                                      ) ]
        
        
        def image_init(self, image):
            """
            Esta função é chamada internamente para inicializar as imagens.
            Ela criará uma lista de imagens com tamanhos diferentes, para que
            possamos prever todas e usar as versões em cache para torná-la mais eficiente em termos de memória.
            """
            rv = [ ]
            
            for depth in range(self.depth):
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):
            """
            Esta função é chamada internamente pelo objeto Particles para prever as imagens que as partículas
            estão usando. Espera-se que ela retorne uma lista de imagens para prever.
            """ 
            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):
        """
        Representa cada partícula na tela.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Inicializa a partícula de neve. É chamada automaticamente quando o objeto é criado.
            """
            
            self.image = image
            
            if speed <= 0:
                speed = 1
                
            self.wind = wind
            
            self.speed = speed

            self.oldst = None
                      
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            """
            Chamada internamente em cada quadro para atualizar a partícula.
            """
            
            # calcula o atraso (lag)
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None
                
            return int(self.xpos), int(self.ypos), st, self.image
