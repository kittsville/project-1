import pygame               # Handles user input and game output
from pygame.locals import * # Allows you to access stuff like KEYDOWN directly rather than via pygame.KEYDOWN

# Creates a fullscreen menu and allows selection of items from said menu
# The term 'item', used in documentation, refers to a single entry in a menu e.g. 'Options'
# Built from the menu class created by avalanch @link http://pygame.org/project-menu_key-2278-.html
class Menu:
    menuItems               = []                                    # Names of all menu items (Start,Options,etc.)
    menuItemObjects         = []                                    # Instances of menuItem for each menu item above
    fontSize                = 32                                    # Size of menu item text
    fontPath                = 'assets/fonts/Electrolize-Regular.ttf'# Location of custom font file
    font                    = pygame.font.Font                      # Handles menu item text rendering @link http://www.pygame.org/docs/ref/font.html
    windowSurface           = pygame.Surface                        # Surface menu is drawn onto
    menuItemCount           = 0                                     # Total number of menu items
    backgroundColour        = (42, 42, 42)                          # Default game menu background colour. Set via setColours()
    textColour              = (221, 221, 221)                       # Default menu item text colour. Set via setColours()
    selectedMenuItemColour  = (0,0,0)                               # Colour of rectangle around a menu item when that item is selected
    selectedMenuItem        = 0                                     # Position in menuItems array of currently selected menu item
    drawPosition            = (0,0)                                 # Where to start drawing the menu items from
    menuWidth               = 0
    menuHeight              = 0
    active                  = False                                 # Whether the menu is currently being displayed

    class menuItem:
        text            = ''                # Name of the menu item (e.g. 'Options')
        gameSurface     = pygame.Surface    # Pygame object for representing images
        itemRect        = pygame.Rect       # Holds rectangular coordinates
        rectSelection   = pygame.Rect       # Holds rectangular coordinates

    def changeDrawPosition(self, top, left):
        self.drawPosition = (top,left) 

    # Changes colours used by current menu, pass False if you don't want to change a colour
    def setColours(self, text, selection, background):
        if text == False:
            text = self.textColour
        if selection == False:
            selection = self.selectedMenuItemColou
        if background == False:
            background = self.backgroundColour
        
        self.backgroundColour = background
        self.textColour =  text
        self.selectedMenuItemColour = selection
        
    def setFontsize(self,font_size):
        self.fontSize = font_size
        
    def setFont(self, path):
        self.fontPath = path
    
    # Returns array position of menu item that was just selected
    def getSelectedMenuItem(self, event):
        if event.type == KEYDOWN and event.key == K_RETURN:
            return self.selectedMenuItem
        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos >= self.drawPosition:
            # Menu item positions are relative to the menu's draw position. Modifying the cursor position by the menu offset fixes this
            pos = ( event.pos[0] - self.drawPosition[0], event.pos[1] - self.drawPosition[1] )
        
            # Loops through menu items, checking if click occurred in menu item's area
            for i in xrange(self.menuItemCount):
                if self.menuItemObjects[i].itemRect.collidepoint( pos ):
                    return i
        
        return False
    
    # Generates a menu, given an array on the names of the menu items and the game surface to render them to
    def __init__(self, menuItems, windowSurface):
        self.menuItems      = menuItems
        self.windowSurface  = windowSurface
        self.menuItemCount  = len(self.menuItems)
        self.drawMenuItems()

    # Updates selected menu item based on mouse position
    def updateSelectedItemMouse(self, mousePos):
        pos = ( mousePos[0] - self.drawPosition[0], mousePos[1] - self.drawPosition[1] )

        # Loops through menu items, checking if mouse position is menu item's area
        for i in xrange(self.menuItemCount):
            if self.menuItemObjects[i].itemRect.collidepoint( pos ):
                self.selectedMenuItem = i

    # Changes selected menu item based on up/down key press
    def updateSelectedItem(self, keyPress ):
        if keyPress == K_UP:
            self.draw(-1)
        elif keyPress == K_DOWN:
            self.draw(1)
    
    # Updates currently selected menu item based on keyboard input
    def draw(self, changePosition=0):
        if changePosition:
            # Updates currently selected menu item
            self.selectedMenuItem += changePosition 
            
            # Wraps menu navigation so going up from the top item selects the bottom item (and vice versa)
            if self.selectedMenuItem < 0:
                self.selectedMenuItem = self.menuItemCount - 1
            
            # Wraps menu item from the bottom
            self.selectedMenuItem %= self.menuItemCount
        
        # Redraws everything
        menu = pygame.Surface((self.menuWidth, self.menuHeight))
        menu.fill(self.backgroundColour)
        rectSelection = self.menuItemObjects[self.selectedMenuItem].rectSelection
        pygame.draw.rect(menu,self.selectedMenuItemColour,rectSelection)

        for i in xrange(self.menuItemCount):
            menu.blit(self.menuItemObjects[i].gameSurface,self.menuItemObjects[i].itemRect)
        self.windowSurface.blit(menu,self.drawPosition)
        return self.selectedMenuItem
    
    # Draws each menu item below the previous one, with the entire menu being horizontally and vertically centred in the game screen
    def drawMenuItems(self):
        changePositioniecie = 0
        self.menuHeight     = 0
        self.font           = pygame.font.Font(self.fontPath, self.fontSize)
        
        # Loops over menu items, rendering them to the screen
        for i in xrange(self.menuItemCount):
            self.menuItemObjects.append(self.menuItem())
            self.menuItemObjects[i].text = self.menuItems[i]
            self.menuItemObjects[i].gameSurface = self.font.render(self.menuItemObjects[i].text, 1, self.textColour)

            self.menuItemObjects[i].itemRect = self.menuItemObjects[i].gameSurface.get_rect()
            changePositioniecie = int(self.fontSize * 0.2)

            height = self.menuItemObjects[i].itemRect.height
            self.menuItemObjects[i].itemRect.left = changePositioniecie
            self.menuItemObjects[i].itemRect.top = changePositioniecie+(changePositioniecie*2+height)*i

            width   = self.menuItemObjects[i].itemRect.width+changePositioniecie*2
            height  = self.menuItemObjects[i].itemRect.height+changePositioniecie*2            
            left    = self.menuItemObjects[i].itemRect.left-changePositioniecie
            top     = self.menuItemObjects[i].itemRect.top-changePositioniecie

            self.menuItemObjects[i].rectSelection = (left,top ,width, height)
            if width > self.menuWidth:
                    self.menuWidth = width
            self.menuHeight += height
        x = self.windowSurface.get_rect().centerx - self.menuWidth / 2
        y = self.windowSurface.get_rect().centery - self.menuHeight / 2
        mx, my = self.drawPosition
        self.drawPosition = (x+mx, y+my)