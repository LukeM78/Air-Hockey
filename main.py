import pygame, sys, random
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Air Hockey')
width, height = 1280, 1040
screen = pygame.display.set_mode((width,height))

# Font variables

font_medium, font_large, font_title, font_main_title = pygame.font.SysFont(None, 50), pygame.font.SysFont(None, 75), pygame.font.SysFont(None, 150), pygame.font.SysFont(None, 175)

# All variables listed at the top

puck = pygame.Rect(width/2-15, height/2-15, 40,40)
player = pygame.Rect(width - 60, height/2-80, 80,80)
opponent = pygame.Rect(0, height/2-80, 80,80)
player_score, opponent_score, score_time, game_choice, opponent_speed, opponent_net = 0,0,1,0,7,0
puck_speed_x, puck_speed_y = 8 * random.choice((1,-1)), 8 * random.choice((1,-1))
line_offset_x, line_offset_y, = 0,0
goal_line_1, goal_line_2 = pygame.Rect(0,200,2,560), pygame.Rect(1258,200,2,560)
button_1, button_2, button_3, button_4, button_5 = pygame.Rect(440, 250, 400, 100), pygame.Rect(440, 400, 400, 100), pygame.Rect(440, 250, 400, 100), pygame.Rect(440, 400, 400, 100), pygame.Rect(440, 550, 400, 100)
player_1_selection, player_2_selection = 0,0
leafs = pygame.image.load('leafs.png')
leafs = pygame.transform.scale(leafs,(174,174))
habs = pygame.image.load('habs.png')
habs = pygame.transform.scale(habs, (180,180))
bruins = pygame.image.load('bruins.png')
bruins = pygame.transform.scale(bruins, (180,180))
wings = pygame.image.load('wings.png')
wings = pygame.transform.scale(wings, (200,145))
rangers = pygame.image.load('rangers.png')
rangers = pygame.transform.scale(rangers, (158,177))
hawks = pygame.image.load('hawks.png')
hawks = pygame.transform.scale(hawks, (180,160))
leafs_button, habs_button, bruins_button, wings_button, rangers_button, hawks_button = pygame.Rect(50, 300, 174, 174), pygame.Rect(250, 300, 180, 180), pygame.Rect(450, 300, 180, 180), pygame.Rect (650, 305, 200, 145), pygame.Rect(855, 300, 160, 180), pygame.Rect(1040, 300, 180, 160)

# Function for drawing text

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Loop function for the main menu

def main_menu():
  click = False
  while True:
        screen.fill((255,255,255))
        mx, my = pygame.mouse.get_pos()
        global game_choice, button_1, button_2
        if button_1.collidepoint((mx, my)):
            if click:
              game_choice = 1
              ai_difficulty()
        if button_2.collidepoint((mx, my)):
            if click:
              game_choice = 2
              home_team()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 255), button_2)
        draw_text('AIR', font_main_title, (255,0,0), screen, 250, 50)
        draw_text('HOCKEY', font_main_title, (0,0,255), screen, 525, 50)
        draw_text('1 PLAYER', font_large, (255, 255, 255), screen, 515, 275)
        draw_text('2 PLAYERS', font_large, (255, 255, 255), screen, 500, 425)   

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)

# Menu for selecting the difficulty of the ai

def ai_difficulty():
  global opponent, opponent_net, player_score, opponent_score, opponent_speed
  click = False
  running = True
  while running:
    player_score, opponent_score = 0,0
    screen.fill((255,255,255))
    mx, my = pygame.mouse.get_pos()
    if button_3.collidepoint((mx, my)):
      if click:
        opponent_net = 0
        opponent_speed = 7
        main_game()
    if button_4.collidepoint((mx, my)):
      if click:
        opponent_speed = 8
        opponent_net = 1
        main_game()
    if button_5.collidepoint((mx, my)):
      if click:
        opponent_speed = 9
        opponent_net = 2
        main_game()

    pygame.draw.rect(screen, (0, 0, 0), button_3)
    pygame.draw.rect(screen, (0, 0, 0), button_4)
    pygame.draw.rect(screen, (0, 0, 0), button_5)
    draw_text('SELECT  DIFFICULTY', font_title, (0,0,0), screen, 125, 50)
    draw_text('EASY', font_large, (255, 255, 255), screen, 560, 275)
    draw_text('HARD', font_large, (255, 255, 255), screen, 560, 425)    
    draw_text('IMPOSSIBLE', font_large, (255, 255, 255), screen, 480, 575) 

    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    pygame.display.update()
    mainClock.tick(60)

# Menu loop for player 1 to select team

def home_team():
  click = False
  running = True
  while running:
        screen.fill((255,255,255))
        global player_1_selection, player_score, opponent_score, leafs, habs, bruins, wings, rangers, hawks, leafs_button, habs_button, bruins_button, wings_button, rangers_button, hawks_button
        player_1_selection, player_score, opponent_score = 0,0,0
        draw_text('PLAYER 1', font_title, (225,0,0), screen, 400, 40)
        draw_text('SELECT YOUR TEAM:', font_large, (0,0,0), screen, 375, 175)
        draw_text('HOME TEAM', font_medium, (0,0,0),screen, 540, 600)

        mx, my = pygame.mouse.get_pos()
        if leafs_button.collidepoint((mx, my)):
            if click:
              player_1_selection += 1
              away_team()
        if habs_button.collidepoint((mx, my)):
            if click:
              player_1_selection += 2
              away_team()
        if bruins_button.collidepoint((mx, my)):
            if click:
              player_1_selection += 3
              away_team()
        if wings_button.collidepoint((mx, my)):
            if click:
              player_1_selection += 4
              away_team()
        if rangers_button.collidepoint((mx, my)):
            if click:
              player_1_selection += 5
              away_team()
        if hawks_button.collidepoint((mx, my)):
            if click:
              player_1_selection += 6
              away_team()
        logos()

        click=False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                  click=True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                  running = False
        pygame.display.update()
        mainClock.tick(60)

# Menu loop for player 2 to select team

def away_team():
  click=False
  running = True
  while running:
        screen.fill((255,255,255))
        draw_text('PLAYER 2', font_title, (0,0,255), screen, 400, 40)
        draw_text('SELECT YOUR TEAM:', font_large, (0,0,0), screen, 375, 175)
        draw_text('AWAY TEAM', font_medium, (0,0,0),screen, 540,600)
        global player_2_selection, player_1_selection, opponent_net, goal_line_1, player_score, opponent_score
        opponent_net, goal_line_1 = 0,pygame.Rect(0,200,2,560)
        player_2_selection, player_score, opponent_score = 0,0,0

        mx, my = pygame.mouse.get_pos()
        if leafs_button.collidepoint((mx, my)):
            if click:
              player_2_selection += 1
              main_game()
        if habs_button.collidepoint((mx, my)):
            if click:
              player_2_selection += 2
              main_game()
        if bruins_button.collidepoint((mx, my)):
            if click:
              player_2_selection += 3
              main_game()
        if wings_button.collidepoint((mx, my)):
            if click:
              player_2_selection += 4
              main_game()
        if rangers_button.collidepoint((mx, my)):
            if click:
              player_2_selection += 5
              main_game()
        if hawks_button.collidepoint((mx, my)):
            if click:
              player_2_selection += 6
              main_game()

        logos()
        if player_1_selection == 1:
          pygame.draw.rect(screen, (255,255,255), leafs_button)
        if player_1_selection == 2:
          pygame.draw.rect(screen, (255,255,255), habs_button)
        if player_1_selection == 3:
          pygame.draw.rect(screen, (255,255,255), bruins_button)
        if player_1_selection == 4:
          pygame.draw.rect(screen, (255,255,255), wings_button)
        if player_1_selection == 5:
          pygame.draw.rect(screen, (255,255,255), rangers_button)
        if player_1_selection == 6:
          pygame.draw.rect(screen, (255,255,255), hawks_button)

        click=False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                  click=True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                  player_1_selection = 0
                  running = False
        pygame.display.update()
        mainClock.tick(60)

# Function for the logos at center ice

def logos():
  pygame.draw.rect(screen, (255,255,255), leafs_button)
  pygame.draw.rect(screen, (255,255,255), habs_button)
  pygame.draw.rect(screen, (255,255,255), bruins_button)
  pygame.draw.rect(screen, (255,255,255), wings_button)
  pygame.draw.rect(screen, (255,255,255), rangers_button)
  pygame.draw.rect(screen, (255,255,255), hawks_button)
  screen.blit(leafs, (50,300))
  screen.blit(habs, (250,300))
  screen.blit(bruins, (450,300))
  screen.blit(wings, (650, 305))
  screen.blit(rangers, (855, 300))
  screen.blit(hawks, (1040, 300))

# Function for the lines and shapes on the ice. Also includes the drawing of the puck and paddles.

def rink_lines():
  global line_offset_y, line_offset_x, player_score, opponent_score, score_time, goal_line_1, puck
  screen.fill((255,255,255))
  pygame.draw.line(screen, (0,0,0), [0,0], [1280,0], 4)
  pygame.draw.line(screen, (0,0,0), [0,958], [1280,958], 4)
  pygame.draw.line(screen, (255,0,0), [640,0], [640,958], 2)
  pygame.draw.line(screen, (0,0,255),[440,0], [440,958], 2)
  pygame.draw.line(screen, (0,0,255), [840,0], [840,958], 2)
  pygame.draw.line(screen, (0,0,0), [640,960], [640,1040], 4)
  pygame.draw.ellipse(screen, (137,209,254), [1242.5, 200, 75, 560])
  pygame.draw.ellipse(screen, (255,0,0), [1242.5, 200, 75, 560],2)

  if game_choice == 2 or opponent_net == 0:
    pygame.draw.ellipse(screen, (137,209,254), [-37.5, 200, 75, 560])
    pygame.draw.ellipse(screen, (255,0,0), [-37.5, 200, 75, 560],2)
  if opponent_net == 1:
    pygame.draw.ellipse(screen, (137,209,254), [-37.5, 300, 75, 360])
    pygame.draw.ellipse(screen, (255,0,0), [-37.5, 300, 75, 360],2)
    goal_line_1 = pygame.Rect(0,300,2,360)
  if opponent_net == 2:
    pygame.draw.ellipse(screen, (137,209,254), [-37.5, 400, 75, 160])
    pygame.draw.ellipse(screen, (255,0,0), [-37.5, 400, 75, 160],2)
    goal_line_1 = pygame.Rect(0,400,2,160)
  
  if game_choice == 2:
    pygame.draw.line(screen, (255,255,255), [640,355], [640,602],4)
    pygame.draw.ellipse(screen, (255,0,0), [514,355,250,250], 2)
    if player_1_selection == 1:
      pygame.draw.ellipse(screen, (0, 0, 255), player)
      screen.blit(leafs, (552,391))
      draw_text('LEAFS', font_medium, (0,0,255),screen, 1150,985)
    if player_1_selection == 2:
      pygame.draw.ellipse(screen, (175, 30, 45), player)
      screen.blit(habs, (548,392))
      draw_text('CANADIENS', font_medium, (175,30,45),screen, 1050,985)
    if player_1_selection == 3:
      pygame.draw.ellipse(screen, (252, 181, 20), player)
      screen.blit(bruins, (548,390))
      draw_text('BRUINS', font_medium, (252,181,20),screen, 1125,985)
    if player_1_selection == 4:
      pygame.draw.ellipse(screen, (206,17,38), player)
      screen.blit(wings, (541,412))
      draw_text('RED WINGS', font_medium, (206,17,38),screen, 1050,985)
    if player_1_selection == 5:
      pygame.draw.ellipse(screen, (0,56,168), player)
      screen.blit(rangers, (559,398))
      draw_text('RANGERS', font_medium, (0,56,168),screen, 1075,985)
    if player_1_selection == 6:
      pygame.draw.ellipse(screen, (0,0,0), player)
      screen.blit(hawks, (550,400))
      draw_text('BLACKHAWKS', font_medium, (0,0,0),screen, 1000,985)
    if player_2_selection == 1:
      pygame.draw.ellipse(screen, (0, 0, 255), opponent)
      draw_text('LEAFS', font_medium, (0,0,255),screen, 10,985)
    if player_2_selection == 2:
      pygame.draw.ellipse(screen, (175, 30, 45), opponent)
      draw_text('CANADIENS', font_medium, (175,30,45),screen, 10,985)
    if player_2_selection == 3:
      pygame.draw.ellipse(screen, (252, 181, 20), opponent)
      draw_text('BRUINS', font_medium, (252,181,20),screen, 10,985)
    if player_2_selection == 4:
      pygame.draw.ellipse(screen, (206,17,38), opponent)
      draw_text('RED WINGS', font_medium, (206,17,38),screen, 10,985)
    if player_2_selection == 5:
      pygame.draw.ellipse(screen, (0,56,168), opponent)
      draw_text('RANGERS', font_medium, (0,56,168),screen, 10,985)
    if player_2_selection == 6:
      pygame.draw.ellipse(screen, (0,0,0), opponent)
      draw_text('BLACKHAWKS', font_medium, (0,0,0),screen, 10,985)

  if game_choice == 1:
      pygame.draw.ellipse(screen, (0,0,0), player)
      pygame.draw.ellipse(screen, (0,0,0), opponent)
      draw_text('ROBOT', font_medium, (0,0,0),screen, 10,985)
      draw_text('HUMAN', font_medium, (0,0,0),screen, 1125,985)

  pygame.draw.ellipse(screen, (0,0,0), puck)
  if score_time:
    puck_restart()
  player_text = font_medium.render(f"{player_score}",False,(0,0,0))
  screen.blit(player_text, (665,985))
  opponent_text = font_medium.render(f"{opponent_score}",False,(0,0,0))
  screen.blit(opponent_text, (600,985))

# Loops for the main game. First loop is for single player, second loop is for two players.

def main_game():
  global score_time
  score_time = pygame.time.get_ticks()
  if game_choice == 1:
    running = True
    while running:
      keys_pressed = pygame.key.get_pressed()
      if keys_pressed[pygame.K_UP]:
        if player.top > 0:
          player.top -=7
      if keys_pressed[pygame.K_DOWN]:
        if player.bottom <= 956:
          player.bottom +=7
      if keys_pressed[pygame.K_LEFT]:
        if player.left > 840:
          player.left -=7
      if keys_pressed[pygame.K_RIGHT]:
        if player.right < 1276:
          player.right +=7
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
      puck_physics()
      opponent_ai()
      rink_lines()
      pygame.display.update()
      mainClock.tick(60)

  if game_choice == 2:
    running = True
    while running:
      keys_pressed = pygame.key.get_pressed()
      if keys_pressed[pygame.K_UP]:
        if player.top > 0:
          player.top -=7
      if keys_pressed[pygame.K_DOWN]:
        if player.bottom <= 956:
          player.bottom +=7
      if keys_pressed[pygame.K_LEFT]:
        if player.left > 840:
          player.left -=7
      if keys_pressed[pygame.K_RIGHT]:
        if player.right < 1280:
          player.right +=7
      keys_pressed = pygame.key.get_pressed()
      if keys_pressed[pygame.K_w]:
        if opponent.top > 0:
          opponent.top -=7
      if keys_pressed[pygame.K_s]:
        if opponent.bottom <= 956:
          opponent.bottom +=7
      if keys_pressed[pygame.K_a]:
        if opponent.left > 0:
          opponent.left -=7
      if keys_pressed[pygame.K_d]:
        if opponent.right < 440:
          opponent.right +=7
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  running = False
      puck_physics()
      rink_lines() 
      pygame.display.update()
      mainClock.tick(60)

# Function that describes the puck physics. First half is when the puck hits the walls and goes in the net, second half is when the puck hits the paddles.

def puck_physics():
  global player, puck_speed_x, puck_speed_y, player_score, opponent_score, score_time
  puck.x += puck_speed_x
  puck.y += puck_speed_y
  if puck.top < 0 and puck_speed_y < 0:
    puck_speed_y *= -1
  if puck.bottom > 960 and puck_speed_y > 0:
    puck_speed_y *= -1
  if puck.left < 0 and puck_speed_x < 0:
    if puck.colliderect(goal_line_1):
      player_score += 1
      score_time = pygame.time.get_ticks()
    else:
      puck_speed_x *= -1
  if puck.right > width and puck_speed_x > 0:
    if puck.colliderect(goal_line_2):
      opponent_score += 1
      score_time = pygame.time.get_ticks()
    else:
      puck_speed_x *= -1

  if puck.colliderect(player):
    if abs(player.top - puck.bottom) < 20 and puck_speed_y > 0:
      puck_speed_y *= -1
    if abs(player.bottom - puck.top) < 20 and puck_speed_y < 0:
      puck_speed_y *= -1
    if abs(player.right - puck.left) < 20 and puck_speed_x < 0:
      puck_speed_x *= -1
    if abs(player.left - puck.right) < 20 and puck_speed_x > 0:
      puck_speed_x *= -1
  if puck.colliderect(opponent):
    if abs(opponent.top - puck.bottom) < 20 and puck_speed_y > 0:
      puck_speed_y *= -1
    if abs(opponent.bottom - puck.top) < 20 and puck_speed_y < 0:
      puck_speed_y *= -1
    if abs(opponent.right - puck.left) < 20 and puck_speed_x < 0:
      puck_speed_x *= -1
    if abs(opponent.left - puck.right) < 20 and puck_speed_x > 0:
      puck_speed_x *= -1

# Function for the ai in single player mode. Computer moves faster with higher difficulty.

def opponent_ai():
  global opponent_speed
  if opponent.top < puck.y:
    if opponent.bottom <956:
      opponent.top += opponent_speed
  if opponent.bottom > puck.y:
      opponent.bottom -= opponent_speed
  if puck.left < 640:
    if opponent.left > 0:
      opponent.left -= 7
  if puck.right > 640:
    if opponent.right <=440:
      opponent.right += 7

# Describes what happens when a goal is scored and restarts in the middle of the ice, also includes the puck start timer.

def puck_restart():
  global puck_speed_x, puck_speed_y, score_time
  puck.center = (width/2, 960/2)
  current_time = pygame.time.get_ticks()
  if current_time - score_time < 1000:
    three = font_large.render('3', False, (0,0,0))
    screen.blit(three,(width/2-15,960/2 -250))
  if 1000 < current_time - score_time < 2000:
    two = font_large.render('2', False, (0,0,0))
    screen.blit(two,(width/2-15,960/2 -250))
  if 2000 < current_time - score_time < 3000:
    one = font_large.render('1', False, (0,0,0))
    screen.blit(one,(width/2-15,960/2 -250))
  if current_time - score_time < 3000:
    puck_speed_x, puck_speed_y = 0,0
  else:
    puck_speed_y = 8 * random.choice((1,-1))
    puck_speed_x = 8 * random.choice((1,-1))
    score_time = None

main_menu()
