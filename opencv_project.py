from tkinter import * 
from tkinter.ttk import *
import cv2
import tkinter as tk

from tkinter import filedialog
win = Tk()

win.geometry('400x400') 

global img 
img  = cv2.imread("nature.jpg")

def open_file():
    img  = cv2.imread("nature.jpg")
    cv2.imshow('original',img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

def resize():

    re_img = cv2.resize(img,(500,500))
    cv2.imshow('resize ', re_img)
    cv2.waitKey(2000)
    
    cv2.destroyAllWindows()

def half():
    re_img1 = cv2.resize(img,(img.shape[1]//2 , img.shape[0]//2))
    cv2.imshow('half ', re_img1)

    cv2.waitKey(2000)
    
    cv2.destroyAllWindows()

def one_third():

    re_img3 = cv2.resize(img,(img.shape[1]//3 , img.shape[0]//3))
    cv2.imshow('third ', re_img3)
    cv2.waitKey(2000)
    
    cv2.destroyAllWindows()



def one_fourth():
    re_img4 = cv2.resize(img,(img.shape[1]//4 , img.shape[0]//4))
    cv2.imshow('fourth ', re_img4)
    cv2.waitKey(2000)
    
    cv2.destroyAllWindows()

     

Label1 = Label(win, text = "Image Resize", font = ('bold ',18))
Label1.place(x = 100 , y = 20 , width = 170, height = 30) 

btn = Button(win, text ='Open',command = open_file)
btn.place(x = 150 , y = 100 , width = 80, height = 30) 


grayscale_btn = Button(win, text ='Resize',command = resize)
grayscale_btn.place(x = 50 , y = 150 , width = 80, height = 30) 

half_btn = Button(win, text ='Half',command = half)
half_btn.place(x = 250 , y = 150 , width = 80, height = 30) 

one_third_btn = Button(win, text ='one_third',command = one_third)
one_third_btn.place(x = 50 , y = 200 , width = 80, height = 30) 

one_fourth_btn = Button(win, text ='one_fourth',command = one_fourth)
one_fourth_btn.place(x = 250 , y = 200 , width = 80, height = 30) 


win.mainloop() 










