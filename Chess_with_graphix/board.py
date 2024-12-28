from graphix import Window, Text, Point, Rectangle, Line, Circle, Polygon
currently_selected_tile = []


def main():
    
    turn = 0
    binary_turn = 0
    win = Window("Chess", 600, 600)
    
    chess_board(win)
    chess_object, chess_piece = draw_initial_pieces(win)
    
    
    
    while True:
        if turn % 2 == 0:
            print("White's turn")
            binary_turn = 0

        else:
            print("black's turn")
            binary_turn = 1
        print(currently_selected_tile)
        tile_x, tile_y = user_click(win)
        for pattern in currently_selected_tile:
               pattern.undraw()
               currently_selected_tile.pop()
        selected_tile(win, tile_x, tile_y)
        
        print(chess_object)
        
        move_x, move_y = user_click(win)
        print("tile", tile_y, "move", move_y)
        
        if (tile_x, tile_y) in chess_object:
            chess_piece = chess_object[(tile_x, tile_y)]
            
            if (move_x, move_y) not in chess_object:
                
                
                content = str(chess_piece[-1])
                piece_letter = str(content.strip()[-4:-2])
                print(piece_letter)
                if is_valid(piece_letter, tile_x, move_x,  tile_y ,move_y):
                    print("valid move")
                else:
                    print("Invalid move")
                    continue
                chess_object.pop((tile_x, tile_y))
                chess_piece[0].move(move_x - tile_x, move_y - tile_y)
                chess_piece[1].move(move_x - tile_x, move_y - tile_y)
                chess_object[(move_x, move_y)] = chess_piece
            

        turn += 1
        
        
    
        
        
    

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
                rec.fill_colour = "brown"
            
def draw_initial_pieces(win):
    piece_colour = ""
    text_colour = ""
    piece_type = ''
    count = 0
    x = 0
    middle = 43
    grid_objects = {}
    pieces_setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    for y in range(0, 600, 75):
        
        
        x = 0
        if y > 150:
            piece_colour = "white"
            text_colour = "black"
            piece_type = 'W'
        else:
            piece_colour = "black"
            text_colour = "white"
            piece_type = 'B'
        
        if y in (0, 525):
            for piece in pieces_setup:
                chess_piece = piece(x + middle, y+ middle, win, piece_colour, text_colour, piece_type)
                #drawn_pieces.append(piece(x + middle, y+ middle, win, piece_colour, text_colour))
                grid_objects[(x, y)] = chess_piece
                
                x+= 75
                
        if y in (75, 450):
             for piece in range(8):
                pawn_piece = Pawn(x + middle, y+ middle, win, piece_colour, text_colour, piece_type)
                #drawn_pieces.append(Pawn(x + middle, y+ middle, win, piece_colour, text_colour)) 
                grid_objects[(x, y)] = pawn_piece
                x+= 75

        
        
    return grid_objects, chess_piece

def selected_tile(win, x, y):
    rec = Rectangle(Point(x, y), Point(x + 75, y + 75))
    rec.outline_width = 5
    rec.draw(win)
    currently_selected_tile.append(rec)
    #key = win.get_key()
    #if key == "right":
       # rec.undraw()
    
def is_valid(piece_letter, x1, x2, y1, y2):
    if piece_letter == "WP":
        return x1 == x2 and y2 == y1 - 75
    if piece_letter == "BP":
        return x1 == x2 and y2 == y1 + 75





def Pawn(x, y, win, piece_colour, text_colour, piece_type):
    pawn_head = Circle(Point(x, y), 14)
    pawn_text = Text(Point(x, y), f"{piece_type}P")
    pawn_head.fill_colour = piece_colour
    pawn_head.outline_colour = "black"
    pawn_text.size = 8
    pawn_text.fill_colour = text_colour
    pawn_head.draw(win)
    pawn_text.draw(win)

    return pawn_head, pawn_text

def Rook(x, y, win, piece_colour, text_colour, piece_type):
    body = Rectangle(Point(x - 16, y - 16), Point(x + 16, y + 10))                
    rook_text = Text(Point(x, y), f"{piece_type}R")
    body.fill_colour = piece_colour
    body.draw(win)
    rook_text.size = 8
    rook_text.fill_colour = text_colour
    rook_text.draw(win)

    return body, rook_text
    
def Knight(x, y, win, piece_colour, text_colour, piece_type):
    points = [Point(x - 10, y - 10), Point(x + 16, y - 20), Point(x + 16, y + 20), Point(x - 10, y + 20)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    knight_text = Text(Point(x, y), f"{piece_type}H")
    knight_text.size = 8
    knight_text.fill_colour = text_colour
    knight_text.draw(win)

    return body, knight_text

def Bishop(x, y, win, piece_colour, text_colour, piece_type):
    points = [Point(x - 12, y - 10), Point(x + 3, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 15), Point(x - 12, y + 15)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    bishop_text = Text(Point(x + 2, y), f"{piece_type}B")
    bishop_text.size = 8
    bishop_text.fill_colour = text_colour
    bishop_text.draw(win)

    return body, bishop_text

def Queen(x, y, win, piece_colour, text_colour, piece_type):
    points = [Point(x - 10, y - 12), Point(x + 3, y - 7), Point(x + 16, y  -12), Point(x + 16, y + 20), Point(x - 10, y + 20)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    queen_text = Text(Point(x + 2, y + 2), f"{piece_type}Q")
    queen_text.size = 8
    queen_text.fill_colour = text_colour
    queen_text.draw(win)

    return body, queen_text

def King(x, y, win, piece_colour, text_colour, piece_type):
    points = [Point(x - 10, y - 10), Point(x + 4, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 20), Point(x - 10,y + 20)]
    body = Polygon(points)
    body.fill_colour = piece_colour
    body.draw(win)
    king_text = Text(Point(x + 2, y), f"{piece_type}K")
    king_text.size = 8
    king_text.fill_colour = text_colour
    king_text.draw(win)

    return body, king_text


main()
