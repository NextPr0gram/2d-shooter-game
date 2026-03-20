import pygame
import sys
from playerClass import *
from weaponClass import *
from collideClass import *
from mapClass import *
from settings import *
import socket
import json
from _thread import *
import time

# setup
pygame.init()
client_id = 0
font = pygame.font.Font("freesansbold.ttf", 25)

def show_text(x, y, text, colour):
    text = font.render(text, True, BLACK)
    SCREEN.blit(text, (x, y))

player_group = pygame.sprite.Group()
other_group = pygame.sprite.Group()
waiting = True

pygame.display.set_caption("game")



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.21"
server = "127.0.0.1"
port = 50103
addr = (server, port)

commands = []

def send(data):

    try:
        if socket != None:
            socket.send(json.dumps(data).encode())

    except socket.error as e:
        print(e)


def move_others(x, y, direction, player_number):

    #cmd = {"Command": "MOVE", "X": x, "Y": y, "DIRECTION": direction}
    cmd = {"Command": "MOVE", "DIR": direction, "PLAYER_NUMBER": player_number}
    #send(cmd)
    commands.append(cmd)

def shoot_others(angle, player_number):

    cmd = {"Command": "SHOOT", "ANGLE":angle, "PLAYER_NUMBER": player_number}
    send(cmd)
    commands.append(cmd)
def rotate_others(angle, player_number):
    cmd = {"Command":"ROTATE", "ANGLE": angle,"PLAYER_NUMBER": player_number}
    send(cmd)
    commands.append(cmd)
"""counter = 0
def rotate_timer(angle):
    global counter
    counter+=1
    if counter == 10:
        rotate_others(angle)
        counter = 0"""

def game(p1):
    # timer
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, p1.weapon.firerate)
    shooting = False
    send_angle = pygame.USEREVENT+2
    pygame.time.set_timer(send_angle, 100)


    fullscreen = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    p1.speed = PLAYER_SPEED / 2
                if event.key == pygame.K_F11:
                    if not fullscreen:
                        pygame.display.toggle_fullscreen()
                        fullscreen = True
                    elif fullscreen:
                        pygame.display.toggle_fullscreen()
                        fullscreen = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    p1.speed = PLAYER_SPEED
            if event.type == pygame.MOUSEBUTTONDOWN:
                shooting = True
            if event.type == pygame.MOUSEBUTTONUP:
                shooting = False
            if event.type == timer_event and shooting:
                p1.shoot()

                shoot_others(p1.angle, p1.player_number)

            #if event.type == send_angle:
                #rotate_others(p1.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if not p1.collide_with_walls_top():
                p1.moveUp()
                #p2.player_y += PLAYER_SPEED
                move_others(p1.get_player_pos()[0], p1.get_player_pos()[1], "up", p1.player_number)

        if keys[pygame.K_s]:
            if not p1.collide_with_walls_bottom():
                p1.moveDown()
                move_others(p1.get_player_pos()[0], p1.get_player_pos()[1], "down", p1.player_number)
#
        if keys[pygame.K_a]:
            if not p1.collide_with_walls_left():
                p1.moveLeft()
                move_others(p1.get_player_pos()[0], p1.get_player_pos()[1], "left", p1.player_number)

        if keys[pygame.K_d]:
            if not p1.collide_with_walls_right():
                p1.moveRight()
                move_others(p1.get_player_pos()[0], p1.get_player_pos()[1], "right", p1.player_number)

        for bullet in bullets_group:
            bullet.update()
            if bullet.bullet_colliding(bullet):
                bullets_group.remove(bullet)
                #add player damage
        #if pygame.time.get_ticks()% FPS/5 == 0:
        #    rotate_others(p1.angle, p1.player_number)
         #   print(p1.angle)


        pygame.display.flip()
        # SCREEN.blit(pygame.image.load(BG).convert(), (0, 0))
        SCREEN.fill(WHITE)
        #floor_group.draw(SCREEN)
        other_group.draw(SCREEN)
        player_group.draw(SCREEN)


        wall_group.draw(SCREEN)
        player_group.update()
        other_group.update()
        show_text(10, 10, ("Player: "+ str(client_id+1)), BLACK)
        show_text(10, 35, ("Angle: "+ str(p1.angle)), BLACK)
        show_text(10, 60, ("Position: "+ "X="+ str(round(p1.get_player_pos()[0]))+ " Y="+ str(round(p1.get_player_pos()[1]))), BLACK)
        for x, other in enumerate(other_group):
            show_text(10, 85+(25*x), ("player: "+str(x+1)+ "X="+ str(round(other.get_player_pos()[0]))+ " Y="+ str(round(other.get_player_pos()[1]))), BLACK)
        for bullets in bullets_group:
            bullets.draw(SCREEN)
        for command in commands:
            send(command)
            commands.remove(command)
            time.sleep(0.01)
        CLOCK.tick(FPS)


# game()

def process_command(cmd):
    global waiting, p1, p2, p3, p4, p5, p6, client_id
    if cmd["Command"] == "Start":
        client_id = cmd["client_id"]
        # swap_players(client_id)
        # Probably want to create the players here - but we need to know where they will be (x,y)

        if client_id == 0:

            p1 = Player(1, PLAYER_TEXTURE_1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, False)
            p2 = Player(2, PLAYER_TEXTURE_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p3 = Player(3, PLAYER_TEXTURE_3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p4 = Player(4, PLAYER_TEXTURE_4, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p5 = Player(5, PLAYER_TEXTURE_5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p6 = Player(6, PLAYER_TEXTURE_6, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)

        elif client_id == 1:

            p1 = Player(2, PLAYER_TEXTURE_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, False)
            p2 = Player(3, PLAYER_TEXTURE_3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p3 = Player(4, PLAYER_TEXTURE_4, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p4 = Player(5, PLAYER_TEXTURE_5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p5 = Player(6, PLAYER_TEXTURE_6, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p6 = Player(1, PLAYER_TEXTURE_1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)

        elif client_id == 2:

            p1 = Player(3, PLAYER_TEXTURE_3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, False)
            p2 = Player(4, PLAYER_TEXTURE_4, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p3 = Player(5, PLAYER_TEXTURE_5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p4 = Player(6, PLAYER_TEXTURE_6, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p5 = Player(1, PLAYER_TEXTURE_1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p6 = Player(2, PLAYER_TEXTURE_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)

        elif client_id == 3:

            p1 = Player(4, PLAYER_TEXTURE_4, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, False)
            p2 = Player(5, PLAYER_TEXTURE_5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p3 = Player(6, PLAYER_TEXTURE_6, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p4 = Player(1, PLAYER_TEXTURE_1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p5 = Player(2, PLAYER_TEXTURE_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p6 = Player(3, PLAYER_TEXTURE_3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)

        elif client_id == 4:

            p1 = Player(5, PLAYER_TEXTURE_5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, False)
            p2 = Player(6, PLAYER_TEXTURE_6, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p3 = Player(1, PLAYER_TEXTURE_1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p4 = Player(2, PLAYER_TEXTURE_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p5 = Player(3, PLAYER_TEXTURE_3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p6 = Player(4, PLAYER_TEXTURE_4, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)

        elif client_id == 5:

            p1 = Player(6, PLAYER_TEXTURE_6, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, False)
            p2 = Player(1, PLAYER_TEXTURE_1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p3 = Player(2, PLAYER_TEXTURE_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p4 = Player(3, PLAYER_TEXTURE_3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p5 = Player(4, PLAYER_TEXTURE_4, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
            p6 = Player(5, PLAYER_TEXTURE_5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)



        player_group.add(p1)

        other_group.add(p2)
        other_group.add(p3)
        other_group.add(p4)
        other_group.add(p5)
        other_group.add(p6)

        waiting = False  # ready to play now

    if cmd["Command"] == "MOVE":

        for other in other_group:
            if cmd["PLAYER_NUMBER"] == other.player_number:
                #print("MOVING OTHER", cmd)
                if cmd["DIR"] == "up":
                    other.rect.y -= PLAYER_SPEED
                    p1.player_y += PLAYER_SPEED

                if cmd["DIR"] == "down":
                    other.rect.y += PLAYER_SPEED
                    p1.player_y -= PLAYER_SPEED

                if cmd["DIR"] == "left":
                    other.rect.x-= PLAYER_SPEED
                    p1.player_x += PLAYER_SPEED

                if cmd["DIR"] == "right":
                    other.rect.x += PLAYER_SPEED
                    p1.player_x -= PLAYER_SPEED

    if cmd["Command"] == "SHOOT":
        for other in other_group:
            if cmd["PLAYER_NUMBER"] == other.player_number:
                bullets_group.add(Bullet(other.player_x, other.player_y, cmd["ANGLE"]))
    if cmd["Command"] == "ROTATE":
        for other in other_group:
            if cmd["PLAYER_NUMBER"] == other.player_number:
                other.angle = cmd["ANGLE"]
                other.rotate()
                other.update()

def receive_message():
    while True:
        response = socket.recv(1024 * 16)
        if response:
            #print("RECIEVED", response)
            cmd = json.loads(response.decode())
            #print(cmd)
            process_command(cmd)


try:

    p1 = Player(1, PLAYER_TEXTURE_1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, False)
    p2 = Player(2, PLAYER_TEXTURE_2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
    p3 = Player(3, PLAYER_TEXTURE_3, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
    p4 = Player(4, PLAYER_TEXTURE_4, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
    p5 = Player(5, PLAYER_TEXTURE_5, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
    p6 = Player(6, PLAYER_TEXTURE_6, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle, other_group, True)
    socket.connect(addr)
    print("Connection established")
    start_new_thread(receive_message, ())
    print("thread created")
    while waiting == True:
        pass

    game(p1)  # pass the players in as parameters
except error as e:
    print(error)
    quit()
