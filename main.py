import pygame
from constants import * 
from player import Player

def main():
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #Game loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for obj in updatable: 
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        lapsed_time = game_clock.tick(60)
        dt = lapsed_time / 1000
    

if __name__ == "__main__":
    main()