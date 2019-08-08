import tkinter 
root=tkinter.Tk()
root.minsize(280,500)
root.title('area_calculator')
input_text=''
input_text_save=''
result=tkinter.StringVar()
result.set('')
hint=tkinter.StringVar()
hint.set('')
length1_flag=0
reset_flag=0

def add_number(number1):
   global input_text
   input_text=input_text+(str(number1))
   result.set(input_text)
   reset()
def add_dot(number1):
   global input_text
   reset()
   count=0
   if(input_text==''):
      return;
   for x in input_text:
      if(x=='.'):
          count=count+1
   if(count>=1):
      return;
   input_text=input_text+(str(number1))
   result.set(input_text)
def create_number_button(x1,y1,width1,height1,number1,fg1):
   btn = tkinter.Button(root,text = number1,font = ('微软雅黑',20),fg = (fg1),bd = 0.5,command=lambda:add_number(number1))
   btn.place(x = x1,y = y1,width = width1,height = height1)
def unit_selection():
    reset();
    unit_label.config(text='you have chosed '+unit_var.get())

def check(text):
    if(text==''):
       return 0
    elif(text[len(text)-1]=='.'):
       return 0
    else:
       return 1
def show_hint():
    figure_label.config(text='you have chosed '+figure_var.get())
    if( figure_var.get()=='□'):
       hint.set("请输入边长")
    if( figure_var.get()=='█'):
       hint.set("请输入长")
    if( figure_var.get()=='△'):
       hint.set("请输入底")
    if( figure_var.get()=='○'):
       hint.set("请输入直径")
def figure_selection():
    reset();
    show_hint();
def clear():
  global input_text
  reset()
  input_text=''
  result.set('')
def confirm(unit_var,figure_var):
   global length1_flag,length2_flag,reset_flag,input_text,input_text_save
   if(reset_flag==1):
          reset()
   elif(check(input_text)==0):
       return
   elif(figure_var=='□'and length1_flag==0):
         hint.set("边长为"+input_text+unit_var+"的"+"正方形面积为")
         label_hint['font']=('微软雅黑',13)
         result.set(square_area_calculator(unit_var,input_text))
         reset_flag=1
   elif(figure_var=='█' and length1_flag==1):
         hint.set("长为"+input_text_save+"宽为"+input_text+unit_var+"的"+"长方形面积为")
         label_hint['font']=('微软雅黑',13)
         result.set(rectangle_area_calculator(unit_var,input_text,input_text_save))
         reset_flag=1
         length1_flag=0
   elif(figure_var=='█' and length1_flag==0):
         hint.set("请输入宽")
         input_text_save=input_text
         input_text=''
         result.set('')
         length1_flag=1
   elif(figure_var=='△' and length1_flag==1):
         hint.set("底为"+input_text_save+"高为"+input_text+unit_var+"的"+"三角形面积为")
         label_hint['font']=('微软雅黑',13)
         result.set(triangle_area_calculator(unit_var,input_text,input_text_save))
         reset_flag=1
         length1_flag=0
   elif(figure_var=='△' and length1_flag==0):
         hint.set("请输入高")
         input_text_save=input_text
         input_text=''
         result.set('')
         length1_flag=1
   elif(figure_var=='○'and length1_flag==0):
         hint.set("直径为"+input_text+unit_var+"的"+"圆面积为")
         label_hint['font']=('微软雅黑',13)
         result.set(circular_area_calculator(unit_var,input_text))
         reset_flag=1
def reset():
   global reset_flag,length1_flag,length2_flag,input_text,input_text_save,figure_var,result
   if(reset_flag==1):
          length1_flag=0
          length2_flag=0
          label_hint['font']=('微软雅黑',20)
          show_hint();
          input_text=''
          input_text_save=''
          reset_flag=0
          result.set('')
          return
def square_area_calculator(unit,input_text):
    if unit == 'cm':
            square_length = float(input_text)
            return "%.3f" % float(square_length*square_length)
    elif unit == 'inch':
            square_length = float(input_text)
            return "%.3f" % float(square_length*square_length/6.4516)
            
def rectangle_area_calculator(unit,input_text,input_text_save):
    if unit == 'cm':
            rectangle_length = float(input_text_save)
            rectangle_width = float(input_text)
            return "%.3f" % float(rectangle_length*rectangle_width)
    elif unit == 'inch':
            rectangle_length = float(input_text_save)
            rectangle_width = float(input_text)
            return "%.3f" % float(rectangle_length*rectangle_width/6.4516)
            
def triangle_area_calculator(unit,input_text,input_text_save):
    if unit == 'cm':
            triangle_base = float(input_text_save)
            triangle_height = float(input_text)
            return "%.3f" % float(triangle_base*triangle_height/2)
    elif unit == 'inch':
            triangle_base = float(input_text_save)
            triangle_height = float(input_text)
            return "%.3f" % float(triangle_base*triangle_height/2/6.4516)
def circular_area_calculator(unit,input_text):
    if unit == 'cm':
            circular_radius = float(input_text)
            return "%.3f" % float(circular_radius*circular_radius*3.14*0.25)
    elif unit == 'inch':
            circular_radius = float(input_text)
            return "%.3f" % float(circular_radius*circular_radius*3.14*0.25/6.4516)
         
unit_label=tkinter.Label(root,bg='blue',width=20,text='Choose unit')
unit_label.pack()
unit_var=tkinter.StringVar()
unit_r1 = tkinter.Radiobutton(root, text='cm', variable=unit_var, value='cm',command=unit_selection)
unit_r1.pack()
unit_r2 = tkinter.Radiobutton(root, text='inch', variable=unit_var, value='inch',command=unit_selection)
unit_r2.pack()
unit_var.set('cm')
unit_selection()
figure_label=tkinter.Label(root,bg='blue',width=20,text='Choose figure')
figure_label.pack()
figure_var=tkinter.StringVar()
figure_r1 = tkinter.Radiobutton(root, text='□',variable=figure_var, value='□',command=figure_selection)
figure_r1.place(x=85,y=100)
figure_r2 = tkinter.Radiobutton(root, text='█', variable=figure_var, value='█',command=figure_selection)
figure_r2.place(x=130,y=100)
figure_r3 = tkinter.Radiobutton(root, text='△', variable=figure_var, value='△',command=figure_selection)
figure_r3.place(x=85,y=120)
figure_r4 = tkinter.Radiobutton(root, text='○', variable=figure_var, value='○',command=figure_selection)
figure_r4.place(x=130,y=120)
figure_var.set('□')
figure_selection()
label_hint= tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',
fg = '#828282',anchor='e',textvariable = hint)
label_hint.place(width=280,height=60,y=155)
label_input=tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',
fg = '#828282',anchor = 'se',textvariable = result)
label_input.place(y=225,width=280,height=60)

for i in range(3):
  for j in range(3):
     create_number_button(70*j,285+55*i,70,55,7-3*i+j,'#4F4F4F')
  create_number_button(70,285+55*3,70,55,0,'#4F4F4F')

btnequ = tkinter.Button(root,text = '确认',bg = 'orange',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command=lambda:confirm(unit_var.get(),figure_var.get()))
btnequ.place(x = 210,y = 285,width = 70,height = 220)
btnac = tkinter.Button(root,text = 'AC',font = ('微软雅黑',20),fg =('#4F4F4F'),bd = 0.5,command=lambda:clear())
btnac.place(x = 0,y = 450,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command=lambda:add_dot('.'))
btnpoint.place(x = 140,y = 450,width = 70,height = 55)

root.mainloop()


