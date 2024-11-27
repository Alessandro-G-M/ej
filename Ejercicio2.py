class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y

  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y

  def reset(self):
    self.x = 0
    self.y = 0

  def compute_distance(self, point: "Point") -> float:
    distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
    return distance



class Rectangle:
    def __init__(self, bottom_left_corner:Point,height:float,width:float):
        self.height = height
        self.width = width
        
        
    def compute_area(self) -> float:
        return self.height * self.width
    
    
    def compute_perimeter(self) -> float:
        return 2*(self.height + self.width)
    
    
class Square(Rectangle):
    
    def __init__(self, bottom_left_corner: Point, side_lenght:float):
      super().__init__(bottom_left_corner, height=side_lenght, width=side_lenght)
       
       
       
    def compute_interference(self, point:Point) -> bool:
    
              
      inside_x = self.x <= point.x <= self.x + self.width
        
      inside_y = self.y <= point.y <= self.x + self.height
        
      return inside_x and inside_y
        
          
class Line:
  
  def __init__(self, start:Point,end:Point):
    self.start = start
    self.end = end
    
  def compute_length(self) -> float:
    return (((self.end.y - self.start.y)**2)+((self.end.x - self.start.x)**2))**0.5
  
  def compute_slope(self):
    if self.end.x == self.start.x:
      return 'La linea es vertical'
    elif self.end.y == self.start.y:
      return 'La linea es horizontal'
    return(self.end.y - self.start.y)/(self.end.x - self.start.x)
  
  def compute_horizontal_cross(self) -> bool:
    return (self.start.y <= 0 and self.end.y >= 0) or(self.end.y <= 0 and self.start.y >= 0)
  
  def compute_vertical_cross(self) -> bool:
    return (self.start.x <= 0 and self.end.x >= 0) or(self.end.x <= 0 and self.start.x >= 0)
    


class Rectangle_Lines:
  
  def __init__(self, bottom_left_corner:Point, height:float, width:float):
    self.height = height
    self.width = width
      
    #* Definir los puntos
    self.bottom_left_corner = bottom_left_corner
    self.top_left_corner = Point(bottom_left_corner.x,bottom_left_corner.y+height)
    self.top_right_corner = Point(bottom_left_corner.x + width,bottom_left_corner.y+height)
    self.bottom_right_corner = Point(bottom_left_corner.x + width, bottom_left_corner.y)
    
    
    #* Define los segmentos del Rectangulo
    self.bottom_edge = Line(self.bottom_left_corner,self.bottom_right_corner)
    self.left_edge = Line(self.bottom_left_corner,self.top_left_corner)
    self.right_edge = Line(self.bottom_right_corner,self.top_right_corner)
    self.top_edge = Line(self.top_left_corner,self.top_right_corner)
        
        
  def compute_area(self) -> float:
    return self.height * self.width
    
    
  def compute_perimeter(self) -> float:
    return 2*(self.height + self.width)



   
    
a = Line(Point(10,2),Point(1,2))

rec = Rectangle_Lines(Point(0,2),Point(5,10))

print(a.compute_horizontal_cross())

print(rec.line1)     
