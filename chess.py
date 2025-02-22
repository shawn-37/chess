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
 
#def getImages(pieces):

def load_piece_images():
    pieces = ["bk", "bq", "br", "bb", "bn", "bp", "wk", "wq", "wr", "wb", "wn", "wp"]
    return {piece: pygame.transform.scale(pygame.image.load(f"ChessPieces/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE)) for piece in pieces}

pieceImages = load_piece_images()

pieces = ["k", "q", "r", "b", "n", "p"]

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
boardImages = [["." for _ in range(8)] for _ in range(8)]


capturedBlackPieces = []
capturedWhitePieces = []

legalMoves = []

turnStep = 0 # 0 = whites turn no piece seleted, 1 = whites turn piece selected, 2 = blacks turn no piece seletected, 3 = blacks turn piece selected
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
                screen.blit(pieceImages[piece], (file * SQUARE_SIZE + BOARD_OFFSET, rank * SQUARE_SIZE + BOARD_OFFSET))


def prepare_pieces():
    for file in range(8):
        for rank in range(8):
            piece = board[rank][file]
            if piece != ".":
                image = pieceImages[piece]
                boardImages[rank][file] = image

def move_piece(start, end):
    x1, y1 = start
    x2, y2 = end

    piece = board[y1][x1]

    board[y2][x2] = piece
    board[y1][x1] = "."

    boardImages[y2][x2] = boardImages[y1][x1]
    boardImages[y1][y2] = "." 

def checkPawn(location, turnStep):
    x, y = location
    if turnStep < 2:
        if 0 <= y - 1 < 8 and board[y - 1] == ".":
            legalMoves.append(board[y - 1])
        if 0 <= x - 1 < 8 and board[y - 1][x - 1] in pieces:
            legalMoves.append(board[y - 1][x - 1])
        if 0 <= x - 1 < 8 and board[y - 1][x + 1] in pieces:
            legalMoves.append(board[y - 1][x + 1])


prepare_pieces()
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
            piece = board[yCoord][xCoord]
            if piece != ".":
                if turnStep < 2 and piece.isupper:
                    if pieceSelected != piece:
                        pieceSelected = piece
                        if piece == "P":
                            checkPawn(coord, turnStep)
                    else:
                        pieceSelected = None
                elif turnStep > 1 and piece.islower:
                    if pieceSelected != piece:
                        pieceSelected = piece
                    else:
                        pieceSelected = None
            else:
                if turnStep == 1:
                    pass
                



    pygame.display.flip()
print(boardImages)
pygame.quit()


'''goal: If piece is selected (!= ".") then make the piece selected and update legal moves table by calling checkPawn func. 
Else (meaning that a empty square was selected) if a piece was previously selected check if the square is that was selected is in legal moves table, if it is use move_piece() to move the piece to new square'''
