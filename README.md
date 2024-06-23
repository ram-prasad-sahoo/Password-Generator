# Password Generator

A simple password generator using Python and PySimpleGUI. This program allows users to generate a secure password based on their input criteria including uppercase letters, lowercase letters, digits, and symbols.

## Features

- Customizable password generation based on user input.
- User-friendly graphical interface using PySimpleGUI.
- Generates a random password that includes uppercase letters, lowercase letters, digits, and symbols.

## Prerequisites

- Python 3.x
- PySimpleGUI

## Installation

1. Clone the repository:

```bash
https://github.com/ram-prasad-sahoo/Password-Generator.git
cd password-generator
```
2:Install the required packages:
pip install PySimpleGUI
Usage
1.Run the script:
python password_generator.py
2.Enter the number of uppercase letters, lowercase letters, digits, and symbols you want in your password.
3.Click the "Generate Password" button.
4.The generated password will be displayed in the text box.
Example

Code Explanation
Here's a brief explanation of the code:

-Import necessary modules: random, string, and PySimpleGUI.
-Set the theme and options for the PySimpleGUI window.
-Define the layout of the window with text inputs for uppercase, lowercase, digits, and symbols.
-Create a window with the specified layout.
-Read user input and generate a password based on the input criteria.
-Display the generated password in a text box.

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
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
-PySimpleGUI
-Python
Author
Ram Prasad Sahoo
