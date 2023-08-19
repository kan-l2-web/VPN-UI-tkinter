import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def connection():
	if connect_btn['text'] == 'DISCONNECT':
		connect_btn['text'] = 'CONNECT'
	else:
		connect_btn['text'] = 'DISCONNECT'


def create_check(country_name, frame, var, icon):
	return ttk.Radiobutton(
		master=frame,
		value=country_name,
		text=country_name,
		variable=var,
		style='success-toolbutton',
		compound='top',
		image=icon,
		)


def start_up():
	root = ttk.Window(themename="cerculean")
	root.title('Liberta')
	root.iconbitmap('./icon.ico')

	""" first frame """
	one_frame = ttk.Frame(master=root, padding=[20, 10])
	one_frame.pack(fill='x', anchor=CENTER)
	one_frame.grid(column=0, row=0)

	meter = ttk.Meter(
		master=one_frame,
		metersize=200,
		bootstyle="info",
		amountused=100,
		textright='gb',
		subtext='NetWork Speed',
		stripethickness=20,
	)
	meter.grid(column=0, row=0, pady=5)

	countrys = [
		{"name": "USA", "icon": ttk.PhotoImage(file='countrys/us.png'), "column": 0, "row": 0},
		{"name": "German", "icon": ttk.PhotoImage(file='countrys/de.png'), "column": 0, "row": 1},
		{"name": "United Kingdom", "icon": ttk.PhotoImage(file='countrys/uk.png'), "column": 1, "row": 0},
		{"name": "Netherlands", "icon": ttk.PhotoImage(file='countrys/nl.png'), "column": 1, "row": 1},
		# {"name": "Russia", "icon": ttk.PhotoImage(file='countrys/nl.png'), "column": 3, "row": 0}
	]

	country_pos = {"padx": 5, "pady": 5, "sticky": 'nsew'}

	coun = ttk.StringVar(value=countrys[0]['name'])

	countrys_frame = ttk.Frame(master=one_frame)
	countrys_frame.grid(column=0, row=1, sticky='nsew')

	for country in countrys:
		c = create_check(frame=countrys_frame, country_name=country["name"], var=coun, icon=country["icon"])
		c.grid(column=country["column"], row=country["row"], **country_pos)


	""" second frame """
	two_frame = ttk.Frame(master=root, padding=[10, 5])
	two_frame.grid(column=0, row=1)

	global connect_btn
	connect_btn = ttk.Button(
		master=two_frame,
		text="CONNECT",
		padding=[10, 5],
		command=connection,
	)
	connect_btn.pack(padx=20, pady=15)

	ip = '127.0.0.1'

	label_ip = ttk.Label(
		master=two_frame,
		text=f'You IP: {ip}',
		font=('Segoe UI Bold', 14)
	)
	label_ip.pack(padx=10, pady=10, anchor='center')


	""" third frame """
	three_frame = ttk.Frame(master=root, padding=10)
	three_frame.grid(column=0, row=2, sticky='nsew')

	icon_lb = ttk.Label(master=three_frame, text='🌎', font=56, padding=[0, 10, 10, 10])
	icon_lb.grid(column=0, row=0, rowspan=2)

	text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure aspernatur libero'
	handbook = ttk.Label(master=three_frame, text=text, wraplength=250, font=('Segoe UI Bold', 10))
	handbook.grid(column=1, row=0, sticky='nsew')

	root.mainloop()


if __name__ == "__main__":
	start_up()
