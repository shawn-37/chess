import pygame


pygame.init()
WIDTH = 1000
HEIGHT = 900
BOARD_OFFSET = 20
BOARD_SIZE = 640
SQUARE_SIZE = BOARD_SIZE / 8

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Python Chess")

font = pygame.font.SysFont("arial", 20)
timer = pygame.time.Clock()
FPS = 60

pieceImages = {
    "k": pygame.transform.scale(pygame.image.load("ChessPieces/bk.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "q": pygame.transform.scale(pygame.image.load("ChessPieces/bq.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "r": pygame.transform.scale(pygame.image.load("ChessPieces/br.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "b": pygame.transform.scale(pygame.image.load("ChessPieces/bb.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "n": pygame.transform.scale(pygame.image.load("ChessPieces/bn.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "p": pygame.transform.scale(pygame.image.load("ChessPieces/bp.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "K": pygame.transform.scale(pygame.image.load("ChessPieces/wk.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "Q": pygame.transform.scale(pygame.image.load("ChessPieces/wq.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "R": pygame.transform.scale(pygame.image.load("ChessPieces/wr.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "B": pygame.transform.scale(pygame.image.load("ChessPieces/wb.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "N": pygame.transform.scale(pygame.image.load("ChessPieces/wn.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "P": pygame.transform.scale(pygame.image.load("ChessPieces/wp.png"), (SQUARE_SIZE, SQUARE_SIZE))
}

board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


capturedBlackPieces = []
capturedWhitePieces = []

turn = 0 # 0 = white, 1 = black
pieceSelected = None

# draw chess board
def draw_board():
    for file in range(8):
        for rank in range(8):
            if (file + rank) % 2 == 0:
                pygame.draw.rect(screen, (184,135,97,1), [rank * (SQUARE_SIZE) + BOARD_OFFSET, file * (SQUARE_SIZE) + BOARD_OFFSET, SQUARE_SIZE, SQUARE_SIZE])
            else:
                pygame.draw.rect(screen, (237,214,174,1), [rank * (SQUARE_SIZE) + BOARD_OFFSET, file * (SQUARE_SIZE) + BOARD_OFFSET, SQUARE_SIZE, SQUARE_SIZE])

# draw bar on the side
def draw_sidebar():
    pygame.draw.rect(screen, (34, 32, 30), [BOARD_SIZE + BOARD_OFFSET + 10, BOARD_OFFSET, WIDTH - BOARD_SIZE - 40, HEIGHT - 100])

def draw_pieces():
    for file in range(8):
        for rank in range(8):
            piece = board[rank][file]
            if piece != ".":
                screen.blit(pieceImages.get(piece), (file * SQUARE_SIZE + BOARD_OFFSET, rank * SQUARE_SIZE + BOARD_OFFSET))
run = True
while run:
    timer.tick(FPS)
    screen.fill((48,46,42,1))

    draw_board()
    draw_sidebar()
    draw_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            xCoord = int((event.pos[0] - BOARD_OFFSET) // SQUARE_SIZE)
            yCoord = int((event.pos[1] - BOARD_OFFSET) // SQUARE_SIZE)
            coord = (xCoord, yCoord)
            print(coord)
            if turn == 0:
                piece = board[yCoord][xCoord]
                if piece.isupper():
                    pieceImages[piece] = pygame.transform.scale_by(pieceImages.get(piece), 1.05)
            if turn == 1:
                piece = board[yCoord][xCoord]
                if piece.islower():
                    pieceImages[piece] = pygame.transform.scale_by(pieceImages.get(piece), 1.05)
    pygame.display.flip()
pygame.quit()
