from tkinter import *
from question_window import layer_qw
from question_window import dense_qw
from question_window import relu_qw
from question_window import add_qw


class layer:
    fill_color = "#F9906F"
    text_color = "#FFFFFF"

    def __init__(self, x, y, name, num, neweditor):
        self.new_editor = neweditor
        self.radius = 50
        self.cmpx = x - self.new_editor.center_x
        self.cmpy = y - self.new_editor.center_y
        self.front = 0  # 起点
        self.end = 0  # 终点
        self.type = name  # 类型
        self.qw = 0
        self.num = num  # 编号
        self.state = 1
        self.circle = 0
        self.text = 0
        self.arrow1 = 0
        self.arrow2 = 0
        self.qwget()

    def qwget(self):
        self.qw = layer_qw(self)

    def draw_line(self, vector_tensor, arrow_side):
        x1 = self.cmpx + self.new_editor.center_x
        y1 = self.cmpy + self.new_editor.center_y
        xs = vector_tensor.cmpx + self.new_editor.center_x
        ys = vector_tensor.cmpy + self.new_editor.center_y
        if (xs - x1) ** 2 + (ys - y1) ** 2 <= self.radius + vector_tensor.radius:
            return 0
        k = ((ys - y1) ** 2 + (xs - x1) ** 2) ** 0.5
        return self.new_editor.rander_target.create_line(
            (xs + (x1 - xs) / k * vector_tensor.radius,
             ys + (y1 - ys) / k * vector_tensor.radius,
             x1 - (x1 - xs) / k * self.radius,
             y1 - (y1 - ys) / k * self.radius),
            arrow=arrow_side,
            width=4)

    def draw_my_self(self):  # 重新画自己的圆和字和箭头
        self.circle = self.new_editor.rander_target.create_oval(self.cmpx + self.new_editor.center_x - self.radius,
                                                                self.cmpy + self.new_editor.center_y - self.radius,
                                                                self.new_editor.center_x + self.cmpx + self.radius,
                                                                self.cmpy + self.new_editor.center_y + self.radius,
                                                                fill=layer.fill_color, width=0)
        self.text = self.new_editor.rander_target.create_text(self.cmpx + self.new_editor.center_x,
                                                              self.cmpy + self.new_editor.center_y, text=self.type,
                                                              font=("Consolas", 16), fill=layer.text_color)
        self.arrow1 = self.draw_line(self.new_editor.vector_tensor[self.front-1],LAST)
        self.arrow2 = self.draw_line(self.new_editor.vector_tensor[self.end-1],FIRST)

    def in_my_area(self, click_x, click_y):  # 检测点击是否在自己范围内
        if (self.cmpx + self.new_editor.center_x - click_x) ** 2 + (
                self.cmpy + self.new_editor.center_y - click_y) ** 2 <= self.radius ** 2:
            return 1
        return 0

    def delete(self):
        self.new_editor.rander_target.delete(self.circle)
        self.new_editor.rander_target.delete(self.text)
        self.new_editor.rander_target.delete(self.arrow1)
        self.new_editor.rander_target.delete(self.arrow2)

    def follow(self, x, y):
        self.cmpx = x - self.new_editor.center_x
        self.cmpy = y - self.new_editor.center_y
        self.draw_my_self()

    def printo(self):
        string1 = "cmp.add_" + self.type + "(\"" + str(self.front) + "\",\"" + str(self.end) + "\");\n"
        # cmp.add_relu("x", "x");
        return string1


class dense(layer):
    def __init__(self, x, y, name, num, neweditor):
        layer.__init__(self, x, y, name, num, neweditor)
        self.inlen = 0
        self.outlen = 0

    def qwget(self):
        self.qw = dense_qw(self)

    def printo(self):
        string1 = "dense " + str(self.front) + " " + str(self.end) + " " + str(self.inlen) + " " + str(
            self.outlen) + "\n"
        # cmp.add_dense("x", "x", 784, 100);
        return string1


class relu(layer):
    def __init__(self, x, y, name, num, neweditor):
        layer.__init__(self, x, y, name, num, neweditor)

    def qwget(self):
        self.qw = relu_qw(self)

    def printo(self):
        string1 = "relu " + str(self.front) + " " + str(self.end) + "\n"
        # cmp.add_relu("x", "x");
        return string1


class add(layer):
    def __init__(self, x, y, name, num, neweditor):
        layer.__init__(self, x, y, name, num, neweditor)
        self.arrow3 = 0
        self.front2 = 0

    def qwget(self):
        self.qw = add_qw(self)

    def draw_my_self(self):
        self.circle = self.new_editor.rander_target.create_oval(self.cmpx + self.new_editor.center_x - self.radius,
                                                                self.cmpy + self.new_editor.center_y - self.radius,
                                                                self.new_editor.center_x + self.cmpx + self.radius,
                                                                self.cmpy + self.new_editor.center_y + self.radius,
                                                                fill=layer.fill_color, width=0)
        self.text = self.new_editor.rander_target.create_text(self.cmpx + self.new_editor.center_x,
                                                              self.cmpy + self.new_editor.center_y, text=self.type,
                                                              font=("Consolas", 16), fill=layer.text_color)
        self.arrow1 = self.draw_line(self.new_editor.vector_tensor[self.front-1], LAST)
        self.arrow2 = self.draw_line(self.new_editor.vector_tensor[self.end-1], FIRST)
        self.arrow3 = self.draw_line(self.new_editor.vector_tensor[self.front2-1], LAST)

    def delete(self):
        self.new_editor.rander_target.delete(self.circle)
        self.new_editor.rander_target.delete(self.text)
        self.new_editor.rander_target.delete(self.arrow1)
        self.new_editor.rander_target.delete(self.arrow2)
        self.new_editor.rander_target.delete(self.arrow3)
