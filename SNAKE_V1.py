#snake
import tkinter as tk
import random
import time



#settings
if input("custom settings (y/n) :")=="y":
    speed=int(input("speed(ms): :"))+3000
    fullness=int(input("fulness of map in promile: "))
else:
    speed=300+3000          #speed in ms
    fullness=0      #promil of map coverd max 250

#variables
direction=0
mx=0
my=0
score=-1
size = 22
size2 = size**2
apple=0

#lists
blocks = []
snake=[253,254,255]


#window setup
window = tk.Tk()
window.title("BLEH")
window.geometry(str(size * 20) + "x" + str(size * 20))
canvas = tk.Canvas(window, width=(size * 20), height=(size * 20), bg="white")
canvas.pack()


#resets
def reset():
    global snake
    for i in range(size):
        blocks.append(1)
    for i in range(size-2):
        blocks.append(1)
        for i in range(size-2):
            if random.randint(0,1000)<=fullness:
                blocks.append(1)
            else:
                blocks.append(0)
        blocks.append(1)
    for i in range(size):
        blocks.append(1)
    if blocks[snake[0]]==1 or blocks[snake[0]]==1 or blocks[snake[2]]==1:
        reset()



def death():
    global cube,blocks,snake,apple,score
    x = 0
    y = 20*size
    weg = 0
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if blocks[weg] == 1:
                cube = canvas.create_rectangle(x, y, x + 20, y - 20, fill="black")
            else:
                cube = canvas.create_rectangle(x, y, x + 20, y - 20, fill="green", outline="darkgreen")
            weg = weg + 1
            x = x + 20
        x = 0
        y = y - 20
    canvas.create_text(200, 200, text=("Score:",score), fill="red", font=("Arial", 50))
    exit()



def new_apple_pos():
    global snake,blocks,apple,score
    score+=1
    for i in range(1000):
        apple=random.randint(0,size2-1)
        if not(apple in snake) and blocks[apple]!=1:
            return False

reset()
new_apple_pos()






def render():
    tick()
    global cube,blocks,snake,apple
    x = 0
    y = 20*size
    weg = 0
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if blocks[weg] == 1:
                cube = canvas.create_rectangle(x, y, x + 20, y - 20, fill="black")
            else:
                cube = canvas.create_rectangle(x, y, x + 20, y - 20, fill="green", outline="darkgreen")
            if weg in snake:
                canvas.create_oval(x, y, x+20, y-20, fill="blue", outline="")
                if snake[0] == weg:
                    canvas.create_oval(x+12, y-10, x+15, y-12, fill="black", outline="")
                    canvas.create_oval(x+4, y-10, x+7, y-12, fill="black", outline="")
            if weg==apple:
                canvas.create_oval(x, y, x+20, y-20, fill="red", outline="")
            weg = weg + 1
            x = x + 20
        x = 0
        y = y - 20
    window.after(speed, render)




def tick():
    global direction,snake,apple,db
    db=direction
    if direction ==0:
        nx=snake[0]+22
    elif direction ==1:
        nx=snake[0]-22
    elif direction ==2:
        nx=snake[0]-1
    elif direction ==3:
        nx=snake[0]+1
    if (blocks[nx]==1):
        death()
    if nx==apple:
        snake=[nx]+snake
        new_apple_pos()
    else:
        snake.pop()
        if (nx in snake):
            death()
        snake=[nx]+snake






#TASTEN
def move(event):
    global direction,db

    if event.keysym == "Up" and db!=1:
        direction=0
    elif event.keysym == "Down" and db!=0:
        direction=1
    elif event.keysym == "Left" and db!=3:
        direction=2
    elif event.keysym == "Right" and db!=2:
        direction=3
window.bind("<Key>", move)




render()
speed=speed-3000
window.mainloop()
