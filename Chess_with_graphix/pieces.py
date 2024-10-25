from graphix import Window, Text, Point, Rectangle, Line, Circle, Polygon

win = Window("The pieces", 600, 600)


def Pawn():
    ''' For a more complicated pawn design
    pawn_head = Circle(Point(103, 95), 5)    
    points = [Point(100, 100), Point(106, 100), Point(110, 120), Point(95, 120)]
    body = Polygon(points)
    base = Rectangle(Point(95, 120), Point(110, 123))
    body.draw(win)
    pawn_head.draw(win)
    base.draw(win)
    '''
    pawn_head = Circle(Point(100, 95), 14)
    pawn_text = Text(Point(100, 95), "P")
    pawn_text.size = 8
    pawn_head.draw(win)
    pawn_text.draw(win)

def King():
    points = [Point(100, 100), Point(108, 90), Point(116, 100), Point(116, 120), Point(100, 120)]
    body = Polygon(points)
    body.draw(win)
    king_text = Text(Point(108, 105), "K")
    king_text.size = 8
    king_text.draw(win)
    
def Queen():
    points = [Point(100, 100), Point(108, 104), Point(116, 100), Point(116, 120), Point(100, 120)]
    body = Polygon(points)
    body.draw(win)
    queen_text = Text(Point(108, 112), "Q")
    queen_text.size = 8
    queen_text.draw(win)
    
            
def Bishop():
    points = [Point(100, 100), Point(108, 90), Point(116, 100), Point(116, 110), Point(100, 110)]
    body = Polygon(points)
    body.draw(win)
    bishop_text = Text(Point(108, 104), "B")
    bishop_text.size = 8
    bishop_text.draw(win)
    
        
def Knight():
    points = [Point(100, 100), Point(116, 90), Point(116, 120), Point(100, 120)]
    body = Polygon(points)
    body.draw(win)
    knight_text = Text(Point(108, 105), "Kn")
    knight_text.size = 8
    knight_text.draw(win)
    
        
def Rook():
    body = Rectangle(Point(100, 100), Point(116, 120))
    body.draw(win)
    rook_text = Text(Point(108, 110), "R")
    rook_text.size = 8
    rook_text.draw(win)
    
