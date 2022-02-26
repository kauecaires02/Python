# Python

from pySimpleGUI import pysimpleGUI as sg

#layout
sg.theme('darkblue')
layout = [
    [sg.Text('User'),sg.Input(key='user')], 
    [sg.text('password'),sg.input(key='password',password_char='*')], 
    [sg.Checkbox('Save to sign up?')]
    [sg.Button('entry')]
]
#Janela
janela = sg.Window('screen to sign up', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entry':
        if value['user'] == 'kaue' and value['password']
        == '123456':
            print('welcome to Truwhpyco.')
