from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

random_point_list = [(random.randint(-400, 400), random.randint(-500, 500)) for n in range(20)]

n = 1
frame = 0

def draw_character(p1, p2):
    clear_canvas()
    KPU_GROUND.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t)*p1[0]+t*p2[0]
        y = (1 - t)*p1[1]+t*p2[1]
        run_character.clip_draw(frame * 100, 0, 100, 100, x, y)

open_canvas(KPU_WIDTH, KPU_HEIGHT)

KPU_GROUND = load_image('KPU_GROUND.png')
run_character = load_image('animation_sheet.png')

while True:
    draw_character(random_point_list[n - 1], random_point_list[n])
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)