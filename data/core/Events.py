import pygame
class new:
    def __init__(self):
        pass
    def listen(self, args=None):
        '''Receives an array of objects with listeners'''
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            # Custom events
            if args != None:
                for arr in args:
                    if arr[0] == event.type:
                        arr[1]()