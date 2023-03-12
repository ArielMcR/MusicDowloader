import PySimpleGUI as sg
from pytube import YouTube
import moviepy.editor  as mp
import re
import os

sg.theme('dark grey 9')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Baixar musica com python')],
            [sg.Text('Digite a URL da musica'), sg.InputText(key="url")],
            [sg.Button('Baixar'), sg.Button('Cancelar')] ]

# Create the Window
window = sg.Window('Baixador de musica em python', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar': # if user closes window or clicks cancel
        break
    link = values['url']
    path ="C:/Users/User/Downloads/mus"
    yt = YouTube(link)

    ys = yt.streams.filter(only_audio=True).first().download(path)

    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    sg.popup('A musica foi baixada com sucesso')
window.close()