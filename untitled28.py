from tkinter import*
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root=Tk()
root.minsize(600,600)
root.maxsize(600,600)

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.55,anchor=CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.05,rely=0.03,anchor=CENTER)


open_button=Button(root,image=open_img,text="OpenFile", command=openFile)
open_button.place(relx)

name=""
def openFile():
    global name
my_text.delete(1.0, END)
input_file_name(0, END)    
text_file = filedialog.askopenfilename(name="open text file", filetypes=(((".*txt"),)))
print(text_file)
name = os.path.basename(text_file)
formulated_name = name.split('.')[0]
input_file_name.insert(END, formated_name)
root.title(formated_name)
text_file = open(name,'r')
paragraph=text_file.read()
my_text.insert(END,paragraph)
text_file.close

def save():
   put_name = input_file_name()
   file = open(input_name+".txt", "w")
   data = my_text.get("1.0",END)
   print(data)
   file.write(data)
   input_file_name(0,END)
   my_text.insert(index, chars, args)
   messagebox.showinfo("Update","Success")   
   
def closeWindow():
  root.destroy()



open_button.Button(root,image=open_img,text="Open File", command=openFile)  
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button.Button(root,image=open_img,text="Open File", command=save)  
save_button.place(relx=0.05,rely=0.03,anchor=CENTER)
open_button.Button(root,image=open_img,text="Open File", command=openFile)  
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)