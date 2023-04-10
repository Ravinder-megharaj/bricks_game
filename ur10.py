from ursina import *
from pygame import mixer
app=Ursina()
dx=0.05
dy=0.05
score=0
dead=False
mixer.init()
def update():
    global dx,dy,score,dead
    if  not dead:
        if board.x<=6 and board.x>=-6:
            if held_keys["right arrow"]:
                board.x+=0.07
            if held_keys["left arrow"]:
                board.x-=0.07
       
       
            board.x=clamp(board.x,-6,6)

        ball.x+=dx
        ball.y+=dy        
        if ball.x>=7 or ball.x<=-7:
            dx*=-1
        if ball.y<=-4:
            dead=True 
        if ball.y>=3.9:
            dy*=-1                    
        hit_info=ball.intersects()
        hit_bord=board.intersects()
        if hit_bord.hit:
            mixer.music.load("bord.mp3")
            mixer.music.set_volume(1.0)
            mixer.music.play()
            time.sleep(0)
        if hit_info.hit:
            dy*=-1
            if hit_info.entity in boxes:
                destroy(hit_info.entity) 
                score+=1
                mixer.music.load("breaks.mp3")
                mixer.music.set_volume(1.0)
                mixer.music.play()
                time.sleep(0)
                if score==39:
                    dead=True
        if score==5:
            dx=0.06
            dy=0.06
        print_on_screen("score: "+str(score),position=(-0.8,0.5),scale=2)   
    else:
        destroy(board)
        destroy(ball)
        for i in boxes:
            destroy(i)
        if score==39:
            print_on_screen("** you have win the Game **",scale=3,position=(-0.3,-0.01))
        else:
            print_on_screen("Game is over",scale=3,position=(-0.3,-0.01))
            print_on_screen("Final score is: "+str(score),position=(-0.2,-0.15))


board=Entity(model="quad",color=color.yellow,position=(0,-4,0),scale=(3,0.3),collider="box")
ball=Entity(model="sphere",color=color.orange,scale=0.3,position=(0,-3.57),collider="box")
box=Entity(model='cube',texture='brick',scale=(1,0.5,0.5),position=(-10,4,0),collider="box")
boxes=[]
for i in range(6,-7,-1):
    for j in range(1,4):
        boxes.append(duplicate(box,x=i,y=j,color=color.random_color()))

app.run()

