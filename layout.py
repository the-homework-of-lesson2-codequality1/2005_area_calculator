import tkinter
def create_button(root,x1,y1,width1,height1,text1,fg1,function):
    btn = tkinter.Button(root,text = text1,font = ('微软雅黑',20),fg = (fg1),bd = 0.5,command=function)
    btn.place(x = x1,y = y1,width = width1,height = height1)
    return btn
def create_main_label(root,anchor1,textvariable1,width1,height1,y1):
    label= tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',
fg = '#828282',anchor=anchor1,textvariable = textvariable1)
    label.place(width=width1,height=height1,y=y1)
    return label
def create_radiobutton(root, text1, variable1,function,x1,y1,pack):
    if(pack==0):
       figure_r1 = tkinter.Radiobutton(root, text=text1,variable=variable1, value=text1,command=function)
       figure_r1.place(x=x1,y=y1)
    if(pack==1):
       figure_r1 = tkinter.Radiobutton(root, text=text1,variable=variable1, value=text1,command=function)
       figure_r1.pack()