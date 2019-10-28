import pygame

BLACK = (0,0,0)

#we create the paddle class - we will derive our objects from this class
#the objects to derive are paddle A and paddle B

class Paddle(pygame.sprite.Sprite):
    #This first class represents a car. It derives from the "Sprite" class in pygame

    def __init__(self, color, width, height):
        # call the parent class (Sprite) constructor
        super().__init__()

        #Pass in the color of the car, and it's x and y pos, width and height
        #Set the background color to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw the paddle - a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        #check not going too far off of the screen
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        #check not going too far off the screen
        if self.rect.y < 0:
            self.rect.y = 0
       
