# TODO: Set progress bar for mask printing ✅
# TODO: Set recognition level for animatronic ✅
# TODO: Set bad ending (animatronic enters the house and kills you) ✅
# TODO: Set bad ending 2 (police gets into the house and gets you) 
# TODO: Set good ending (escaped from the house with a mask of the owner)
# TODO: Main menu
# TODO: Pause menu
# TODO: Credits scene
# TODO: Gamepad support 🔽
# TODO: Project cleaning 🔽
# TODO: Uploading to Github, itch.io and announcement through Twitter 🔽 


# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰
# 				'''Source code of "Fake It Till You Make It" by appvoid'''						 #
# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰
# Packages 📦
# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰
from data.core import Window, SFX, Events, Player, BGMotion, Timer
from pygame.locals import *
import pygame, random, os
#
# Loaders and inits 📤
# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰
win, timer = Window.new(), Timer.new()
player, sfx, event, layer = Player.new(), SFX.new(), Events.new(), BGMotion.Layer(win.screen)
layer.add(BGMotion.BG(win.screen, player.position))

# Globals 'n General vars
W, H = win.screen.get_width(), win.screen.get_height()
red_screen = pygame.Surface((W,H), pygame.SRCALPHA)

time_elapsed_since_last_animatronic_action = 0
time_elapsed_since_last_wind_sound_playback = 0
time_elapsed_since_last_second = 0

seconds_clock = 0
time_limit = 211 # 180 seconds = 3 minutes and 30 seconds till police reaches home

clock = pygame.time.Clock()

GAME_OVER = False

POLICE_TIMER = ''

OPERATION_COMPLETED = False
PRINTING_PROGRESS = 0
PRINTING_PROGRESS_SPEED = 0.025

WIND_SOUND_TIMING_THRESHOLD = 47999 # 48 seconds, the time it takes to finish sound

LAPTOP_TEXT_ALPHA = 0
ANIMATRONIC_ALPHA = 0

ANIMATRONIC_ROOMS = ['front','left','right']

ANIMATRONIC_PATIENCE_THRESHOLD = 5
ANIMATRONIC_FACE_RECOGNIZED = 0

ANIMATRONIC_TIMING_THRESHOLD = 1000 # Animatronic changes room each 1 second
ANIMATRONIC_TIMING_FACTOR = 100 # Animatronic will slow 100 ms each time it moves

ANIMATRONIC_SIZE_POSITION_RIGHT = (W*0.20,H*0.20)
ANIMATRONIC_SIZE_POSITION_FRONT = (W*0.25,H*0.25)
ANIMATRONIC_SIZE_POSITION_LEFT = (W*0.45,H*0.45)

ANIMATRONIC_SCREEN_POSITION_RIGHT = (W*0.5,H*0.13)
ANIMATRONIC_SCREEN_POSITION_FRONT = (W*0.65,H*0.35)
ANIMATRONIC_SCREEN_POSITION_LEFT = (W*0.55,H*0.36)

ANIMATRONIC_CURRENT_SCREEN_POSITION = (0,0)
ANIMATRONIC_CURRENT_SIZE = (0,0)

ANIMATRONIC_ACTIVATION_DELAY = 10000 # ten seconds
ANIMATRONIC_HEAD_MOVEMENT = 0.1

# Fonts
pygame.font.init()
font = pygame.font.SysFont("Arial", 128)
game_font = pygame.font.SysFont('Ubuntu', 16)
progress_txt = font.render('Printing progress', False, (255, 255, 255))
progress_txt_render = pygame.transform.scale(progress_txt, (128, 17))

# Laptop font
laptop_text = 'Model loaded'
laptop_text_render = pygame.transform.rotate(game_font.render(laptop_text, False, (25, 175, 125)), 1)

# Timer text
timer_text_render = game_font.render('', False, (255, 255, 255))

# Animatronic
animatronic = pygame.image.load('data/assets/sprites/animatronic.png').convert_alpha()
resized_animatronic = pygame.transform.scale(animatronic, (W*0.25,H*0.25))
animatronic_position = 'back'

# Functions 🔗
# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰

def play_wind_sound():
    sfx.play('wind')

def player_not_moving():
    player.is_moving = False
    if player.position == animatronic_position:
        sfx.play('angry')

def player_moving(new_position):
    sfx.stop('angry')
    sfx.play(random.choice(['squeaky','squeaky_4']))
    sfx.play('scene_movement')
    player.position = new_position
    player.is_moving = True
    timer.wait(1.55, player_not_moving) # delay to avoid issues when transitioning to another room
    layer.fade(win.screen, new_position)

def handle_player_movement():
    sfx.stop('printing')
    global laptop_text, laptop_text_render, PRINTING_PROGRESS, LAPTOP_TEXT_ALPHA

    if not player.is_moving:
        corner_threshold = 128
        mouse_x, mouse_y = pygame.mouse.get_pos()
        left_corner_click = mouse_x < corner_threshold
        # upper_corner_click = mouse_y < corner_threshold
        right_corner_click = mouse_x > (win.screen.get_width() - corner_threshold)
        lower_corner_click = mouse_y > (win.screen.get_height() - corner_threshold)

        if player.position == 'front':
            if left_corner_click: player_moving('left')
            elif right_corner_click: player_moving('right')
            
            if OPERATION_COMPLETED == False:
                if lower_corner_click:
                    sfx.play('printing')
                    LAPTOP_TEXT_ALPHA = 0
                    laptop_text = 'Printing mask_05_.obj...'
                    laptop_text_render = pygame.transform.rotate(game_font.render(laptop_text, False, (25, 175, 125)), 1)
                else:
                    sfx.stop('printing')
                    LAPTOP_TEXT_ALPHA = 0
                    laptop_text = 'Operation Paused'
                    laptop_text_render = pygame.transform.rotate(game_font.render(laptop_text, False, (25, 175, 125)), 1)

        elif player.position == 'left':
            if right_corner_click: player_moving('front'); sfx.stop('printing')

        elif player.position == 'right':
            if left_corner_click: player_moving('front'); sfx.stop('printing')

def handle_animatronic_movement():
    global ANIMATRONIC_TIMING_THRESHOLD, ANIMATRONIC_ROOMS, ANIMATRONIC_TIMING_FACTOR 
    global animatronic_position
    ANIMATRONIC_TIMING_THRESHOLD += ANIMATRONIC_TIMING_FACTOR

    if animatronic_position == 'front' or animatronic_position == 'back':
        animatronic_position = random.choice(ANIMATRONIC_ROOMS)
    elif animatronic_position == 'left' or animatronic_position == 'left':
        animatronic_position = random.choice(['left','front'])
    elif animatronic_position == 'right':
        animatronic_position = random.choice(['right','front'])

    if player.position == animatronic_position:
        sfx.play('angry')
    else:
        sfx.stop('angry')

def reload_animatronic_size(size):
    global resized_animatronic
    resized_animatronic = pygame.transform.scale(animatronic, size)

def stop_sounds():
    pygame.mixer.init()

def kill_game():
    os.system('killall python3 && sleep 0.1 && python3 launcher.py')

# Renderer 🌌
# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰

def loop():
    # General variables
    global GAME_OVER
    global OPERATION_COMPLETED
    global PRINTING_PROGRESS
    global PRINTING_PROGRESS_SPEED
    global LAPTOP_TEXT_ALPHA
    global ANIMATRONIC_ALPHA
    global ANIMATRONIC_CURRENT_SCREEN_POSITION
    global ANIMATRONIC_CURRENT_SIZE
    global ANIMATRONIC_SIZE_POSITION_FRONT
    global ANIMATRONIC_SIZE_POSITION_LEFT
    global ANIMATRONIC_SIZE_POSITION_RIGHT
    global ANIMATRONIC_TIMING_THRESHOLD
    global ANIMATRONIC_FACE_RECOGNIZED
    global ANIMATRONIC_PATIENCE_THRESHOLD
    global ANIMATRONIC_HEAD_MOVEMENT
    global ANIMATRONIC_ACTIVATION_DELAY
    global POLICE_TIMER

    global timer_text_render
    global seconds_clock
    global time_limit
    global time_elapsed_since_last_second
    global time_elapsed_since_last_wind_sound_playback
    global time_elapsed_since_last_animatronic_action
    global resized_animatronic, animatronic_position
    global laptop_text, laptop_text_render, progress_txt_render

    dt = clock.tick()

        # Global Events 📜
    # ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥰

    if not GAME_OVER:
        event.listen([ 
            [ MOUSEBUTTONDOWN, handle_player_movement ]
        ])
        # Live Code 🎮
    # ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥰

        # Timers
        # Thanks to @Shashank for giving a helpful answer about timers
        # https://stackoverflow.com/questions/18948981/do-something-every-x-milliseconds-in-pygame
        time_elapsed_since_last_animatronic_action += dt
        time_elapsed_since_last_wind_sound_playback += dt
        time_elapsed_since_last_second += dt
        seconds_clock += dt

        # Seconds timer
        # Thanks to https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
        if seconds_clock >= 1000:
            time_limit -= 1
            mins, secs = divmod(time_limit, 60)
            POLICE_TIMER = '{:02d}:{:02d}'.format(mins, secs) # Sets global timer
            timer_text_render = game_font.render(POLICE_TIMER, False, (255, 255, 255))
            seconds_clock = 0 # resets timer for the next second

            if time_limit <= 0:

                timer.wait(1,kill_game)

        # dt is measured in milliseconds, therefore 500 ms = 0.5 seconds
        if time_elapsed_since_last_second >= ANIMATRONIC_ACTIVATION_DELAY: # wait 10 seconds to activate animatronic
            if time_elapsed_since_last_animatronic_action > ANIMATRONIC_TIMING_THRESHOLD:
                handle_animatronic_movement() # animatronic move
                time_elapsed_since_last_animatronic_action = 0 # reset it to 0 so you can count again

        # dt is measured in milliseconds, therefore 500 ms = 0.5 seconds
        if time_elapsed_since_last_wind_sound_playback > WIND_SOUND_TIMING_THRESHOLD:
            play_wind_sound()
            time_elapsed_since_last_wind_sound_playback = 0 # reset it to 0 so you can count again

        # Alpha objects and animatronic's logic
        if player.position == animatronic_position and not player.is_moving:
            if ANIMATRONIC_ALPHA < 255:
                ANIMATRONIC_ALPHA += 10
                if animatronic_position == 'front': 
                    ANIMATRONIC_CURRENT_SCREEN_POSITION = ANIMATRONIC_SCREEN_POSITION_FRONT
                    reload_animatronic_size(ANIMATRONIC_SIZE_POSITION_FRONT)
                elif animatronic_position == 'left':
                    ANIMATRONIC_CURRENT_SCREEN_POSITION = ANIMATRONIC_SCREEN_POSITION_LEFT
                    reload_animatronic_size(ANIMATRONIC_SIZE_POSITION_LEFT)
                elif animatronic_position == 'right': 
                    ANIMATRONIC_CURRENT_SCREEN_POSITION = ANIMATRONIC_SCREEN_POSITION_RIGHT
                    reload_animatronic_size(ANIMATRONIC_SIZE_POSITION_RIGHT)
            elif ANIMATRONIC_ALPHA >= 255:
                if ANIMATRONIC_FACE_RECOGNIZED < 100:
                    ANIMATRONIC_FACE_RECOGNIZED += ANIMATRONIC_PATIENCE_THRESHOLD
        else:
            if ANIMATRONIC_ALPHA > 0: ANIMATRONIC_ALPHA -= 10

        # os.system('clear')

        if ANIMATRONIC_FACE_RECOGNIZED >= 100:
            timer.wait(0.3, stop_sounds)
            sfx.play('bark')
            reload_animatronic_size((W*1.5+ANIMATRONIC_HEAD_MOVEMENT,H*1.5+ANIMATRONIC_HEAD_MOVEMENT))
            timer.wait(0.5,kill_game)
            GAME_OVER = True

        if ANIMATRONIC_FACE_RECOGNIZED >= 1: ANIMATRONIC_FACE_RECOGNIZED -= ANIMATRONIC_PATIENCE_THRESHOLD*0.1
        #print(ANIMATRONIC_FACE_RECOGNIZED)

        if player_moving and LAPTOP_TEXT_ALPHA > 0: LAPTOP_TEXT_ALPHA -= 15

        if not player.is_moving and player.position == 'front':
            if LAPTOP_TEXT_ALPHA < 255: LAPTOP_TEXT_ALPHA += 40

        # Progress bar
        if laptop_text == 'Printing mask_05_.obj...' and not OPERATION_COMPLETED and PRINTING_PROGRESS < 100:
            PRINTING_PROGRESS += PRINTING_PROGRESS_SPEED
        if PRINTING_PROGRESS >= 100 and OPERATION_COMPLETED == False:
            OPERATION_COMPLETED = True
            sfx.stop('printing')
            laptop_text = 'Operation completed'
            laptop_text_render = pygame.transform.rotate(game_font.render(laptop_text, False, (25, 175, 125)), 1)

        # resized_animatronic.set_alpha(ANIMATRONIC_ALPHA)
        laptop_text_render.set_alpha(LAPTOP_TEXT_ALPHA)
        timer_text_render.set_alpha(100)

        win.screen.blit(laptop_text_render, (W*0.51,H*0.69))

        win.screen.blit(timer_text_render, (W*0.01,H*0.01))

        # Progess UI
        if not OPERATION_COMPLETED:
            progress_txt_render.set_alpha(100)
            win.screen.blit(progress_txt_render, (W*0.01, H*0.97))
            pygame.draw.rect(win.screen, 'white', pygame.Rect(0, H-4, (W*PRINTING_PROGRESS)/100,1))
        else:
            animatronic_position = 'back'

        ##############################################################################################
        # Controller support coming soon!
        # def handle_player_movement_gamepad(pos=None):
        # if not player.is_moving:
        #
        #     if player.position == 'front':
        #         if pos=='left': player_moving('left')
        #         elif pos=='right': player_moving('right')
        #
        #     elif player.position == 'left':
        #         if pos=='right': player_moving('front')
        #
        #     elif player.position == 'right':
        #         if pos=='left': player_moving('front')
        # pygame.joystick.init()
        # controller1 = pygame.joystick.Joystick(0)
        # controller1.init()
        # GET AXIS
        # AXIS_X_controller1 = controller1.get_axis(0) #AXIS_X
        # AXIS_Y_controller1 = controller1.get_axis(1) #AXIS_Y
        # print(str(AXIS_X_controller1))
        # print (str(AXIS_Y_controller1))
        # #GET_ID (pygame.joystick.Joystick.get_id)
        # print("DEVICE ID > "+str(controller1.get_id()))
        # #GET_NAME(pygame.joystick.Joystick.get_name)
        # print ("DEVICE NAME > " + str(controller1.get_name()))
        # #GET NUM AXES(pygame.joystick.Joystick.get_numaxes)
        # print ("NUMAXES > "+str(controller1.get_numaxes()))
        # #GET BUTTON(pygame.joystick.Joystick.get_button)
        # for check in range(0,11):
        #     if controller1.get_button(4) ==1:
        #         handle_player_movement_gamepad('left')
        #     elif controller1.get_button(5) ==1:
        #         handle_player_movement_gamepad('right')
        #     print ("BUTTON" +str (check) + " > " + str(controller1.get_button(check)))
        ##############################################################################################

    else:
        event.listen()
        global red_screen
        ANIMATRONIC_HEAD_MOVEMENT += 10
        if ANIMATRONIC_HEAD_MOVEMENT < 255:
            red_screen.fill((255,0,0,ANIMATRONIC_HEAD_MOVEMENT))
        else:
            red_screen.fill((255,0,0,255))
        win.screen.blit(red_screen, (0,0))
        ANIMATRONIC_CURRENT_SCREEN_POSITION = (-W*0.25,-H*0.5+ANIMATRONIC_HEAD_MOVEMENT)
        win.screen.blit(resized_animatronic, ANIMATRONIC_CURRENT_SCREEN_POSITION)

# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰

# Start 🏴
# ⦿ ⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥪⥫⥰

sfx.play('sitting')
play_wind_sound()
sfx.play('speech1')

win.render(loop, bg=layer) # Loop ∞
