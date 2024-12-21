from graphix import Window, Text, Point, Rectangle, Line, Circle, Polygon

def main():
    turn = 0
    win = Window("Chess", 600, 600)
    chess_board(win)
    draw_initial_pieces(win)
    
    while True:
        tile_x, tile_y = user_click(win)
        selected_tile(win, tile_x, tile_y)
        piece_x, piece_y = tile_x + 43, tile_y + 43
        print(piece_x, piece_y)
        
    

def user_click(win):
    click = win.get_mouse()
    tile_x, tile_y = click.x//75 * 75, click.y//75 * 75
    print(tile_x, tile_y)
    return tile_x, tile_y
    
    
def chess_board(win):
    for y in range(0,600, 75):
        for x in range(0, 600, 75):
            top_left = Point(x, y)
            bottom_right = Point(x+75, y+75)
            rec = Rectangle(top_left, bottom_right)
            rec.draw(win)
            
            if y % 2 == 0 and x % 2 == 0:
                rec.fill_colour = "white"
            elif y % 2 != 0 and x % 2 != 0:            
                rec.fill_colour = "white"
            else:
                rec.fill_colour = "grey"
            
def draw_initial_pieces(win):
    drawn_pieces = []
    piece_colour = ""
    text_colour = ""
    count = 0
    x = 0
    middle = 43
    pieces_setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    for y in range(0, 600, 75):
        x = 0
        if y > 150:
            piece_colour = "white"
            text_colour = "black"
        else:
            piece_colour = "black"
            text_colour = "white"
        
        if y in (0, 525):
            for piece in pieces_setup:
                piece(x + middle, y+ middle, win, piece_colour, text_colour)
                drawn_pieces.append(piece)
                x+= 75
        if y in (75, 450):
             for piece in range(8):
                Pawn(x + middle, y+ middle, win, piece_colour, text_colour)
                drawn_pieces.append(Pawn)
                x+= 75
        
        
    return drawn_pieces

def selected_tile(win, x, y):
    rec = Rectangle(Point(x, y), Point(x + 75, y + 75))
    rec.outline_width = 5
    rec.draw(win)
    

def Pawn(x, y, win, piece_colour, text_colour):
    pawn_head = Circle(Point(x, y), 14)
    pawn_text = Text(Point(x, y), "P")
    pawn_head.fill_colour = piece_colour
    pawn_head.outline_colour = "black"
    pawn_text.size = 8
    pawn_text.fill_colour = text_colour
    pawn_head.draw(win)
    pawn_text.draw(win)

def Rook(x, y, win, piece_colour, text_colour):
    body = Rectangle(Point(x - 16, y - 16), Point(x + 16, y + 10))                
    rook_text = Text(Point(x, y), "R")
    body.fill_colour = piece_colour
    body.draw(win)
    rook_text.size = 8
    rook_text.fill_colour = text_colour
    rook_text.draw(win)
    
def Knight(x, y, win, piece_colour, text_colour):
    points = [Point(x - 10, y - 10), Point(x + 16, y - 20), Point(x + 16, y + 20), Point(x - 10, y + 20)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    knight_text = Text(Point(x, y), "Kn")
    knight_text.size = 8
    knight_text.fill_colour = text_colour
    knight_text.draw(win)

def Bishop(x, y, win, piece_colour, text_colour):
    points = [Point(x - 12, y - 10), Point(x + 3, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 15), Point(x - 12, y + 15)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    bishop_text = Text(Point(x + 2, y), "B")
    bishop_text.size = 8
    bishop_text.fill_colour = text_colour
    bishop_text.draw(win)

def Queen(x, y, win, piece_colour, text_colour):
    points = [Point(x - 10, y - 12), Point(x + 3, y - 7), Point(x + 16, y  -12), Point(x + 16, y + 20), Point(x - 10, y + 20)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    queen_text = Text(Point(x + 2, y + 2), "Q")
    queen_text.size = 8
    queen_text.fill_colour = text_colour
    queen_text.draw(win)

def King(x, y, win, piece_colour, text_colour):
    points = [Point(x - 10, y - 10), Point(x + 4, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 20), Point(x - 10,y + 20)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    king_text = Text(Point(x + 2, y), "K")
    king_text.size = 8
    king_text.fill_colour = text_colour
    king_text.draw(win)

main()
