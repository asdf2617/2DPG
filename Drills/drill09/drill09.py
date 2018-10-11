from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= speed_change_list[list_num]

        if self.y < 60:
            speed_change_list[list_num] = 0

    def draw(self):
        self.image.draw(self.x, self.y)


class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= speed_change_list[list_num]

        if self.y < 70:
            speed_change_list[list_num] = 0

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

big_ball_num = random.randint(0, 20)
small_ball_num = 20 - big_ball_num
boy = Boy()
grass = Grass()
big = BigBall()
small = SmallBall()
team = [Boy() for i in range(11)]
big_group = [BigBall() for j in range(big_ball_num)]
small_group = [SmallBall() for k in range(small_ball_num)]
speed_change_list = [random.randint(3, 10) for l in range(20)]
list_num = 0

running = True

while running:
    handle_events()

    for boy in team:
        boy.update()
    for big in big_group:
        big.update()
        list_num += 1

        if list_num > 19:
            list_num = 0

    for small in small_group:
        small.update()
        list_num += 1

        if list_num > 19:
            list_num = 0

    clear_canvas()

    for boy in team:
        boy.draw()

    grass.draw()

    for big in big_group:
        big.draw()

    for small in small_group:
        small.draw()

    update_canvas()

    delay(0.05)


close_canvas()