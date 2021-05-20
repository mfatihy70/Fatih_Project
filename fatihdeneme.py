import pygame

pygame.init()

class game_win():
    def __init__(self):
        # Oyun penceresi
        self.run = True
        pygame.display.set_caption("Fatih deneme")
        self.height = 640
        self.widht = 640
        self.win = pygame.display.set_mode((self.height, self.widht))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont("Arial", 40)
        self.sit = "at game menu"

        # Oyun ekranı ayarları        
        self.bg = pygame.image.load("Images/bg.png")
        self.start = pygame.image.load("Images/basla.png")
        self.exit = pygame.image.load("Images/çıkış.png")
        self.retry = pygame.image.load("Images/tekraroyna.png")

        # KÜÇÜK ADAM
        # Küçük adam aşağı
        self.lilman_down = [pygame.image.load("Images/pxl_D1.png"),
                            pygame.image.load("Images/pxl_D2.png"),
                            pygame.image.load("Images/pxl_D1.png"),
                            pygame.image.load("Images/pxl_D3.png")]

        # Küçük adam yukarı
        self.lilman_up = [pygame.image.load("Images/pxl_U1.png"),
                          pygame.image.load("Images/pxl_U2.png"),
                          pygame.image.load("Images/pxl_U1.png"),
                          pygame.image.load("Images/pxl_U3.png")]

        # Küçük adam sağa
        self.lilman_right = [pygame.image.load("Images/pxl_R1.png"),
                             pygame.image.load("Images/pxl_R2.png"),
                             pygame.image.load("Images/pxl_R1.png"),
                             pygame.image.load("Images/pxl_R3.png")]

        # Küçük adam sola
        self.lilman_left = [pygame.image.load("Images/pxl_L1.png"),
                            pygame.image.load("Images/pxl_L2.png"),
                            pygame.image.load("Images/pxl_L1.png"),
                            pygame.image.load("Images/pxl_L3.png")]

        # Küçük adam ev
        self.lilman_home = pygame.image.load("Images/lilmanhouse.png")

        # Küçük adam araba
        self.lilman_car_LE = pygame.image.load("Images/lilman_car_LE.png")
        self.lilman_car_DE = pygame.image.load("Images/lilman_car_DE.png")
        self.lilman_car_RE = pygame.image.load("Images/lilman_car_RE.png")
        self.lilman_car_UE = pygame.image.load("Images/lilman_car_UE.png")
        self.lilman_car_U = pygame.image.load("Images/lilman_car_U.png")
        self.lilman_car_D = pygame.image.load("Images/lilman_car_D.png")
        self.lilman_car_R = pygame.image.load("Images/lilman_car_R.png")
        self.lilman_car_L = pygame.image.load("Images/lilman_car_L.png")

        # Küçük adam özellikler
        self.lilman_y = 60
        self.lilman_x = 180
        self.lilman_is_up = False
        self.lilman_is_down = False
        self.lilman_is_right = False
        self.lilman_is_left = False
        self.lilman_is_standing = True
        self.lilman_walk_count = 0
        self.lilman_at_home = False
        self.lilman_home_door = pygame.Rect(96, 292, 50, 62)
        self.lilman_car_x = 64
        self.lilman_car_y = 480
        self.lilman_car_is_U = False
        self.lilman_car_is_D = False
        self.lilman_car_is_R = False
        self.lilman_car_is_L = False
        self.lilman_at_car = False
        self.lilman_exitted_car = False

        # KÜÇÜK KADIN
        # Küçük kadın aşağı
        self.lilwoman_down = [pygame.image.load("Images/wpxl_D1.png"),
                              pygame.image.load("Images/wpxl_D2.png"),
                              pygame.image.load("Images/wpxl_D1.png"),
                              pygame.image.load("Images/wpxl_D3.png")]

        # Küçük kadın yukarı
        self.lilwoman_up = [pygame.image.load("Images/wpxl_U1.png"),
                            pygame.image.load("Images/wpxl_U2.png"),
                            pygame.image.load("Images/wpxl_U1.png"),
                            pygame.image.load("Images/wpxl_U3.png")]

        # Küçük kadın sağa
        self.lilwoman_right = [pygame.image.load("Images/wpxl_R1.png"),
                               pygame.image.load("Images/wpxl_R2.png"),
                               pygame.image.load("Images/wpxl_R1.png"),
                               pygame.image.load("Images/wpxl_R3.png")]

        # Küçük kadın sola
        self.lilwoman_left = [pygame.image.load("Images/wpxl_L1.png"),
                              pygame.image.load("Images/wpxl_L2.png"),
                              pygame.image.load("Images/wpxl_L1.png"),
                              pygame.image.load("Images/wpxl_L3.png")]

        # Küçük kadın ev
        self.lilwoman_home = pygame.image.load("Images/lilwomanhouse.png")

        # Küçük kadın araba
        self.lilwoman_car_RE = pygame.image.load("Images/lilwoman_car_RE.png")
        self.lilwoman_car_LE = pygame.image.load("Images/lilwoman_car_LE.png")
        self.lilwoman_car_DE = pygame.image.load("Images/lilwoman_car_DE.png")
        self.lilwoman_car_UE = pygame.image.load("Images/lilwoman_car_UE.png")
        self.lilwoman_car_U = pygame.image.load("Images/lilwoman_car_U.png")
        self.lilwoman_car_D = pygame.image.load("Images/lilwoman_car_D.png")
        self.lilwoman_car_R = pygame.image.load("Images/lilwoman_car_R.png")
        self.lilwoman_car_L = pygame.image.load("Images/lilwoman_car_L.png")

        # Küçük kadın özellikleri
        self.lilwoman_y = 60
        self.lilwoman_x = 400
        self.lilwoman_is_up = False
        self.lilwoman_is_down = False
        self.lilwoman_is_right = False
        self.lilwoman_is_left = False
        self.lilwoman_is_standing = True
        self.lilwoman_walk_count = 0
        self.lilwoman_at_home = False
        self.lilwoman_home_door = pygame.Rect(492, 292, 50, 62)
        self.lilwoman_car_x = 448
        self.lilwoman_car_y = 480
        self.lilwoman_car_is_U = False
        self.lilwoman_car_is_D = False
        self.lilwoman_car_is_R = False
        self.lilwoman_car_is_L = False
        self.lilwoman_at_car = False
        self.lilwoman_exitted_car = False

    def draw(self):
        if self.sit == "at game menu":
            self.win.fill((0, 255, 255))                    
            self.win.blit(self.game_font.render("Fatih Pygame Deneme", True, (255,255,255)), (130, 200))
            self.win.blit(self.start, (250, 400))
            if 250 < self.mouse_x < 400 and 400 < self.mouse_y < 450 and pygame.mouse.get_pressed()[0] == 1:
                self.sit = "at game"



        elif self.sit  == "at game":
            # Arkaplan
            self.win.blit(self.bg, (0, 0))

            # Evler
            self.win.blit(self.lilman_home, (-8, 100))
            self.win.blit(self.lilwoman_home, (392, 100))

            # Arabalar
            if not self.lilman_at_car and not self.lilman_exitted_car:
                self.win.blit(self.lilman_car_RE, (self.lilman_car_x, self.lilman_car_y))

            if not self.lilwoman_at_car and not self.lilwoman_exitted_car:
                self.win.blit(self.lilwoman_car_LE, (self.lilwoman_car_x, self.lilwoman_car_y))

            # Küçük adam animasyon
            if not self.lilman_at_home and not self.lilman_at_car:
                if self.lilman_walk_count + 1 >= 12:
                    self.lilman_walk_count = 0
                if self.lilman_is_up:
                    self.win.blit(self.lilman_up[self.lilman_walk_count // 3], (self.lilman_x, self.lilman_y))
                    self.lilman_walk_count += 1
                    self.lilman_is_up = False
                elif self.lilman_is_down:
                    self.win.blit(self.lilman_down[self.lilman_walk_count // 3], (self.lilman_x, self.lilman_y))
                    self.lilman_walk_count += 1
                    self.lilman_is_down = False
                elif self.lilman_is_right:
                    self.win.blit(self.lilman_right[self.lilman_walk_count // 3], (self.lilman_x, self.lilman_y))
                    self.lilman_walk_count += 1
                    self.lilman_is_right = False
                elif self.lilman_is_left:
                    self.win.blit(self.lilman_left[self.lilman_walk_count // 3], (self.lilman_x, self.lilman_y))
                    self.lilman_walk_count += 1
                    self.lilman_is_left = False
                else:
                    self.win.blit(self.lilman_down[0], (self.lilman_x, self.lilman_y))

            # Küçük kadın animasyon
            if not self.lilwoman_at_home and not self.lilwoman_at_car:
                if self.lilwoman_walk_count + 1 >= 12:
                    self.lilwoman_walk_count = 0
                if self.lilwoman_is_up:
                    self.win.blit(self.lilwoman_up[self.lilwoman_walk_count // 3], (self.lilwoman_x, self.lilwoman_y))
                    self.lilwoman_walk_count += 1
                    self.lilwoman_is_up = False
                elif self.lilwoman_is_down:
                    self.win.blit(self.lilwoman_down[self.lilwoman_walk_count // 3], (self.lilwoman_x, self.lilwoman_y))
                    self.lilwoman_walk_count += 1
                    self.lilwoman_is_down = False
                elif self.lilwoman_is_right:
                    self.win.blit(self.lilwoman_right[self.lilwoman_walk_count // 3], (self.lilwoman_x, self.lilwoman_y))
                    self.lilwoman_walk_count += 1
                    self.lilwoman_is_right = False
                elif self.lilwoman_is_left:
                    self.win.blit(self.lilwoman_left[self.lilwoman_walk_count // 3], (self.lilwoman_x, self.lilwoman_y))
                    self.lilwoman_walk_count += 1
                    self.lilwoman_is_left = False
                else:
                    self.win.blit(self.lilwoman_down[0], (self.lilwoman_x, self.lilwoman_y))

            self.lilmanbox = pygame.Rect(self.lilman_x, self.lilman_y, 64, 64)
            self.lilwomanbox = pygame.Rect(self.lilwoman_x, self.lilwoman_y, 64, 64)
            self.lilman_car_box = pygame.Rect(self.lilman_car_x, self.lilman_car_y, 128, 128)
            self.lilwoman_car_box = pygame.Rect(self.lilwoman_car_x, self.lilwoman_car_y, 128, 128)

            # Küçük adam eve gelme
            if self.lilmanbox.colliderect(self.lilman_home_door) and self.button[pygame.K_q]:
                self.lilman_at_home = True
            elif not self.lilmanbox.colliderect(self.lilman_home_door):
                self.lilman_at_home = False

            # Küçük kadın eve gelme
            if self.lilwomanbox.colliderect(self.lilwoman_home_door) and self.button[pygame.K_PAGEUP]:
                self.lilwoman_at_home = True
            elif not self.lilwomanbox.colliderect(self.lilwoman_home_door):
                self.lilwoman_at_home = False

            # Küçük adam arabaya binme
            if self.lilmanbox.colliderect(self.lilman_car_box) and self.button[pygame.K_SPACE]:
                self.lilman_at_car = True
                self.lilman_exitted_car = False
            elif not self.lilmanbox.colliderect(self.lilman_car_box) and self.button[pygame.K_SPACE]:
                self.lilman_at_car = False
                self.lilman_exitted_car = True

            # Küçük kadın arabaya binme
            if self.lilwomanbox.colliderect(self.lilwoman_car_box) and self.button[pygame.K_o]:
                self.lilwoman_at_car = True
                self.lilwoman_exitted_car = False
            elif not self.lilwomanbox.colliderect(self.lilwoman_car_box) and self.button[pygame.K_o]:
                self.lilwoman_at_car = False
                self.lilwoman_exitted_car = True

            # Küçük adam arabayı sürme
            if self.lilman_at_car and \
                    self.lilman_car_is_R == False and \
                    self.lilman_car_is_L == False and \
                    self.lilman_car_is_D == False and \
                    self.lilman_car_is_U == False:
                self.win.blit(self.lilman_car_R, (self.lilman_car_x, self.lilman_car_y))

            if self.lilman_car_is_U:
               self.win.blit(self.lilman_car_U, (self.lilman_car_x, self.lilman_car_y))
            if self.lilman_car_is_D:
               self.win.blit(self.lilman_car_D, (self.lilman_car_x, self.lilman_car_y))
            if self.lilman_car_is_R:
               self.win.blit(self.lilman_car_R, (self.lilman_car_x, self.lilman_car_y))
            if self.lilman_car_is_L:
               self.win.blit(self.lilman_car_L, (self.lilman_car_x, self.lilman_car_y))

            # Küçük adam arabadan inme
            if self.lilman_exitted_car:
                if self.lilman_car_is_U:
                    self.win.blit(self.lilman_car_UE, (self.lilman_car_x, self.lilman_car_y))
                elif self.lilman_car_is_D:
                    self.win.blit(self.lilman_car_DE, (self.lilman_car_x, self.lilman_car_y))
                elif self.lilman_car_is_R:
                    self.win.blit(self.lilman_car_RE, (self.lilman_car_x, self.lilman_car_y))
                elif self.lilman_car_is_L:
                    self.win.blit(self.lilman_car_LE, (self.lilman_car_x, self.lilman_car_y))

            # Küçük kadın arabaya binme
            if self.lilwoman_at_car and \
                    self.lilwoman_car_is_R == False and \
                    self.lilwoman_car_is_L == False and \
                    self.lilwoman_car_is_D == False and \
                    self.lilwoman_car_is_U == False:
                self.win.blit(self.lilwoman_car_L, (self.lilwoman_car_x, self.lilwoman_car_y))

            if self.lilwoman_car_is_U:
               self.win.blit(self.lilwoman_car_U, (self.lilwoman_car_x, self.lilwoman_car_y))
            if self.lilwoman_car_is_D:
               self.win.blit(self.lilwoman_car_D, (self.lilwoman_car_x, self.lilwoman_car_y))
            if self.lilwoman_car_is_R:
               self.win.blit(self.lilwoman_car_R, (self.lilwoman_car_x, self.lilwoman_car_y))
            if self.lilwoman_car_is_L:
               self.win.blit(self.lilwoman_car_L, (self.lilwoman_car_x, self.lilwoman_car_y))

               # Küçük kadın arabadan inme
            if self.lilwoman_exitted_car:
                if self.lilwoman_car_is_U:
                    self.win.blit(self.lilwoman_car_UE, (self.lilwoman_car_x, self.lilwoman_car_y))
                elif self.lilwoman_car_is_D:
                    self.win.blit(self.lilwoman_car_DE, (self.lilwoman_car_x, self.lilwoman_car_y))
                elif self.lilwoman_car_is_R:
                    self.win.blit(self.lilwoman_car_RE, (self.lilwoman_car_x, self.lilwoman_car_y))
                elif self.lilwoman_car_is_L:
                    self.win.blit(self.lilwoman_car_LE, (self.lilwoman_car_x, self.lilwoman_car_y))

        """elif self.sit == "second game":
            self.win.blit(self.bg2, (0, 0))
            self.lilman_x = 60
            self.lilman_y = 500
            self.lilwoman_x = 520
            self.lilwoman_y = 500
            self.win.blit(self.lilman_down[0], (self.lilman_x, self.lilman_y))
            self.win.blit(self.lilwoman_down[0], (self.lilwoman_x, self.lilwoman_y))

            if self.lilman_walk_count + 1 >= 12:
                self.lilman_walk_count = 0
            if self.lilman_is_up:
                self.win.blit(self.lilman_up[self.lilman_walk_count // 3], (self.lilman_x, self.lilman_y))
                self.lilman_walk_count += 1
                self.lilman_is_up = False
            elif self.lilman_is_down:
                self.win.blit(self.lilman_down[self.lilman_walk_count // 3], (self.lilman_x, self.lilman_y))
                self.lilman_walk_count += 1
                self.lilman_is_down = False

            if self.lilwoman_walk_count + 1 >= 12:
                self.lilwoman_walk_count = 0
            if self.lilwoman_is_up:
                self.win.blit(self.lilwoman_up[self.lilwoman_walk_count // 3], (self.lilwoman_x, self.lilwoman_y))
                self.lilman_walk_count += 1
                self.lilman_is_up = False
            elif self.lilman_is_down:
                self.win.blit(self.lilwoman_down[self.lilwoman_walk_count // 3], (self.lilwoman_x, self.lilwoman_y))
                self.lilwoman_walk_count += 1
                self.lilwoman_is_down = False"""


        if self.sit == "at game over menu":
            self.win.fill((255,0,0))
            self.win.blit(self.game_font.render("Oyundan çıktınız", True, (255,255,255)), (170, 200))
            self.win.blit(self.exit, (400, 400))
            self.win.blit(self.retry, (100, 400))
            if 400 < self.mouse_x < 550 and 100 < self.mouse_y < 450 and pygame.mouse.get_pressed()[0] == 1:
                self.run = False
            elif 100 < self.mouse_x < 250 and 100 < self.mouse_y < 450 and pygame.mouse.get_pressed()[0] == 1:
                self.sit = "at game menu"       

        """# Fetih canavar
        self.win.blit(self.fetih_pasa,(self.fetih_x, self.fetih_y))"""

        self.clock.tick(60)

        pygame.display.update()

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sit = "at game over menu"

        self.mouse_x ,self.mouse_y = pygame.mouse.get_pos()
        self.button = pygame.key.get_pressed()

        if self.button[pygame.K_ESCAPE]:          
            self.sit = "at game over menu"
            

        speed = 5

        # Küçük adam kontrolleri
        if self.button[pygame.K_w] and self.lilman_y > 0:
            self.lilman_y -= speed
            self.lilman_is_up = True
            self.lilman_is_down = False
            self.lilman_is_right = False
            self.lilman_is_left = False
            self.lilman_is_standing = False

        if self.button[pygame.K_s] and self.lilman_y < 560:
            self.lilman_y += speed
            self.lilman_is_up = False
            self.lilman_is_down = True
            self.lilman_is_right = False
            self.lilman_is_left = False
            self.lilman_is_standing = False

        if self.button[pygame.K_a] and self.lilman_x > 0:
            self.lilman_x -= speed
            self.lilman_is_up = False
            self.lilman_is_down = False
            self.lilman_is_right = False
            self.lilman_is_left = True
            self.lilman_is_standing = False

        if self.button[pygame.K_d] and self.lilman_x < 580:
            self.lilman_x += speed
            self.lilman_is_up = False
            self.lilman_is_down = False
            self.lilman_is_right = True
            self.lilman_is_left = False
            self.lilman_is_standing = False

        # Küçük kadın kontrolleri
        if self.button[pygame.K_UP] and self.lilwoman_y > 0:
            self.lilwoman_y -= speed
            self.lilwoman_is_up = True
            self.lilwoman_is_down = False
            self.lilwoman_is_right = False
            self.lilwoman_is_left = False
        if self.button[pygame.K_DOWN] and self.lilwoman_y < 560:
            self.lilwoman_y += speed
            self.lilwoman_is_up = False
            self.lilwoman_is_down = True
            self.lilwoman_is_right = False
            self.lilwoman_is_left = False
        if self.button[pygame.K_LEFT] and self.lilwoman_x > 0:
            self.lilwoman_x -= speed
            self.lilwoman_is_up = False
            self.lilwoman_is_down = False
            self.lilwoman_is_right = False
            self.lilwoman_is_left = True
        if self.button[pygame.K_RIGHT] and self.lilwoman_x < 580:
            self.lilwoman_x += speed
            self.lilwoman_is_up = False
            self.lilwoman_is_down = False
            self.lilwoman_is_right = True
            self.lilwoman_is_left = False

        # Arabayı sürme
        car_speed = 10
        if self.lilman_at_car:
            if self.button[pygame.K_w] and self.lilman_car_y > 0:
                self.lilman_car_y -= car_speed
                self.lilman_car_is_U = True
                self.lilman_car_is_D = False
                self.lilman_car_is_R = False
                self.lilman_car_is_L = False

            if self.button[pygame.K_s] and self.lilman_car_y < 512:
                self.lilman_car_y += car_speed
                self.lilman_car_is_D = True
                self.lilman_car_is_U = False
                self.lilman_car_is_L = False
                self.lilman_car_is_R = False

            if self.button[pygame.K_a] and self.lilman_car_x > 0:
                self.lilman_car_x -= car_speed
                self.lilman_car_is_L = True
                self.lilman_car_is_D = False
                self.lilman_car_is_R = False
                self.lilman_car_is_U = False

            if self.button[pygame.K_d] and self.lilman_car_x < 512:
                self.lilman_car_x += car_speed
                self.lilman_car_is_R = True
                self.lilman_car_is_L = False
                self.lilman_car_is_D = False
                self.lilman_car_is_U = False

            if self.button[pygame.K_v]:
                self.lilman_x = self.lilman_car_x
                self.lilman_y = self.lilman_car_y
                self.lilman_exitted_car = True
                self.lilman_at_car = False

        if self.lilwoman_at_car:
            if self.button[pygame.K_UP] and self.lilwoman_car_y > 0:
                self.lilwoman_car_y -= car_speed
                self.lilwoman_car_is_U = True
                self.lilwoman_car_is_D = False
                self.lilwoman_car_is_R = False
                self.lilwoman_car_is_L = False

            if self.button[pygame.K_DOWN] and self.lilwoman_car_y < 512:
                self.lilwoman_car_y += car_speed
                self.lilwoman_car_is_D = True
                self.lilwoman_car_is_U = False
                self.lilwoman_car_is_L = False
                self.lilwoman_car_is_R = False

            if self.button[pygame.K_LEFT] and self.lilwoman_car_x > 0:
                self.lilwoman_car_x -= car_speed
                self.lilwoman_car_is_L = True
                self.lilwoman_car_is_D = False
                self.lilwoman_car_is_R = False
                self.lilwoman_car_is_U = False

            if self.button[pygame.K_RIGHT] and self.lilwoman_car_x < 512:
                self.lilwoman_car_x += car_speed
                self.lilwoman_car_is_R = True
                self.lilwoman_car_is_L = False
                self.lilwoman_car_is_D = False
                self.lilwoman_car_is_U = False

            if self.button[pygame.K_p]:
                self.lilwoman_x = self.lilwoman_car_x
                self.lilwoman_y = self.lilwoman_car_y
                self.lilwoman_exitted_car = True
                self.lilwoman_at_car = False

        """# Fetih paşanın canavarı
        if self.button[pygame.K_i] and self.fetih_y > 0:
            self.fetih_y -= speed
        elif self.button[pygame.K_k] and self.fetih_y < 580:
            self.fetih_y += speed
        elif self.button[pygame.K_j] and self.fetih_x > 0:
            self.fetih_x -= speed
        elif self.button[pygame.K_l] and self.fetih_x < 580:
            self.fetih_x += speed"""

        self.draw()

Game = game_win()

while Game.run:
    pygame.time.delay(30)
    pose = Game.game()

    if pose:
        self.run = False

pygame.quit()
