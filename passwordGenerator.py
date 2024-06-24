import random
import string
import PySimpleGUI  as sg
sg.theme('DarkBlack1')
sg.set_options(font='Arial 15')
layout =[
    [sg.Text('Uppercase: '),sg.Push() ,sg.Input(size=20 , key='-UP-')],
    [sg.Text('Lowercase: '),sg.Push(), sg.Input(size=20 , key='-LOW-')],
    [sg.Text('Digits: ') ,sg.Push(), sg.Input(size=20 , key='-DIG-')],
    [sg.Text('Symbols: ') ,sg.Push(), sg.Input(size=20 , key='-SYB-')],
    [sg.Button('Generated Password'), sg.Button("Cancel")],
    [sg.Text('Password') ,sg.Push() , sg.Multiline(size=20 , key='-PAS-' ,no_scrollbar=True,disabled=True)]
]
window = sg.Window('Password Generator', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    if event == 'Generated Password':
        try:
            U_upper = int(values['-UP-'])
            upper = random.sample(string.ascii_uppercase , U_upper)
            U_lower= int(values['-LOW-'])
            lower = random.sample(string.ascii_lowercase , U_lower)
            U_digits = int(values['-DIG-'])
            digits = random.sample(string.digits , U_digits)
            U_symbol= int(values['-SYB-'])
            symbols = random.sample(string.punctuation , U_symbol)
            total =upper+lower+digits+symbols
            total = random.sample(total,len(total))
            total=''.join(total)
            window['-PAS-'].update(total)
        except ValueError:
            window['-PAS-'].update("Enter Valid Number. ")
window.close()
