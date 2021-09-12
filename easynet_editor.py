from tkinter import *
import tkinter.ttk
import random
window=Tk()
window.title("不学cuda")
window.state("zoomed")
window.resizable(width=False, height=False)
class tensor:
    def __init__(self,x,y,name):
        self.radius=20#半径
        self.cmpx=x-new_editor.center_x#两个相对坐标
        self.cmpy=y-new_editor.center_y
        self.num=name#编号
        self.circle=new_editor.rander_target.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill="blue")
        self.text=new_editor.rander_target.create_text(x,y,text=name)
        #这里调用了别的类中的函数之后可以修改一下
    def draw_my_self(self,x,y):#重新画自己的圆和字
        self.circle=new_editor.rander_target.create_oval(self.cmpx+x-self.radius,self.cmpy+y-self.radius,x+self.cmpx+self.radius,self.cmpy+y+self.radius,fill="blue")
        self.text=new_editor.rander_target.create_text(self.cmpx+x,self.cmpy+y,text=self.num)

    def in_my_area(self,x,y,click_x,click_y):#检测点击是否在自己范围内
        if (self.cmpx+x-click_x)**2+(self.cmpy+y-click_y)**2<=self.radius**2:
            return 1
        return 0
class layer:
    def __init__(self,x,y,name,front,end,num):
        self.radius=30
        self.cmpx=x-new_editor.center_x
        self.cmpy=y-new_editor.center_y
        self.front=front#起点
        self.end=end#终点
        self.type=name#类型
        self.num=num#编号
        self.circle=new_editor.rander_target.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill="orange")
        self.text=new_editor.rander_target.create_text(x,y,text=name)
        #这里调用了别的类中的函数之后可以修改一下
    def draw_my_self(self,x,y):#重新画自己的圆和字
        self.circle=new_editor.rander_target.create_oval(self.cmpx+x-self.radius,self.cmpy+y-self.radius,x+self.cmpx+self.radius,self.cmpy+y+self.radius,fill="orange")
        self.text=new_editor.rander_target.create_text(self.cmpx+x,self.cmpy+y,text=self.type)

    def in_my_area(self,x,y,click_x,click_y):#检测点击是否在自己范围内
        if (self.cmpx+x-click_x)**2+(self.cmpy+y-click_y)**2<=self.radius**2:
            return 1
        return 0
class editor:
    def __init__(self,x_pos,y_pos,):
    
        #显示器
        self.rander_target=Canvas(window,width=200+window.winfo_width(),height=200+window.winfo_height(),background="green")
        self.rander_target.grid(row=1,column=0,rowspan=100,columnspan=100);
        self.rander_target.bind("<Button-1>",self.press_down)
        self.rander_target.bind("<B1-Motion>",self.press_motion)
        self.rander_target.bind("<ButtonRelease-1>",self.press_up)

        #tensor按钮
        self.btn_tensor=Button(window,activeforeground="black",text="add_tensor",font=("Arial Bold",16),bg="blue",fg="black")
        self.btn_tensor.grid(row=0,column=0)
        self.btn_tensor.bind("<Button-1>",self.add_tensor)

        #layer列表
        self.layer_combobox=tkinter.ttk.Combobox(window,width=35,height=30,values=["dense","relu","add","choose what type of layer you want to add"])
        self.layer_combobox.current(3)
        self.layer_combobox.grid(row=0,column=1)
        
        #layer按钮
        self.btn_layer=Button(window,activeforeground="black",text="add_layer",font=("Arial Bold",16),bg="blue",fg="black")
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
        window.update()
        self.vector_tensor.append(tensor(window.winfo_x()+window.winfo_width()/2,window.winfo_y()+window.winfo_height()/2,self.tensor_num+1))
        self.tensor_num+=1
        print("Add a tensor successfully")
    
    def add_layer(self,event):
        if self.layer_combobox.current()==3:
            return
        window.update()
        self.layer_num+=1
        self.vector_layer.append(layer(window.winfo_x()+window.winfo_width()/2,window.winfo_y()+window.winfo_height()/2,self.layer_combobox.get(),1,1,self.layer_num))
        print("Add a layer successfully")
    
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
    
#print(window.winfo_x(),window.winfo_width(),window.winfo_y(),window.winfo_height())
window.update()
new_editor=editor(window.winfo_x()+window.winfo_width()/2,window.winfo_y()+window.winfo_height()/2)
window.mainloop()
