


class Toolbox:
    def __init__(self ):

        self.tools=[]

    def ToolAdd(self,tool):
        self.tools.append(tool)

    def ToolRemove(self,tool):
        try:
            self.tools.remove(tool)

        except ValueError:
            print(" these tool doesn't exist")



class Hammer:

    def __init__(self, color):
        self.color=color
        


    def planter(self):
        pass


    def remove(self):
        pass


    def changeColor(self,color):
        self.color=color

   

class screwdriver:
    
    def __init__(self, height):
        self.height=height

    def serrer(self):
        pass

    def remove(self):
        pass