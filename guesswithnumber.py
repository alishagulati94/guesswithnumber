import os
import random
from tkinter import *
import tkinter.messagebox
from turtle import title
# from PIL import Image,ImageTk

def run():
        global chances,smallerorbigger,asds,guess,chancesvar,randomn,r
        guesss=guess.get()
    # try:
        if(chances <= 8 and chances > 0):
            guesss=int(guesss)
            chancesvar.set(chances)
            c.update()
            if(int(guesss )== int(randomn)):
                msg=tkinter.messagebox.askyesno("You won","You have won\nEvery next level the range will increased by 10X \n\nDo you want to continue for the next level")
                if(msg == True):
                    guess.set("")
                    chances=8
                    chancesvar.set(chances)
                    c.update()
                    smallerorbigger.set("")
                    # randomn=random.randint(0,int(randomn*10))
                    r=r*10
                    randomn=random.randint(0,r)
                    asds.set("Guess the number - ")
                if(msg == False):
                    guess.set("")
                    chances=8
                    chancesvar.set(chances)
                    c.update()
                    smallerorbigger.set("")
                    # randomn=random.randint(0,int(randomn*10))
                    r=r
                    randomn=random.randint(0,r)
                    asds.set("Guess the number - ")
            


            if(int(guesss )< int(randomn)):
                smallerorbigger.set("Try to get a bigger number")
                ss.update()
                chances-=1
                chancesvar.set(chances)
                c.update()
            if(int(guesss )> int(randomn)):
                smallerorbigger.set("Try to get a smaller number")
                ss.update()
                chances-=1
                chancesvar.set(chances)
                c.update()
            if(chances==1 and int(guesss )== int(randomn)):
                tkinter.messagebox.showinfo("You lost",f"You have Lost the game \n The number was {randomn}")
                
                guess.set("")
                chances=8
                chancesvar.set(chances)
                c.update()
                smallerorbigger.set("")
                randomn=random.randint(0,100)




    # except:
        # print("Pls enter a valid number")


def htp():
    print("You need to guess a number between 1 to 100 in the first level")
main_root = Tk()
main_root.geometry("720x600")

main_menu = Menu(main_root)
main_menu.add_command(label="How To Play")
main_menu.add_command(label="Rules")
main_menu.add_command(label="About us")
main_menu.add_command(label="Code")
main_menu.add_command(label="Dev")
main_root.config(menu=main_menu)

main_root.title("Guess The Number")


Label(main_root,text="Guess The Number",font="lucida 16 bold").grid(padx=150,pady=10,row=0,column=2)

asds=StringVar()
asds.set("Guess the number (between 1 to 100) - ")
guess=StringVar()

asdsl=Label(main_root,textvar=asds).grid(row=2,column=0,pady=10)
Entry(main_root,textvariable=guess).grid(row=2,column=1,pady=10)
Button(main_root,text="Guess",command=run).grid()


chancesvar=StringVar()
Label(main_root,text="Chances Left").grid(row=5,column=0,pady=10)
c=Label(main_root,textvar=chancesvar)
c.grid(row=5,column=1)

smallerorbigger=StringVar()

ss=Label(main_root,textvar=smallerorbigger)
ss.grid(row=6)

chances=8
r=100
randomn=random.randint(0,r)


main_root.mainloop()