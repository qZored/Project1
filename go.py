import pygame
import hero

DARKBACKGROUND = (54, 55, 55)
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("My best game")
clock = pygame.time.Clock()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
DONE = False
FPS = 30

my_hero = hero.Hero(7, 7, 7, 2, 1, 1)
move_x = 0
move_y = 0
enemy = hero.Enemy()

while not DONE:

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                DONE = True
                quit()

            if event.key == pygame.K_w:
                hero.hero_move[1] = -3

            if event.key == pygame.K_s:
                hero.hero_move[1] = 3

            if event.key == pygame.K_a:
                hero.hero_move[0] = -3

            if event.key == pygame.K_d:
                hero.hero_move[0] = 3

            if event.key == pygame.K_UP:
                hero.Bullet(my_hero.get_position(), (0, -5), True)

            if event.key == pygame.K_DOWN:
                hero.Bullet(my_hero.get_position(), (0, 5), True)

            if event.key == pygame.K_LEFT:
                hero.Bullet(my_hero.get_position(), (-5, 0), True)

            if event.key == pygame.K_RIGHT:
                hero.Bullet(my_hero.get_position(), (5, 0), True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                hero.hero_move[1] = 0

            if event.key == pygame.K_a or event.key == pygame.K_d:
                hero.hero_move[0] = 0

    screen.fill(DARKBACKGROUND)
    hero.all_bullets.draw(screen)
    hero.all_bullets.update()
    hero.hero_group.draw(screen)
    hero.hero_group.update()
    hero.enemy_group.draw(screen)
    hero.enemy_group.update()
    clock.tick(FPS)
    pygame.display.flip()
