from tkinter import *
from tkinter import filedialog
import tkinter.ttk
from tensor import tensor
from layer import layer
from layer import dense
from layer import relu
from layer import add
import tkinter.messagebox


class editor:
    button_back_color = "#D3E0F3"
    button_fg_color = "#395260"
    canvas_background = "#D1D9E0"

    def __init__(self, x_pos, y_pos, tkwindow):
        self.window = tkwindow

        # 显示器
        self.rander_target = Canvas(self.window, width=200 + self.window.winfo_width(),
                                    height=200 + self.window.winfo_height(), background=editor.canvas_background)
        self.rander_target.grid(row=1, column=0, rowspan=100, columnspan=100)
        self.rander_target.bind("<Button-1>", self.press_down)
        self.rander_target.bind("<Double-Button-1>", self.double_press_down)
        self.rander_target.bind("<ButtonRelease-3>", self.delete_sth)
        self.rander_target.bind("<B1-Motion>", self.press_motion)
        self.rander_target.bind("<ButtonRelease-1>", self.press_up)

        # tensor按钮
        self.btn_tensor = Button(self.window, activeforeground="black", text="加入点", font=("Microsoft YaHei UI", 16),
                                 bg=editor.button_back_color, fg=editor.button_fg_color)
        self.btn_tensor.grid(row=0, column=0)
        self.btn_tensor.bind("<Button-1>", self.add_tensor)

        # layer列表
        self.layer_combobox = tkinter.ttk.Combobox(self.window, width=35, height=30,
                                                   values=['选择Layer', 'add', 'batch norm', 'conv', 'dense', 'dropout',
                                                           'fast_sig', 'fast_tan', 'flatten', 'hadamard', 'leaky_relu',
                                                           'relu'])
        self.layer_combobox.current(3)
        self.layer_combobox.grid(row=0, column=1)

        # layer按钮
        self.btn_layer = Button(self.window, activeforeground="black", text="加入边", font=("Microsoft YaHei UI", 16),
                                bg=editor.button_back_color, fg=editor.button_fg_color)
        self.btn_layer.grid(row=0, column=2)
        self.btn_layer.bind("<Button-1>", self.add_layer)

        # 输入点输出点
        self.caution_front = Label(self.window, text="输入点")
        self.caution_front.grid(row=0, column=3)
        self.question_front = Entry(self.window)
        self.question_front.grid(row=0, column=4)
        self.question_front.insert(0, "请用空格隔开")
        self.caution_end = Label(self.window, text="输出点")
        self.caution_end.grid(row=0, column=5)
        self.question_end = Entry(self.window)
        self.question_end.grid(row=0, column=6)
        self.question_end.insert(0, "请用空格隔开")

        # 保存按钮
        self.save_button = Button(self.window, activeforeground="black", text="保存", font=("Microsoft YaHei UI", 16),
                                  bg=editor.button_back_color, fg=editor.button_fg_color)
        self.save_button.grid(row=0, column=7)
        self.save_button.bind("<ButtonRelease-1>", self.save_structure)

        # 相对坐标系坐标
        self.center_x = x_pos
        self.center_y = y_pos

        # tensor list,layer list
        self.vector_tensor = []
        self.tensor_num = 0
        self.vector_layer = []
        self.layer_num = 0
        # state
        self.state = 0
        self.now_pressed = 0

        # 拖动时暂时坐标
        self.register_x = 0
        self.register_y = 0

    def add_tensor(self, event):
        if self.state == -1:
            return
        self.window.update()
        self.tensor_num += 1
        self.vector_tensor.append(tensor(self.window.winfo_x() + self.window.winfo_width() / 2,
                                         self.window.winfo_y() + self.window.winfo_height() / 2, self.tensor_num, self))
        print("Successfully added a tensor")

    def add_layer(self, event):
        if self.layer_combobox.current() == 3 or self.layer_combobox.current() == -1:
            return
        if self.state == -1:
            return
        print(self.layer_combobox.current())
        self.window.update()
        self.layer_num += 1
        self.state = -1
        self.switch_layer()

    def switch_layer(self):
        if self.layer_combobox.current() == 0:
            self.vector_layer.append(dense(self.window.winfo_x() + self.window.winfo_width() / 2,
                                           self.window.winfo_y() + self.window.winfo_height() / 2,
                                           self.layer_combobox.get(), self.layer_num, self))
        elif self.layer_combobox.current() == 1:
            self.vector_layer.append(relu(self.window.winfo_x() + self.window.winfo_width() / 2,
                                          self.window.winfo_y() + self.window.winfo_height() / 2,
                                          self.layer_combobox.get(), self.layer_num, self))
        elif self.layer_combobox.current() == 2:
            self.vector_layer.append(add(self.window.winfo_x() + self.window.winfo_width() / 2,
                                         self.window.winfo_y() + self.window.winfo_height() / 2,
                                         self.layer_combobox.get(), self.layer_num, self))
        else:
            self.vector_layer.append(layer(self.window.winfo_x() + self.window.winfo_width() / 2,
                                           self.window.winfo_y() + self.window.winfo_height() / 2,
                                           self.layer_combobox.get(), self.layer_num, self))

    def redraw(self):
        self.rander_target.delete(ALL)
        for i in self.vector_tensor:
            if i.state == 1:
                # self.center_x+=100
                i.draw_my_self()
        for i in self.vector_layer:
            if i.state == 1:
                i.draw_my_self()

    def press_down(self, event):
        print("get a press down")
        if self.state == -1:
            return
        self.state = 0
        self.now_pressed = 0
        for i in self.vector_tensor:
            if i.state == 0:
                continue
            if i.in_my_area(event.x, event.y) == 1:
                self.state = 1
                self.now_pressed = i.num
        for i in self.vector_layer:
            if i.state == 0:
                continue
            if i.in_my_area(event.x, event.y) == 1:
                self.state = 2
                self.now_pressed = i.num
        self.register_x = event.x
        self.register_y = event.y
        print(self.state, self.now_pressed)  # 现在的状态和已选中的点的编号

    def double_press_down(self, event):
        print("get a double press down")
        if self.state == -1:
            return
        self.state = 0
        self.now_pressed = 0
        for i in self.vector_layer:
            if i.state == 0:
                continue
            if i.in_my_area(event.x, event.y) == 1:
                self.state = 2
                self.now_pressed = i.num
        print(self.state, self.now_pressed)  # 现在的状态和已选中的点的编号
        if self.state == 2:
            self.state = -1
            self.vector_layer[self.now_pressed - 1].qw.rebutton()

    def press_motion(self, event):
        # print("get a left click motion")
        if self.state == -1:
            return
        if self.state == 0:
            self.center_x += event.x - self.register_x
            self.center_y += event.y - self.register_y
            self.register_x = event.x
            self.register_y = event.y
            self.redraw()
            return
        if self.state == 1:
            self.vector_tensor[self.now_pressed - 1].delete()
            self.vector_tensor[self.now_pressed - 1].follow(event.x, event.y)
            return
        if self.state == 2:
            self.vector_layer[self.now_pressed - 1].delete()
            self.vector_layer[self.now_pressed - 1].follow(event.x, event.y)  # 移动

    def press_up(self, event):
        print("up")  # 抬手

    def delete_sth(self, event):
        print("get a right press down")
        if self.state == -1:
            return
        self.state = 0
        self.now_pressed = 0
        for i in self.vector_tensor:
            if i.state == 0:
                continue
            if i.in_my_area(event.x, event.y) == 1:
                self.state = 1
                self.now_pressed = i.num
        for i in self.vector_layer:
            if i.state == 0:
                continue
            if i.in_my_area(event.x, event.y) == 1:
                self.state = 2
                self.now_pressed = i.num
        self.register_x = event.x
        self.register_y = event.y
        print(self.state, self.now_pressed)  # 现在的状态和已选中的点的编号
        if self.state == 1 and tkinter.messagebox.askyesno(title='删除确认', message="与此tensor有关的边都会被删掉，确定删除此tensor吗？"):
            self.vector_tensor[self.now_pressed - 1].state = 0
            self.vector_tensor[self.now_pressed - 1].delete()
            for i in self.vector_tensor[self.now_pressed - 1].inlayer:
                if i.state == 1:
                    i.state = 0
                    i.delete()
            for i in self.vector_tensor[self.now_pressed - 1].outlayer:
                if i.state == 1:
                    i.state = 0
                    i.delete()

        if self.state == 2 and tkinter.messagebox.askyesno(title='删除确认', message="确定删除这个layer吗？"):
            self.vector_layer[self.now_pressed - 1].state = 0
            self.vector_layer[self.now_pressed - 1].delete()

    def save_structure(self, event):
        filename = filedialog.asksaveasfilename(defaultextension='.easynet', filetypes=[("Easynet files", ".easynet")])
        print(filename)
        summ = 0
        string1 = ""
        for i in self.vector_tensor:
            if i.state == 1:
                string1 = string1 + i.printo()
                summ += 1
        string1 = str(summ) + "\n" + string1 + "\n"
        for i in self.vector_layer:
            if i.state == 1:
                string1 = string1 + i.printo()
        summ = 0
        geshu = 0
        listin = []
        for i in self.question_front.get():
            if i == ' ':
                geshu += 1
                listin.append(summ)
                summ = 0
                continue
            else:
                summ = summ * 10 + int(i)
                print(summ)
        geshu += 1
        listin.append(summ)
        string2 = "input_node " + str(geshu)
        for i in listin:
            string2 = string2 + " " + str(i)
        string2 += "\n"

        summ = 0
        geshu = 0
        listout = []
        for i in self.question_end.get():
            if i == ' ':
                geshu += 1
                listout.append(summ)
                summ = 0
                continue
            else:
                summ = summ * 10 + int(i)
                print(summ)
        geshu += 1
        listout.append(summ)
        string3 = "output_node " + str(geshu)
        for i in listout:
            string3 = string3 + " " + str(i)
        string3 += "\n"
        string1 = string1 + string2 + string3
        with open(filename, 'w') as fl:
            fl.write("Easynet Strcture File:\n")
            fl.write(string1)
