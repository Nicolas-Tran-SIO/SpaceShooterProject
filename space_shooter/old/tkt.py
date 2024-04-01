import pygame

pygame.init()

width=280
height=280

bleu_ciel = 98, 157, 237
rouge = 255, 0, 0
BALLE_RAYON=20

fenetre = pygame.display.set_mode( (width, height ) )
clock = pygame.time.Clock()
pygame.display.set_caption('Appuyez sur gauche ou droite')

robot = pygame.image.load("./img/monstre.png").convert()

coordonnee_mobile = 40
vitesse = 0
continuer = True
while (continuer):
    pygame.draw.rect (fenetre,bleu_ciel, [0,0,280,280])
    disque = pygame.Surface((2*BALLE_RAYON, 2*BALLE_RAYON))
    pygame.draw.rect(disque, bleu_ciel, disque.get_rect())
    pygame.draw.circle(disque, rouge, (BALLE_RAYON, BALLE_RAYON), BALLE_RAYON)
    fenetre.blit(disque, (coordonnee_mobile,50))
    coordonnee_mobile = (coordonnee_mobile+vitesse)%220
    pygame.display.flip()
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vitesse=-2
            if event.key == pygame.K_RIGHT:
                vitesse =2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vitesse=0
            if event.key == pygame.K_RIGHT:
                vitesse=0

pygame.quit()




###############################################################################
###############################################################################
###############################################################################



if event.type == pygame.QUIT:
        continuer = False

if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
    if mon_vaisseau.x_vaisseau<LARGEUR-mon_vaisseau.longueur_vaisseau:
        mon_vaisseau.x_vaisseau= space_functions.Vaisseau.move_right(mon_vaisseau)
    #print('décalé a droite',mon_vaisseau.x_vaisseau)

elif keys[pygame.K_LEFT] or keys[pygame.K_a]:

    #print('décalé a gauche',mon_vaisseau.x_vaisseau)

