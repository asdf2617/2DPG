import game_framework
from pico2d import *
import main_state


name = "PauseState"
image = None


def enter():
    global image
    global blink
    blink = 0
    image = load_image('pause(change).png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                resume()
    pass


def draw():
    clear_canvas()
    main_state.draw()
    if(blink < 1):
        image.draw(400, 300)
    update_canvas()
    pass


def update():
    global blink
    blink = (blink + 0.05) % 4
    pass


def pause():
    pass


def resume():
    game_framework.pop_state()
    pass

