import pygame
import time
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (213, 50, 80)
VERT = (0, 255, 0)
BLEU = (50, 153, 213)

# Taille de la fenêtre
LARGEUR_FENETRE = 600
HAUTEUR_FENETRE = 400

# Dimensions du serpent et de la nourriture
TAILLE_SERPENT = 10
TAILLE_NOURRITURE = 10

# Définir la fenêtre de jeu
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption('Snake Game')

# Horloge pour contrôler la vitesse du jeu
clock = pygame.time.Clock()

# Police pour le texte
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Fonction pour afficher le score
def afficher_score(score):
    valeur = score_font.render("Score: " + str(score), True, BLANC)
    fenetre.blit(valeur, [0, 0])

# Fonction pour dessiner le serpent
def dessiner_serpent(serpent):
    for x in serpent:
        pygame.draw.rect(fenetre, VERT, [x[0], x[1], TAILLE_SERPENT, TAILLE_SERPENT])

# Fonction pour afficher un message à l'écran
def message(msg, couleur):
    mesg = font_style.render(msg, True, couleur)
    fenetre.blit(mesg, [LARGEUR_FENETRE / 6, HAUTEUR_FENETRE / 3])

# Fonction principale du jeu
def jeu():
    # Position initiale du serpent
    x1 = LARGEUR_FENETRE / 2
    y1 = HAUTEUR_FENETRE / 2

    # Vitesse du serpent
    x1_change = 0
    y1_change = 0

    # Liste du serpent et sa longueur
    serpent = []
    longueur_serpent = 1

    # Générer la nourriture
    nourriturex = round(random.randrange(0, LARGEUR_FENETRE - TAILLE_NOURRITURE) / 10.0) * 10.0
    nourriturey = round(random.randrange(0, HAUTEUR_FENETRE - TAILLE_NOURRITURE) / 10.0) * 10.0

    # Variable pour vérifier si le jeu est terminé
    game_over = False

    # Boucle principale du jeu
    while not game_over:

        # Boucle d'événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -TAILLE_SERPENT
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = TAILLE_SERPENT
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -TAILLE_SERPENT
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = TAILLE_SERPENT
                    x1_change = 0

        # Vérifier les conditions de fin de jeu
        if x1 >= LARGEUR_FENETRE or x1 < 0 or y1 >= HAUTEUR_FENETRE or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        fenetre.fill(BLEU)
        pygame.draw.rect(fenetre, ROUGE, [nourriturex, nourriturey, TAILLE_NOURRITURE, TAILLE_NOURRITURE])

        # Ajout du serpent
        serpent tete = []
        tete.append(x1)
        tete.append(y1)
        serpent.append(tete)
        if len(serpent) > longueur_serpent:
            del serpent[0]

        for segment in serpent[:-1]:
            if segment == tete:
                game_over = True

        dessiner_serpent(serpent)
        afficher_score(longueur_serpent - 1)

        pygame.display.update()

        # Vérifier si le serpent mange la nourriture
        if x1 == nourriturex and y1 == nourriturey:
            nourriturex = round(random.randrange(0, LARGEUR_FENETRE - TAILLE_NOURRITURE) / 10.0) * 10.0
            nourriturey = round(random.randrange(0, HAUTEUR_FENETRE - TAILLE_NOURRITURE) / 10.0) * 10.0
            longueur_serpent += 1

        # Contrôler la vitesse du serpent
        clock.tick(15)

    # Afficher le message de fin de jeu
    message("Tu as perdu ! Appuie sur Q pour quitter ou C pour rejouer", ROUGE)
    pygame.display.update()

    # Attendre que l'utilisateur appuie sur une touche
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                attente = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    attente = False
                    pygame.quit()
                if event.key == pygame.K_c:
                    jeu()

# Lancer le jeu
jeu()
