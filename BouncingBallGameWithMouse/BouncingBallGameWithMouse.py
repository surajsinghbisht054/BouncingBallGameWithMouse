#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
print __author__
# ----------------------------------------------------------------------

try:
    import Tkinter
except:
    import tkinter as Tkinter
import time
BALL_SPEED=5

class GameCanvas(Tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        Tkinter.Canvas.__init__(self, *args, **kwargs)
        self.create_bouncing_ball()
        self.create_moving_bat()
        
    def create_moving_bat(self):
        self.bat=Tkinter.Canvas.create_rectangle(self,0,570,100,580, fill='lightslateblue')
        self.bind('<Motion>', self.update_bat_moves)
        return
    
    def update_bat_moves(self, event=None):
        x=event.x
        x1,y1,x2,y2=self.coords(self.bat)
        gap=(x2-x1)/2
        center=x1+gap
        move=x-center
        self.move(self.bat,move,0)
        return
        
    def create_bouncing_ball(self):
        self.ball=Tkinter.Canvas.create_oval(self, 0,0,20,20, fill='cornflowerblue')
        self.x=BALL_SPEED
        self.y=BALL_SPEED
        return
    
    def update_board(self):
        width=self.winfo_width()
        height=self.winfo_height()
        x1,y1,x2,y2=self.coords(self.ball)
        hit=len(self.find_overlapping(x1,y1,x2,y2))
        if hit>=2:
            self.y=-BALL_SPEED
            self.move(self.ball,self.x,self.y)
        elif x1<0:
            self.x=BALL_SPEED
            self.move(self.ball,self.x,self.y)
        elif x2>width:
            self.x=-BALL_SPEED
            self.move(self.ball,self.x,self.y)
        elif y1<0:
            self.y=BALL_SPEED
            self.move(self.ball,self.x,self.y)
        elif y2>height:
            x=width/2
            y=height/2
            self.create_text(x,y, text='Game Over', font=('arial 50 bold'), fill='red')
            self.y=-BALL_SPEED
            self.move(self.ball,self.x,self.y)            
        else:
            self.move(self.ball,self.x,self.y)
        return





# Gui Handler
def main():
    root=Tkinter.Tk()
    root.minsize(800,600)
    root.maxsize(800,600)
    board=GameCanvas(root, bg='lavender')
    board.pack(expand='yes', fill='both')
    # Program Loop
    while True:
        root.update()
        root.update_idletasks()
        board.update_board()
        time.sleep(0.01)

# main Trigger
if __name__=='__main__':
    main()
