import tkinter 
import calculate
import layout
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

def create_number_button(root,x1,y1,width1,height1,number1,fg1):
   btn = tkinter.Button(root,text = number1,font = ('微软雅黑',20),fg = (fg1),bd = 0.5)
   btn.configure(command=lambda:add_number(number1))
   btn.place(x = x1,y = y1,width = width1,height = height1)
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
      return
   for x in input_text:
      if(x=='.'):
          count=count+1
   if(count>=1):
      return
   input_text=input_text+(str(number1))
   result.set(input_text)
def unit_selection():
    reset()
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
    reset()
    show_hint()
def clear():
  global input_text
  reset()
  input_text=''
  result.set('')
def confirm(unit_var,figure_var):
   global length1_flag,length2_flag,reset_flag,input_text,input_text_save
   font_size=20
   if(reset_flag==1):
          reset()
   elif(check(input_text)==0):
       return
   elif(figure_var=='□'and length1_flag==0):
         hint.set("边长为"+input_text+unit_var+"的"+"正方形面积为")
         font_size=13      
         result.set(calculate.square_area_calculator(unit_var,input_text))
         reset_flag=1
   elif(figure_var=='█' and length1_flag==1):
         hint.set("长为"+input_text_save+"宽为"+input_text+unit_var+"的"+"长方形面积为")
         font_size=13  
         result.set(calculate.rectangle_area_calculator(unit_var,input_text,input_text_save))
         reset_flag=1
         length1_flag=0
   elif(figure_var=='█' and length1_flag==0):
         hint.set("请输入宽")
         input_text_save=input_text
         font_size=20  
         input_text=''
         result.set('')
         length1_flag=1
   elif(figure_var=='△' and length1_flag==1):
         hint.set("底为"+input_text_save+"高为"+input_text+unit_var+"的"+"三角形面积为")
         font_size=13  
         result.set(calculate.triangle_area_calculator(unit_var,input_text,input_text_save))
         reset_flag=1
         length1_flag=0
   elif(figure_var=='△' and length1_flag==0):
         hint.set("请输入高")
         input_text_save=input_text
         font_size=20
         input_text=''
         result.set('')
         length1_flag=1
   elif(figure_var=='○'and length1_flag==0):
         hint.set("直径为"+input_text+unit_var+"的"+"圆面积为")
         font_size=13  
         result.set(calculate.circular_area_calculator(unit_var,input_text))
         reset_flag=1
   label_hint.configure(font=('微软雅黑',font_size))
def reset():
   global reset_flag,length1_flag,length2_flag,input_text,input_text_save,figure_var,result
   if(reset_flag==1):
          length1_flag=0
          length2_flag=0
          label_hint['font']=('微软雅黑',20)
          show_hint()
          input_text=''
          input_text_save=''
          reset_flag=0
          result.set('')
          return
       
unit_label=tkinter.Label(root,bg='blue',width=20,text='Choose unit')
unit_label.pack()
unit_var=tkinter.StringVar()
layout.create_radiobutton(root, 'cm', unit_var,unit_selection,0,0,1)
layout.create_radiobutton(root, 'inch', unit_var,unit_selection,0,0,1)
unit_var.set('cm')
unit_selection()
figure_label=tkinter.Label(root,bg='blue',width=20,text='Choose figure')
figure_label.pack()
figure_var=tkinter.StringVar()
layout.create_radiobutton(root, '□', figure_var,figure_selection,85,100,0)
layout.create_radiobutton(root, '█', figure_var,figure_selection,130,100,0)
layout.create_radiobutton(root, '△', figure_var,figure_selection,85,120,0)
layout.create_radiobutton(root, '○', figure_var,figure_selection,130,120,0)
figure_var.set('□')
figure_selection()
label_hint=layout.create_main_label(root,'e',hint,280,60,155)
label_input=layout.create_main_label(root,'se',result,280,60,225)

for i in range(3):
  for j in range(3):
     create_number_button(root,70*j,285+55*i,70,55,7-3*i+j,'#4F4F4F') 

create_number_button(root,70,285+55*3,70,55,0,'#4F4F4F')

button_confirm = tkinter.Button(root,text = '确认',bg = 'orange',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command=lambda:confirm(unit_var.get(),figure_var.get()))
button_confirm.place(x = 210,y = 285,width = 70,height = 220)
button_clear = tkinter.Button(root,text = 'AC',font = ('微软雅黑',20),fg =('#4F4F4F'),bd = 0.5,command=lambda:clear())
button_clear.place(x = 0,y = 450,width = 70,height = 55)
button_dot = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command=lambda:add_dot('.'))
button_dot.place(x = 140,y = 450,width = 70,height = 55)
root.mainloop()


