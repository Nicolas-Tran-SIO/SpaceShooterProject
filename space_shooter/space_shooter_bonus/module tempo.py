import pygame
import math
import random
import space_functions


LARGEUR = 800
HAUTEUR = 450

pygame.init()
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Space Shooter")

background_space_tempo = pygame.image.load("./img/espace.jpg").convert_alpha()
background_space=pygame.transform.scale(background_space_tempo, (LARGEUR ,HAUTEUR))
image_vaisseau = pygame.image.load("./img/vaisseau.png").convert_alpha()

mon_vaisseau = space_functions.Vaisseau(LARGEUR,HAUTEUR)
mon_monstre = space_functions.Monstre(LARGEUR,HAUTEUR)




def placement_monstres():
    for i in range(4):
        for j in range(25):
            pass
def afficher(self):
    fenetre.blit(self.img_vaisseau, (self.x_vaisseau, self.y_vaisseau))

def dessiner_tout():
    fenetre.blit(background_space, (0, 0))
    space_functions.Monstre.afficher(mon_monstre,fenetre)
    space_functions.Vaisseau.afficher(mon_vaisseau,fenetre)



continuer = True
while continuer:
    dessiner_tout()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                continuer = False

        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            if mon_vaisseau.x_vaisseau<LARGEUR-mon_vaisseau.longueur_vaisseau:
                mon_vaisseau.x_vaisseau= space_functions.Vaisseau.move_right(mon_vaisseau)
            #print('décalé a droite',mon_vaisseau.x_vaisseau)

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if mon_vaisseau.x_vaisseau>0:
                mon_vaisseau.x_vaisseau= space_functions.Vaisseau.move_left(mon_vaisseau)
            #print('décalé a gauche',mon_vaisseau.x_vaisseau)



    pygame.display.flip()
    clock.tick(50)
pygame.quit()