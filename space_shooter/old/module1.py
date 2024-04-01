import pygame



LARGEUR = 1600
HAUTEUR = 900



couleur_espace = (6, 10, 31)
pygame.init()
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Space Shooter")

dessin_vaisseau1=pygame.image.load("./img/vaisseau.png").convert_alpha()
dessin_vaisseau2 = pygame.transform.scale(dessin_vaisseau1, (150, 150))
continuer = True
while continuer:
    fenetre.blit(dessin_vaisseau2,(500,200))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                continuer = False



    pygame.display.flip()
    clock.tick(30)
pygame.quit()