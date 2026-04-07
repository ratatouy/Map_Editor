import pygame

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Map Editor")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()