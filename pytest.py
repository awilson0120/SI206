from pygame import *
from pygame.sprite import *
import pyglet
 
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
 
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load('harry.bmp').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
                pygame.quit()
            else:
                self.rect.left = block.rect.right
                pygame.quit()
 
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                pygame.quit()
            else:
                self.rect.top = block.rect.bottom
                pygame.quit()

class Cup(pygame.sprite.Sprite):
      def __init__(self, x, y):
        super().__init__()
        self.image = image.load('Triwizard_Cup.bmp').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Room(object):
    wall_list = []
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
 
 
class Room1(Room):
    def __init__(self):
        super().__init__()
        walls = [[0, 0, 20, 350, GREEN],
                 [0, 350, 20, 350, GREEN],
                 [780, 0, 20, 250, GREEN],
                 [780, 350, 20, 250, GREEN],
                 [20, 0, 760, 20, GREEN],
                 [20, 580, 760, 20, GREEN],
                 [250, 70, 20, 450, GREEN],
                 [250, 300, 450, 20, GREEN],
                 [700, 300, 20, 100, GREEN]
                ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room2(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, GREEN],
                 [0, 350, 20, 250, GREEN],
                 [780, 0, 20, 250, GREEN],
                 [780, 350, 20, 250, GREEN],
                 [20, 0, 760, 20, GREEN],
                 [20, 580, 760, 20, GREEN],
                 [190, 0, 20, 525, GREEN],
                 [590, 75, 20, 505, GREEN],
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, GREEN],
                 [0, 350, 20, 250, GREEN],
                 [780, 0, 20, 250, GREEN],
                 [780, 350, 20, 250, GREEN],
                 [20, 0, 760, 20, GREEN],
                 [20, 580, 760, 20, GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
        
        
        
            
        #for x in range(100, 800, 100):
            # for y in range(50, 451, 300):
            #     wall = Wall(x, y, 20, 200, GREEN)
            #     self.wall_list.add(wall)
 
        #for x in range(150, 700, 100):
            # wall = Wall(x, 200, 20, 200, GREEN)
            # self.wall_list.add(wall)
 
 
def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    player = Player(50, 50)
    cup = Cup(700,250)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    staticsprites = pygame.sprite.Group()
    staticsprites.add(cup)

    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
 
    room = Room3()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]

    done = False

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 25)
    frame_count = 0
    frame_rate = 60
    start_time = 45
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
        
        player.move(current_room.wall_list)
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
        
        total_seconds = start_time - (frame_count//frame_rate)
        if total_seconds < 0:
            pygame.quit()
        minutes = total_seconds//60
        seconds = total_seconds%60
        output_string = "Time left: {0:02}:{1:02}".format(minutes,seconds)
        text = font.render(output_string, True, GREEN)
        screen.blit(text, [50,50])
        frame_count+=1
        clock.tick(frame_rate)
        pygame.display.flip()

        screen.fill(BLACK)
        
        movingsprites.draw(screen)
        if current_room_no ==2:
            staticsprites.draw(screen)
        current_room.wall_list.draw(screen)

    
    pygame.quit()
 
if __name__ == "__main__":
    main()