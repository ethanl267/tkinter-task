import tkinter as tk 
from tkinter import messagebox 
from functools import partial 


# Declaration of global variable 
Cel_temp = "Celsius"

# getting drop down value 
def store_temp(set_temp): 
	global Cel_temp 
	Cel_temp = set_temp 

# Conversion of temperature 
def con_temp(cel_lab, temp_input): 
	temp = temp_input.get() 
	
	if Cel_temp == 'Celsius': 
		
		# Conversion of celsius temperature to fahrenheit 
		f = float((float(temp) * 9 / 5) + 32) 
		cel_lab.config(text ="%.1f Fahrenheit" % f) 
		messagebox.showinfo("Temperature Converter", 
							"Successfully converted to Fahrenheit ", ) 
		
	if Cel_temp == 'Fahrenheit': 
		
		# Conversion of fahrenheit temperature 
		# to celsius 
		c = float((float(temp) - 32) * 5 / 9) 
		cel_lab.config(text ="%.1f Celsius" % c) 
		messagebox.showinfo("Temperature Converter", 
							"Successfully converted to Celsius ") 
	return


# creating Tk window 
main = tk.Tk() 

# setting geometry of tk window 
main.geometry("300x400") 

# Using title() to display a message in the 
# dialogue box of the message in the title bar 
main.title('Temperature Converter') 

# Lay out widgets 
main.grid_columnconfigure(1, weight = 1) 
main.grid_rowconfigure(1, weight = 1) 

temp_inputumber = tk.StringVar() 
var = tk.StringVar() 

# label and entry field 
temp_label = tk.Label(main, text ="Enter temperature") 
temp_entry = tk.Entry(main, textvariable = temp_inputumber) 
temp_label.grid(row = 1) 
temp_entry.grid(row = 1, column = 1) 
fin_ans = tk.Label(main) 
fin_ans.grid(row = 3, columnspan = 4) 

# drop down setup 
dropDownList = ["Celsius", "Fahrenheit"] 
drop_down = tk.OptionMenu(main, var, *dropDownList, 
						command = store_temp) 
var.set(dropDownList[0]) 
drop_down.grid(row = 1, column = 2) 

# button widget 
con_temp = partial(con_temp, fin_ans, 
					temp_inputumber) 
temp_button = tk.Button(main, text ="Convert", 
						command = con_temp) 
temp_button.grid(row = 2, columnspan = 2) 

# infinite loop which is required to 
# run tkinter program infinitely 
# until an interrupt occurs 
main.mainloop() 
