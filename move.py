# Software implementando uma interface gráfica em TkInter para visualizar o processo de casamento de fitas de DNA que obtém duas fitas de DNA informadas pelo usuário que permite deslizar continuamente a segunda fita em relação a primeira, para direita ou esquerda, para cima ou para baixo e e cada configuração obtém o número de casamentos em cada configuração.

# Use as setas para navegar com a fita.
# Tab reseta a fita para posição inicial.
# Esc para sair da aplicação.
# m para encontrar a posição com o máximo número de combinações.
# Shift-L para embaralhar as fitas.

from tkinter import *
from DNAStrand import DNAStrand
from random import shuffle

class GFG:
	def __init__(self, master, st1, st2):
		#Main frame
		self.master = master
		#First strand given
		self.dna1 = st1
		#Second strand given
		self.dna2 = st2
		#Right shift started with 0
		self.rs = 0
		#Left shift started with 0
		self.ls = 0
		#This method is used to find matches between dna1 with dna2 in the 0 shift position and text1 holds this information to be used in the canvas
		self.text1 = self.dna1.findMatchesWithLeftShift(self.dna2, self.rs)
		#This method is used to find matches between dna2 with dna1 in the 0 shift position and text2 holds this information to be used in the canvas
		self.text2 = self.dna2.findMatchesWithLeftShift(self.dna1, self.ls)
		#This method is used to count how many matches there is between dna1 and dna2 and title holds this information to be used as the title of the main frame
		self.title = "DNA Strand with " + str(self.dna1.countMatchesWithLeftShift(self.dna2, self.ls)) + " matches"
		self.master.title(self.title)

		#A new canvas is created with width and height the same as the frame width and height
		self.canvas = Canvas(self.master, width=self.master.winfo_width(), height=self.master.winfo_height())
		#A new canvas object is created. The text object is centered on the half of the frame width and height, depends on how many letters there is on the strand and on their font weight
		#First canva object
		self.canva1 = self.canvas.create_text(self.master.winfo_width()//2-((len(self.dna1.strand)/2)*20), self.master.winfo_height()//2-20, text=self.text1, font="Courier 20", anchor="w")
		#Second canva object
		self.canva2 = self.canvas.create_text(self.master.winfo_width()//2-((len(self.dna1.strand)/2)*20), self.master.winfo_height()//2, text=self.text2, font="Courier 20", anchor="w")
		self.canvas.pack()

		

	def moveRight(self, event):
		#If the left shift is 0
		if self.ls == 0:
			#The right shift is incremented
			self.rs += 1
			#For the first strand is like moving the second strand to the right
			self.text1 = self.dna1.findMatchesWithRightShift(self.dna2, self.rs)
			#For the second strand is like moving the first strand to the left
			self.text2 = self.dna2.findMatchesWithLeftShift(self.dna1, self.rs)
			print(event.keysym)
			#The second canva is moved to the right
			self.canvas.move(self.canva2, 16, 0)
			#The canvas itens gains their new texts
			self.canvas.itemconfig(self.canva2, text=self.text2)
			self.canvas.itemconfig(self.canva1, text=self.text1)
			#The title is changed accordingly to the right shift in the second strand
			self.title = "DNA Strand with " + str(self.dna1.countMatchesWithRightShift(self.dna2, self.rs)) + " matches"
			self.master.title(self.title)
		#If the left shift is not 0
		else:
			#The left shift is decremented
			self.ls -= 1
			#For the first strand is like moving the second strand to the left
			self.text1 = self.dna1.findMatchesWithLeftShift(self.dna2, self.ls)
			#For the second strand is like moving the first strand to the right
			self.text2 = self.dna2.findMatchesWithRightShift(self.dna1, self.ls)
			print(event.keysym)
			#The second canva is moved to the right
			self.canvas.move(self.canva2, 16, 0)
			#The canvas itens gains their new texts
			self.canvas.itemconfig(self.canva2, text=self.text2)
			self.canvas.itemconfig(self.canva1, text=self.text1)
			#The title is changed accordingly to the left shift in the second strand
			self.title = "DNA Strand with " + str(self.dna1.countMatchesWithLeftShift(self.dna2, self.ls)) + " matches"
			self.master.title(self.title)
		#If the second canvas crosses the width boundaries, the canvas goes back to its initial position
		if self.canvas.coords(self.canva2)[0] > self.master.winfo_width():
			self.reset(event)

	def moveLeft(self, event):
		#If the right shift is 0
		if self.rs == 0:
			#The left shift is incremented
			self.ls += 1
			#For the first strand is like moving the second strand to the left
			self.text1 = self.dna1.findMatchesWithLeftShift(self.dna2, self.ls)
			#For the second strand is like moving the first strand to the right
			self.text2 = self.dna2.findMatchesWithRightShift(self.dna1, self.ls)
			print(event.keysym)
			#The second canva is moved to the left
			self.canvas.move(self.canva2, -16, 0)
			#The canvas itens gains their new texts
			self.canvas.itemconfig(self.canva2, text=self.text2)
			self.canvas.itemconfig(self.canva1, text=self.text1)
			#The title is changed accordingly to the left shift in the second strand
			self.title = "DNA Strand with " + str(self.dna1.countMatchesWithLeftShift(self.dna2, self.ls)) + " matches"
			self.master.title(self.title)
		#If the right shift is not 0
		else:
			#The right shift is decremented
			self.rs -= 1
			#For the first strand is like moving the second strand to the right
			self.text1 = self.dna1.findMatchesWithRightShift(self.dna2, self.rs)
			#For the second strand is like moving the first strand to the left
			self.text2 = self.dna2.findMatchesWithLeftShift(self.dna1, self.rs)
			print(event.keysym)
			#The second canva is moved to the left
			self.canvas.move(self.canva2, -16, 0)
			#The canvas itens gains their new texts
			self.canvas.itemconfig(self.canva2, text=self.text2)
			self.canvas.itemconfig(self.canva1, text=self.text1)
			#The title is changed accordingly to the right shift in the second strand
			self.title = "DNA Strand with " + str(self.dna1.countMatchesWithRightShift(self.dna2, self.rs)) + " matches"
			self.master.title(self.title)
		#If the second canvas crosses the width boundaries, the canvas goes back to its inicial position
		if self.canvas.coords(self.canva2)[0] < (0 - ((len(self.dna2.strand) - 1) * 20)) :
			self.reset(event)

	def moveUp(self, event):
		print(event.keysym)
		#The second canva is moved upwards
		self.canvas.move(self.canva2, 0, -16)
		#If the second canvas crosses the height boundaries, the canvas goes back to its inicial position
		if self.canvas.coords(self.canva2)[1] < 0:
			self.reset(event)

	def moveDown(self, event):
		print(event.keysym)
		#The second canva is moved downwards
		self.canvas.move(self.canva2, 0, 16)
		#If the second canvas crosses the height boundaries, the canvas goes back to its inicial position
		if self.canvas.coords(self.canva2)[1] > self.master.winfo_height():
			self.reset(event)

	def shuffle(self, event):
		#The second strand 
		l = list(self.dna2.strand)
		#The list is shuffled
		shuffle(l)
		str = ""
		#The shuffled list is held in str
		for i in range(len(l)):
			str += l[i]
		#The second strands receives str
		self.dna2.strand = str
		self.reset(event)

	def reset(self, event):
		#All the initial sets are restored
		self.rs = 0
		self.ls = 0
		self.text1 = self.dna1.findMatchesWithLeftShift(self.dna2, self.rs)
		self.text2 = self.dna2.findMatchesWithLeftShift(self.dna1, self.ls)		
		#print(event.keysym)
		self.canvas.coords(self.canva2, self.master.winfo_width()//2-((len(self.dna1.strand)/2)*20), self.master.winfo_height()//2)
		self.canvas.itemconfig(self.canva2, text=self.text2)
		self.canvas.itemconfig(self.canva1, text=self.text1)
		self.title = "DNA Strand with " + str(self.dna1.countMatchesWithLeftShift(self.dna2, 0)) + " matches"
		self.master.title(self.title)

	def help(self, event):
		print("Use as setas para navegar com a fita.\nTab reseta a fita para posição inicial.\nEsc para sair da aplicação.\nm para encontrar a posição com o máximo número de combinações.\nShift-L para embaralhar as fitas.")

	def maximumMatches(self, event):
		#First we reset the strands
		self.reset(event)
		#This method is used to find in which position there is the maximum of matches between both given strands
		info = self.dna2.findMaxPossibleMatches(self.dna1)
		#The second information given by the method used is the direction
		if info[1] == "right":
			#The first information given by the method used is the position
			self.rs = info[0]
			#All the sets are configured as in moveRight
			self.text1 = self.dna1.findMatchesWithRightShift(self.dna2, self.rs)
			self.text2 = self.dna2.findMatchesWithLeftShift(self.dna1, self.rs)
			self.canvas.move(self.canva2, 16*self.rs, 0)
			self.canvas.itemconfig(self.canva2, text=self.text2)
			self.canvas.itemconfig(self.canva1, text=self.text1)
			self.title = "DNA Strand with " + str(self.dna1.countMatchesWithRightShift(self.dna2, self.rs)) + " matches"
			self.master.title(self.title)
		else:
			self.ls = info[0]
			#All the sets are configured as in moveLeft
			self.text1 = self.dna1.findMatchesWithLeftShift(self.dna2, self.ls)
			self.text2 = self.dna2.findMatchesWithRightShift(self.dna1, self.ls)
			self.canvas.move(self.canva2, -16*self.ls, 0)
			self.canvas.itemconfig(self.canva2, text=self.text2)
			self.canvas.itemconfig(self.canva1, text=self.text1)
			self.title = "DNA Strand with " + str(self.dna1.countMatchesWithLeftShift(self.dna2, self.ls)) + " matches"
			self.master.title(self.title)

	def resize(self, event):
		#First we reset the strands
		self.reset(event)
		#The canvas and the canvas objects are configured to fit in the new sizes of the main frame
		self.canvas.config(width=self.master.winfo_width(), height=self.master.winfo_height())
		self.canvas.coords(self.canva1, self.master.winfo_width()//2-((len(self.dna1.strand)/2)*20), self.master.winfo_height()//2-20)
		self.canvas.coords(self.canva2, self.master.winfo_width()//2-((len(self.dna1.strand)/2)*20), self.master.winfo_height()//2)

if __name__ == "__main__":
	#A function to insert the given strand in the strands array
	def insertStrand(event):
		#If the strands array already has two strands
		if len(strands) == 2:
			#The previous widgets are destroyed
			label.destroy()
			entry.destroy()
			#And the class GFG is called
			move = GFG(master, strands[0], strands[1])

			master.bind("<Right>", lambda e: move.moveRight(e))
			master.bind("<Left>", lambda e: move.moveLeft(e))
			master.bind("<Up>", lambda e: move.moveUp(e))
			master.bind("<Down>", lambda e: move.moveDown(e))
			master.bind("<Tab>", lambda e: move.reset(e))
			master.bind("<m>", lambda e:  move.maximumMatches(e))
			master.bind("<h>", lambda e: move.help(e))
			master.bind("<Shift-L>", lambda e: move.shuffle(e))
			master.bind("<Configure>", lambda e: move.resize(e))

		#If the given strand is a valid strand
		try:
			strands.append(DNAStrand(entry.get()))
			label.configure(text="Insira a outra fita de DNA")
			entry.delete(0, END)
			if len(strands) >= 2:
				insertStrand(event)
		#If the given strand is not a valid strand
		except:
			if len(strands) < 2:
				label.configure(text="Fita informada inválida, tente novamente")
				entry.delete(0, END)
	#A function to close the main frame and finished the application
	def exit(event):
		master.destroy()

	#An array to store the strand given by the user
	strands = []

	master = Tk()
	#Standart frame pattern
	master.geometry("400x100+0+0")
	#Label to let the user know what has to be done
	label = Label(text="Insira o nome do arquivo ou uma fita de DNA")
	#Entry to capture what the user types
	entry = Entry()

	label.pack()
	entry.pack()
	#Code to run the function insertStrand when the enter key is hit
	entry.bind("<Return>", insertStrand)
	#Code to run the function exit when the Esc key is hit
	master.bind("<Escape>", exit)

	mainloop()