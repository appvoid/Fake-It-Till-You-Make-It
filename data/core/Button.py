import pygame
pygame.font.init()
class new:
    """Create a button, then blit the surface in the while loop"""
    def __init__(self, text,  pos=[0,0], size=32, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Ubuntu",size=size)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
    
    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def render(self,screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event, color='black', action=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg=color)
                    if action != None:
                        action()