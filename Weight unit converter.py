import tkinter as tk
from tkinter import ttk

def convert_lbs():
    weight_input = entry_float.get()
    kg_output = weight_input / 2.20462
    output_string.set(kg_output)
    
def convert_kg():
    weight_input = entry_float_2.get()
    lbs_output = weight_input / 0.4536
    output_string.set(lbs_output)

# window
window = tk.Tk()
window.title('Weight Converter')
window.geometry('600x300')

# title
title_label = ttk.Label(master = window, text = 'Lbs/Kg Converter', font = 'Calibri 24 bold')
title_label.pack()

# input frame
input_frame = ttk.Frame(master = window)
subtitle_label = ttk.Label(master = window, text = 'Lbs to kg', font = 'Calibri 16')
entry_float = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_float)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert_lbs)
subtitle_label.pack()
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 15)

# output_label
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack()

# input frame 2
input_frame_2 = ttk.Frame(master = window)
subtitle_label_2 = ttk.Label(master = window, text = 'Kg to lbs', font = 'Calibri 16')
entry_float_2 = tk.IntVar()
entry_2 = ttk.Entry(master = input_frame_2, textvariable = entry_float_2)
button = ttk.Button(master = input_frame_2, text = 'Convert', command = convert_kg)
subtitle_label_2.pack()
entry_2.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame_2.pack(pady = 15)

# output_label_2
output_string_2 = tk.StringVar()
output_label_2 = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string_2)
output_label_2.pack()

# run
window.mainloop()