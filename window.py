import pygame

white = (255,255,255)
class Window:
    def __init__(self, game):
        self.height = 600
        self.width = 600
        self.size = 600/3
        self.game = game
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Jogo da VeIA")
        pygame.font.init()

    def draw_board(self):
        for i in range(1,3):
            pygame.draw.line(self.window, (0,0,0), (0, i*self.size), (self.width, i*self.size), 3)
            pygame.draw.line(self.window, (0,0,0), (i*self.size,0), (i*self.size, self.height ), 3)
        
        for i in range(3):
            for j in range(3):
                font = pygame.font.SysFont("roboto", 100)
                x = j*self.size
                y = i*self.size

                text = font.render(self.game.board[i][j], 1, (128,0,0))
                self.window.blit(text, ((x+75),(y+75)))
    
    def redraw_board(self):
        self.window.fill(white)
        self.draw_board()

    def update_display(self):
        pygame.display.update()

    def input_user_event(self, played):
        for event in pygame.event.get():
            #print(event.type)
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                print('Clique')
                pos = event.pos
                print(pos)
                i = int(pos[1]/200)
                j = int(pos[0]/200)
                print(i)
                print(j)
                if played == False:
                    played = True
                return i,j
    
    def quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return