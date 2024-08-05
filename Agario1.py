from threading import Thread, Lock
from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox
from tkinter import Label
import random
import time
import os


#fill = "#" + ("%06x" % random.randint(0, 16777215))level after
#Two lists of colours for the circles
colors = ["green", "blue", "red", "black", "orange"]
colors1 = ["green", "blue", "red", "black", "orange"]
#instantations of global variables
# FINAL PROGRAM THAT HAS CHEATKEY AND BOSSKEY
score = 0
activity = True
temp = 20
value = 20
data_lock = Lock()
cheat = 0
level = "0"
def changetemp(value1):
	#Change value for countdown
	global value
	value = value1
def setWindowDimensions(w, h):
	window = Tk()
	window.title("Game")
	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	window.geometry('%dx%d+%d+%d' % (w, h, x, y))
	return window
def create_circle(x, y, r, canvasName, colour, tag): 
	#function to create a circle
	x0 = x - r
	y0 = y - r
	x1 = x + r
	y1 = y + r
	return canvasName.create_oval(x0, y0, x1, y1, tags= tag, fill=colour)
def stop():
	#Function to pause the game
	global activity
	activity = False
	messagebox.showinfo("Paused")
def start():
	#Function to restart the game
	global activity
	activity = True
	global value
	global level
	#Run the countdown with new value
	t1 = Thread(target = Countdown, args = (value,) )
	t1.start()
	#Run the correct movement for objects
	if level == "2":
		t2 = Thread(target = moveobjects,)
		t2.start()
	elif level == "3":
		t2 = Thread(target = moveobjects2, args =(-5,5))
		t2.start()
	elif level == "4":
		t2 = Thread(target = moveobjects2, args =(-10,10))
		t2.start()
	elif level == "5":
		t2 = Thread(target = moveobjects2, args =(-20,20))
		t2.start()



def moveobjects():
	global activity
	for i in range(50):
		while activity == True:
			for x in range(len(circles)-1):
				positions = []
				try:
					#Allowing the circles to re-enter the canvas
					positions.append(canvas1.coords(circles[x]))				
					if positions[0][0] < 0:
						canvas1.coords(circles[x],width,positions[0][1],width-10,positions[0][3])
					elif positions[0][2] > width:
						canvas1.coords(circles[x],0-10,positions[0][1],0,positions[0][3])
					elif positions[0][3] > height:
						canvas1.coords(circles[x],positions[0][0],0 - 10,positions[0][2],0)
					elif positions[0][1] < 0:
						canvas.coords(circles[x],positions[0][0],height,positions[0][2],height-10)
					positions.clear() 
					#Move the circles 
					canvas1.move("move", 5, 0)
					canvas1.update()
					time.sleep(0.05)
				except:
					positions.clear() 
					canvas1.move("move", 5, 0)
					canvas1.update()
					time.sleep(0.05)




def moveobjects2(range1, range2):
	global activity
	x = 0
	for i in range(50):
		x = random.randint(range1, range2)
		y = random.randint(range1, range2)
		while activity == True:
			for x in range(len(circles)-1):
				positions = []
				try:
					#Allowing the circles to re-enter the canvas
					positions.append(canvas1.coords(circles[x]))
					if positions[0][0] < 0:
						canvas1.coords(circles[x],width,positions[0][1],width-10,positions[0][3])
					elif positions[0][2] > width:
						canvas1.coords(circles[x],0-10,positions[0][1],0,positions[0][3])
					elif positions[0][3] > height:
						canvas1.coords(circles[x],positions[0][0],0 - 10,positions[0][2],0)
					elif positions[0][1] < 0:
						canvas.coords(circles[x],positions[0][0],height,positions[0][2],height-10)
					positions.clear()
					#Move the circles with the range
					canvas1.move(circles[x], x, y)
					canvas1.update()
					time.sleep(0.05)
				except:
					break
					positions.clear()
					canvas1.update()
					time.sleep(0.05)
def Countdown(temp):
	second=StringVar()
	second.set("00")
	global activity
	global score
	global e
	#Countdown to simulate Game timer
	while temp >-1 and activity == True:
		secs = temp % 60
		second.set("{0:2d}".format(secs))
		time.sleep(1)
		if (temp == 0):
			#Display final score 
			messagebox.showinfo("score:", str(score))
			global v
			#Change label text
			v.set("Press C to Continue and type your username at the bottom")
		temp -= 1
		#Keep track of time for pause
	changetemp(temp)
def printleaderboard():
	global level
	#Open file for correct level
	try:
		filename = "Level" + level + ".txt"
		file = open(filename, "r")
		filelines = file.readlines()
		#Sort the Data in order
		sorteddata = sorted(filelines, reverse = True)
		file.close()
		leaderboard = []
		#Add sorted data to list
		if len(sorteddata) > 4:
			for line in range(5):
				leaderboard.append(str(line +1) + ": " + str(sorteddata[line]))
			
		return leaderboard
	except:
		return False
def eating(a, b, shapecol, foodcol):
	#Checking if Circles with the same colour collide
	if foodcol == shapecol:
		if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
			return True
	return False
def F10key(event):
	#Close current window and open new window containing an image
	newwindow.withdraw()
	canvas2 = Canvas(bosswindow, bg="white", width=width, height=height)
	canvas2.pack()
	photolabel = Label(bosswindow, image = Bossphoto)
	value = bosswindow.winfo_geometry()
	bosswindow.geometry("1200x675")
	photolabel.place(x=0, y=0)
	bosswindow.deiconify()
def Spacekey(event):
	#Pause and unpause the game
	if activity == True:
		stop()
	else:
		start()
def level1():
	global colors1
	colors1 = ["green", "blue", "red", "black", "orange"]
	v.set("New level")
	global lines
	global circles
	global level
	#Update level variable, clear circles list
	level = "2"
	circles.clear()
	#Populate the canvas
	for x in range(20):
		#Randomise colour selection and placement of circles 
		theColour = random.choice(colors)
		X = random.randint(0,width)
		Y = random.randint(0,height)
		
		circles.append(create_circle(X, Y, 5, canvas1, theColour, "move"))
		
	MainColour = random.choice(colors)
	global circle 
	circle = create_circle(X, Y, 20, canvas1, MainColour, "user")

	
	global score
	score = 0
	temp = 20
	#Run Background countdown and movement of circles
	t1 = Thread(target = Countdown, args = (temp,) )
	t1.start()
	t2 = Thread(target = moveobjects,)
	t2.start()
def level2():
	global colors1
	colors1 = ["green", "blue", "red", "black", "orange"]
	v.set("New level")
	global level
	level = "3"
	global circles
	circles.clear()
	#Populate the canvas
	for x in range(20):
		#Randomise colour selection and placement of circles
		theColour = random.choice(colors)
		X = random.randint(0,width)
		Y = random.randint(0,height)
		
		circles.append(create_circle(X, Y, 5, canvas1, theColour, "move"))
		
	MainColour = random.choice(colors)
	global circle 
	circle = create_circle(X, Y, 20, canvas1, MainColour, "user")
	global score
	score = 0
	temp = 20
	#Run Background countdown and  random movement of circles
	t1 = Thread(target = Countdown, args = (temp,) )
	t1.start()
	t2 = Thread(target = moveobjects2, args =(-5,5))
	t2.start()
def level4():
	global colors1
	#colours1.clear()
	#for colour in colors
	colors1 = ["green", "blue", "red", "black", "orange"]
	v.set("New level")
	global level
	level = "5"
	global circles
	circles.clear()
	#Populate the canvas
	for x in range(20):
		#Randomise colour selection and placement of circles
		theColour = random.choice(colors)
		X = random.randint(0,width)
		Y = random.randint(0,height)
		
		circles.append(create_circle(X, Y, 5, canvas1, theColour, "move"))
		
	MainColour = random.choice(colors)
	global circle 
	circle = create_circle(X, Y, 20, canvas1, MainColour, "user")
	global score
	score = 0
	temp = 20
	#Run Background countdown and  random movement of circles
	t1 = Thread(target = Countdown, args = (temp,) )
	t1.start()
	t2 = Thread(target = moveobjects2, args =(-20,20))
	t2.start()
def level3():
	global colors1
	colors1 = ["green", "blue", "red", "black", "orange"]
	v.set("New level")
	global level
	level = "4"
	global circles
	circles.clear()
	#Populate the canvas
	for x in range(20):
		#Randomise colour selection and placement of circles
		theColour = random.choice(colors)
		X = random.randint(0,width)
		Y = random.randint(0,height)
		
		circles.append(create_circle(X, Y, 5, canvas1, theColour, "move"))
		
	MainColour = random.choice(colors)
	global circle 
	circle = create_circle(X, Y, 20, canvas1, MainColour, "user")
	global score
	score = 0
	#mylabel = Label(newwindow,textvariable=v).pack()
	t1 = Thread(target = Countdown, args = (temp,) )
	t1.start()
	t2 = Thread(target = moveobjects2, args = (-10,10))
	t2.start()

def level5():
	global colors1
	colors1 = ["green", "blue", "red", "black", "orange"]
	v.set("New level")
	global level
	level = "6"
	global circles
	circles.clear()
	#Populate the canvas
	for x in range(20):
		#Randomise colour selection and placement of circles
		theColour = random.choice(colors)
		X = random.randint(0,width)
		Y = random.randint(0,height)
		
		circles.append(create_circle(X, Y, 5, canvas1, theColour, "move"))
		
	MainColour = random.choice(colors)
	global circle 
	circle = create_circle(X, Y, 20, canvas1, MainColour, "user")
	global score
	score = 0
	#mylabel = Label(newwindow,textvariable=v).pack()
	t1 = Thread(target = Countdown, args = (temp,) )
	t1.start()
	t2 = Thread(target = moveobjects2, args = (-50,50))
	t2.start()

def leftKey(event):
		newwindow.update()
		positions = []
		#Keep circle from going out the left bound of the canvas
		positions.append(canvas1.coords(circle))
		if positions[0][0] > 0:
			#Move the circle 
			canvas1.move(circle, -10,0)
		#Track coords and colour of all the circles 
		for x in range(len(circles)-1):
			pos1 = canvas1.coords(circle)
			pos2 = canvas1.coords(circles[x])
			fcolour = canvas1.itemcget(circles[x], 'fill')
			ccolour = canvas1.itemcget(circle, 'fill')
			#Check if circles are colliding
			if eating(pos1, pos2, ccolour, fcolour):
				with data_lock:
					#Remove eaten circle from canvas and list
					canvas1.delete(circles[x])
					circles.remove(circles[x])
					global score
					global mylabel1
					global txt 
					#Update the score

					score += 1
					txt.set("score:" + str(score))
					
		
def rightKey(event):
		newwindow.update()
		positions = []
		#Keep circle from going out the right bound of the canvas
		positions.append(canvas1.coords(circle))
		if positions[0][0] < 525:
			#Move the circle
			canvas1.move(circle, 10,0)
		#Track coords and colour of all the circles 
		for x in range(len(circles)-1):
			pos1 = canvas1.coords(circle)
			pos2 = canvas1.coords(circles[x])
			fcolour = canvas1.itemcget(circles[x], 'fill')
			ccolour = canvas1.itemcget(circle, 'fill')
			#Check if circles are colliding
			if eating(pos1, pos2, ccolour, fcolour):
				with data_lock:
					#Remove eaten circle from canvas and list
					canvas1.delete(circles[x])
					circles.remove(circles[x])
					global score
					global mylabel1
					global txt
					#Update the score
					score += 1
					txt.set("score:" + str(score))
					
def upKey(event):
		newwindow.update()
		global txt
		positions = []
		#Keep circle from going out the upper bound of the canvas
		positions.append(canvas1.coords(circle))
		if positions[0][1] > 0:
			#Move the circle
			canvas1.move(circle, 0,-10)
		#Track coords and colour of all the circles
		for x in range(len(circles)-1):
			pos1 = canvas1.coords(circle)
			pos2 = canvas1.coords(circles[x])
			fcolour = canvas1.itemcget(circles[x], 'fill')
			ccolour = canvas1.itemcget(circle, 'fill')
			if eating(pos1, pos2, ccolour, fcolour):
				with data_lock:
					#Remove eaten circle from canvas and list
					canvas1.delete(circles[x])
					circles.remove(circles[x])
					global score
					global mylabel1
					#Update the score
					score += 1
					txt.set("score:" + str(score))
									
def downKey(event):
		newwindow.update()
		positions = []
		#Keep circle from going out the lower bound of the canvas
		positions.append(canvas1.coords(circle))
		if positions[0][1] < 525:
			canvas1.move(circle, 0,10)
		#Track coords and colour of all the circles
		for x in range(len(circles)-1):
			pos1 = canvas1.coords(circle)
			pos2 = canvas1.coords(circles[x])
			fcolour = canvas1.itemcget(circles[x], 'fill')
			ccolour = canvas1.itemcget(circle, 'fill')
			if eating(pos1, pos2, ccolour, fcolour):
				with data_lock:
					#Remove eaten circle from canvas and list
					canvas1.delete(circles[x])
					circles.remove(circles[x])
					global score
					global mylabel1
					global txt
					#Update the score
					score += 1
					txt.set("score:" + str(score))
					
def ckey(event):
	global e
	#Take name from textbox then clear textbox
	name = e.get()
	global drop
	ccolour = canvas1.itemcget(circle, 'fill')
	#Check if level is complete
	remaining = len(circles)
	if remaining >=10:
		finished = False
		
	else:
		finished = True
	if finished == True:
		messagebox.showinfo("Level", "Complete")
		canvas1.delete('all')
		#Display correct Leaderboard in dropdown box
		answer = printleaderboard()
		if answer != False:
			display = StringVar()
			display.set("Leaderboard")
			drop["menu"].delete(0, "end")
			for string in answer:
				drop["menu"].add_command(label=string, command=lambda value=string: display.set(value))
		#Write the score to correct file and start the next level
		if level == "1":
			file = open("Level0.txt", "a")
			file.write(str(score)+","+ name+"\n")
			file.close()
			level1()
		elif level == "2":
			file = open("Level1.txt", "a")
			file.write(str(score)+","+ name+"\n")
			file.close()
			level2()
		elif level == "3":
			file = open("Level2.txt", "a")
			file.write(str(score)+","+ name+"\n")
			file.close()
			level3()
		elif level == "4":
			file = open("Level3.txt", "a")
			file.write(str(score)+","+ name+"\n")
			file.close()
			level4()
		elif level == "5":
			file = open("Level4.txt", "a")
			file.write(str(score)+","+ name+"\n")
			file.close()
			level5()
		else:
			activity = False
			messagebox.showinfo("Game Finished")
			time.sleep(5)
			os._exit(1)

		
	else:
		messagebox.showinfo("Level", "incomplete")
		canvas1.delete('all')
		activity = False
		v.set("Press E to End")
		

def cheatkey(event):
	global cheat
	global circle
	if cheat >=2:
		#Create larger circle of the same colour
		circlecolour = canvas1.itemcget(circle, 'fill')
		canvas1.delete(circle)
		circle = create_circle(30, 450, 50, canvas1, circlecolour, "user")

def nextkey(event):
	global e
	#Clear textbox
	#e.delete(0, 'end')
	global circle
	global colours1
	global colours2
	circlecolour = canvas1.itemcget(circle, 'fill')
	#Remove taken colour from list
	colors1.remove(circlecolour)
	MainColour = random.choice(colors1)
	#Create new circle with a new colour
	canvas1.itemconfig(circle, fill=MainColour)

def F9key(event):
	global cheat
	cheat += 1
	#Return back to the orginal game window
	bosswindow.withdraw()
	newwindow.deiconify()
def quit_click():
	#End Python script
	os._exit(1)
def endkey(event):
	#End Python script
	os._exit(1)
def Rules_button_click():
	global canvas
	#Clear the Canvas
	canvas.delete('all')
	btn1.place_forget()
	btn.place_forget()
	btn2.place_forget()
	e.place_forget()

	#Repopulate the Canvas with Text
	canvas.create_text(width/2,24,fill="blue",font="Verdana 30  bold",text="Rules")
	canvas.create_text(width/3,60,fill="blue",font="Verdana 20  ",text="• Use Arrow Keys to Move")
	canvas.create_text((width/3) + 40,150,fill="blue",font="Verdana 16  ",text="• Use Space to Pause and Continue")
	canvas.create_text((width/3) + 45,270,fill="blue",font="Verdana 16  ",text="• Use C to Continue levels and Enter to Start")
	canvas.create_text((width/3) + 15,300,fill="blue",font="Verdana 10  ",text="• Press f10 key for bosskey and f9 to return to game window")
	canvas.create_text((width/3) + 30,400,fill="blue",font="Verdana 8 ",text="• Press f8 key for cheatkey only works if you went to bosskey 2 or more times")
	canvas.create_text((width/3) + 10,370,fill="blue",font="Verdana 16  ",text="• Each level lasts 20 seconds ")
	canvas.create_text((width/3) + 25, 470, fill="blue",font="Verdana 16 ",text="• Press n to change colour ")
	canvas.create_text((width/3) + 35,100,fill="blue",font="Verdana 16 ",text="•   Leaderboard at the top of each Level ")
	#Place Start Button
	btn4 = Button(window, text='Start', width=15, command=lambda : start_button_click())
	btn4.place(x=width/2, y=500)
def start_button_click():
	#Display correct Window
	window.withdraw()
	newwindow.deiconify()
	newwindow.title("New Window")
	global canvas1
	global circles
	global v
	global level 
	global drop
	#Display First Leaderboard
	display = StringVar()
	display.set("Leaderboard")
	answer = printleaderboard()
	drop = OptionMenu(newwindow,display, answer)

	#Update level
	level = "1"
	v.set("Press Enter to Start")
	circles = []
	i = 0
	#Create and populate the Canvas
	canvas1 = Canvas(newwindow, bg="white", width=width, height=height)
	for x in range(20):
		
		theColour = random.choice(colors)
		X = random.randint(30,width)
		Y = random.randint(30,height)
		#Add to circles List
		circles.append(create_circle(X, Y, 5, canvas1, theColour, "move"))
		i += 1
	MainColour = random.choice(colors)
	global circle 
	circle = create_circle(30, 30, 20, canvas1, MainColour, "user")
	global mylabel
	#Create Main Label
	mylabel = Label(newwindow,textvariable=v).pack()
	canvas1.pack()
	global score
	score = 0

	
	
	def enterkey(event):
		global e
		global activity
		activity = True
		#Start the Countdown
		t1.start()
		txt.set("score:" + str(score))
		#Create the score Label
		mylabel1 = Label(newwindow,textvariable = txt).pack()
		
	
	#Bind movement and control keys		
	newwindow.bind("<Left>", leftKey)
	newwindow.bind("<Right>", rightKey)
	newwindow.bind("<Up>", upKey)
	newwindow.bind("<Down>", downKey)
	newwindow.bind("<Return>", enterkey)
	newwindow.bind("<F10>", F10key)
	bosswindow.bind("<F9>", F9key)
	newwindow.bind("<space>", Spacekey)
	window.bind("<c>", ckey)
	newwindow.bind("<F8>", cheatkey)
	newwindow.bind("<n>", nextkey)
	newwindow.bind("<e>", endkey)
	canvas1.pack()

	



#Create the different Threads
t1 = Thread(target = Countdown, args = (temp,) )
t2 = Thread(target = start_button_click)
t2.daemon == True
t1.daemon== True
#Create Window and Canvas Dimensions
width = 550
height = 550
window = setWindowDimensions(width, height)
#Add new Windows
newwindow = Toplevel(window)
bosswindow = Toplevel(window)
#Create and populate the Canvas
canvas = Canvas(window, bg="orange", width=width, height=height)
btn = Button(window, text='Start', width=15, command=lambda : start_button_click()  )
btn.place(x=width/3, y=10)
btn2 = Button(window, text='Rules', width=15, command=lambda : Rules_button_click()  )
btn2.place(x=width/3, y=150)
btn1 = Button(window, text='Quit', width=15,command=lambda : quit_click() )
btn1.place(x=width/3, y=270)
#Create the Entry box
canvas.create_text(100,530,fill="blue",font="Verdana 20  ",text="Username:")
e = Entry(window)
e.place(x= 170, y=520)
e.focus_set()
#Save Boss Image
Bossphoto = PhotoImage(file ="Google_Homepage.png" )
#Create the Canvas for the different window
canvas2 = Canvas(bosswindow, bg="white", width=width, height=height)
canvas2.pack()
#Add Image to the Canvas in the correct size
photolabel = Label(bosswindow, image = Bossphoto)
value = bosswindow.winfo_geometry()
bosswindow.geometry("1200x675")
photolabel.place(x=0, y=0)
#Hide Windows that are not being used
bosswindow.withdraw()
newwindow.withdraw()
#Instantiate String Vars
v = StringVar()
txt = StringVar()
canvas.pack()
window.mainloop()


