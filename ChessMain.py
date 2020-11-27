'''
Handles User Input and displays information. (Driver File)
'''
import pygame as p

from Chess import ChessEngine
p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15

images = {}
#Loads Images for pieces from image file 
def load_images():
    pieces = ['wP','bP','wR','bR','wK','bK','wN','bN','wB','bB','wQ','bQ']

    for piece in pieces:
        images[piece]= p.transform.scale(p.image.load("images/"+piece+'.png'),(SQ_SIZE,SQ_SIZE))
        #we can acsess an image by saying 'images['wP']'

#main driver
def main():
    p.init()
    screen = p.display.setMode(WIDTH,HEIGHT)
    clock = p.time.Clock()
    screen.fill(p.color("White"))
    gs =ChessEngine.GameState()
    print(gs.board)

main()