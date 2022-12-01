# Tools/Webpages: Stable Diffusion, FreeSound, ShotCut, CapCut, Gimp
import os; os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
class new:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    def render(self,main=None,fps=60,bg=None):
        while True:
            self.screen.fill((0, 0, 0))
            if bg: bg.refresh()
            if main: main()
            pygame.display.flip()   # Refresh on-screen display
            self.clock.tick(fps)    # wait until next frame (at 60 FPS)