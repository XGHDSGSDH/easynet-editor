from tkinter import *
import tkinter.ttk
from tensor import tensor
from layer import layer
class editor:
    def __init__(self,x_pos,y_pos, tkwindow):
        self.window=tkwindow
        #显示器
        self.rander_target=Canvas(self.window,width=200+self.window.winfo_width(),height=200+self.window.winfo_height(),background="green")
        self.rander_target.grid(row=1,column=0,rowspan=100,columnspan=100);
        self.rander_target.bind("<Button-1>",self.press_down)
        self.rander_target.bind("<B1-Motion>",self.press_motion)
        self.rander_target.bind("<ButtonRelease-1>",self.press_up)

        #tensor按钮
        self.btn_tensor=Button(self.window,activeforeground="black",text="add_tensor",font=("Arial Bold",16),bg="blue",fg="black")
        self.btn_tensor.grid(row=0,column=0)
        self.btn_tensor.bind("<Button-1>",self.add_tensor)

        #layer列表
        self.layer_combobox=tkinter.ttk.Combobox(self.window,width=35,height=30,values=["dense","relu","add","choose what type of layer you want to add"])
        self.layer_combobox.current(3)
        self.layer_combobox.grid(row=0,column=1)
        
        #layer按钮
        self.btn_layer=Button(self.window,activeforeground="black",text="add_layer",font=("Arial Bold",16),bg="blue",fg="black")
        self.btn_layer.grid(row=0,column=2)
        self.btn_layer.bind("<Button-1>",self.question)
        
        #相对坐标系坐标
        self.center_x=x_pos
        self.center_y=y_pos
        
        #tensor list,layer list
        self.vector_tensor=[]
        self.tensor_num=0
        self.vector_layer=[]
        self.layer_num=0
        #state
        self.state=0
        self.now_pressed=0
        
        #拖动时暂时坐标
        self.register_x=0
        self.register_y=0
        
        #输入窗口
        self.question_window=0
        self.caution_end=0
        self.caution_front=0
        self.question_end=0
        self.question_window=0
        self.button_for_quit=0
    
    def question(self,event):
        if self.state==-1 or self.layer_combobox.current()==3 or self.layer_combobox.current()==-1:
            return
        self.state=-1
        print(self.state)
        self.question_window=Tk()
        self.question_window.title("layer information")
        self.caution_front=Label(self.question_window,text="起点")
        self.caution_front.grid(row=0,sticky=W)
        self.question_front=Entry(self.question_window)
        self.question_front.grid(row=0,column=1,sticky=E)
        self.question_front.insert(0,"1")
        
        self.caution_end=Label(self.question_window,text="终点")
        self.caution_end.grid(row=1,sticky=W)
        self.question_end=Entry(self.question_window)
        self.question_end.grid(row=1,column=1,sticky=E)
        self.question_end.insert(0,"1")
        
        self.button_for_quit=Button(self.question_window,text="确定")
        self.button_for_quit.grid(row=2,column=0)
        self.button_for_quit.bind("<ButtonRelease-1>",self.add_layer)
        self.question_window.mainloop()
        
    def add_tensor(self,event):
        if self.state==-1:
            return
        self.window.update()
        self.tensor_num+=1
        self.vector_tensor.append(tensor(self.window.winfo_x()+self.window.winfo_width()/2, self.window.winfo_y()+self.window.winfo_height()/2, self.tensor_num, self))
        print("Successfully added a tensor")
    
    def add_layer(self,event):
        if int(self.question_front.get())==int(self.question_end.get()):
            return 0;
        print(self.layer_combobox.current())
        self.window.update()
        self.layer_num+=1
        self.vector_layer.append(layer(self.window.winfo_x()+self.window.winfo_width()/2,self.window.winfo_y()+self.window.winfo_height()/2,self.layer_combobox.get(),int(self.question_front.get()),int(self.question_end.get()),self.layer_num,self))
        print("Successfully added a layer")
        self.vector_tensor[int(self.question_end.get())-1].inlayer.append(self.vector_layer[self.layer_num-1])
        self.vector_tensor[int(self.question_front.get())-1].outlayer.append(self.vector_layer[self.layer_num-1])
        self.question_window.destroy()
        self.caution_end=0
        self.caution_front=0
        self.question_end=0
        self.question_window=0
        self.button_for_quit=0
        self.state=0
    
    def redraw(self):
        self.rander_target.delete(ALL)
        for i in self.vector_tensor:
            #self.center_x+=100
            i.draw_my_self()
        for i in self.vector_layer:
            i.draw_my_self()
    
    def press_down(self,event):
        #print("get a press down")
        print(self.state)
        if self.state==-1:
            return 
        self.state=0
        self.now_pressed=0
        for i in self.vector_tensor:
            #print("fuck")
            if i.in_my_area(event.x,event.y)==1:
                self.state=1
                self.now_pressed=i.num
        for i in self.vector_layer:
            if i.in_my_area(event.x,event.y)==1:
                self.state=2
                self.now_pressed=i.num
        self.register_x=event.x
        self.register_y=event.y
        print(self.state,self.now_pressed)#现在的状态和已选中的点的编号
    def press_motion(self,event):
        #print("get a left click motion")
        if self.state==-1:
            return 
        if self.state==0:
            self.center_x+=event.x-self.register_x
            self.center_y+=event.y-self.register_y
            self.register_x=event.x
            self.register_y=event.y
            self.redraw()
            return
        if self.state==1:
            self.vector_tensor[self.now_pressed-1].delete()
            self.vector_tensor[self.now_pressed-1].follow(event.x,event.y)
            return
        if self.state==2:
            self.vector_layer[self.now_pressed-1].delete()
            self.vector_layer[self.now_pressed-1].follow(event.x,event.y)
    def press_up(self,event):
        print(0)