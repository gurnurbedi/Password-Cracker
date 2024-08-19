#page1 contains the GUI

from tkinter import *

root = Tk()  
root.geometry("600x250")
root.title("Password Cracker")
root['bg']="Light Blue"

def nextpage():
    root.destroy()
    import backup_project_page2

passw_label = Label(root, text = 'Password Hacking Program',
                    font = ('calibre',24,'bold', 'italic'), bg='Light Blue')

label= Label(root,
             text= "Hello, this program will find the password entered by the user\n along with the time taken to compute the password",
             font= ('Times New Roman', 15, 'italic'), bg='Light Blue')

btn=Button(root,text = 'Crack password', bg='pink',
            font= ('Times New Roman', 10, 'italic'), command = nextpage)

passw_label.pack()
label.pack()
btn.pack()



root.mainloop()
