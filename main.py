from itertools import cycle
import PySimpleGUI as sg
from distances import medium_distances, long_distances

screenWidth, screenHeight = sg.Window.get_screen_size()

layout = [[sg.Button('hide', size=(8, 1), key='hide_btn'),
          sg.Button('long', size=(8, 1), key='projectile_btn'),
          sg.Button('still', size=(8, 1), key='move_btn'),
          sg.Graph(canvas_size=(screenWidth, screenHeight),
          graph_bottom_left=(0, screenHeight),
          graph_top_right=(screenWidth, 0),
          background_color='red',
          key="graph"),
          ]]

window = sg.Window('',
                   layout,
                   background_color='red',
                   keep_on_top=True,
                   transparent_color='red',
                   alpha_channel=1,
                   grab_anywhere=False,
                   resizable=True,
                   finalize=True,
                   margins=(0, 0),
                   element_padding=(0, 0),
                   no_titlebar=True)

window.maximize()

graph: sg.Graph = window['graph']


screenWidth_offset = screenWidth//2 -210
def draw_line(height, color='yellow'):
    graph.DrawLine((screenWidth_offset -3, height),
                   (screenWidth_offset +3, height), color=color, width=2)


def draw_text(height, text, color='yellow'):
    graph.DrawText(text, (screenWidth_offset + 20, height), color=color)


def draw_line_up(projectile, move):
    multiplier = pow(2, 4)
    point_distance = screenHeight // 4 // multiplier
    molly_distances = eval(f'{projectile}.{move}')
    for idx, quantidade in enumerate(range(2, multiplier * 2 - 4, 2)):
        draw_line(point_distance * quantidade)
        draw_text(point_distance * quantidade, str(molly_distances[idx]))


move_list = cycle(['still', 'run', 'jump'])
project = 'long_distances'
next(move_list)
move = 'still'
is_clean = True

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "hide_btn":
        if is_clean:
            draw_line_up(project, move)
        else:
            graph.erase()
        is_clean = not is_clean

    if event == "projectile_btn":
        project = 'medium_distances' if project == 'long_distances' else 'long_distances'
        window['projectile_btn'].update(text=f'{project[:4]}')
        graph.erase()
        draw_line_up(project, move)

    if event == "move_btn":
        move = next(move_list)
        window['move_btn'].update(text=f'{move}')
        graph.erase()
        draw_line_up(project, move)