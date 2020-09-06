import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.filedialog

import csv
from xml.etree import ElementTree

LARGE_FONT= ("Verdana", 12)



class window(tk.Tk):
    
    def __init__(self):
        
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "XML to CSV Converter")
        
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Welcome", font=("Verdana", 16))
        label.pack(pady=10,padx=10)

        self.pack(expand=True, fill='both')

        label_1 = tk.Label(self, text="Press the button to read in data")                  
        label_1.pack()
        ttk.Button(self, text="Select and convert XML Data into a CSV File", command =lambda: self.ReadInXML()).pack()
    
        label_1 = tk.Label(self, text="The file: csv_file.csv can be found in the main folder now.")                  
        label_1.pack()

        label_1_1 = tk.Label(self, text="Please rename the file directly so no other files can be appended to it.")                  
        label_1_1.pack()
      
        label = tk.Label(self, text="Programmed by Philip Schmidt 2020", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

    def ReadInXML(self):                                
        x = tkinter.filedialog.askopenfilename()

        tree = ElementTree.parse(x)
        root = tree.getroot()
        
        for att in root:
            first = att.find('attval').text             # Here your own attribute of your self designed xml format has to be adapted, not "attval". Instead what?
            for subatt in att.find('children'):         # Here your second attribute of your self designed xml format has to be adapted, not "children". Instead what?
                second = subatt.find('attval').text     # Here your own attribute of your self designed xml format has to be adapted, not "attval". Instead what?
                global list1
                csv_data = '{},{}'.format(first, second)
                list1 = [csv_data]
                with open('csv_file.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(csv_data.split())
                                            

app = window()
app.mainloop()

