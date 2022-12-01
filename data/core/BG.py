import pygame, os
class load (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, path, win, loop=False):
        super().__init__()
        self.path = path
        self.loop = loop
        self.looping_back = False
        self.sprites = []
        self.velocity = 0.25
        self.backgrounds = pygame.sprite.Group()
        for f in self.sprites_in_path(self.path):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f), (win.screen.get_width(), win.screen.get_height())))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def sprites_in_path(self,_path):
        res = []
        for path in os.listdir(_path):    
            if os.path.isfile(os.path.join(_path, path)): res.append(_path+'/'+path)
        res.sort(); return res

    def update(self):
        counter_addition = 1
        
        if self.loop == True:
            if self.looping_back == False:
                if self.current_sprite > len(self.sprites):
                    self.current_sprite = len(self.sprites)-1
                    self.looping_back = True
                    self.current_sprite -= counter_addition+1
                self.current_sprite += counter_addition
            else:
                if self.current_sprite < 0:
                    self.current_sprite = 1
                    self.looping_back = False
                    self.current_sprite += counter_addition+1
                self.current_sprite -= counter_addition

        else:
            self.current_sprite += counter_addition
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite*self.velocity-0.1)]