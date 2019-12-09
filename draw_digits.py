import pygame

class Color:
    def __init__(self, color_code, char_value):
        self.color_code = color_code
        self.value = char_value

class GridCell:
    def __init__(self, size, x, y):
        self.original_image = pygame.Surface((size, size))
        self.original_image.fill((0, 0, 0))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hovered = False
        self.value = ' '

    def Hovered(self, color_selected):
        self.hovered = True

        highlight = pygame.Surface((self.rect.width, self.rect.height))
        highlight.fill((255, 255, 255))
        highlight.set_alpha(35)

        new_color = pygame.Surface((self.rect.width, self.rect.height))
        new_color.fill(color_selected.color_code)

        self.image = self.original_image.copy()
        self.image.blit(new_color, (0, 0))
        self.image.blit(highlight, (0, 0))

    def NotHovered(self):
        self.hovered = False
        self.image = self.original_image.copy()

    def Change(self, color):
        self.value = color.value
        self.original_image.fill(color.color_code)
        self.image.fill(color.color_code)

def CreateCells(list_of_cells, cell_size, cells_wide, cells_high):
    for x in range(cells_wide):
        for y in range(cells_high):
            new_cell = GridCell(cell_size, x * cell_size, y * cell_size)
            list_of_cells.append(new_cell)

def Save(number, cells, cell_size, cells_wide, cells_high):
    written_cells = []
    for row in range(cells_high):
        new_row = '0'*cells_wide
        written_cells.append(new_row)

    for cell in cells:
        x = int(cell.rect.x / cell_size)
        y = int(cell.rect.y / cell_size)
        chars = list(written_cells[y])
        chars[x] = '1' if cell.value != ' ' else '0'
        written_cells[y] = "".join(chars)

    write_file = open("myDigits/"  + str(number) + "_digit.txt", 'w')
    for row in range(len(written_cells)):
        write_file.write(written_cells[row])
        # if row == len(written_cells) - 1:
        #     write_file.write("]")
        # else:
        #     write_file.write(",")
        write_file.write('\n')
    print("file saved")


def play():
    pygame.init()

    cell_size = 16

    cells_wide = 32
    cells_high = 32
    cells = []

    screen_width = cells_wide * cell_size
    screen_height = cells_high * cell_size

    black = Color((0, 0, 0), ' ')
    red = Color((255, 0, 0), 'r')
    white = Color((255, 255, 255), 'w')
    grey = Color((128, 128, 128), 'g')

    color_select = white
    screen = pygame.display.set_mode((screen_width, screen_height))
    CreateCells(cells, cell_size, cells_wide, cells_high)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:

                color_select = white

                if event.key == pygame.K_s or event.key == pygame.K_ESCAPE:
                    print("what is the number?")
                    number = int(input())
                    Save(number, cells, cell_size, cells_wide, cells_high)
                    return

            elif pygame.mouse.get_pressed()[0]:
                for cell in cells:
                    if cell.hovered:
                        cell.Change(color_select)

        mouse_pos = pygame.mouse.get_pos()

        for cell in cells:
            if cell.rect.collidepoint(mouse_pos):
                cell.Hovered(color_select)
            else:
                cell.NotHovered()

        for cell in cells:
            screen.blit(cell.image, cell.rect)

        pygame.display.flip()

# if __name__ == "__main__":
#     main()
