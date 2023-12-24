import pygame
import random
import sys

pygame.init()

# Колір
WHITE = (255, 255, 255)

# Розміри екрану
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

# Ініціалізація екрану
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Камінь, ножиці, бумага")

# Шрифт
font = pygame.font.Font(None, 36)

# Початкові значення
win = draw = lose = 0

def main():
    global win, draw, lose

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                check_button_click(x, y)

        # Відображення результатів та кнопок
        display_results()
        display_buttons()

        pygame.time.delay(100)  # Затримка для уникнення мерцання

def play_round(player_choice):
    global win, draw, lose

    comp_choice = random.randint(1, 3)

    if player_choice == comp_choice:
        draw += 1
        result_text = "Нічия"
    elif (player_choice == 1 and comp_choice == 2) or (player_choice == 2 and comp_choice == 3) or (player_choice == 3 and comp_choice == 1):
        win += 1
        result_text = "Перемога"
    else:
        lose += 1
        result_text = "Програш"

    print(f"Ваш вибір: {get_choice_name(player_choice)}")
    print(f"Вибір комп'ютера: {get_choice_name(comp_choice)}")
    print(result_text)
    print(f"Перемог: {win}, Програшів: {lose}, Нічий: {draw}")
    print()

def get_choice_name(choice):
    if choice == 1:
        return "Камінь"
    elif choice == 2:
        return "Ножиці"
    elif choice == 3:
        return "Бумага"

def check_button_click(x, y):
    if 200 <= x <= 400 and 300 <= y <= 350:
        play_round(1)  # Камінь
    elif 400 <= x <= 600 and 300 <= y <= 350:
        play_round(2)  # Ножиці
    elif 600 <= x <= 800 and 300 <= y <= 350:
        play_round(3)  # Бумага

def display_results():
    screen.fill(WHITE)

    win_text = font.render(f"Перемог: {win}", True, (0, 128, 0))
    draw_text = font.render(f"Нічий: {draw}", True, (0, 0, 128))
    lose_text = font.render(f"Програшів: {lose}", True, (128, 0, 0))

    screen.blit(win_text, (50, 50))
    screen.blit(draw_text, (50, 100))
    screen.blit(lose_text, (50, 150))

    pygame.display.flip()

def display_buttons():
    # Відображення кнопок "Камінь", "Ножиці", "Бумага"
    rock_button = pygame.draw.rect(screen, (0, 128, 255), (200, 300, 200, 50))
    scissors_button = pygame.draw.rect(screen, (255, 0, 0), (400, 300, 200, 50))
    paper_button = pygame.draw.rect(screen, (0, 255, 0), (600, 300, 200, 50))

    # Текст на кнопках
    font_button = pygame.font.Font(None, 36)
    rock_text = font_button.render("Камінь", True, WHITE)
    scissors_text = font_button.render("Ножиці", True, WHITE)
    paper_text = font_button.render("Бумага", True, WHITE)

    screen.blit(rock_text, (270, 310))
    screen.blit(scissors_text, (470, 310))
    screen.blit(paper_text, (670, 310))

    pygame.display.flip()

if __name__ == "__main__":
    main()
