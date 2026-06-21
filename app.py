from tkinter import *
class NLPApp :
  
  def __init__(self):
    #login ka gui load krna hai 
    self.root = Tk()
    self.root.title('NLP App')
    self.root.iconbitmap("resources/logo_a_dark.ico")
    self.root.geometry("400x600")
    self.root.configure(bg='#8C8682')

    self.login_gui()

    self.root.mainloop()

  def login_gui(self):
    self.clear()
    heading = Label(self.root,text='NLP App',bg='#8C8682',fg='black')
    heading.pack(pady=(30,30))
    heading.configure(font=('verdana','24','bold'))

    lable1 = Label(self.root,text='Enter  E-Mail',bg='#8C8682',fg='black')
    lable1.pack(pady=(10,10))
    lable1.configure(font=('verdana','9','bold'))

    self.email_input = Entry(self.root,width=35)
    self.email_input.pack(pady=(5,10),ipady=5)
    self.email_input.configure(font=('verdana','10','bold'))


    lable2 = Label(self.root,text='Enter Password',bg='#8C8682',fg='black')
    lable2.pack(pady=(10,10))
    lable2.configure(font=('verdana','9','bold'))

    self.password_input = Entry(self.root,width=35,fg='green', show='*')
    self.password_input.pack(pady=(5,10),ipady=5)
    self.password_input.configure(font=('verdana','10','bold'))

    login_button = Button(self.root,text='Login',width = 18, height=2)
    login_button.pack(pady=(10,10))
    login_button.configure(font=('verdana','8','bold'))


    lable3 = Label(self.root,text='Not a member ?',bg='#8C8682',fg='black')
    lable3.pack(pady=(10,5))
    lable3.configure(font=('verdana','9','bold'))

    redirect_button = Button(self.root,text='Register Now',width = 10, height=2,command=self.register_gui)
    redirect_button.pack()
    redirect_button.configure(font=('verdana','8','bold'))


  def clear(self):
    #clear the existing gui
    for i in self.root.pack_slaves():
      i.destroy()

  def register_gui(self):
    self.clear()

    heading = Label(self.root,text='NLP App',bg='#8C8682',fg='black')
    heading.pack(pady=(30,30))
    heading.configure(font=('verdana','24','bold'))

    lable0 = Label(self.root,text='Enter Name',bg='#8C8682',fg='black')
    lable0.pack(pady=(10,10))
    lable0.configure(font=('verdana','9','bold'))

    self.name_input = Entry(self.root,width=35)
    self.name_input.pack(pady=(5,10),ipady=5)
    self.name_input.configure(font=('verdana','10','bold'))

    lable1 = Label(self.root,text='Enter  E-Mail',bg='#8C8682',fg='black')
    lable1.pack(pady=(10,10))
    lable1.configure(font=('verdana','9','bold'))

    self.email_input = Entry(self.root,width=35)
    self.email_input.pack(pady=(5,10),ipady=5)
    self.email_input.configure(font=('verdana','10','bold'))


    lable2 = Label(self.root,text='Enter Password',bg='#8C8682',fg='black')
    lable2.pack(pady=(10,10))
    lable2.configure(font=('verdana','9','bold'))

    self.password_input = Entry(self.root,width=35,fg='green', show='*')
    self.password_input.pack(pady=(5,10),ipady=5)
    self.password_input.configure(font=('verdana','10','bold'))

    register_button = Button(self.root,text='Register',width = 18, height=2)
    register_button.pack(pady=(10,10))
    register_button.configure(font=('verdana','8','bold'))


    lable3 = Label(self.root,text='Already a Member ?',bg='#8C8682',fg='black')
    lable3.pack(pady=(10,5))
    lable3.configure(font=('verdana','9','bold'))

    redirect_button = Button(self.root,text='Login',width = 8, height=2,command=self.login_gui)
    redirect_button.pack()
    redirect_button.configure(font=('verdana','9','bold'))

nlp = NLPApp()