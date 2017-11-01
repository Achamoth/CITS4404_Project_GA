# By Zen Ly
from __future__ import print_function
from argparse import ArgumentParser, ArgumentTypeError, ArgumentError
from pygame.locals import *
from Room import Room
from Grid import Grid
from Robot import Robot
import sys, math, pygame, FileOps, random


# Methods are from a previous project, hsl to rgb conversion
def hsl_to_rgb(h, s, l):
    # type: (float, float, float) -> (int, int, int)
    """Hue [0,360), S [0,1] V [0,1]
    Reference https://en.wikipedia.org/wiki/HSL_and_HSV#From_HSL
    """
    c = (1 - abs(2 * l - 1)) * s
    h = h * 6 #360/60
    x = c * (1 - abs(h % 2 - 1))
    i = int(h)
    rgb = [0, 0, 0]
    rgb[(7 - i) % 3] = x
    rgb[int((i + 1) / 2) % 3] = c
    m = l - c / 2
    rgb = [x + m for x in rgb]
    rgb = [int(min(x * 256, 255)) for x in rgb]
    return tuple(rgb)


def match_aspect_ratio(target, current):
    # type: ((int, int), (int, int)) -> (int, int)
    if current[0] / target[0] > current[1] / target[1]:
        return (int(target[0] * current[1] / target[1]), int(target[1] * current[1] / target[1]))
    else:
        return (int(target[0] * current[0] / target[0]), int(target[1] * current[0] / target[0]))


if __name__ == '__main__':

    args = ArgumentParser()
    args.add_argument("-rw", "--room-width", type=int, default=10, required=False,
                      help="Width of room")
    args.add_argument("-rh", "--room-height", type=int, default=10, required=False,
                      help="Height of room")
    args.add_argument("-rx", "--robot-x", type=int, default=-1, required=False,
                      help="Robot Starting Position X")
    args.add_argument("-ry", "--robot-y", type=int, default=-1, required=False,
                      help="Robot Starting Position Y")
    args.add_argument("-cc", "--can-chance", type=float, default=0.5, required=False,
                      help="Chance for a cell to contain a can")

    def check_solution(sol):
        sol = eval(sol)
        if not type(sol) is list:
            raise ArgumentTypeError(sol, "Expected a List")
        if not len(sol) == 243 or not all(isinstance(i, int) for i in sol):
            raise ArgumentError(sol, "Expected a list of 243 integers")
        if not all(0 <= i <= 6 for i in sol):
            raise ArgumentError(sol, "Integers must be within the range [0,6]")
        return sol

    args.add_argument("-s", "--solution",
                      type=check_solution,
                      # Ammar's 10000 generation, best solution so far.
                      default=[1, 5, 4, 3, 5, 5, 2, 5, 3, 2, 2, 1, 3, 2, 3, 2, 5, 6, 0, 5, 1, 3, 5, 2, 1, 1, 6, 6, 5, 2, 3, 1, 1, 1, 5,
                1, 2, 1, 6, 3, 2, 0, 2, 5, 4, 3, 5, 0, 3, 5, 1, 0, 5, 5, 2, 5, 5, 2, 2, 3, 1, 2, 6, 2, 5, 4, 2, 3, 0, 2,
                5, 4, 0, 5, 6, 3, 2, 1, 0, 2, 1, 0, 5, 4, 0, 5, 2, 2, 0, 0, 2, 2, 4, 2, 2, 6, 3, 6, 4, 0, 5, 6, 3, 0, 6,
                2, 5, 6, 0, 1, 1, 6, 1, 0, 1, 5, 0, 0, 1, 4, 3, 2, 3, 3, 1, 2, 0, 5, 5, 3, 5, 5, 2, 3, 6, 0, 5, 0, 2, 3,
                5, 0, 5, 4, 0, 5, 5, 3, 3, 5, 2, 5, 6, 0, 5, 3, 1, 2, 3, 1, 3, 3, 1, 5, 4, 3, 5, 4, 2, 5, 4, 6, 2, 4, 1,
                2, 4, 2, 5, 6, 3, 5, 6, 3, 5, 3, 1, 4, 5, 1, 5, 6, 1, 1, 3, 1, 5, 4, 1, 2, 6, 0, 2, 5, 2, 5, 5, 1, 5, 0,
                6, 6, 5, 5, 4, 5, 3, 4, 6, 1, 5, 6, 0, 6, 4, 2, 2, 6, 5, 0, 1, 3, 0, 6, 6, 0, 4, 4, 5, 4, 5, 6, 1],
                      required=False,
                      help="Solution to test (list of 243 integers in range [0,6])")

    args.add_argument("-f", "--fps", type=int, default=2, required=False,
                      help="Frames per second of the simulation")
    args.add_argument("-p", "--pause", action='store_true',
                      help="If the simulation should start paused. SPACE to toggle pause.")
    args.add_argument("-sc", "--scale", type=int, default=-1, required=False,
                      help="How much to scale up the display."
                           "Default is to scale it up to the largest possible power of two scale.")
    args = vars(args.parse_args())

    # Arguments
    rw, rh = args["room_width"], args["room_height"]
    robot_start_pos = (args["robot_x"], args["robot_y"])
    can_chance = args["can_chance"]
    solution = args["solution"]
    fps = args["fps"]
    paused = args["pause"]
    scale = args["scale"]
    situations = FileOps.readSituations('Situations.txt')

    # Colours
    BLACK = hsl_to_rgb(0, 0, 0)
    WHITE = hsl_to_rgb(0, 0, 1)
    DARK_GRAY = hsl_to_rgb(0, 0, 0.2)
    CLEAR = (0, 0, 0, 0)
    RED = hsl_to_rgb(0, 1, 0.5)
    LIGHT_BLUE = hsl_to_rgb(200.0/360, 1, 0.5)

    # Grid
    grid = Grid((rw, rh), (7, 7), 1)

    # PyGame Setup
    pygame.init()
    clock = pygame.time.Clock()
    render_flags = pygame.HWSURFACE
    screen_flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

    display_info = pygame.display.Info()
    dw = display_info.current_w
    dh = display_info.current_h

    ww, wh = grid.draw_size()
    if scale <= 0:
        while ww <= dw and wh <= dh:
            ww *= 2
            wh *= 2
        ww = int(ww / 2)
        wh = int(wh / 2)
    else:
        ww *= scale
        wh *= scale
        while (ww > dw or wh > dh) and scale > 1:
            ww /= scale
            wh /= scale
            scale -= 1
            ww *= scale
            wh *= scale

    screen = pygame.display.set_mode((ww, wh), screen_flags)

    pygame.display.set_caption("Robby the Cleaner")

    # Render buffers
    screen_buffer = pygame.SurfaceType(grid.draw_size(), render_flags)
    grid_buffer = pygame.SurfaceType(grid.draw_size(), render_flags)
    grid_buffer.fill(BLACK)
    grid.draw(grid_buffer, DARK_GRAY)

    # Assets
    img_robot = pygame.image.load("assets/robot.png").convert_alpha()
    img_can = pygame.image.load("assets/can.png").convert_alpha()
    img_up = pygame.image.load("assets/up.png").convert_alpha()
    img_down = pygame.image.load("assets/down.png").convert_alpha()
    img_right = pygame.image.load("assets/right.png").convert_alpha()
    img_left = pygame.image.load("assets/left.png").convert_alpha()
    img_nop = pygame.image.load("assets/nop.png").convert_alpha()
    img_pickup = pygame.image.load("assets/pickup.png").convert_alpha()
    img_random = pygame.image.load("assets/random.png").convert_alpha()
    action_imgs = [img_up, img_down, img_right, img_left, img_nop, img_pickup, img_random]
    cell_temp = img_can.copy()

    # Simulation objects
    room = Room(rw, rh, can_chance)
    robot = Robot()
    robot.changeStrat(solution)
    if room.isWall(*robot_start_pos):
        robot.moveRobot(random.randrange(0, rw), random.randrange(0, rh))
    else:
        robot.moveRobot(*robot_start_pos)

    step = 0
    last_action = -1
    last_pos = (0, 0)
    cans = 0

    while True:
        clock.tick(fps)
        pygame.display.set_caption("Robby the Cleaner - Round: {} - Points:{} - Cans:{} ({} Remaining)".format(step, robot.points, cans, room.numCans))

        # Events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), screen_flags)
                screen.fill(BLACK)
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    paused = not paused

        # Render
        # Draw grid on the screen buffer
        screen_buffer.blit(grid_buffer, (0, 0))

        # Cans
        for y in range(rh):
            for x in range(rw):
                if room.isCan(x, y):
                    cell_temp.fill(CLEAR)
                    cell_temp.blit(img_can, (0, 0))
                    cell_temp.fill(RED, None, pygame.BLEND_RGB_MULT)
                    screen_buffer.blit(cell_temp, grid.cell_rect((x, y)))
        # Robot
        cell_temp.fill(CLEAR)
        cell_temp.blit(img_robot, (0, 0))
        cell_temp.fill(WHITE, None, pygame.BLEND_RGB_MULT)
        screen_buffer.blit(cell_temp, grid.cell_rect((robot.x, robot.y)))

        # Last Action
        if last_action >= 0:
            cell_temp.fill(CLEAR)
            cell_temp.blit(action_imgs[last_action], (0, 0))
            cell_temp.fill(LIGHT_BLUE, None, pygame.BLEND_RGB_MULT)
            screen_buffer.blit(cell_temp, grid.cell_rect(last_pos))

        screen_size = screen.get_size()
        new_size = match_aspect_ratio(screen_buffer.get_size(), screen_size)
        new_position = tuple(int((screen_size[i] - new_size[i]) / 2) for i in [0, 1])
        screen.blit(pygame.transform.scale(screen_buffer, new_size), new_position)
        pygame.display.flip()

        # Logic
        # Skip logic if paused
        if paused:
            continue
        step += 1
        last_cans = room.numCans
        last_pos = (robot.x, robot.y)
        last_action = robot.decide(room, situations)
        cans += last_cans - room.numCans

