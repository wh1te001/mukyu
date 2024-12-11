import pyglet
import os
import sys


# def resource_path(relative_path):
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("."), relative_path)
#
# resource_path('Mukyu.mp3')
# resource_path('mukyu.png')
# resource_path('pathci.jpg')
# resource_path('чукасочка.png')



def resource_path(relative_path):
    """ Получает путь к ресурсам, независимо от того, запущено приложение из .py или .exe """
    try:
        # PyInstaller создает временную папку и хранит ресурсы там
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Пример использования
image_path = resource_path("mukyu.png")
sound_path = resource_path("Mukyu.mp3")
icon_image_path = resource_path("pathci.jpg.mp3")


image = pyglet.resource.image('pathci.jpg')
sound = pyglet.media.load('Mukyu.mp3', streaming=False)
icon_image = pyglet.resource.image('mukyu.png')

window = pyglet.window.Window(width=image.width, height=image.height, caption='пачуля')

window.set_icon(icon_image)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if 0 <= x <= image.width and 0 <= y <= image.height:
        sound.play() 

@window.event
def on_draw():
    window.clear() 
    image.blit(0, 0) 

pyglet.app.run()

