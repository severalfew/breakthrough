from .__init__ import name, __version__, __author__
from .locations import locations
import pyglet

started = False
window = pyglet.window.Window(fullscreen=True, caption=f"{name} - {__version__}")
terrain = pyglet.resource.image("terrain.jpeg")
terrain.scale = min(min(terrain.height, window.height) / max(terrain.height, window.height),
                    min(terrain.width, window.width) / max(terrain.width, window.width))
terrain.width = window.width
terrain.height = window.height
background = pyglet.resource.image("background.png")
background.scale = min(min(background.height, window.height) / max(background.height, window.height),
                       min(background.width, window.width) / max(background.width, window.width))
background.width = window.width
background.height = window.height


def draw_splash():
    terrain.blit(0, 0)
    pyglet.text.Label(
        name,
        font_name='Bahnschrift',
        font_size=36,
        x=window.width // 2, y=window.height // 2,
        anchor_x='center', anchor_y='center',
        color=(70, 70, 70, 255),
        bold=True
    ).draw()
    pyglet.text.Label(
        f"Created by {__author__}",
        font_name='Bahnschrift',
        font_size=28,
        x=window.width // 2, y=window.height // 2 - 50,
        anchor_x='center', anchor_y='center',
        color=(70, 70, 70, 255),
        bold=True
    ).draw()


def draw_board():
    background.blit(0, 0)
    for location in locations:
     location.sprite.draw()


@window.event
def on_draw():
    window.clear()
    # if not started:
    #     draw_splash()
    # else:
    draw_board()


@window.event
def on_mouse_press(x, y, button, modifiers):
    global started
    started = True


pyglet.app.run()
