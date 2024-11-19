"""
These are the things i need to import for my project.
For this protoype I will only pygame as i am just creating a window with a background and some buttons.
These buttons will not yet work, so no other imports are required.
"""
import pygame


"""This is initalising the units"""
pygame.init()
pygame.font.init()
pygame.mixer.init()

"""
Here is how the screen is created, there is a width and height value used to create the screen size.
There is also the colour which is then set to fill the screen for this example.
Then I made a base variable for the game state and wether or not the program is running, so if the "X" is clicked the program
closes.
"""
width = 700
height=700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Another Bad Rougelike Game")
main_bg = pygame.image.load("Images/Main_Menu.png")


running = True
game_state = "main_menu"

"""
This will be used to keep the game running and set what state the game is currently in
"""
while running == True:
    while game_state == "main_menu":
        my_sound = pygame.mixer.Sound('Audio/Menu_Music.mp3')
        my_sound.play()
        my_font = pygame.font.SysFont('impact', 40)
        title = my_font.render('Another Bad Roguelike Game', True, (255, 255, 255))
        screen.blit(main_bg, (0,0))
        screen.blit(title, (125,100))
        
        # This is the class that allows me to create the buttons for the main menu
        class Button():
            def __init__(self, colour, x, y, width, height, text=" "):
                self.colour = colour
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.text = text
            
            def draw_button(self, win):
                pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 0)
                
        #Need this in order for the buttons to know where the mouse is when it is clicked
        mouse_x,mouse_y = pygame.mouse.get_pos()
        
        """this is how pygame can determine when the mouse is clicked, it also determines which mouse
            button is pressed using a value pygame assigns to event.button"""
        
        left_click = False
        right_click = False
        middle_click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_click = True
                    
                if event.button == 2:
                    middle_click = True
                    
                if event.button == 3:
                    right_click = True
                    
        
        
        """This is all the buttons on the menu being set up an appearing on the screen.
            Each button will be tied to a different function past prototype 1"""
        
        play_button = Button((20, 200, 20), 200, 200, 300, 50, "PLAY")
        play_button.draw_button(screen)
        play_text = my_font.render('Play', True, (0, 0, 0))
        screen.blit(play_text, (315,200))
        
        settings_button = Button((0, 0, 255), 250, 300, 200, 50, "SETTINGS")
        settings_button.draw_button(screen)
        settings_text = my_font.render('Settings', True, (0, 0, 0))
        screen.blit(settings_text, (290,300))
        if 250<=mouse_x<=450 and 300<=mouse_y<=350 and left_click == True:
            game_state = "settings"
            

        
        
        quit_button = Button((255, 0, 0), 300, 400, 100, 50, "QUIT")
        quit_button.draw_button(screen)
        quit_text = my_font.render('Quit', True, (0, 0, 0))
        screen.blit(quit_text, (315,400))
        if 300<=mouse_x<=400 and 400<=mouse_y<=450 and left_click == True:
            pygame.quit()
            
        pygame.display.flip()
        
        if middle_click == True:
            screen.fill((0, 0, 0))
            pygame.display.flip()
        
    """After switching the game state to settings in order to create the settings menu this will be run.
    I will need a varied background and colour options in order to prevent the menu from being too repetitive.
    There will be several buttons and sliders which each adjust different settings.
    I included a music playing file here and went back and added it to the menu as well.
    """   
    while game_state == "settings":
        my_sound = pygame.mixer.Sound('Audio/Menu_Music.mp3')
        my_sound.play()
        settings_bg = pygame.image.load("Images/Settings3.jpg")
        settings_font = pygame.font.SysFont('arial', 40)
        settings_title = settings_font.render('Settings', True, (255, 255, 255))
        screen.blit(settings_bg, (0,0))
        screen.blit(settings_title, (50,100))
        
        
        #Same class for button as previous
        class Button():
            def __init__(self, colour, x, y, width, height, text=" "):
                self.colour = colour
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.text = text
            
            def draw_button(self, win):
                pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 0)
                
        #Same click reader
        left_click = False
        right_click = False
        middle_click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_click = True
                    
                if event.button == 2:
                    middle_click = True
                    
                if event.button == 3:
                    right_click = True
                    
                    
        #Same mouse position getter
        mouse_x,mouse_y = pygame.mouse.get_pos()
        

        #back button to return to menu
        back_button = Button((0, 0, 255), 0, 650, 100, 50, "BACK")
        back_button.draw_button(screen)
        back_text = settings_font.render('Back', True, (0, 0, 0))
        screen.blit(back_text, (10,655))
        if 0<=mouse_x<=700 and 650<=mouse_y<=700 and left_click == True:
            game_state = "main_menu"
            
        """Here is the class for the sliders. it takes an x and y value for the size and an x and y value for the slider position.
            It also takes a font which i will use my set font for the settings page.
        """
        class Slider:
            def __init__(self, x, y, width, height, font, scale_x, scale_y):
                self.scale_x = scale_x #use scale_x and scale_y to resize the whole slider for a new resolution
                self.scale_y = scale_y
                self.x, self.y = x, y
                self.width, self.height = width, height
                self.value = 0
                self.maxValue = 100
                self.minValue = 0
                self.percentage = 0
                self.font = settings_font
                self.sliderRect = pygame.Rect(self.x, self.y, self.width, self.height)
                self.text = self.font.render(f"{self.value}", True, (255, 255, 255)) #displays the current value of the slider
                self.sliderHandle = pygame.Rect(self.x, self.y, 20 * scale_x, self.height)
 
            def draw(self, screen):
                pygame.draw.rect(screen, (93,101,50), self.sliderRect)
                pygame.draw.rect(screen, (255, 255, 255), self.sliderHandle)
                screen.blit(
                    self.text,
                    (
                        self.sliderRect.centerx - self.text.get_width() / 2,
                        self.sliderRect.bottom + self.text.get_height() - 50 * self.scale_y,
                    ),
                )
 
            def update(self):
                mousePos = pygame.mouse.get_pos()
                if self.sliderRect.collidepoint(mousePos) and pygame.mouse.get_pressed() == (1, 0, 0):
                    self.sliderHandle.centerx = mousePos[0] #move slider handle to whereever user drags it
                try:
                    self.percentage = max(
                        0,
                        min(
                            (self.sliderHandle.x - self.sliderRect.x)
                            / (self.sliderRect.width - self.sliderHandle.width),
                            1,
                        ),
                    )
                except:
                    self.percentage = 50 #if invalid, default to 50% 
                self.value = int(
                    (self.percentage * (self.maxValue - self.minValue)) + self.minValue
                )
                self.text = self.font.render(f"{self.value}", True, (255, 255, 255))
                
        #Music slider - should set as a percentage, will assign to music_vol later
        music_slider = Slider(50, 200, 500, 50, settings_font, 1, 1)
        music_slider.draw(screen)
        music_slider.update()
        pygame.display.flip()
        music_vol_text = settings_font.render('Music Volume', True, (255, 255, 255))
        screen.blit(music_vol_text, (50, 150))
        pygame.display.flip()
        
        #SFX slider - should set as a percentage, will assign to SFX_vol when added
        sfx_slider = Slider(50, 300, 500, 50, settings_font, 1, 1)
        sfx_slider.draw(screen)
        sfx_vol_text = settings_font.render('Effects Volume', True, (255, 255, 255))
        screen.blit(sfx_vol_text, (50, 250))
        pygame.display.flip()
        
        
        #Customise Key binds button and text - Wont be able to do anything until the main game loop is created in order to have keys to customise
        key_binds_text = settings_font.render('Key Binds', True, (255, 255, 255))
        screen.blit(key_binds_text, (50, 350))
        customise_button = Button((93,101,50), 50, 400, 150, 50, "CUSTOMISE")
        customise_button.draw_button(screen)
        customise_text = settings_font.render('customise', True, (0, 0, 0))
        screen.blit(customise_text, (50,400))
        if 50<=mouse_x<=200 and 400<=mouse_y<=450 and left_click == True:
            game_state = "main_menu"
        pygame.display.flip()
            
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False