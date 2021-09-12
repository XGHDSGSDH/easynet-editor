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
        self.btn_layer.bind("<Button-1>",self.add_layer)
        
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
    
    def add_tensor(self,event):
        self.window.update()
        self.vector_tensor.append(tensor(self.window.winfo_x()+self.window.winfo_width()/2, self.window.winfo_y()+self.window.winfo_height()/2, self.tensor_num+1, self))
        self.tensor_num+=1
        print("Successfully added a tensor")
    
    def add_layer(self,event):
        if self.layer_combobox.current()==3:
            return
        self.window.update()
        self.layer_num+=1
        self.vector_layer.append(layer(self.window.winfo_x()+self.window.winfo_width()/2,self.window.winfo_y()+self.window.winfo_height()/2,self.layer_combobox.get(),1,1,self.layer_num, self))
        print("Successfully added a layer")
    
    def redraw(self):
        self.rander_target.delete(ALL)
        for i in self.vector_tensor:
            #self.center_x+=100
            i.draw_my_self(self.center_x,self.center_y)
        for i in self.vector_layer:
            i.draw_my_self(self.center_x,self.center_y)
    
    def press_down(self,event):
        print("get a press down")
        self.state=0
        self.now_pressed=0
        for i in self.vector_tensor:
            #print("fuck")
            if i.in_my_area(self.center_x,self.center_y,event.x,event.y)==1:
                self.state=1
                self.now_pressed=i.num
        for i in self.vector_layer:
            if i.in_my_area(self.center_x,self.center_y,event.x,event.y)==1:
                self.state==2
                self.now_pressed=i.num
        self.register_x=event.x
        self.register_y=event.y
        print(self.state,self.now_pressed)#现在的状态和已选中的点的编号
    def press_motion(self,event):
        print("get a left click motion")
        if self.state==0:
            self.center_x+=event.x-self.register_x
            self.center_y+=event.y-self.register_y
            self.register_x=event.x
            self.register_y=event.y
            self.redraw()
    def press_up(self,event):
        print(0)
    