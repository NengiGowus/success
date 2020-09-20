import tkinter
from tkinter import *
from tkinter import messagebox as mb
root = tkinter.Tk()
root.title("Sucessful")
canvass = Canvas(root,width=400,height=300,relief='raised')
canvass.pack()
def fame():
                mb.showinfo("Famous","If you want to be famous in life, you have to be the best in what you do, there are plenty musicians out there, but only few are known, and you know only those few because they are the best at what they do, they sing or rap so well that you cant avoid them, if you are into cosmetics,why not create the best cometic,it will give you a solid fan base, and people will be interested in paying you whatever amount you want and to be the best at what you do, you have to keep learning and praticing, it could be your passion e.g, programmer,graphic designer, skin care or your job like e.g law. So become the best and see how your life will transform")
def rich():
                mb.showinfo("Rich","If you truly want to be rich, you have to sell something, for example, you can be selling the skills you got in college to a company or start a company and start selling your skills. If you have a passion, after you are the best in that passion, show case your work and monetise that passion, maybe your passion is singing, then monetise it but also make sure your songs make some sense. But before you thinkl about money, make sure your products make people happy. If you want to be just a trader, its a nice decision but it is much more better to be a manufacturer than a distributor, there are so many truths about that. If you dont know what to create or manufacture, then use your passions, everyone has passions. Do you love movies, then make movies or movie scripts and sell them!")
def learning():
                mb.showinfo("Secrets to learn and remember forever","Learning is not just a one day or one time process, it is a life time process, when you learn something, dont just drop it and forget it, can you realise that most of the stuffs you were taught in children baby schools, you can still remember them because you kept repeating them , so if you really want to learn something and remember, keep reading it again and again, for days. Everyday, keep a particular time to remeber that thing you have read, if you continue like that for five days, i assure you, you will not FORGET easily")
def time():
                mb.showinfo("TIME!","Time is a very important topic and it is important in general, you have to always make sure that whatever you are doing with your time, never be IDLE, always make sure you are doing something important tomake you better at what you do. Always make sure you invest your time in things that will make you better at whatever you do, become the best, because once time is gone, you can never bring it back so use your time wisely")
def about():
                mb.askokcancel("About","This app is developed by Nengi Gowus, it is to help you become the better version of your self at those particular topics listed. Thanks")
def exito():
                exit()
chooselabel = Label(root,text="Hello, am going to be teaching you",font=('times',16))
contlabell = Label(root,text="HOW TO BECOME A SUCCESS",font=('times',16))
contlabel = Label(root,text="These are proven worth steps",font=('times',16))
canvass.create_window(150,10,window=chooselabel)
canvass.create_window(180,40,window=contlabell)
canvass.create_window(250,70,window=contlabel)
butA = Button(root,text="FAMOUS",width=7,height=2,command =fame)
butB = Button(root,text="RICH",width=7,height=2,command=rich)
butC = Button(root,text="secrets to learning",width=15,height=2,command=learning)
butD = Button(root,text="Time Management",width=15,height=2,command=time)
canvass.create_window(30,120,window=butA)
canvass.create_window(30,150,window=butB)
canvass.create_window(50,180,window=butC)

canvass.create_window(50,210,window=butD)
msg1 = Message(root,text="Pick anyone of the options to get real advice and tips from them",font=('times',18))
canvass.create_window(250,170,window=msg1)
aboutbut = Button(root,text="About",width=9,height=2,command=about)
canvass.create_window(30,250,window=aboutbut)
exitbut = Button(root,text="Exit",width=5,height=2,command=exito)
canvass.create_window(380,270,window=exitbut)

root.mainloop()
