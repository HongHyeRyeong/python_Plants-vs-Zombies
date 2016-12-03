from pico2d import *
import random

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 25.0  # Km / Hour 속도
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class Stage:
    def __init__(self):
        self.stage1_image = load_image('resource/stage1.png')
        self.stage2_image = load_image('resource/stage2.png')
        self.stage3_image = load_image('resource/stage3.png')
        self.font = load_font('resource/ConsolaMalgun.ttf', 17)
        self.state = 'stage1'
        self.zombie_cnt, self.random_cnt = 0, 10

    def update(self):
        self.zombie_cnt += 1

    def draw(self, sun_point):
        if self.state == 'stage1':
            self.stage1_image.draw(700, 300)
        elif self.state == 'stage2':
            self.stage2_image.draw(700, 300)
        elif self.state == 'stage3':
            self.stage3_image.draw(700, 300)
        self.font.draw(20, 504, '%d' % sun_point)

    def zombie_set_count(self):
        if self.state == 'stage1':
            self.random_cnt = random.randint(250, 300)
        elif self.state == 'stage2':
            self.random_cnt = random.randint(200, 250)
        elif self.state == 'stage3':
            self.random_cnt = random.randint(150, 200)
        self.zombie_cnt = 0

    def cnt_init(self):
        self.zombie_cnt, self.random_cnt = 0, 10

class Item:
    def __init__(self):
        self.select_image = load_image('resource/select_plant.png')
        self.shovel_image = load_image('resource/shovel.png')
        self.shovel_frame, self.shovel_total_frames = 0.0, 0.0

    def update(self, frame_time):
        self.shovel_total_frames += FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time
        self.shovel_frame = int(self.shovel_total_frames + 1) % 2

    def draw(self, select_plant, mouse_x, mouse_y):
        if select_plant == 6:
            self.shovel_image.clip_draw(int(self.shovel_frame * 100), 0, 100, 100, mouse_x, mouse_y)
        else:
            self.select_image.clip_draw((select_plant - 1) * 100 + 10, 0, 100, 100, mouse_x, mouse_y)

        self.select_image.clip_draw((select_plant - 1) * 100 + 10, 0, 100, 100, 1350, 545)