# Simple library wrapper for pygame animated backgrounds
import pygame, os
from threading import Timer
class Layer(pygame.sprite.Group):
    def __init__(self, screen):
        pygame.sprite.Group.__init__(self)
        self.screen = screen
    
    def refresh(self):
        self.draw(self.screen)
        self.update()

    def fade(self, screen, scene):
        try: # hacky way to check if a transition is running
            if self.sprites()[0].alpha > 250 and len(self.sprites()) < 2:
                for bg in self.sprites():
                    bg.fade = True
                Timer(0, lambda: self.add(BG(screen, scene)), args=None, kwargs=None).start()
        except: pass

class BG(pygame.sprite.Sprite):
    def __init__(self, screen, path, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.fade = False
        self.fade_amount = 45
        
        for f in self.sprites_in_path('data/assets/mbg/'+path):
            self.images.append(pygame.transform.scale(pygame.image.load(f), (screen.get_width(), screen.get_height())))

        self.index = 0
        self.image = self.images[self.index]; self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.rect.topleft = [x, y]
        self.counter = 0; self.alpha = 0
    
    def sprites_in_path(self,_path):
        res = []
        for path in os.listdir(_path):    
            if os.path.isfile(os.path.join(_path, path)): res.append(_path+'/'+path)
        res.sort(); return res

    def update(self):
        speed = .1
        self.counter += 1;
        if self.counter >= speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]; self.image.set_alpha(self.alpha)

        if self.index >= len(self.images) - 1 and self.counter >= speed:
            self.counter = 0; self.index = 0

        if self.alpha > 300:
            self.alpha = 300

        if self.fade == True:
            self.alpha -= self.fade_amount
            if self.alpha < 0:
                self.kill()

        else:
            self.alpha += self.fade_amount