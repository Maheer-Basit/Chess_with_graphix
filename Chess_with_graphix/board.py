from graphix import Window, Text, Point, Rectangle, Line

class chess_board():
        
    def Tiles():
        win = Window("Board", 1200, 800)
        tile_id = 0
        x1 = 200
        x2 = 266
        y1 = 34
        y2 = 100
        black_tiles = [1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23, 24, 26, 28, 30, 33, 35, 37, 39, 40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62, 65]
        for i in range(8):
            if tile_id % 8 == 0:
                x1 = 200
                x2 = 266
                y1 += 66
                y2 += 66
            for i in range(8):
                tile = Rectangle(Point(x1, y1), Point(x2, y2))
                if tile_id in black_tiles:
                    tile. fill_colour = "black"
                tile.draw(win)
                x1 += 66
                x2 += 66
                tile_id += 1
                print(tile_id)
            
            
        
        
        Board = Rectangle(Point(200, 100), Point(728, 628))
        Board.draw(win)
        
        
chess_board.Tiles()