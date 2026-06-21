from tkinter import *
class NLPApp :
  
  def __init__(self):
    #login ka gui load krna hai 
    self.root = Tk()
    self.root.title('NLP App')
    self.root.iconbitmap("resources/logo_a_dark.ico")
    self.root.geometry("400x600")
    self.root.configure(bg='#8C8682')
    self.root.mainloop()

nlp = NLPApp()