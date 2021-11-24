from tkinter import *
import tkinter.messagebox
class layer_qw:
    def __init__(self,layerdad):
        self.dad=layerdad
        self.first=1
        self.question_window=Toplevel()
        self.question_window.title("layer information")
        self.question_window.wm_attributes('-topmost',1)
        self.caution_front=Label(self.question_window,text="起点")
        self.caution_front.grid(row=0,sticky=W)
        self.question_front=Entry(self.question_window)
        self.question_front.grid(row=0,column=1,sticky=E)
        self.question_front.insert(0,"1")
        #起点询问
        self.caution_end=Label(self.question_window,text="终点")
        self.caution_end.grid(row=1,sticky=W)
        self.question_end=Entry(self.question_window)
        self.question_end.grid(row=1,column=1,sticky=E)
        self.question_end.insert(0,"1")
        #终点询问
        self.button_for_quit=Button(self.question_window,text="确定")
        self.button_for_quit.grid(row=100,column=0)
        self.button_for_quit.bind("<ButtonRelease-1>",self.enter)
        
    def rebutton(self):
        self.question_window=Toplevel()
        self.question_window.title("layer information")
        self.caution_front=Label(self.question_window,text="起点")
        self.caution_front.grid(row=0,sticky=W)
        self.question_front=Entry(self.question_window)
        self.question_front.grid(row=0,column=1,sticky=E)
        self.question_front.insert(0,self.dad.front)
        #起点询问
        self.caution_end=Label(self.question_window,text="终点")
        self.caution_end.grid(row=1,sticky=W)
        self.question_end=Entry(self.question_window)
        self.question_end.grid(row=1,column=1,sticky=E)
        self.question_end.insert(0,self.dad.end)
        #终点询问
        self.button_for_quit=Button(self.question_window,text="确定")
        self.button_for_quit.grid(row=100,column=0)
        self.button_for_quit.bind("<ButtonRelease-1>",self.enter)
    def enter(self,event):
        try: 
            front = int(self.question_front.get())-1
            end = int(self.question_end.get())-1
        except ValueError:
            print("Go fucking check the type of the vaule!")
            tkinter.messagebox.showwarning(title="我是你爹",message="请勿乱写！")
            self.question_window.wm_attributes('-topmost',1)
            return
        if self.question_front.get()==self.question_end.get() or self.dad.new_editor.vector_tensor[front].state==0 or self.dad.new_editor.vector_tensor[end].state==0:
            return
        self.dad.front=front+1
        self.dad.end=end+1
        if self.first==1:
            self.first=0
        else:
            self.dad.delete()
        print("Successfully added a layer")
        self.transform(front,end)
        self.endd()
    def transform(self,front,end):
        self.dad.new_editor.vector_tensor[end].inlayer.append(self.dad)
        self.dad.new_editor.vector_tensor[front].outlayer.append(self.dad)
    def endd(self):
        self.dad.new_editor.state=0
        self.question_window.destroy()
        self.dad.draw_my_self()
        self.dad.new_editor.window.update()
        self.dad.new_editor.window.deiconify()

class dense_qw(layer_qw):
    def __init__(self,layerdad):
        layer_qw.__init__(self, layerdad)
        self.caution_inlen=Label(self.question_window,text="inlen")
        self.caution_inlen.grid(row=2,sticky=W)
        self.question_inlen=Entry(self.question_window)
        self.question_inlen.grid(row=2,column=1,sticky=E)
        self.question_inlen.insert(0,"1")
        #w询问
        self.caution_outlen=Label(self.question_window,text="outlen")
        self.caution_outlen.grid(row=3,sticky=W)
        self.question_outlen=Entry(self.question_window)
        self.question_outlen.grid(row=3,column=1,sticky=E)
        self.question_outlen.insert(0,"1")
        #b询问
    def rebutton(self):
        layer_qw.rebutton(self)
        self.caution_inlen=Label(self.question_window,text="inlen")
        self.caution_inlen.grid(row=2,sticky=W)
        self.question_inlen=Entry(self.question_window)
        self.question_inlen.grid(row=2,column=1,sticky=E)
        self.question_inlen.insert(0,self.dad.inlen)
        #w询问
        self.caution_outlen=Label(self.question_window,text="outlen")
        self.caution_outlen.grid(row=3,sticky=W)
        self.question_outlen=Entry(self.question_window)
        self.question_outlen.grid(row=3,column=1,sticky=E)
        self.question_outlen.insert(0,self.dad.outlen)
        #b询问
    def transform(self,front,end):
        try: 
            inlen = int(self.question_inlen.get())
            outlen = int(self.question_outlen.get())
        except ValueError:
            print("Go fucking check the type of the vaule!")
            tkinter.messagebox.showwarning(title="我是你爹",message="请勿乱写！")
            self.question_window.wm_attributes('-topmost',1)
            return 
        self.dad.new_editor.vector_tensor[end].inlayer.append(self.dad)
        self.dad.new_editor.vector_tensor[front].outlayer.append(self.dad)
        self.dad.inlen=inlen
        self.dad.outlen=outlen
        
class relu_qw(layer_qw):
    def __init__(self,layerdad):
        layer_qw.__init__(self,layerdad)

class add_qw(layer_qw):
    def __init__(self,layerdad):
        layer_qw.__init__(self,layerdad)
        self.caution_front2=Label(self.question_window,text="起点2")
        self.caution_front2.grid(row=2,sticky=W)
        self.question_front2=Entry(self.question_window)
        self.question_front2.grid(row=2,column=1,sticky=E)
        self.question_front2.insert(0,"1")
    def rebutton(self):
        layer_qw.rebutton(self)
        self.caution_front2=Label(self.question_window,text="起点2")
        self.caution_front2.grid(row=2,sticky=W)
        self.question_front2=Entry(self.question_window)
        self.question_front2.grid(row=2,column=1,sticky=E)
        self.question_front2.insert(0,self.dad.front2)
    def transform(self,front,end):
        try: 
            front2 = int(self.question_front2.get())-1
        except ValueError:
            print("Go fucking check the type of the vaule!")
            tkinter.messagebox.showwarning(title="我是你爹",message="请勿乱写！")
            self.question_window.wm_attributes('-topmost',1)
            return 
        self.dad.front2=front2+1
        self.dad.new_editor.vector_tensor[end].inlayer.append(self.dad)
        self.dad.new_editor.vector_tensor[front].outlayer.append(self.dad)
        self.dad.new_editor.vector_tensor[front2].outlayer.append(self.dad)
        
        