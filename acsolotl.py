from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import ctypes
import os
import sqlite3
import webbrowser

print("programm \nstart!")
print("Привет,\nмир!")
tk = Tk()
tk.geometry("1024x768")
tk.iconbitmap(r'acsolotl_ico.ico')
tk.resizable(width=False, height=False)
#tk.iconbitmap(r'hameleon.ico')
tk.title('Acsolotl||Untitled')
tk.configure(background='#7F00FF')
path = os.getcwd()
'''image = Image.open("acsolotl_ico.png")  # Загрузить изображение
background_image = ImageTk.PhotoImage(image)
bg_canvas = Canvas(tk, width=1024,height=768)
bg_canvas.pack()
bg_label = Label(bg_canvas, image=background_image)  # Установить изображение как фон метки
bg_label.pack()
bg_canvas.tag_lover(bg_label)'''


menu_frame = Frame()

title_frame = Frame(tk, bg='#7F00FF')
title_frame.pack(side=TOP)

prog = LabelFrame(tk, text='Program', fg='white', bg='#7F00FF')
prog.pack()

visual = LabelFrame(tk, text='Visual', fg='white', bg='#7F00FF')
visual.pack()

dbn = "untitled.db"
all_commands = ""
columns = 'id|'
working_table_name = ''

#Function-----------------------------------------------------------------------------------
def clear_data_base():
	global dbn
	os.remove(path + "\ "[:-1] + dbn, dir_fd=None)
	file = open(dbn, "w+")
	file.close()
	ctypes.windll.user32.MessageBoxW(0, """All tables deleted.""", "Delete", 0)

def clear_comm_menu():
	l_f['text'] = ""
	l_s['text'] = ""
	l_th['text'] = ""
	l_fo['text'] = ""
	l_fi['text'] = ""
	l_si['text'] = ""
	l_se['text'] =""
	l_e['text'] = ""
	l_n['text'] = ""
	l_t['text'] = ""

def documentation():
	webbrowser.open_new(r"Documentation(RU).pdf")
	#subprocess.Popen([file],shell=True)

def help_comm():
	ctypes.windll.user32.MessageBoxW(0,"""Version: 1.0.
		Created by Mr_next. 
		Date of update: 20.08.2024.
		""",0)

def create_project():
	global dbn
	new = Toplevel()
	new.geometry("300x100")
	new.title("Create")
	new.configure(background='#7F00FF')

	def create_proj():
		global dbn
		name = entry_name.get()
		name = name + '.db'
		file = open(name, "w+")
		file.close()
		tk.title('Acsolotl||' + name[:-3])
		dbn = name
		new.destroy()

	title_create = Label(new, text="Enter name file:", fg="white", bg="#7F00FF")
	title_create.pack()
	entry_name = Entry(new)
	entry_name.pack(fill=X, pady=10, padx=25)
	name_btn = Button(new, text="Create", bg="#7F00FF", fg="white", command=create_proj)
	name_btn.pack()
def open_project():
	opened = Toplevel()
	opened.geometry("300x100")
	opened.title("Create")
	opened.configure(background='#7F00FF')

	def open_proj():
		global dbn
		name = entry_name.get()
		name = name + '.db'
		tk.title('Acsolotl||' + name[:-3])
		dbn = name
		opened.destroy()

	title_open = Label(opened, text="Enter name file:", fg="white", bg="#7F00FF")
	title_open.pack()
	entry_name = Entry(opened)
	entry_name.pack(fill=X, pady=10, padx=25)
	name_btn = Button(opened, text="Create", bg="#7F00FF", fg="white", command=open_proj)
	name_btn.pack()

#Hot_keyboard-------------------------------------------------------------------------------
def clear_db(event):
	global dbn
	os.remove(path + "\ "[:-1] + dbn, dir_fd=None)
	file = open(dbn, "w+")
	file.close()
	ctypes.windll.user32.MessageBoxW(0, """All tables deleted.""", "Delete", 0)

def clear_comm(event):
	l_f['text'] = ""
	l_s['text'] = ""
	l_th['text'] = ""
	l_fo['text'] = ""
	l_fi['text'] = ""
	l_si['text'] = ""
	l_se['text'] =""
	l_e['text'] = ""
	l_n['text'] = ""
	l_t['text'] = ""

def create(event):
	global dbn
	new = Toplevel()
	new.geometry("300x100")
	new.title("Create")
	new.configure(background='#7F00FF')

	def create_proj():
		global dbn
		name = entry_name.get()
		name = name + '.db'
		file = open(name, "w+")
		file.close()
		tk.title('Acsolotl||' + name[:-3])
		dbn = name
		new.destroy()

	title_create = Label(new, text="Enter name file", fg="white", bg="#7F00FF")
	title_create.pack()
	entry_name = Entry(new)
	entry_name.pack(fill=X, pady=10, padx=25)
	name_btn = Button(new, text="Create", bg="#7F00FF", fg="white", command=create_proj)
	name_btn.pack()

def open_file(event):
	opened = Toplevel()
	opened.geometry("300x100")
	opened.title("Create")
	opened.configure(background='#7F00FF')

	def open_proj():
		global dbn
		name = entry_name.get()
		name = name + '.db'
		tk.title('Acsolotl||' + name[:-3])
		dbn = name
		opened.destroy()

	title_open = Label(opened, text="Enter name file:", fg="white", bg="#7F00FF")
	title_open.pack()
	entry_name = Entry(opened)
	entry_name.pack(fill=X, pady=10, padx=25)
	name_btn = Button(opened, text="Create", bg="#7F00FF", fg="white", command=open_proj)
	name_btn.pack()

def exit(event):
	tk.destroy()

'''def help(event):
	ctypes.windll.user32.MessageBoxW(0,"""Команды:
		create table [name] ([name_column] [data_type], ...) - создаёт таблицу.
		delete table [name] - удалет таблицу.
		insert [name] ([name_column, ...])([values]) - ввод данных в столбец.
		replace [name] ([name_column])([new_value]) - замена значения в столбце.
		delete [name] ([name_column] = [value]) - удаление определённой строки.
		delete [name] - удаление всех строк.

		Все строковые значения указываются в скобках!
		""",0)'''

#-------------------------------------------------------------------------------------------
def visual_screen():
	#insert bb(name, age)("John", 13)
	#create table b(name str, age int, number int, dog str)
	global columns, working_table_name
	rows = ""
	n = 0

	conn = sqlite3.connect(dbn)
	cursor = conn.cursor()
	querty = "SELECT COUNT(*) FROM  " + working_table_name
	cursor.execute(querty)
	result = cursor.fetchone()
	rows_count = result[0]
	print("rows_count: " + rows_count)

	visual_wind = Toplevel()
	visual_wind.geometry("1024x768")
	if working_table_name == '':
		working_table_name = "Untitled"
	visual_wind.title("Acsolotl - visual - " + working_table_name)
	visual_wind.configure(background='black')
	columns_names = columns.split("|")
	for j in columns_names:
		j.replace("|","")
	tree = ttk.Treeview(visual_wind, columns=columns_names, show="headings")
	tree.pack(fill=BOTH)
	columns_names.remove('')
	for g in columns_names:
		tree.heading(g, text=g)
		conn = sqlite3.connect(dbn)
		cursor = conn.cursor()
		querty = "SEL" + "ECT " + g + " FROM " + working_table_name
		cursor.execute(querty)
		row_values_querty = cursor.fetchall()
		print(row_values_querty)
		for h in row_values_querty:
			a = h
			for j in a:
				rows = rows + str(j) + ","
				print(rows)
		rows_array = rows.split(",")
		conn.commit()
		conn.close()
		tree.insert("", END, values=rows_array)

def command_screen():
	global all_commands

	value_insert = 1.0
	end_value_insert = value_insert	 + 1.0
	h = 0

	screen_wind = Toplevel()
	screen_wind.geometry("1024x768")
	screen_wind.title("Acsolotl - screen")
	screen_wind.configure(background='black')
	all_com = Text(screen_wind)
	all_com.pack()
	all_commands_tuple = all_commands.split('\n')
	#print("'\n".join(all_commands))
	for h in all_commands_tuple:
		h = h + "\n"
		pos_a = all_com.search("a", value_insert,stopindex=end_value_insert)
		if pos_a == '' or pos_a == ' ': 
			all_com.insert(value_insert, h)
		else:
			value_insert += 1
			print("plus")
		pos_e = all_com.search("e", value_insert, stopindex=end_value_insert)
		if pos_e == "" or pos_e == ' ': 
			all_com.insert(value_insert, h)
		else:
			value_insert += 1
			print("plus")


def enter():
	global all_commands
	global columns
	global working_table_name

	text_check=''
	pos = 1.0

	text_check = entry.get()
	if text_check == '' or text_check == ' ':
		pass

	else:
		l_f['text'] = l_s['text']
		l_s['text'] = l_th['text']
		l_th['text'] = l_fo['text']
		l_fo['text'] = l_fi['text']
		l_fi['text'] = l_si['text']
		l_si['text'] = l_se['text']
		l_se['text'] = l_e['text']
		l_e['text'] = l_n['text']
		l_n['text'] = l_t['text']
		l_t['text'] =  '>>> ' + text_check
		print(text_check)


		#TABLE------------------------------------------------------

		if " table " in text_check:
			
			#create------------------------------------------------------

			if "create" in text_check or "Create" in text_check:
				text_check = text_check.replace("create", "")
				text_check = text_check.replace("Create", "")
				text_check = text_check.replace(" table ", "")
				text_for_created = text_check.split("(")
				name_of_table = text_for_created[0].replace(" ", "")
				working_table_name = name_of_table

				create_command = 'CREATE TABLE ' + 'IF NOT EXISTS ' + name_of_table + "(" + "id INTEGER PRIMARY KEY AUTOINCREMENT, "

				variables_for_created = text_for_created[1].split(',')
				i = 1
				n = 1

				for n in variables_for_created:
					if ")" in n:
						n.replace(")", "")
						print("replased ')'")
						if " int" in n:
							print("int detected")
							int_var = n.split("int")
							#if int_var[n] == "" or int_var[n] == " ": break  invalid literal for int() with base 10: 'prompt int'
							create_command = create_command + int_var[0] + "INTEGER, "
							print(int_var[0])
							columns = columns + int_var[0] + "|"
						elif " str" in n:
							print("string detected")
							str_var = n.split("str")
							#if int_var[n] == "" or int_var[n] == " ": break  invalid literal for int() with base 10: 'prompt int'
							create_command = create_command + str_var[0] + "TEXT, "
							columns = columns + str_var[0] + "|"
							print(str_var[0])

					else:
						if " int" in n:
							int_var = n.split("int")
							#l_f['text'] = int_var[0], int_var[1]
							create_command = create_command + int_var[0] + "INTEGER, "
							columns = columns + int_var[0] + "|"
							print(int_var[0])
						elif " str" in n:
							print("string detected")
							str_var = n.split("str")
							#if int_var[n] == "" or int_var[n] == " ": break  invalid literal for int() with base 10: 'prompt int'
							create_command = create_command + str_var[0] + "TEXT, "
							columns = columns + str_var[0] + "|"
							print(str_var[0])

				#l_e['text'] = int_var[0]
				#l_se['text'] = str_var[0]
				create_command = create_command[:-2] + ")"
				print(create_command)
				conn = sqlite3.connect(dbn)
				cursor = conn.cursor()
				querty = create_command
				cursor.execute(querty)
				conn.commit()
				conn.close()
				create_command = create_command + "\n"
				all_commands = all_commands + create_command

				#create table aboba (prompt int, help str, fff int)

				#delete------------------------------------------------------

			if "delete" in text_check or "Delete" in text_check:
				print("delete")
				text_check = text_check.replace("delete", "")
				text_check = text_check.replace("Delete", "")
				text_check = text_check.replace(" table ", "")
				name_of_table = text_check.replace(" ", "")
				print(name_of_table)
				delete_command = "DROP TABLE IF EXISTS " + name_of_table
				conn = sqlite3.connect(dbn)
				cursor = conn.cursor()
				querty = delete_command
				cursor.execute(querty)
				conn.commit()
				conn.close()
				delete_command = delete_command + "\n"
				all_commands = all_commands + delete_command

		#NOT TABLE------------------------------------------------------

		if " table " not in text_check:

			#insert------------------------------------------------------
			
			if "insert" in text_check or "Insert" in text_check:
				text_check = text_check.replace("insert", "")
				text_check = text_check.replace("Insert", "")
				text_for_insert = text_check.split("(")
				name_of_table = text_for_insert[0].replace(" ", "")
				print(name_of_table)
				insert_command = "INS" + "ERT " + "INTO " + name_of_table + "("
				name_column_for_changes = text_for_insert[1].split(',')
				print(text_for_insert[1])

				for n in name_column_for_changes:
					if n == " , ":
						n.replace(' , ','')
					if ")" in n:
						n.replace(")", "")
						print("replased ')'")
						insert_var = n
						insert_command = insert_command + insert_var #1
					else:
						insert_var = n
						insert_command = insert_command + insert_var #2
						insert_command = insert_command + ", "

				insert_command = insert_command + " VALUES ("

				name_column_for_changes = text_for_insert[2].split(',')

				for n in name_column_for_changes:
					if ")" in n:
						n.replace(")", "")
						print("replased ')'")
						insert_var = n
						insert_command = insert_command + insert_var + " " #3
					else:
						insert_var = n
						insert_command = insert_command + insert_var #4
						insert_command = insert_command  + ", "

				insert_command = insert_command[:-2] + ")"
				l_f['text'] = insert_command
				conn = sqlite3.connect(dbn)
				cursor = conn.cursor()
				querty = insert_command
				cursor.execute(querty)
				conn.commit()
				conn.close()
				insert_command = insert_command + "\n"
				all_commands = all_commands + insert_command

				#insert a(aa, bb)(11, "fdfd") 

			#replace------------------------------------------------------
			
			if "replace" in text_check or "Replace" in text_check: 
				text_check = text_check.replace("replace", "")
				text_check = text_check.replace("Replace", "")
				text_for_insert = text_check.split("(")
				name_of_table = text_for_insert[0].replace(" ", "")
				print(name_of_table)
				replace_command = "RE" + "PLACE " + "INTO " + name_of_table + "("
				name_column_for_changes = text_for_insert[1].split(',')
				print(text_for_insert[1] + "text")

				for n in name_column_for_changes:
					if n == " , ":
						n.replace(' , ','')
					if ")" in n:
						n.replace(")", "")
						print("replased ')'")
						replace_var = n
						replace_command = replace_command + replace_var #1
					else:
						replace_var = n
						replace_command = replace_command + replace_var #2
						replace_command = replace_command  + ", "

				replace_command = replace_command + " VALUES ("

				name_column_for_changes = text_for_insert[2].split(',')

				for n in name_column_for_changes:
					if ")" in n:
						n.replace(")", "")
						print("replased ')'")
						replace_var = n
						replace_command = replace_command + replace_var + " " #3
					else:
						replace_var = n
						replace_command = replace_command + replace_var #4
						replace_command = replace_command  + ", " 

				replace_command = replace_command[:-2] + ")"
				conn = sqlite3.connect(dbn)
				cursor = conn.cursor()
				querty = replace_command
				cursor.execute(querty)
				conn.commit()
				conn.close()
				replace_command = replace_command + "\n"
				all_commands = all_commands + replace_command

				#replase a(aa, bb)(1, "fgggfg")

			#delete------------------------------------------------------

			if "delete" in text_check or "Delete" in text_check:
				print("delete")
				text_check = text_check.replace("delete", "")
				text_check = text_check.replace("Delete", "")
				text_check = text_check.replace(" ", "")
				text_check = text_check.split('(')
				name_of_table = text_check[0]
				print(text_check)
				print("name: "+name_of_table)
				if '=' in text_check[1]:
		
					print(name_of_table)
					name_of_table.replace('(','')
					name_of_table.replace(" ", "")
					print(text_check[1])
					text_check[1].replace(" ", "")
					values = text_check[1]
					

					delete_command = "DELE" + "TE FROM " + name_of_table + " WHERE " + values[:-1]
					print("delete: " + delete_command)
					conn = sqlite3.connect(dbn)
					cursor = conn.cursor()
					querty = delete_command
					cursor.execute(querty)
					l_f['text'] = delete_command
					conn.commit()
					conn.close()
				else:
					delete_command = "DELE" + "TE FROM " + name_of_table
					print("delete: " + delete_command)
					conn = sqlite3.connect(dbn)
					cursor = conn.cursor()
					querty = delete_command
					cursor.execute(querty)
					l_f['text'] = delete_command
					conn.commit()
					conn.close()
					delete_command = delete_command + "\n"
					all_commands = all_commands + delete_command

					#delete a || delete a(aa=11)

# menu

mainmenu = Menu()

file_menu = Menu(tearoff=0)
edit_menu = Menu(tearoff=0)
window_menu = Menu(tearoff=0)
help_menu = Menu(tearoff=0)

mainmenu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label = "New", accelerator = "Ctrl+N", command=create_project)
file_menu.add_command(label = "Open", accelerator = "Ctrl+O", command=open_project)
#file_menu.add_command(label = "Save", accelerator = "Ctrl+S")
#file_menu.add_separator()
#file_menu.add_command(label = "Help", accelerator = "Ctrl+H", command=help_comm)
file_menu.add_separator()
file_menu.add_command(label = "Exit", accelerator = "Ctrl+E", command=tk.destroy)

mainmenu.add_cascade(label='Edit', menu=edit_menu)
'''edit_menu.add_command(label="Start untitled virtual machine", accelerator="Ctrl+Shift+V")
edit_menu.add_command(label="Open data base in virtual machine", accelerator="Ctrl+Shift+O")
edit_menu.add_command(label="Start untitled virtual machine", accelerator="Ctrl+Shift+S")
edit_menu.add_command(label="Aply virtual data base to real file", accelerator="Ctrl+Shift+F")
edit_menu.add_command(label="Stop virtual machine", accelerator="Ctrl+Shift+P")
edit_menu.add_separator()'''
edit_menu.add_command(label="Clear command menu", accelerator="Alt+C", command=clear_comm_menu)
edit_menu.add_command(label="Clear data base", accelerator="Alt+A", command=clear_data_base)

mainmenu.add_cascade(label='Windows', menu=window_menu)
window_menu.add_command(label = "Command screen", command=command_screen)
mainmenu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label="Documentation", command=documentation)
help_menu.add_command(label="Info", command=help_comm)
#window_menu.add_separator()
#window_menu.add_command(label = "Visual screen", command=visual_screen)


tk.config(menu = mainmenu)

# program

title = Label(title_frame, fg='white', bg='#7F00FF', text='Acsolotl')
title.config(font=('Bold', 30))
title.pack(pady=20)

code_label = Label(prog, fg='white', bg='#7F00FF', text='Program window:')
code_label.config(font=('Bold', 15))
code_label.pack(pady=10)

#last_entryes

l_f = Label(prog, bg='#7F00FF', fg='white');
l_f.pack(padx=10, pady=5)

l_s = Label(prog, bg='#7F00FF', fg='white');
l_s.pack(padx=10, pady=5)

l_th = Label(prog, bg='#7F00FF', fg='white');
l_th.pack(padx=10, pady=5)

l_fo = Label(prog, bg='#7F00FF', fg='white');
l_fo.pack(padx=10, pady=5)

l_fi = Label(prog, bg='#7F00FF', fg='white');
l_fi.pack(padx=10, pady=5)

l_si = Label(prog, bg='#7F00FF', fg='white');
l_si.pack(padx=10, pady=5)

l_se = Label(prog, bg='#7F00FF', fg='white');
l_se.pack(padx=10, pady=5)

l_e = Label(prog, bg='#7F00FF', fg='white');
l_e.pack(padx=10, pady=5)

l_n = Label(prog, bg='#7F00FF', fg='white');
l_n.pack(padx=10, pady=5)

l_t = Label(prog, bg='#7F00FF', fg='white');
l_t.pack(padx=10, pady=5)

# entry
entry = Entry(prog, width=100)
entry.pack(padx=20, pady = 20)
entry_btn = Button(prog, text="Enter", command=enter, fg="white", bg="#7F00FF")
entry_btn.pack(pady = 10)

#Visual

tk.bind('<Control-n>', create)
tk.bind('<Control-o>', open_file)
tk.bind('<Control-e>', exit)
#tk.bind('<Control-h>', help)

tk.bind('<Alt-c>', clear_comm)
tk.bind('<Alt-a>', clear_db)

tk.mainloop()

#Mr_next_nikola
