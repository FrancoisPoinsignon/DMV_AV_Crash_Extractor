t1 = [(1224, 480), (1303, 559)]
t2 = [(1464, 480), (1545, 559)]
t3 = [(2688, 480), (2767, 559)]
t4 = [(2912, 480), (2991, 559)]

height = 125

y_min = [480 + 126*i for i in range(11)] \
      + [480 + 126*10 + 156*i for i in range(1, 3)] \
      + [480 + 126*10 + 156*2 + 126*i for i in range(1, 5)] \
      + [480 + 126*10 + 156*2 + 126*4 + 156] \
      + [480 + 126*10 + 156*2 + 126*4 + 156 + 143] \
      + [480 + 126*10 + 156*2 + 126*4 + 156 + 143 + 126] \
      + [480 + 126*10 + 156*2 + 126*4 + 156 + 143 + 126 + 156*i for i in range(1, 5)] \
      + [480 + 126*10 + 156*2 + 126*4 + 156 + 143 + 126 + 156*4 + 126*i for i in range(1, 3)] \
      + [480 + 126*10 + 156*2 + 126*4 + 156 + 143 + 126 + 156*4 + 126*2 + 156]


y1_min = y_min.copy()
y1_min.pop(18)
y1_min.pop(13)
y1_min.pop(7)

y2_min = y_min.copy()
y2_min.pop(18)


x1_min = 1224
x1_max = 1303

x2_min = 1464
x2_max = 1545

x3_min = 2688
x3_max = 2767

x4_min = 2912
x4_max = 2991

car1_col1 = [(x1_min, x1_max, y_e, y_e + 79) for y_e in y1_min]
car2_col1 = [(x2_min, x2_max, y_e, y_e + 79) for y_e in y1_min]
car1_col2 = [(x3_min, x3_max, y_e, y_e + 79) for y_e in y2_min]
car2_col2 = [(x4_min, x4_max, y_e, y_e + 79) for y_e in y2_min]

