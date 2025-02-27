import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 640  # Window size (640x640 for an 8x8 board)
BOARD_SIZE = 8     # 8x8 chessboard
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE

# Colors
WHITE = (247, 248, 236)
GREEN = (116, 151, 79)  
LIGHT_GREEN = (139, 177, 92)
LIGHTER_GREEN = (225, 232, 151)  # Even lighter green
BLACK = (0, 0, 0)

# Knight image
KNIGHT_IMAGE_PATH = 'knight.png'  # Path to your knight image

# Create the window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Knight on Chessboard")

# Font for displaying indices
font = pygame.font.Font(None, 36)


def draw_chessboard(visited_positions, visited_indices):
    """Draws the chessboard with visited squares highlighted."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Determine the base color of the square
            if (row + col) % 2 == 0:
                base_color = WHITE
            else:
                base_color = GREEN

            # Highlight visited squares
            if (row, col) in visited_positions:
                if base_color == GREEN:
                    color = LIGHT_GREEN
                else:
                    color = LIGHTER_GREEN
            else:
                color = base_color

            # Draw the square
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Draw the index if the square is visited
            if (row, col) in visited_positions:
                index = visited_indices[(row, col)]
                text = font.render(str(index), True, BLACK)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                  row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(text, text_rect)


def draw_knight(x, y):
    """Draws the knight image at the given (x, y) position."""
    # Load the knight image (with transparency)
    knight_image = pygame.image.load(KNIGHT_IMAGE_PATH).convert_alpha()
    
    # Resize the knight image to fit the square
    knight_image = pygame.transform.scale(knight_image, (SQUARE_SIZE, SQUARE_SIZE))
    
    # Calculate the position to center the knight image on the square
    position = (y * SQUARE_SIZE, x * SQUARE_SIZE)
    
    # Draw the knight image on the chessboard at the correct position
    screen.blit(knight_image, position)


def draw(knight_position, visited_positions):
    path_index = 0  # Track current position in the path
    visited_indices = {pos: i + 1 for i, pos in enumerate(visited_positions)}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # Move forward
                    path_index = (path_index + 1) % len(visited_positions)
                    knight_position = visited_positions[path_index]
                elif event.key == pygame.K_LEFT:  # Move backward
                    path_index = (path_index - 1) % len(visited_positions)
                    knight_position = visited_positions[path_index]

        # Draw the board and knight
        # Only show visited squares up to the current position in the path
        draw_chessboard(visited_positions[:path_index + 1], visited_indices)
        draw_knight(*knight_position)

        # Update the display
        pygame.display.flip()



"""
if it's not running run this export LD_PRELOAD=/usr/lib64/libstdc++.so.6
"""
