# IMPORTS

import PySimpleGUI as sg
import os
import sys
import chess
import chess.engine

# 4kb1r/p2rqppp/5n2/1B2p1B1/4P3/1Q6/PPP2PPP/2K4R w k - 0 14

# TO LAUNCH, do: python3.8 deepq.py

engine = chess.engine.SimpleEngine.popen_uci("./stockfish-11-64")

#print(engine.id.get("name"))

# First Window, entering in how many FENs and what depth to analyze to.
def first_window():
        layout = [
            [sg.Text('Please enter number of FENs and depth to analyze at: ')],
            [sg.Text('Number of FENs: ', size=(15, 1)), sg.InputText()],
            [sg.Text('Depth: ', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]

        win1 = sg.Window('DeepQ').Layout(layout)
        event, values = win1.Read()
        win1.Close()

        # values[0] is n_FENs, values[1] is the depth, both in str form.

        n_FENs = int(values[0])
        my_d = int(values[1])
        return n_FENs,my_d

n_FENs, my_d = first_window()

list_of_fens = []

def fenfunc():
	layout_2 = [
	    [sg.Text('Please enter your FENs below')],
	    [sg.Text('FEN: ', size=(15, 1)), sg.InputText()],
	    [sg.Submit(), sg.Cancel()]
	]

	win2 = sg.Window('DeepQ').Layout(layout_2)
	event_2, values_2 = win2.Read()

	my_fen = values_2[0]
	list_of_fens.append(my_fen)
	win2.Hide()

i = 0
while i < n_FENs:
	fenfunc()
	i += 1

engine_output = []
for fen in list_of_fens:
    board = chess.Board(fen)
    info = engine.analyse(board, chess.engine.Limit(depth=my_d))
    happystr = str(info)
    engine_output.append(happystr)

# This intializes the ending sequence of the program.

def end_program():
    os._exit(0)

sg.Popup('Analysis Output',engine_output)

end_program()
