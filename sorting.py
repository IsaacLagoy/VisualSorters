# imports
import math
import random
import pygame

# classes
class rectangle():
    
    def __init__(self, left, top, width, height, color):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        
    def set_color(self, color):
        self.color = color
        
    def set_rect(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

# definitions
def quick_sort(array, low, high):
    
    if low < high:
 
        # selects a pivot point
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                
                # updates screen on change
                (array[i], array[j]) = (array[j], array[i])
                change_screen(array)
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        change_screen(array)
        pivoit = i + 1
 
        # sorts left, right
        quick_sort(array, low, pivoit - 1)
        quick_sort(array, pivoit + 1, high)
        
# cocktail, quick, bubble, and gnome sort provided by geeks-for-geeks
def cocktail_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
 
        swapped = False
        
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
                change_screen(a)
 
        if (swapped==False):
            break
 
        swapped = False
 
        end = end-1
 
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
                change_screen(a)
 
        start = start+1
        
def gnome_sort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
            change_screen(arr)
 
    return arr

def bubble_sort(array):
    
  for i in range(len(array)):
        
    swapped = False
    
    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        change_screen(array)

        swapped = True
        
    if not swapped:
      break
  
def bogo_sort(array):
    
    while True:
        random.shuffle(array) # randomizes array and checks if its true
        change_screen(array)
        check = True
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                check = False
                break
        if check:
            clock.tick(2)
            return # returns nothing to break out of sequence
        clock.tick(15)
        
def change_screen(array):
    
    global rect_array
        
    # allows program to quit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    """render"""
    
    # resets screen
    surface.fill('black')
            
    # renders rectangles if rectangles have changed
    for i in range(len(array)):
        
        rect_array[i].set_color('white') # resets all color to white
            
        if math.ceil(height*array[i]/len(array)) != rect_array[i].height: # checks if rectangles have been changed
            rect_array[i].set_color('red') # sets color to red for moved rectangles
            
        rect_array[i].set_rect(
            math.ceil(width/len(array)*i), # left
            height-math.ceil(height*array[i]/len(array)), # top
            math.ceil(width/len(array)), # width
            math.ceil(height*array[i]/len(array))) # height
        pygame.draw.rect(surface, rect_array[i].color, pygame.Rect(rect_array[i].left, rect_array[i].top, rect_array[i].width, rect_array[i].height))
        

    # renders objects to screen
    pygame.display.flip()
    
def get_array(size):
    
    global rect_array
    array = [i for i in range(size)] # generates and shuffles a new array
    random.shuffle(array) 
    rect_array = [rectangle(math.ceil(width/len(array)*i), height-math.ceil(height*array[i]/len(array)), math.ceil(width/len(array)), math.ceil(height*array[i]/len(array)), 'white') for i in range(len(array))] # adds array to initial rectangle array
    return array

"""set up"""

width, height = 1024, 512 # set screen dimensions

# pygame setup
pygame.init()
running = True
clock = pygame.time.Clock()
    
# sets screen dimensions
surface = pygame.display.set_mode((width, height))

"""start loop"""

while True:
    
    num = random.randint(0,4) # selects random sorting algorithm
    match num: 
        case 0: 
            array = get_array(1024)
            quick_sort(array, 0, len(array)-1)
        case 1: 
            array = get_array(128)
            cocktail_sort(array)
        case 2: 
            array = get_array(256)
            gnome_sort(array, len(array))
        case 3:
            array = get_array(256)
            bubble_sort(array)
        case 4:
            array = get_array(4)
            bogo_sort(array)
            