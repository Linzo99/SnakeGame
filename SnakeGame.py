from tkinter import *
from random import randrange
import time
import threading

class SnakeGame(Canvas):
	def __init__(self, master=None):
		super().__init__(master)
		master.title("SnakeGame")
		self.config(width=500, height=500, bg="black")
		self.start()


	def start(self):
		self.delete("all")
		self.snake = []
		self.snake.append(self.create_rectangle(0,0,10,10, fill="green"))
		self.move(self.snake[0], randrange(0, 480, 10), randrange(0, 480, 10))
		self.total = 1
		self.food()

	def update_snake(self, previous):
		self.snake.append(self.create_rectangle(previous, fill="white"))
		self.food()

	def food(self):
		self.target = self.create_oval(0,0,10,10, fill="red")
		self.move(self.target, randrange(0, 480, 10), randrange(0, 480, 10))
		self.bind_all("<Key>", self.move_snake)

	def dead(self):
		x_pos = self.coords(self.snake[0])[0]
		y_pos = self.coords(self.snake[0])[1]
		if x_pos < 0:
			self.move(self.snake[0], 500,0)
		elif x_pos > 500: 
			self.move(self.snake[0], -500,0)
		if y_pos < 0:
			self.move(self.snake[0], 0,500)
		elif y_pos > 500:
			self.move(self.snake[0], 0,-500)

		# check for collapse of head and tail
		for i in range(1,len(self.snake)):
			if self.coords(self.snake[0]) == self.coords(self.snake[i]):
				return True



	def eaten(self):
		return self.coords(self.target) == self.coords(self.snake[0])


	def move_snake(self, event):
		last_tail = self.coords(self.snake[-1])

		if event.keysym == "Up":
			last_position = [self.coords(self.snake[0])]
			self.move(self.snake[0], 0,-10)
			for i in range(1, self.total):
					last_position.append(self.coords(self.snake[i]))
					self.coords(self.snake[i], last_position[i-1])				
			
		elif event.keysym == "Down":
			last_position = [self.coords(self.snake[0])]
			self.move(self.snake[0], 0,10)
			for i in range(1, self.total):
					last_position.append(self.coords(self.snake[i]))
					self.coords(self.snake[i], last_position[i-1])
		elif event.keysym == "Left":
			last_position = [self.coords(self.snake[0])]
			self.move(self.snake[0],-10,0)
			for i in range(1, self.total):
					last_position.append(self.coords(self.snake[i]))
					self.coords(self.snake[i], last_position[i-1])
		elif event.keysym == "Right":
			last_position = [self.coords(self.snake[0])]
			self.move(self.snake[0], 10,0)
			for i in range(1, self.total):
					last_position.append(self.coords(self.snake[i]))
					self.coords(self.snake[i], last_position[i-1])

		if self.dead():
			print("DEEEAAD")
			self.start()

		if self.eaten():
			self.delete(self.target)
			self.total+=1
			self.update_snake(last_tail)
		self.dead()


fen = Tk()
game = SnakeGame(fen)
game.pack()

fen.mainloop()