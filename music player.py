from tkinter import *
import pygame
import os

root = Tk()

class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("MusicPlayer")
        self.root.geometry("600x400+200+200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        trackframe = LabelFrame(self.root,text="Song Track",font=("times",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)
        songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times",16,"bold"),bg="blue",fg="white").grid(row=0,column=0,padx=10,pady=5)
        trackstatus = Label(trackframe,textvariable=self.status,font=("times",16,"bold"),bg="blue",fg="white").grid(row=0,column=1,padx=10,pady=5)

        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)

        playbtn = Button(buttonframe,text="PLAY",command=self.play_song,height=1,width=8,font=("times",16,"bold"),fg="white",bg="blue").grid(row=0,column=0,padx=10,pady=5)
        playbtn = Button(buttonframe,text="PAUSE",command=self.pause_song,width=8,height=1,font=("times",16,"bold"),fg="white",bg="blue").grid(row=0,column=1,padx=10,pady=5)
        playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpause_song,width=10,height=1,font=("times",16,"bold"),fg="white",bg="blue").grid(row=0,column=2,padx=10,pady=5)
        playbtn = Button(buttonframe,text="STOP",command=self.stop_song,width=10,height=1,font=("times",16,"bold"),fg="white",bg="blue").grid(row=0,column=3,padx=10,pady=5)

        songsframe = LabelFrame(self.root,text="Playlist",font=("times",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=0,y=200,width=600,height=200)

        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="blue",selectmode=SINGLE,font=("times",16,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        os.chdir("D:\songs")
        songtracks = os.listdir()
        for track in songtracks:
          self.playlist.insert(END,track)
          
    def play_song(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()
        
    def stop_song(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()
        
    def pause_song(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()
        
    def unpause_song(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()


MusicPlayer(root)
root.mainloop()
    
    
    
