from tkinter import *
  
root = Tk()

root.geometry("600x400")
root.title("notebook")
root.minsize(height=400, width=600)
root.maxsize(height=400, width=600)

scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT,
               fill=Y)
  
  
text_info = Text(root,
                 yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

scrollbar.config(command=text_info.yview)
  
root.mainloop()
