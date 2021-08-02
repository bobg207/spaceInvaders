import pygame as pg
import sprites
from settings import *


pg.init()

# Set Base Screen
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Space Invaders")

playing = True

clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
enemy_sprites = pg.sprite.Group()

for row in range(len(LAYOUT)):
    for col in range(len(LAYOUT[row])):
        if LAYOUT[row][col] == '1':
            enemy = sprites.Enemy(GREEN, 40, 30, col * 50, 50 + row * 40)
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)
        elif LAYOUT[row][col] == '3':
            player = sprites.Player(YELLOW, 30, 30, WIDTH // 2, HEIGHT - 50)
            all_sprites.add(player)


while playing:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.velo = -5
            elif event.key == pg.K_RIGHT:
                player.velo = 5
        elif event.type == pg.KEYUP:
            player.velo = 0

    all_sprites.update()

    screen.fill(BLACK)

    enemy_sprites.draw(screen)
    player.draw(screen)

    pg.display.flip()

    clock.tick(FPS)

pg.quit()
