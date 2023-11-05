import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the game board
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Initialize variables
player_turn = 'X'
game_over = False

# Function to draw the game board
def draw_board():
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw the X and O symbols
def draw_symbols():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (col * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, ((col + 1) * CELL_SIZE, row * CELL_SIZE), (col * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - LINE_WIDTH, LINE_WIDTH)

# Function to check for a win
def check_win():
    # Check rows
    for row in range(BOARD_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True

    # Check columns
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if board[row][col] == '':
                board[row][col] = player_turn
                if player_turn == 'X':
                    player_turn = 'O'
                else:
                    player_turn = 'X'

                if check_win():
                    game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the game board
    draw_board()

    # Draw X and O symbols
    draw_symbols()

    # Check for a win and display the winner
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player {player_turn} wins!", True, LINE_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()
