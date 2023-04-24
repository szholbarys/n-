# Perfect Circle ойынын python-мен жасау
import pygame, math, time

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Perfect Circle")
    clock = pygame.time.Clock()

    prev_x, prev_y, cur_x, cur_y = -1, -1, -1 , -1

    started_time = time.time()
    
    display.fill((0, 0, 0))
    display.fill(pygame.Color('white'), pygame.Rect(380, 400, 20, 20))

    rectangle_position = (380, 400)

    mouse_type = 0
    color = (0, 255, 0)
    Down = False
    points = []
    while True:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]:
            color = (255, 0, 0)
        elif pressed[pygame.K_g]:
            color = (0, 255, 0)
        elif pressed[pygame.K_b]:
            color = (0, 0, 255)
        elif pressed[pygame.K_w]:
            color = (255, 255, 255)
        if pressed[pygame.K_SPACE]:
            display.fill((0, 0, 0))
        if pressed[pygame.K_0]:
            mouse_type = 0

        # Түзу сызық
        if mouse_type == 0:
            cur_x = prev_x
            cur_y = prev_y

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Down = True
                       
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        Down = False

                if event.type == pygame.MOUSEMOTION:
                    cur_x = event.pos[0]
                    cur_y = event.pos[1]

            # Тінтуірмен сурет салу мүмкіндігін іске асыру
            if Down:
                pygame.draw.line(display, color, (prev_x, prev_y), (cur_x, cur_y), 5)
                if len(points) == 0:
                    points.append(prev_x)
                    points.append(prev_y)
                # Егер ойыншы нүктеге тым жақын сурет салса, қатені көрсету
                mouse_position = pygame.mouse.get_pos()
                distance = math.sqrt((mouse_position[0] - rectangle_position[0]) ** 2 +
                       (mouse_position[1] - rectangle_position[1]) ** 2)
                if distance < 40:
                    error_font = pygame.font.SysFont(None, 36)
                    error_text = error_font.render("Too close to target!", True, (255, 0, 0))
                    display.blit(error_text, (280, 430))
                    pygame.display.flip()
                    time.sleep(2.5)
                    display.fill((0, 0, 0))
                    display.fill(pygame.Color('white'), pygame.Rect(380, 400, 20, 20))

                # Егер ойыншы тым баяу сурет салса, қатені көрсету  
                end_time = time.time()
                drawing_time = abs(end_time - started_time)
                drawing_speed = 1 / drawing_time
                if drawing_speed > 80:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Too slow!", True, (255, 0, 0))
                    display.blit(text, (340, 430))
                    pygame.display.flip()
                    time.sleep(2.5)
                    display.fill((0, 0, 0))
                    display.fill(pygame.Color('white'), pygame.Rect(380, 400, 20, 20))

                # Шеңбердің сапасы нашарлаған сайын түсін қызыл түске өзгертіңіз
                distance = math.sqrt((mouse_position[0] - rectangle_position[0]) ** 2 +
                    (mouse_position[1] - rectangle_position[1]) ** 2)
                radius = math.sqrt(abs((points[0] - rectangle_position[0]) ** 2 +
                    (points[1] - rectangle_position[1]) ** 2))
    
                if(distance > radius-30 and distance < radius+30):
                    color = (0, 255, 0)
                elif(distance > radius-60 and distance < radius+60):
                    color = (255, 255, 0)
                elif(distance > radius-90 and distance < radius+90):
                    color = (255, 165, 0)
                elif(distance > radius-120 and distance < radius+120):
                    color = (255, 0, 0)
                else:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Wrong way!", True, (255, 0, 0))
                    display.blit(text, (340, 430))
                    pygame.display.flip()
                    time.sleep(2.5)
                    display.fill((0, 0, 0))
                    display.fill(pygame.Color('white'), pygame.Rect(380, 400, 20, 20))

            started_time = time.time()
            prev_x = cur_x
            prev_y = cur_y

            pygame.display.flip()
            clock.tick(60)
main()