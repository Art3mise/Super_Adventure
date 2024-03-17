import pygame
import sys
import random
import time

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
tile_size = 50
screen_width_in_tiles = 10
screen_height_in_tiles = 7
buffer = 3  # Zone tampon pour le défilement

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Matrice du labyrinthe (0 pour un espace vide, 1 pour un mur)
labyrinth_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],   
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],   
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],    
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],    
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],   
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],    
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],   
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],    
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]    
]
# Taille de la fenêtre
screen_width = screen_width_in_tiles * tile_size
screen_height = screen_height_in_tiles * tile_size

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))

# Chargement des images
mur_0018 = pygame.image.load("Tiles_NV1/tile_0018.png") #mur avec bodure haute
mur_0018 = pygame.transform.scale(mur_0018, (tile_size, tile_size))

mur_0034 = pygame.image.load("Tiles_NV1/tile_0034.png") #mur sans bordure
mur_0034 = pygame.transform.scale(mur_0034, (tile_size, tile_size))

mur_0019 = pygame.image.load("Tiles_NV1/tile_0019.png") #mur avec coin haut droit
mur_0019 = pygame.transform.scale(mur_0019, (tile_size, tile_size))

mur_0017 = pygame.image.load("Tiles_NV1/tile_0017.png") #mur avec coin haut gauche
mur_0017 = pygame.transform.scale(mur_0017, (tile_size, tile_size))

mur_0018 = pygame.image.load("Tiles_NV1/tile_0018.png") #mur bordure haute
mur_0018 = pygame.transform.scale(mur_0018, (tile_size, tile_size))

mur_0006 = pygame.image.load("Tiles_NV1/tile_0006.png") #ballot de paille
mur_0006 = pygame.transform.scale(mur_0006, (tile_size, tile_size))

mur_0035 = pygame.image.load("Tiles_NV1/tile_0035.png") #mur bordure droit
mur_0035 = pygame.transform.scale(mur_0035, (tile_size, tile_size))

mur_0033 = pygame.image.load("Tiles_NV1/tile_0033.png") #mur bordure gauche
mur_0033 = pygame.transform.scale(mur_0033, (tile_size, tile_size))

mur_0001 = pygame.image.load("Tiles_NV1/tile_0001.png") #mur sans bordure droit
mur_0001 = pygame.transform.scale(mur_0001, (tile_size, tile_size)) 

mur_0002 = pygame.image.load("Tiles_NV1/tile_0002.png")
mur_0002 = pygame.transform.scale(mur_0002, (tile_size, tile_size))

mur_0003 = pygame.image.load("Tiles_NV1/tile_0003.png") #mur sans bordure gauche
mur_0003 = pygame.transform.scale(mur_0003, (tile_size, tile_size))

arbre_0092 = pygame.image.load("Tiles_NV1/tile_0092.png") # tron arbre milieu
arbre_0092 = pygame.transform.scale(arbre_0092, (tile_size, tile_size))

arbre_0109 = pygame.image.load("Tiles_NV1/tile_0109.png") # tron arbre bas
arbre_0109 = pygame.transform.scale(arbre_0109, (tile_size, tile_size))

arbre_0077 = pygame.image.load("Tiles_NV1/tile_0077.png") # tron arbre haut
arbre_0077 = pygame.transform.scale(arbre_0077, (tile_size, tile_size))

feuille_0045 = pygame.image.load("Tiles_NV1/tile_0045.png") # feuillage angle bas gauche
feuille_0045 = pygame.transform.scale(feuille_0045, (tile_size, tile_size))

feuille_0029 = pygame.image.load("Tiles_NV1/tile_0029.png") # feuillage bordure gauche
feuille_0029 = pygame.transform.scale(feuille_0029, (tile_size, tile_size))

feuille_0013 = pygame.image.load("Tiles_NV1/tile_0013.png") # feuillage angle haut gauche
feuille_0013 = pygame.transform.scale(feuille_0013, (tile_size, tile_size))

feuille_0014 = pygame.image.load("Tiles_NV1/tile_0014.png") # feuillage bordure haut
feuille_0014 = pygame.transform.scale(feuille_0014, (tile_size, tile_size))

feuille_0015 = pygame.image.load("Tiles_NV1/tile_0015.png") # feuillage angle haut droit
feuille_0015 = pygame.transform.scale(feuille_0015, (tile_size, tile_size))

feuille_0031 = pygame.image.load("Tiles_NV1/tile_0031.png") # feuillage bordure droit
feuille_0031 = pygame.transform.scale(feuille_0031, (tile_size, tile_size))

feuille_0047 = pygame.image.load("Tiles_NV1/tile_0047.png") # feuillage angle bas droit
feuille_0047 = pygame.transform.scale(feuille_0047, (tile_size, tile_size))

feuille_0030 = pygame.image.load("Tiles_NV1/tile_0030.png") # feuillage centre
feuille_0030 = pygame.transform.scale(feuille_0030, (tile_size, tile_size))

personnage_image = pygame.image.load("Tiles_NV1/perso1.png")
personnage_image = pygame.transform.scale(personnage_image, (tile_size, tile_size))

piece_image = pygame.image.load("Tiles_NV1/piece.png")
piece_image = pygame.transform.scale(piece_image, (tile_size, tile_size))

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False

# Création des pièces
pieces = [Piece(random.randint(0, len(labyrinth_matrix[0]) - 1), random.randint(0, len(labyrinth_matrix) - 1)) for _ in range(10)]

# Position initiale du joueur
player_x = 0
player_y = 8

# Position de la caméra
camera_x = 0
camera_y = 5

# Gestion du saut
is_jumping = False
jump_start_time = 0
jump_duration = 0.005  # en secondes

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Déplacement du joueur
    if keys[pygame.K_LEFT] and player_x > 0 and labyrinth_matrix[player_y][player_x - 1] == 0:
        player_x -= 1
        if labyrinth_matrix[int(player_y)+1][int(player_x)]==0:
                is_jumping = True
    if keys[pygame.K_RIGHT] and player_x < len(labyrinth_matrix[0]) - 1 and labyrinth_matrix[player_y][player_x + 1] == 0:
        player_x += 1
        if labyrinth_matrix[int(player_y)+1][int(player_x)]==0:
                is_jumping = True
        print(labyrinth_matrix[int(player_y)+1][int(player_x)])

    # Gestion du saut
    if keys[pygame.K_SPACE]:
        jump_start_time = time.time()
        is_jumping = True

    if is_jumping:
        # Calculez le temps écoulé depuis le début du saut
        jump_écoulé = time.time() - jump_start_time
        # Montée pendant une certaine durée
        if jump_écoulé < jump_duration:
            player_y -= 1
        else:
            # Le saut est terminé, commencez à descendre
            player_y += 1
            if labyrinth_matrix[int(player_y)+1][int(player_x)]==1:
                is_jumping = False
            

    # Mise à jour de la position de la caméra
    if player_x - camera_x < buffer:
        camera_x = max(0, player_x - buffer)
    elif player_x - camera_x > screen_width_in_tiles - buffer:
        camera_x = min(len(labyrinth_matrix[0]) - screen_width_in_tiles, player_x - screen_width_in_tiles + buffer)

    if player_y - camera_y < buffer:
        camera_y = max(0, player_y - buffer)
    elif player_y - camera_y > screen_height_in_tiles - buffer:
        camera_y = min(len(labyrinth_matrix) - screen_height_in_tiles, player_y - screen_height_in_tiles + buffer)

    # Vérification de la collecte de pièces
    for piece in pieces:
        if not piece.collected and player_x == piece.x and player_y == piece.y:
            piece.collected = True
            print("Piece collected!")

    # Effacement de l'écran
    screen.fill(BLACK)

    # Affichage du labyrinthe
    for y in range(camera_y, camera_y + screen_height_in_tiles):
        for x in range(camera_x, camera_x + screen_width_in_tiles):
            tile = labyrinth_matrix[y][x]
            if tile == 1:
                if y == 9 and (x == 0 or x == 1 or x == 2) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10 or y == 11 or y == 12 or y == 13 ) and (x == 0 or x == 1 or x == 2) :
                    screen.blit(mur_0034, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 9) and (x == 3) :
                    screen.blit(mur_0019, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 8) and (x == 2) :
                    screen.blit(mur_0006, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10 or y == 11 or y == 12 or y == 13 ) and (x == 3) :
                    screen.blit(mur_0035, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 6 and (x == 4) :
                    screen.blit(mur_0001, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 6 and (x == 5) :
                    screen.blit(mur_0003, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 5 and (x == 5) :
                    screen.blit(mur_0006, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 12 or y == 13) and (x == 6 or x == 7) :
                    screen.blit(mur_0034, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 11 ) and (x == 6 or x == 7) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 11 ) and (x == 5 ) :
                    screen.blit(mur_0017, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 11 ) and (x == 8 ) :
                    screen.blit(mur_0019, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 12 or y == 13 ) and (x == 5 ) :
                    screen.blit(mur_0033, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 12 or y == 13 ) and (x == 8 ) :
                    screen.blit(mur_0035, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 6) and (x == 8 ) :
                    screen.blit(arbre_0077, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 6) and (x == 7 ) :
                    screen.blit(feuille_0045, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 5) and (x == 7 ) :
                    screen.blit(feuille_0029, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 7 ) :
                    screen.blit(feuille_0013, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 8 ) :
                    screen.blit(feuille_0014, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 9 ) :
                    screen.blit(feuille_0015, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 5) and (x == 9) :
                    screen.blit(feuille_0031, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 6) and (x == 9) :
                    screen.blit(feuille_0047, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 5) and (x == 8) :
                    screen.blit(feuille_0030, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 13 or y == 12 or y == 11) and (x == 10) :
                    screen.blit(mur_0033, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 13 or y == 12 or y == 11) and (x == 13) :
                    screen.blit(mur_0035, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10) and (x == 10) :
                    screen.blit(mur_0017, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10) and (x == 11 or x == 12) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10) and (x == 13) :
                    screen.blit(mur_0019, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10) and (x == 11 or x == 12) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 11 or y == 12 or y == 13) and (x == 11 or x == 12) :
                    screen.blit(mur_0034, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 11 and (x == 14 or x == 15) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 11 and (x == 16) :
                    screen.blit(mur_0019, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 12 or y == 13 ) and (x == 16 ) :
                    screen.blit(mur_0035, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 12 or y == 13 ) and (x == 15 or x == 14 ) :
                    screen.blit(mur_0034, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))

                ### arbre
                if (y == 5) and (x == 11 ) :
                    screen.blit(feuille_0045, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 11 ) :
                    screen.blit(feuille_0029, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 3) and (x == 11 ) :
                    screen.blit(feuille_0013, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 3) and (x == 12 ) :
                    screen.blit(feuille_0014, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 3) and (x == 13 ) :
                    screen.blit(feuille_0015, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 13) :
                    screen.blit(feuille_0031, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 5) and (x == 13) :
                    screen.blit(feuille_0047, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 12) :
                    screen.blit(feuille_0030, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 5) and (x == 12 ) :
                    screen.blit(arbre_0077, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 13 or y == 12 or y == 11) and (x == 18) :
                    screen.blit(mur_0033, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10) and (x == 18) :
                    screen.blit(mur_0017, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10) and (x == 19) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 13 or y == 12 or y == 11) and (x == 19) :
                    screen.blit(mur_0034, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 13 or y == 12 or y == 11 or y == 10) and (x == 20) :
                    screen.blit(mur_0033, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 9) and (x == 20) :
                    screen.blit(mur_0017, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 9) and (x == 21) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10 or y == 11 or y == 13 or y == 12) and (x == 21) :
                    screen.blit(mur_0034, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 13 or y == 12 or y == 11 or y == 10 or y == 9) and (x == 22) :
                    screen.blit(mur_0033, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 8) and (x == 22) :
                    screen.blit(mur_0017, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 8) and (x == 23 or x == 24 or x == 25) :
                    screen.blit(mur_0018, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 10 or y == 11 or y == 13 or y == 12 or y == 9) and (x == 23 or x == 24 or x == 25) :
                    screen.blit(mur_0034, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 20 ) :
                    screen.blit(feuille_0045, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 3) and (x == 20 ) :
                    screen.blit(feuille_0029, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 2) and (x == 20 ) :
                    screen.blit(feuille_0013, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 2) and (x == 21 ) :
                    screen.blit(feuille_0014, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 2) and (x == 22 ) :
                    screen.blit(feuille_0015, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 3) and (x == 22) :
                    screen.blit(feuille_0031, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 22) :
                    screen.blit(feuille_0047, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 3) and (x == 21) :
                    screen.blit(feuille_0030, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 4) and (x == 21 ) :
                    screen.blit(arbre_0077, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 6 and (x == 15) :
                    screen.blit(mur_0001, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 6 and (x == 16) :
                    screen.blit(mur_0002, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 6 and (x == 17) :
                    screen.blit(mur_0003, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if y == 9 and (x == 19) :
                    screen.blit(mur_0006, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                
            if tile == 0 :
                if (y == 9 or y == 8 or y == 7) and (x == 8 ):
                    screen.blit(arbre_0092, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size)) 
                if (y == 10) and (x == 8 ) :
                    screen.blit(arbre_0109, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 8 or y == 7 or y==6) and (x == 12 ):
                    screen.blit(arbre_0092, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size)) 
                if (y == 9) and (x == 12 ) :
                    screen.blit(arbre_0109, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                if (y == 5 or y == 6 or y==7) and (x == 21 ):
                    screen.blit(arbre_0092, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size)) 
                if (y == 8) and (x == 21) :
                    screen.blit(arbre_0109, (x * tile_size - camera_x * tile_size, y * tile_size - camera_y * tile_size))
                
    # Affichage des pièces non collectées
    for piece in pieces:
        if not piece.collected and labyrinth_matrix[piece.y][piece.x] == 0:
            screen.blit(piece_image, (piece.x * tile_size - camera_x * tile_size, piece.y * tile_size - camera_y * tile_size))

    # Affichage du joueur
    screen.blit(personnage_image, (player_x * tile_size - camera_x * tile_size, player_y * tile_size - camera_y * tile_size))

    # Mise à jour de l'écran
    pygame.display.update()

    # Limiter la vitesse de la boucle principale
    pygame.time.Clock().tick(10)  # Ajusté à 10 images par seconde
