# Adapted from https://developpaper.com/python-uses-tkinter-to-realize-the-effect-of-rolling-lottery/
from tkinter import *
from tkinter import messagebox
#import tkinter.font as font
from PIL import ImageTk,Image 
import csv
import random
from datetime import datetime

class NTC:
    def __init__(self, master):
        self.winners = []
        self.is_run = False
        self.WIP = True
        self.counter = 0
        self.timer = 0
        pool = StringVar(value="")
        prize = StringVar(value="Consolation Prizes")
        
        self.master = master
        master.title("NTC Lucky draw")
        master.geometry("580x550")
        master.configure(bg = "white")

        self.label1 = Label(master, \
                            text = f"NTC {datetime.now().year} Lucky Draw", \
                            font = ("Trebuchet MS", 24, "bold"), bg = "white", \
                            fg = "black" )
        #self.label1.place(relx=.5, rely=.5, anchor="center")
        self.label1.pack(side="top")
        
        self.b1 = Button(master, text="Generate lucky draw winners", \
                         bg="orange", fg="black", font=("Trebuchet MS", 18),\
                         command = lambda: self.generate(pool,prize))
                         #command = lambda: [master.withdraw(), self.generate()])
        #self.b1.place(relx = 0.3, rely = 0.8, anchor=CENTER)
        self.b1.place(x=200,y=400, anchor=CENTER)
        #self.b1["font"] = font.Font(size=20)
        #self.b1.pack(padx=10,side=LEFT)
        
        self.b2 = Button(master, text="Claimed!", \
                         bg="black", fg="white", font=("Trebuchet MS", 18),\
                         command = lambda: self.claimed(pool,prize))
        #self.b2.pack(padx=10,side=LEFT)
        self.b2.place(x=450, y=400, anchor=CENTER)

        self.label2 = Label(master,\
                            textvariable = pool, \
                            font = ("Trebuchet MS", 16, "bold"), bg = "white", \
                            fg = "red" )
        self.label2.pack(side="bottom",pady=5)
        
        self.label3 = Label(master,\
                            textvariable = prize, \
                            font = ("Trebuchet MS", 16, "bold"), bg = "white",\
                            fg = "black" )
        self.label3.pack(side="bottom")
        
        with open('NTC_Participants.csv', newline='') as f:
            reader = csv.reader(f)
            next(reader, None) #Skip header
            ppl_nested = list(reader) # returns a nested list
            # Convert to a 1D list
            self.ppl = [item for i in ppl_nested for item in i]
            
    def drawinprocess(self, pool, prize):
        # Need to initialise list to fix the length
        # Not needed for consolation which is handled in claimed() 
        tmp = [["3rd prize",""],["2nd prize",""],["1st prize",""]]
        winner = random.choice(self.ppl)
        pool.set(winner)
        if self.WIP == True:
            root.after(50, NTC.drawinprocess, self, pool, prize)
            self.timer += 1
        else:
            #prize.set(f"{winner}")
            winner_n = self.ppl.pop(self.ppl.index(winner))
            if self.counter < 10:
                self.winners = [] # If click generate twice, reset the list of winners to avoid error in concat and saving; note that it discards the first 10 generated from potential pool
                self.winners.append(winner) # Add the last winner shown
                pool.set("Congratulations! Click Claimed to continue to the next prize")
                random.shuffle(self.ppl)
                self.winners.extend(self.ppl[0:9]) # To account for that last winner shown that is added
                self.ppl = self.ppl[9:]
                winners_str = '\n'.join(self.winners)
                messagebox.showinfo("Consolation Prize Winners",winners_str)
                self.winners = [["Consolation",self.winners[i]] for i in range(len(self.winners))]
                # Need to fix length of ist to avoid errors when saving to csv
                self.winners.extend(tmp)
            elif self.counter == 11:
                self.winners[10] = (["3rd prize",winner_n]) # python starts from 0
            elif self.counter == 12:
                self.winners[11] = (["2nd prize",winner_n])
            elif self.counter == 13:
                self.winners[12] = (["1st prize",winner_n])
            
             #self.winners.append(winner_n)  
             
        if self.timer == 30:
             self.WIP = False
             self.is_run = False
             self.timer = 0
        else:
             self.WIP = True
        return
    
    
    def generate(self, pool, prize):
        if self.is_run:
            return
        if self.counter > 13:
            messagebox.showerror("Max prizes reached",\
                                 "All prizes have been given out.")
            return
        
        self.is_run = True
        if self.counter == 0: # This code is to avoid errors if claimed is hit before consol prizes generated
            self.counter = 1
        NTC.drawinprocess(self, pool, prize)

        
    def claimed(self,pool,prize):
        # If lucky draw still running, don't do anything to counter
        if self.is_run: 
            return
        
        self.counter += 1
        if self.counter == 1:
            self.counter -= 1
            messagebox.showwarning("Warning","You haven't generated a list of consolation prize winners yet. Click 'Generate' first, then 'Claimed!'.")
        elif self.counter <= 10:
            #prize.set(value = "Consolation prizes")
            self.claimed(pool,prize)
            # Make the counter run itself up to 10 and skip to 3rd prize
        elif self.counter == 11:
            prize.set(value = "3rd prize")
            pool.set(value="Click Generate! Who will win the 3rd prize?")
        elif self.counter == 12:
            prize.set(value = "2nd prize")
            pool.set(value="Click Generate! Who will win the 2nd prize?")
        elif self.counter == 13:
            prize.set(value = "Grand prize")
            pool.set(value="Click Generate! Who will be the lucky winner?")
        elif self.counter == 14:
            prize.set("End of lucky draw")      
            with open("Lucky Draw Winners.csv","w",newline="") as f_out:
                writer = csv.writer(f_out)
                writer.writerow(["Prize Type","Name"])
                writer.writerows(self.winners)
        # If self.counter is more than 14 (i.e. keep clicking claimed
        # after end of lucky draw), do nothing

        return
        

root = Tk()

# Show logo
canvas = Canvas(root, width = 500, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("ntc logo.png"))
canvas.create_image(0, 0, anchor=NW, image=img)

my_gui = NTC(root)
root.mainloop()