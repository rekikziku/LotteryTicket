import random
import tkinter as tk
from tkinter import ttk
yournumbers = [34,6,8,32,5,4]
Title_Font = ("Verdana", 12)
Body_Font = ("Verdana", 10)
Note_Font = ("Verdana", 18)
 
def generateNumbers():
   randomNumbers = random.randint(0,49)
   return randomNumbers
 
def generateLotteryNumbers(numberofLotteryNumbers):
   NumbersOfLottery = []
   for currentLotteryNumberIndex in range(numberofLotteryNumbers):
       randomNumber = generateNumbers()
       NumbersOfLottery.append(randomNumber)
   return NumbersOfLottery
 
def printingLotteryNumbers(NumbersOfLottery):
   for currentLotteryNumberIndex in range(len(NumbersOfLottery)):
       if currentLotteryNumberIndex == len(NumbersOfLottery)-1:
           print(NumbersOfLottery[currentLotteryNumberIndex], end=".")
       else:
           print(NumbersOfLottery[currentLotteryNumberIndex], end="-")
 
def printingyourlotterynumbers(yournumbers):
   for yourlotterynumberindex in range(len(yournumbers)):
       if yourlotterynumberindex == len(yournumbers)-1:
           print(yournumbers[yourlotterynumberindex], end=".")
       else:
           print(yournumbers[yourlotterynumberindex], end="-")
 
def main(NUMBER_OF_LOTTERY_NUMBERS):
   lotteryNumbers = generateLotteryNumbers(NUMBER_OF_LOTTERY_NUMBERS)
   print(" The", NUMBER_OF_LOTTERY_NUMBERS, "lottery numbers for today are: ")
   printingLotteryNumbers(lotteryNumbers)
   num = NUMBER_OF_LOTTERY_NUMBERS
   fac = 1
   for i in range(1, num + 1):
       fac = fac * i
   factorial = 1
   for i in range(1, 50):
       factorial = factorial * i
   fact = 1
   for i in range(1, 50 - NUMBER_OF_LOTTERY_NUMBERS):
       fact = fact * i
   print("\n The chances of winning are one in:","\n",(factorial/(fac*fact)))
   print("\nThe numbers you chose were...")
   printingyourlotterynumbers(yournumbers)
 
   def goaway():
       msg.destroy()
   if lotteryNumbers == yournumbers:
       class Lottery(tk.Tk):
           def __init__(self, *args, **kwargs):
               tk.Tk.__init__(self, *args, **kwargs)
               tk.Tk.wm_title(self, "Lottery")
               container = tk.Frame(self)
               container.pack(side="top", fill="both", expand=True)
               container.grid_rowconfigure(0, weight=1)
               container.grid_columnconfigure(0, weight=1)
 
               self.frames = {}
               frame = Result(container, self)
               self.frames[Result] = frame
               frame.grid(row=0, column=0, sticky="nsew")
               self.show_frame(Result)
 
           def show_frame(self, cont):
               frame = self.frames[cont]
               frame.tkraise()
 
       class Result(tk.Frame):
           def __init__(self, parent, controller):
               tk.Frame.__init__(self, parent)
               label = tk.Label(self, text="Congratualtions! You have won!", font=Title_Font)
               label.pack(side="top", fill="x", pady=10)
               button1 = ttk.Button(self, text="Click here to recieve your money.", command=goaway)
               button1.pack()
 
       msg = Lottery()
       msg.mainloop()
   else:
       class Lottery2(tk.Tk):
           def __init__(self, *args, **kwargs):
               tk.Tk.__init__(self, *args, **kwargs)
               tk.Tk.wm_title(self, "Lottery")
               container = tk.Frame(self)
               container.pack(side="top", fill="both", expand=True)
               container.grid_rowconfigure(0, weight=1)
               container.grid_columnconfigure(0, weight=1)
 
               self.frames = {}
               frame = Result(container, self)
               self.frames[Result] = frame
               frame.grid(row=0, column=0, sticky="nsew")
               self.show_frame(Result)
 
           def show_frame(self, cont):
               frame = self.frames[cont]
               frame.tkraise()
       class Result(tk.Frame):
           def __init__(self, parent, controller):
               tk.Frame.__init__(self, parent)
               label = tk.Label(self, text="Sorry, you have lost", font=Title_Font)
               label.pack(side="top", fill="x", pady=10)
               button1 = ttk.Button(self, text="Click here", command=goaway)
               button1.pack()
 
       msg = Lottery2()
       msg.mainloop()
main(6)
