import pygame
import random
pygame.font.init()

# Game setup
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

WHITE = 255, 255, 255

pygame.display.set_caption("Space Tac Toe")

IMG_NOR = pygame.transform.scale(
    pygame.image.load('assets/button.png'), (240, 240))
IMG_HIGH = pygame.transform.scale(pygame.image.load(
    'assets/button_high_light3.png'), (240, 240))
LINES = pygame.image.load("assets/board2.png")
BG = pygame.image.load("assets/space.jpg")
PLAYER_X = pygame.transform.scale(
    pygame.image.load("assets/player_X.png"), (240, 240))
PLAYER_O = pygame.transform.scale(
    pygame.image.load("assets/player_O.png"), (240, 240))

WINNER_FONT = pygame.font.SysFont('comicsans', 100)


class Button():
    def __init__(self, height, width, x, y, num):
        self.rect = pygame.Rect(x, y, width, height)
        self.hoverd = False
        self.img = IMG_NOR
        self.img_hovered = IMG_HIGH
        self.id = num

    def draw(self, window):
        if self.hoverd:
            window.blit(self.img_hovered, self.rect)
        else:
            window.blit(self.img, self.rect)


def create_button(board_buttons):
    num = 0
    for y in (10, 275, 542):
        for x in (15, 282, 545):
            num += 1
            button = Button(240, 240, x, y, num)
            board_buttons.append(button)


def win_check(player):
    if (1 in player and 2 in player and 3 in player or
        4 in player and 5 in player and 6 in player or
        7 in player and 8 in player and 9 in player or
        1 in player and 4 in player and 7 in player or
        2 in player and 5 in player and 8 in player or
        3 in player and 6 in player and 9 in player or
        1 in player and 5 in player and 9 in player or
            3 in player and 5 in player and 7 in player):
        return True


def end_game(text):
    pygame.time.delay(500)
    WIN.blit(BG, (0, 0))
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(2000)

    main()


def main():
    # Game Variables
    board_buttons = []
    player_x_button = []
    player_x_buttonid = []
    player_o_button = []
    player_o_buttonid = []
    clicks = random.randint(1, 2)

    create_button(board_buttons)

    # Game Loop
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        WIN.blit(BG, (0, 0))
        WIN.blit(LINES, (0, 0))
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            for button in board_buttons:
                button.hoverd = button.rect.collidepoint(pos)
                if button.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP:
                    if clicks % 2 == 0:
                        player_o_button.append(button)
                        player_o_buttonid.append(button.id)
                    else:
                        player_x_button.append(button)
                        player_x_buttonid.append(button.id)

                    board_buttons.remove(button)
                    clicks += 1

        for button in board_buttons:
            button.draw(WIN)
        for button in player_o_button:
            WIN.blit(PLAYER_O, button.rect)
        for button in player_x_button:
            WIN.blit(PLAYER_X, button.rect)

        pygame.display.update()

        if win_check(player_x_buttonid):
            winner_text = "Player X WON!"
            end_game(winner_text)

        if win_check(player_o_buttonid):
            winner_text = "Player O WON!"
            end_game(winner_text)

        if board_buttons == []:
            pygame.time.delay(200)
            draw_text = "IT'S A DRAW"
            end_game(draw_text)


if __name__ == "__main__":
    main()
