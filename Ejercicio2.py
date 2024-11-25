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



class Rectangle(Point):
    def __init__(self, bottom_left_corner:Point,height:float,width:float):
        
        super().__init__(bottom_left_corner.x, bottom_left_corner.y)

        self.height = height
        
        self.width = width
        
    def compute_area(self) -> float:
        return self.height * self.width
    
    
    def compute_perimeter(self) -> float:
        return (2*self.height)+(2*self.width)
    
    
class Square(Rectangle):
    
    def __init__(self, bottom_left_corner: Point, side_length: float):
        
       super().__init__(bottom_left_corner, height=side_length, width=side_length)
       
       
       
    def compute_interference(self, point:Point) -> bool:
        
        inside_x = self.x <= point.x <= self.x + self.width
        
        inside_y = self.y <= point.y <= self.x + self.height
        
        return inside_x and inside_y
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class Point:
    """
    Representa un punto en el espacio 2D con coordenadas x e y.
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


class Rectangle:
    """
    Representa un rectángulo en el espacio 2D, inicializado con:
    - Un punto (esquina inferior izquierda).
    - Un ancho y una altura.
    """
    def __init__(self, bottom_left_corner: Point, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.bottom_left_corner = bottom_left_corner
        self.width = width
        self.height = height

    def __repr__(self):
        return (f"Rectangle(bottom_left_corner={self.bottom_left_corner}, "
                f"width={self.width}, height={self.height})")

    def area(self) -> float:
        """
        Calcula el área del rectángulo.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calcula el perímetro del rectángulo.
        """
        return 2 * (self.width + self.height)

    def top_right_corner(self) -> Point:
        """
        Devuelve el punto superior derecho del rectángulo.
        """
        return Point(self.bottom_left_corner.x + self.width, 
                     self.bottom_left_corner.y + self.height)

    def contains_point(self, point: Point) -> bool:
        """
        Verifica si un punto está dentro del rectángulo.
        """
        within_x = self.bottom_left_corner.x <= point.x <= self.bottom_left_corner.x + self.width
        within_y = self.bottom_left_corner.y <= point.y <= self.bottom_left_corner.y + self.height
        return within_x and within_y

        
    
    
        
        
      
