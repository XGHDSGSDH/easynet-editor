
class tensor:
    def __init__(self,x,y,name,neweditor):
        self.new_editor = neweditor
        self.radius=20#半径
        self.cmpx=x-self.new_editor.center_x#两个相对坐标
        self.cmpy=y-self.new_editor.center_y
        self.num=name#编号
        self.circle=self.new_editor.rander_target.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill="blue")
        self.text=self.new_editor.rander_target.create_text(x,y,text=name)
        self.inlayer=[]
        self.outlayer=[]
        #这里调用了别的类中的函数之后可以修改一下
    def draw_my_self(self):#重新画自己的圆和字
        self.circle=self.new_editor.rander_target.create_oval(self.cmpx+self.new_editor.center_x-self.radius,self.cmpy+self.new_editor.center_y-self.radius,self.new_editor.center_x+self.cmpx+self.radius,self.cmpy+self.new_editor.center_y+self.radius,fill="blue")
        self.text=self.new_editor.rander_target.create_text(self.cmpx+self.new_editor.center_x,self.cmpy+self.new_editor.center_y,text=self.num)

    def in_my_area(self,click_x,click_y):#检测点击是否在自己范围内
        if (self.cmpx+self.new_editor.center_x-click_x)**2+(self.cmpy+self.new_editor.center_y-click_y)**2<=self.radius**2:
            return 1
        return 0
    
    def delete(self):
        self.new_editor.rander_target.delete(self.circle)
        self.new_editor.rander_target.delete(self.text)
    def follow(self,x,y):
        self.cmpx=x-self.new_editor.center_x
        self.cmpy=y-self.new_editor.center_y
        self.circle=self.new_editor.rander_target.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill="blue")
        self.text=self.new_editor.rander_target.create_text(x,y,text=self.num)
        for i in self.inlayer:
            i.delete()
            i.draw_my_self()
        for i in self.outlayer:
            i.delete()
            i.draw_my_self()