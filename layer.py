class layer:
    def __init__(self,x,y,name,front,end,num,neweditor):
        self.new_editor = neweditor
        self.radius=30
        self.cmpx=x-self.new_editor.center_x
        self.cmpy=y-self.new_editor.center_y
        self.front=front#起点
        self.end=end#终点
        self.type=name#类型
        self.num=num#编号
        self.circle=self.new_editor.rander_target.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill="orange")
        self.text=self.new_editor.rander_target.create_text(x,y,text=name)
        #这里调用了别的类中的函数之后可以修改一下
    def draw_my_self(self,x,y):#重新画自己的圆和字
        self.circle=self.new_editor.rander_target.create_oval(self.cmpx+x-self.radius,self.cmpy+y-self.radius,x+self.cmpx+self.radius,self.cmpy+y+self.radius,fill="orange")
        self.text=self.new_editor.rander_target.create_text(self.cmpx+x,self.cmpy+y,text=self.type)

    def in_my_area(self,x,y,click_x,click_y):#检测点击是否在自己范围内
        if (self.cmpx+x-click_x)**2+(self.cmpy+y-click_y)**2<=self.radius**2:
            return 1
        return 0