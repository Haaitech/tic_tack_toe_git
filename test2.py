import pygame


class Box:
    def __init__(self, height, width, x, y):
        self.rect = pygame.Rect(x, y, width, height)

        self.hoverd = False

        self.img = pygame.transform.scale(
            pygame.image.load('assets/button.png'), (240, 240))
        self.img_hovered = pygame.transform.scale(
            pygame.image.load('assets/button_high_light.png'), (240, 240))

    def draw(self, window):
        if self.hoverd:
            window.blit(self.img_hovered, self.rect)
        else:
            window.blit(self.img, self.rect)


pygame.init()
WIDTH, HEIGHT = 800, 800
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# create object without drawing

board_boxes = []

for y in (10, 276, 542):
    for x in (10, 276, 542):
        box = Box(240, 240, x, y)
        board_boxes.append(box)

# mainloop

run = True

while run:

    # --- events ---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # --- changes/moves ---

    pos = pygame.mouse.get_pos()

    for box in board_boxes:
        box.hoverd = box.rect.collidepoint(pos)

    # --- draws ---

    # pygame.WIN.fill( (0,0,0) ) # clear WIN with black color

    for box in board_boxes:
        box.draw(WIN)

    clock.tick(FPS)
    pygame.display.update()

# end

pygame.quit()
