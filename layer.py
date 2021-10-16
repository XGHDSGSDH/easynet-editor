from tkinter import *


class layer:
    def __init__(self, x, y, name, front, end, num, neweditor):
        self.new_editor = neweditor
        self.radius = 30
        self.cmpx = x - self.new_editor.center_x
        self.cmpy = y - self.new_editor.center_y
        self.front = front  # 起点
        self.end = end  # 终点
        self.type = name  # 类型
        self.num = num  # 编号
        self.circle = self.new_editor.rander_target.create_oval(x - self.radius, y - self.radius, x + self.radius,
                                                                y + self.radius, fill="orange")
        self.text = self.new_editor.rander_target.create_text(x, y, text=name)
        self.arrow1 = draw_line1(self)
        self.arrow2 = draw_line2(self)
        # 这里调用了别的类中的函数之后可以修改一下

    def draw_my_self(self):  # 重新画自己的圆和字和箭头
        self.circle = self.new_editor.rander_target.create_oval(self.cmpx + self.new_editor.center_x - self.radius,
                                                                self.cmpy + self.new_editor.center_y - self.radius,
                                                                self.new_editor.center_x + self.cmpx + self.radius,
                                                                self.cmpy + self.new_editor.center_y + self.radius,
                                                                fill="orange")
        self.text = self.new_editor.rander_target.create_text(self.cmpx + self.new_editor.center_x,
                                                              self.cmpy + self.new_editor.center_y, text=self.type)
        self.arrow1 = draw_line1(self)
        self.arrow2 = draw_line2(self)

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
        self.circle = self.new_editor.rander_target.create_oval(x - self.radius, y - self.radius, x + self.radius,
                                                                y + self.radius, fill="orange")
        self.text = self.new_editor.rander_target.create_text(x, y, text=self.type)
        self.arrow1 = draw_line1(self)
        self.arrow2 = draw_line2(self)


def draw_line1(layera):
    # print("fuck")
    x1 = layera.cmpx + layera.new_editor.center_x
    y1 = layera.cmpy + layera.new_editor.center_y
    xs = layera.new_editor.vector_tensor[layera.front - 1].cmpx + layera.new_editor.center_x
    ys = layera.new_editor.vector_tensor[layera.front - 1].cmpy + layera.new_editor.center_y
    if (xs - x1) ** 2 + (ys - y1) ** 2 <= layera.radius + layera.new_editor.vector_tensor[layera.front - 1].radius:
        return 0
    k = ((ys - y1) ** 2 + (xs - x1) ** 2) ** 0.5
    return layera.new_editor.rander_target.create_line(
        (xs + (x1 - xs) / k * layera.new_editor.vector_tensor[layera.front - 1].radius,
         ys + (y1 - ys) / k * layera.new_editor.vector_tensor[layera.front - 1].radius,
         x1 - (x1 - xs) / k * layera.radius,
         y1 - (y1 - ys) / k * layera.radius),
        arrow=LAST)


def draw_line2(layera):
    x1 = layera.cmpx + layera.new_editor.center_x
    y1 = layera.cmpy + layera.new_editor.center_y
    xe = layera.new_editor.vector_tensor[layera.end - 1].cmpx + layera.new_editor.center_x
    ye = layera.new_editor.vector_tensor[layera.end - 1].cmpy + layera.new_editor.center_y
    if (xe - x1) ** 2 + (ye - y1) ** 2 <= layera.radius + layera.new_editor.vector_tensor[layera.end - 1].radius:
        return 0
    k = ((ye - y1) ** 2 + (xe - x1) ** 2) ** 0.5
    return layera.new_editor.rander_target.create_line(
        (xe + (x1 - xe) / k * layera.new_editor.vector_tensor[layera.end - 1].radius,
         ye + (y1 - ye) / k * layera.new_editor.vector_tensor[layera.end - 1].radius,
         x1 - (x1 - xe) / k * layera.radius,
         y1 - (y1 - ye) / k * layera.radius),
        arrow=FIRST)
