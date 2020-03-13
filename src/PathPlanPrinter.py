from PIL import Image, ImageDraw, ImageColor
import time

class PathPlanPrinter():
    def __init__(self, plan=[], input_file="",
                 output_file=""):
        if not plan:
            raise ValueError("Provided plan is empty.")
        if type(plan[0]) is not tuple\
           and type(plan[0]) is not list:
            raise TypeError("Type of points in plan must be"+\
                            " tuple or list.\n"+\
                            "Current type is "+str(type(plan[0])))
        if input_file == "" or type(input_file) is not str:
            raise ValueError("No input file was provided.\n"+\
                             "Unable to print plan.")
        if type(output_file) is not str:
            raise TypeError("Type of output file must be a string.\n"+\
                            "Type of argument provided: "+\
                            str(type(output_file)))
        if output_file == "":
            output_file = input_file.split(".")[0]+\
                  str(time.time())+".png"
        self.plan = plan
        self.img = Image.open(input_file)
        self.img.load()
        self.output_file = output_file
        self.__plan_drawn = False

    def draw_plan(self):
        if self.__plan_drawn:
            return
        img_d = ImageDraw.Draw(self.img)
        img_d.line(self.plan, fill=(155, 0, 100), width=3)
        '''for p in self.plan:
            img_d.ellipse(p, fill=(255, 0, 0))'''
        del img_d
        self.__plan_draw = True

    def print_plan(self):
        if not self.__plan_drawn:
            self.draw_plan()
        self.img.save(self.output_file, "PNG")
        
        
