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
