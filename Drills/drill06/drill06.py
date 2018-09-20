from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global a, b
    global num1, num2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                a, b = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
a, b = KPU_WIDTH // 2, KPU_HEIGHT // 2
num1, num2 = 0, 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, num1 - 25, num2 + 25)
    hand_arrow.draw(x, y)
    update_canvas()
    frame = (frame + 1) % 8

    if(num1 <= a and num2 <= b):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, num1 - 25, num2 + 25)
        hand_arrow.draw(x, y)
        update_canvas()
        frame = (frame + 1) % 8
        num1 += 1
        num2 += 1

        delay(0.0002)
        handle_events()

    if(num1 > a and num2 > b):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, num1 - 25, num2 + 25)
        hand_arrow.draw(x, y)
        update_canvas()
        frame = (frame + 1) % 8
        num1 -= 1
        num2 -= 1

        delay(0.0002)
        handle_events()

    if(num1 <= a and num2 > b):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, num1 - 25, num2 + 25)
        hand_arrow.draw(x, y)
        update_canvas()
        frame = (frame + 1) % 8
        num1 += 1
        num2 -= 1

        delay(0.0002)
        handle_events()

    if(num1 > a and num2 <= b):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, num1 - 25, num2 + 25)
        hand_arrow.draw(x, y)
        update_canvas()
        frame = (frame + 1) % 8
        num1 -= 1
        num2 += 1

    delay(0.0002)
    handle_events()
close_canvas()


