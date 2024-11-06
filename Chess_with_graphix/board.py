from graphix import Window, Text, Point, Rectangle, Line, Circle, Polygon

class ChessBoard:
    TILE_SIZE = 66

    def __init__(self):
        self.win = Window("Board", 1200, 800)
        self.draw_board()
        self.draw_tiles()
        self.initialize_pieces()
        self.move_piece()

    def draw_board(self):
        board = Rectangle(Point(200, 100), Point(728, 628))
        board.draw(self.win)

    def draw_tiles(self):
        tile_id = 0
        #colours in the black tiles 
        black_tiles = [1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23, 24, 26, 28, 30, 33, 35, 37, 39, 40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62, 65]
        for row in range(8):
            for col in range(8):
                #builds the board by going through the y axis then moving up 1 in the x axis
                x1 = 200 + col * self.TILE_SIZE
                y1 = 100 + row * self.TILE_SIZE
                x2 = x1 + self.TILE_SIZE
                y2 = y1 + self.TILE_SIZE
                tile = Rectangle(Point(x1, y1), Point(x2, y2))
                if tile_id in black_tiles:
                    tile.fill_colour = "black"
                tile.draw(self.win)
                tile_id += 1

    def initialize_pieces(self):
        #Positions of the white and black pieces
        self.white_positions = {"A2": "PAWN",
                    "B2":"PAWN",
                    "C2": "PAWN",
                    "D2":"PAWN",
                    "E2": "PAWN",
                    "F2":"PAWN",
                    "G2": "PAWN",
                    "H2":"PAWN",
                    "A1": "ROOK",
                    "H1":"ROOK",
                    "B1": "KNIGHT",
                    "G1": "KNIGHT",
                    "C1":"BISHOP",
                    "F1":"BISHOP",
                    "D1":"QUEEN",
                    "E1":"KING",
                    }
        self.black_positions = {"A7": "PAWN",
                    "B7":"PAWN",
                    "C7": "PAWN",
                    "D7":"PAWN",
                    "E7": "PAWN",
                    "F7":"PAWN",
                    "G7": "PAWN",
                    "H7":"PAWN",
                    "A8": "ROOK",
                    "H8":"ROOK",
                    "B8": "KNIGHT",
                    "G8": "KNIGHT",
                    "C8":"BISHOP",
                    "F8":"BISHOP",
                    "D8":"QUEEN",
                    "E8":"KING",}
        
        #Converts single chess notations into pixels co ordinates
        self.notation_to_pixel = {"A": 233,
                             "B": 299,
                             "C": 365,
                             "D": 431,
                             "E": 497,
                             "F": 563,
                             "G": 629,
                             "H": 695,
                             "1": 133,
                             "2": 199,
                             "3": 265,
                             "4": 331,
                             "5": 397,
                             "6": 463,
                             "7": 529,
                             "8": 595}
        #Goes through the white and black dictionaires collecting the chess notations and placing the pieces on the board
        #after converting the chess notation to pixels
        for position, piece_type in self.white_positions.items():
            x =  self.notation_to_pixel.get(position[0])
            y =  self.notation_to_pixel.get(position[1])
            if piece_type == "PAWN":
                pawn_head = Circle(Point(x, y), 14)
                pawn_text = Text(Point(x, y), "P")
                pawn_head.fill_colour = "white"
                pawn_head.outline_colour = "black"
                pawn_text.size = 8
                pawn_head.draw(self.win)
                pawn_text.draw(self.win)
            
            elif piece_type == "ROOK":
                body = Rectangle(Point(x - 16, y - 16), Point(x + 16, y + 10))                
                rook_text = Text(Point(x, y), "R")
                body.fill_colour = "white"
                body.draw(self.win)
                rook_text.size = 8
                rook_text.draw(self.win)
                
            elif piece_type == "KNIGHT":
                points = [Point(x - 10, y - 10), Point(x + 16, y - 20), Point(x + 16, y + 20), Point(x - 10, y + 20)]
                body = Polygon(points)
                body.fill_colour = "white"
                body.draw(self.win)
                knight_text = Text(Point(x, y), "Kn")
                knight_text.size = 8
                knight_text.draw(self.win)
            
            elif piece_type == "BISHOP":
                points = [Point(x - 12, y - 10), Point(x + 3, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 15), Point(x - 12, y + 15)]
                body = Polygon(points)
                body.fill_colour = "white"
                body.draw(self.win)
                bishop_text = Text(Point(x + 2, y), "B")
                bishop_text.size = 8
                bishop_text.draw(self.win)
            
            elif piece_type == "QUEEN":
                points = [Point(x - 10, y - 12), Point(x + 3, y - 7), Point(x + 16, y  -12), Point(x + 16, y + 20), Point(x - 10, y + 20)]
                body = Polygon(points)
                body.fill_colour = "white"
                body.draw(self.win)
                queen_text = Text(Point(x + 2, y + 2), "Q")
                queen_text.size = 8
                queen_text.draw(self.win)
            
            elif piece_type == "KING":
                points = [Point(x - 10, y - 10), Point(x + 4, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 20), Point(x - 10,y + 20)]
                body = Polygon(points)
                body.fill_colour = "white"
                body.draw(self.win)
                king_text = Text(Point(x + 2, y), "K")
                king_text.size = 8
                king_text.draw(self.win)
                

        for position, piece_type in self.black_positions.items():
            x =  self.notation_to_pixel.get(position[0])
            y =  self.notation_to_pixel.get(position[1])
            if piece_type == "PAWN":
                pawn_head = Circle(Point(x, y), 14)
                pawn_text = Text(Point(x, y), "P")
                pawn_head.fill_colour = "black"
                pawn_text.fill_colour = "white"
                pawn_head.outline_colour = "white"
                pawn_text.size = 8
                pawn_head.draw(self.win)
                pawn_text.draw(self.win)
            
            elif piece_type == "ROOK":
                body = Rectangle(Point(x - 16, y - 16), Point(x + 16, y + 10))                
                rook_text = Text(Point(x, y), "R")
                body.fill_colour = "black"
                rook_text.fill_colour = "white"
                body.outline_colour = "white"
                body.draw(self.win)
                rook_text.size = 8
                rook_text.draw(self.win)
            
            elif piece_type == "KNIGHT":  
                points = [Point(x - 10, y - 10), Point(x + 16, y - 20), Point(x + 16, y + 20), Point(x - 10, y + 20)]
                body = Polygon(points)
                body.fill_colour = "black"
                body.outline_colour = "white"
                body.draw(self.win)
                knight_text = Text(Point(x, y), "Kn")
                knight_text.fill_colour = "white"
                knight_text.size = 8
                knight_text.draw(self.win)
                
            elif piece_type == "BISHOP":
                points = [Point(x - 12, y - 10), Point(x + 3, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 15), Point(x - 12, y + 15)]
                body = Polygon(points)
                body.fill_colour = "black"
                body.outline_colour = "white"                
                body.draw(self.win)
                bishop_text = Text(Point(x + 2, y), "B")
                bishop_text.fill_colour = "white"
                bishop_text.size = 8
                bishop_text.draw(self.win)
            
            elif piece_type == "QUEEN":
                points = [Point(x - 10, y - 12), Point(x + 3, y - 7), Point(x + 16, y  -12), Point(x + 16, y + 20), Point(x - 10, y + 20)]
                body = Polygon(points)
                body.fill_colour = "black"
                body.outline_colour = "white"  
                body.draw(self.win)
                queen_text = Text(Point(x + 2, y + 2), "Q")
                queen_text.fill_colour = "white"
                queen_text.size = 8
                queen_text.draw(self.win)
            
            elif piece_type == "KING":
                points = [Point(x - 10, y - 10), Point(x + 4, y - 20), Point(x + 16, y - 10), Point(x + 16, y + 20), Point(x - 10,y + 20)]
                body = Polygon(points)
                body.fill_colour = "black"
                body.outline_colour = "white"  
                body.draw(self.win)
                king_text = Text(Point(x + 2, y), "K")
                king_text.fill_colour = "white"
                king_text.size = 8
                king_text.draw(self.win)

        
 


    

    # TODO: Implement method to handle piece movement
    def move_piece(self):#, from_pos, to_pos
        #check which tile user has clicked, use co ordinates to calculate which tile it is
        #Create a dictionary to store the users pervious moves
        self.moves_history = {}
        #Create a pixel to chess notation dictionary
        self.pixel_to_notation = { 233 : "A",
                                299 : "B", 
                                365:"C",
                                431:"D",
                                497:"E",
                                563:"F",
                                629:"G",
                                695:"H",
                                133:"1",
                                199:"2",
                                265:"3",
                                331:"4",
                                397:"5",
                                463:"6",
                                529:"7",
                                595:"8" }
        #Get the user clicks, store it as x and y values then use the pixel_to_chess notation to figure out the position and piece
        #Gets the user mouse click, converts the point into string to get the x and y co ords then makes them into an interger
        p = self.win.get_mouse()
        string_p = str(p)
        x = int(string_p[6:9])
        y = int(string_p[11:14])
        print(x, y)
        
        
        if x > 200 and x < 728:
            if y > 100 and y < 628:
                print("Inside grid")
            else:
                print("Please select a chess piece")
        else:
            print("Please select a chess piece")
        
        #if it is a piece then light up the tile
        #show the user the different moves they can do if they can do any with that piece
        #Make sure special moves like en pessant and castling can also work
        #def move_pawn():
        

        pass

class ChessPiece:
    def __init__(self, colour, position):
        self.colour = colour
        self.position = position 
        
    

    def draw(self, win):
        pass


def main():
    board = ChessBoard()


        

if __name__ == "__main__":
    main()
