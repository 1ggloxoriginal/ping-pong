#Создай собственный Шутер!

from pygame import *


window = display.set_mode((700,500))
display.set_caption('пинг-понг')
background = transform.scale(image.load('maxresdefault.jpg'),(700,500))

mixer.init()
mixer.music.load('musicmine.mp3')
mixer.music.play()



game = True

clock = time.Clock()
fps = 60
while game:  
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(fps)
    display.update()        