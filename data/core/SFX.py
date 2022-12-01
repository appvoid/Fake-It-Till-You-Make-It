import pygame
pygame.mixer.init()

class new:
    """Create a sound object, then appends sfx"""
    def __init__(self):
        
        sfx_path = 'data/assets/audio/sfx/'

        self.sounds = [
            #{'name': 'button', 'sound': pygame.mixer.Sound('assets/data/ui_sfx.wav')},
            {'name': 'wind', 'sound': pygame.mixer.Sound(sfx_path+'405561__inspectorj__wind-realistic-a.mp3')},
            {'name': 'speech1', 'sound': pygame.mixer.Sound(sfx_path+'intruder_ai_speech.wav')},
            {'name': 'sitting', 'sound': pygame.mixer.Sound(sfx_path+'633895__aesterial-arts__squeaky-chair.wav')},
            {'name': 'scene_movement', 'sound': pygame.mixer.Sound(sfx_path+'428417__sofi-om__72-silla-ruedas.wav')},
            {'name': 'scene_movement_2', 'sound': pygame.mixer.Sound(sfx_path+'415935__aiwha__fast-office-chair.wav')},
            {'name': 'squeaky', 'sound': pygame.mixer.Sound(sfx_path+'540148__aidansamuel__chair-squeak.wav')}, 
            {'name': 'squeaky_4', 'sound': pygame.mixer.Sound(sfx_path+'94134__bmaczero__squeakyclick2.wav')},
            {'name': 'printing', 'sound': pygame.mixer.Sound(sfx_path+'545642__johnchu__3d-printer.wav')},
            {'name': 'angry', 'sound': pygame.mixer.Sound(sfx_path+'395921__locontrario23__very-angry-dog.wav')},
            {'name': 'bark', 'sound': pygame.mixer.Sound(sfx_path+'260777__deleted-user-3424813__angry-dog-bark-snarl-with-reverb.wav')},
        ]

        # Volume defaults
        self.volume('button', 0.1)
        self.volume('printing', 0.1)
        self.volume('wind', 0.1)
        self.volume('sitting', 0.07)
        self.volume('speech1', 0.08)
        self.volume('squeaky', 0.04) # pass
        self.volume('squeaky_4', 0.04) # pass
        self.volume('angry', 0.03)
        self.volume('bark', 0.9)
        self.volume('scene_movement', 0.12)

    def volume(self, sound, volume):
        for objc in self.sounds:
            if sound == objc['name']:
                pygame.mixer.Sound.set_volume(objc['sound'], volume)

    def play(self, sound):
        for objc in self.sounds:
            if sound == objc['name']:
                pygame.mixer.Sound.play(objc['sound'])

    def stop(self, sound):
        for objc in self.sounds:
            if sound == objc['name']:
                (objc['sound']).stop()