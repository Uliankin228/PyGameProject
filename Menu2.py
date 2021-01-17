import pygame
import os

size = width, height = 1270, 750
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Меню')

pygame.font.init()
pygame.mixer.init()

music_pleer = ['Музыка 1', 'Музыка 2', 'Музыка 3', 'Музыка 4']
MUSICSOUND = 0

pygame.mixer.music.load('{}.mp3'.format(music_pleer[MUSICSOUND]))
ACTUAL_SOUND = music_pleer[MUSICSOUND]
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

SOUND_PAUSE = False

RUSSIA = True
ENGLISH = False

ARROWS = True
WASD = False

HIT_J = True
HIT_K = False
HIT_L = False


class Cur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_cur)
        self.image = load_image("cur.png")  # загружает спрайт
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

    def get_coords(self, coords):
        self.rect.x, self.rect.y = coords


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_color_key(color_key)
    else:
        image = image.convert_alpha()

    return image


class Main_menu(pygame.sprite.Sprite):

    def __init__(self, name_file, coord_x, coord_y, size_x, size_y):
        super().__init__(all_sprites_main_menu)

        self.image = load_image(name_file)  # загружает спрайт
        self.image = pygame.transform.scale(self.image, (size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coord_x, coord_y

    def get_cords(self,  last_y):
        if self.rect.y < last_y:
            self.rect.y += 20

    def rename(self, name):
        self.image = load_image(name)
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))


class Options_background(pygame.sprite.Sprite):  # настройки

    def __init__(self, name_file, coord_x, coord_y, size_x, size_y):
        super().__init__(all_Background_options)

        self.image = load_image(name_file)  # загружает спрайт
        self.image = pygame.transform.scale(self.image, (size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coord_x, coord_y

    def get_left(self, last_x):
        if self.rect.x > last_x:
            self.rect.x -= 40

    def get_right(self, last_x):
        if self.rect.x < last_x:
            self.rect.x += 40

    def rename(self, name):
        self.image = load_image(name)
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))


all_Background_options = pygame.sprite.Group()  # настройки
all_sprites_main_menu = pygame.sprite.Group()  # кнопки: Старт, Настройки, Выход
all_cur = pygame.sprite.Group()  # курсор

image1 = load_image("FON1.jpg")  # загрузка фона
image11 = pygame.transform.scale(image1, (1280, 750))

if __name__ == '__main__':
    cur = Cur()

    # меню
    start = Main_menu("START_RUSSIA.png", width // 2 - 150, -500, 300, 100)  # кнопка Старт(Start)
    options = Main_menu("OPTIONS_RUSSIA.png", width // 2 - 125, -300, 250, 70)  # кнопка Настройки(Options)
    exit = Main_menu("EXIT_RUSSIA.png", width // 2 - 75, -100, 150, 50)  # кнопка Выход(Exit)

    # музыка в меню
    music_sound = Main_menu("SOUND_PAUSE_FALSE.png", width - 90, -500, 26, 25)
    right_pleer = Main_menu("RIGHT_PLEER.png", width - 55, -500, 25, 25)
    left_pleer = Main_menu("LEFT_PLEER.png", width - 125, -500, 25, 25)
    note = Main_menu("Нота.png", width - 250, -500, 25, 25)

    # настройки_фон
    background_fon = Options_background("Прозрачный фон.png", width, 0, 1280, 750)  # прозрачный фон

    # настройки_управление_ персонажем
    optinons_control = Options_background("CONTROL_RUSSIA.png", width + width // 4, 50, 200, 50)  # спрайт управления
    options_control_arrows = Options_background("ARROWS.png", width + width // 4 + 25, 115, 150, 40)  # стрелочки
    control_right = Options_background("arrow_right.png", width + width // 4 + 180, 120, 25, 25)  # смена(вправо)
    control_left = Options_background("arrow_left.png", width + width // 4 + 35, 120, 25, 25)  # смена(влево)

    # настройки_прыжок
    options_JUMP = Options_background("JUMP_RUSSIA.png", width + width // 4, 180, 200, 50)  # спрайт прыжок
    options_Jump_space = Options_background("SPACE.png", width + width // 4 + 25, 240, 150, 40)  # прыжок(пробел)

    # настройки_удар
    options_hit = Options_background("HIT_RUSSIA.png", width + width // 4, 310, 200, 50)  # спрайт удара
    hit_button = Options_background("HIT_J.png", width + width // 4 + 25, 370, 150, 40)  # кнопка удара
    hit_right = Options_background("arrow_right.png", width + width // 4 + 180, 375, 25, 25)  # смена(вправо)
    hit_left = Options_background("arrow_left.png", width // 4 + 35 + width, 375, 25, 25)  # смена(влево)

    # настройки_языки
    option_languages = Options_background("LANGUAGES_RUSSIA.png", width + width // 4 + width // 4, 50, 200, 50)
    languages_sprite = Options_background("LANG_RUSSIA.png", width + width // 4 + width // 4 + 20, 120, 80, 20)
    language_right = Options_background("arrow_right.png", width + width // 4 + width // 4 + 50, 120, 25, 25)
    language_left = Options_background("arrow_left.png", width + width // 4 + width // 4, 120, 25, 25)

    # возвращение в главное меню
    back_main = Options_background("BACK_RUSSIA.png", width + 50, height - 25, 50, 25)

    running, draw_sprite = True, False

    background_options = False
    while running:
        pygame.mouse.set_visible(False)  # скрывает курсор
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cur.get_coords(event.pos)
                if pygame.mouse.get_focused():
                    draw_sprite = True
                else:
                    draw_sprite = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if width // 2 - 130 < x < width // 2 + 115 and 320 < y < 390:  # открытие настрооек
                    background_options = True

                if background_options:
                    if 0 < x < 50 and height - 25 < y < height:  # закрытие настроек
                        background_options = False

                    if (width // 4 + width // 4 + 150 < x < width // 4 + width // 4 + 180 and 120 < y < 145) or\
                            (width // 4 + width // 4 - 15 < x < width // 4 + width // 4 + 10 and 120 < y < 145):  # язык
                        if not ENGLISH:
                            RUSSIA = False
                            ENGLISH = True
                            start.rename("START_ENGLISH.png", )
                            options.rename("OPTIONS_ENGLISH.png")
                            exit.rename("EXIT_ENGLISH.png")

                            optinons_control.rename("CONTROL_ENGLISH.png")

                            options_JUMP.rename("JUMP_ENGLISH.png")

                            option_languages.rename("LANGUAGES_ENGLISH.png")
                            languages_sprite.rename("LANG_ENGLISH.png")

                            back_main.rename("BACK_ENGLISH.png")
                        else:
                            RUSSIA = True
                            ENGLISH = False
                            start.rename("START_RUSSIA.png")
                            options.rename("OPTIONS_RUSSIA.png")
                            exit.rename("EXIT_RUSSIA.png")

                            optinons_control.rename("CONTROL_RUSSIA.png")

                            options_JUMP.rename("JUMP_RUSSIA.png")

                            option_languages.rename("LANGUAGES_RUSSIA.png")
                            languages_sprite.rename("LANG_RUSSIA.png")

                            back_main.rename("BACK_RUSSIA.png")
                    if (width // 4 + 120 < x < width // 4 + 155 and 375 < y < 400) or\
                            (width // 4 + 20 < x < width // 4 + 45 and 375 < y < 400):  # смена кнопки удара
                        if HIT_J:
                            HIT_J = False
                            HIT_K = True
                            hit_button.rename("HIT_K.png")
                        elif HIT_K:
                            HIT_K = False
                            HIT_L = True
                            hit_button.rename("HIT_L.png")
                        elif HIT_L:
                            HIT_L = False
                            HIT_J = True
                            hit_button.rename("HIT_J.png")
                    if (width // 4 + 160 < x < width // 4 + 190 and 120 < y < 145) or\
                            (width // 4 - 25 < x < width // 4 + 5 and 120 < y < 145):  # смена управления
                        if ARROWS:
                            ARROWS = False
                            WASD = True
                            options_control_arrows.rename("WASD.png")
                        elif WASD:
                            ARROWS = True
                            WASD = False
                            options_control_arrows.rename("ARROWS.png")
                else:
                    if width // 2 - 80 < x < width // 2 + 70 and 400 < y < 445:  # нажатие на кнопку выхода
                        running = False
                    if width - 100 < x < width - 70 and 20 < y < 45:  # остановки и воспроизведение музыки
                        if not SOUND_PAUSE:
                            SOUND_PAUSE = True
                            music_sound.rename("SOUND_PAUSE_TRUE.png")
                            pygame.mixer.music.pause()
                        else:
                            SOUND_PAUSE = False
                            music_sound.rename("SOUND_PAUSE_FALSE.png")
                            pygame.mixer.music.unpause()
                    if width - 65 < x < width - 40 and 20 < y < 45:  # смена музыки вправо
                        MUSICSOUND += 1
                        if MUSICSOUND == 4:
                            MUSICSOUND = 0
                        pygame.mixer.music.load('{}.mp3'.format(music_pleer[MUSICSOUND]))
                        ACTUAL_SOUND = music_pleer[MUSICSOUND]
                        pygame.mixer.music.play(-1)
                        if SOUND_PAUSE:
                            pygame.mixer.music.pause()
                    if width - 135 < x < width - 105 and 20 < y < 45:  # смена музыки влево
                        MUSICSOUND -= 1
                        if MUSICSOUND == -1:
                            MUSICSOUND = 3
                        ACTUAL_SOUND = music_pleer[MUSICSOUND]
                        pygame.mixer.music.load('{}.mp3'.format(music_pleer[MUSICSOUND]))
                        pygame.mixer.music.play(-1)
                        if SOUND_PAUSE:
                            pygame.mixer.music.pause()

        start.get_cords(200)
        options.get_cords(320)
        exit.get_cords(400)

        music_sound.get_cords(20)
        right_pleer.get_cords(20)
        left_pleer.get_cords(20)
        note.get_cords(20)

        screen.blit(image11, (0, 0))
        all_sprites_main_menu.draw(screen)
        font = pygame.font.Font(None, 25)
        text = font.render(ACTUAL_SOUND.upper(), True, (255, 255, 255))
        screen.blit(text, (1050, 25))
        all_Background_options.draw(screen)

        if background_options:  # открытие настроек
            background_fon.get_left(0)

            optinons_control.get_left(width // 4 + 20)
            options_control_arrows.get_left(width // 4 + 20)
            control_right.get_left(width // 4 + 180)
            control_left.get_left(width // 4)

            options_JUMP.get_left(width // 4 + 20)
            options_Jump_space.get_left(width // 4 + 20)

            options_hit.get_left(width // 4 + 20)
            hit_button.get_left(width // 4 + 20)
            hit_right.get_left(width // 4 + 160)
            hit_left.get_left(width // 4 + 60)

            option_languages.get_left(width // 4 + width // 4)
            languages_sprite.get_left(width // 4 + width // 4 + 60)
            language_right.get_left(width // 4 + width // 4 + 160)
            language_left.get_left(width // 4 + width // 4)

            back_main.get_left(0)
        else:  # закрытие настроек
            background_fon.get_right(width)

            optinons_control.get_right(width + width // 4)
            options_control_arrows.get_right(width + width // 4)
            control_right.get_right(width + width // 4 + 170)
            control_left.get_right(width + width // 4 - 30)

            options_JUMP.get_right(width + width // 4)
            options_Jump_space.get_right(width + width // 4)

            options_hit.get_right(width + width // 4)
            hit_button.get_right(width + width // 4)
            hit_right.get_right(width + width // 4 + 170)
            hit_left.get_right(width + width // 4 - 30)

            option_languages.get_right(width + width // 4 + width // 4)
            languages_sprite.get_right(width + width // 4 + width // 4 + 100)
            language_right.get_right(width + width // 4 + width // 4 + 50)
            language_left.get_right(width + width // 4)

            back_main.get_right(width)

        if draw_sprite:
            all_cur.draw(screen)
        pygame.time.Clock().tick(60)
        pygame.display.flip()