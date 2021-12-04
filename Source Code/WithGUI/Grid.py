# By Zen, from a previous project, grid drawing helper class
import pygame


def draw_grid_size(size, cell_size, line_width):
    # type: ((int, int), (int, int), int) -> Tuple[Union[int, Any], ...]
    return tuple(gs * (cs + line_width) + line_width for gs, cs in zip(size, cell_size))


def draw_grid(surface, size, cell_size, line_width, line_color):
    # type: (pygame.Surface, (int, int), (int, int), int, color) -> None
    win_size = draw_grid_size(size, cell_size, line_width)
    for y in range(size[1] + 1):
        y *= cell_size[1] + line_width
        y += line_width / 2
        pygame.draw.line(surface, line_color, (0, y), (win_size[0], y), line_width)
        # pygame.gfxdraw.hline(surface, 0, win_size[0], y, line_color)

    for x in range(size[0] + 1):
        x *= cell_size[0] + line_width
        x += line_width / 2
        pygame.draw.line(surface, line_color, (x, 0), (x, win_size[1]), line_width)
        # pygame.gfxdraw.vline(surface, x, 0, win_size[1], line_color)


class Grid:
    def __init__(self, size, cell_size, line_width):
        # type: ((int, int), (int, int), int) -> None
        self.size = size
        self.cell_size = cell_size
        self.line_width = line_width

    def draw_size(self):
        # type: () -> (int, int)
        """Size of the rectangle required to draw this"""
        return draw_grid_size(self.size, self.cell_size, self.line_width)

    def draw(self, surface, line_color):
        # type: (pygame.SurfaceType, (int, int, int)) -> None
        return draw_grid(surface, self.size, self.cell_size, self.line_width, line_color)

    def cell_pos(self, position):
        # type: ((int, int)) -> (int, int)
        """Returns the position of the cell"""
        return tuple(self.line_width + (self.cell_size[i] + self.line_width) * position[i] for i in [0, 1])

    def cell_rect(self, position):
        # type: ((int, int)) -> pygame.Rect
        """Returns a rectangle that contains the cell"""
        return pygame.Rect(
            tuple(self.line_width + (self.cell_size[i] + self.line_width) * position[i] for i in [0, 1]),
            self.cell_size
        )
