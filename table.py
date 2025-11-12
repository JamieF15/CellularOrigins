class table:
    def __init__(self, size=5):
        self.size = size
        self.min_coord = 0
        self.max_coord = size
        
    def position_is_valid(self, x, y):
        """Check if a position is within table bounds when a 'move' command is issued."""
        return (self.min_coord <= x <= self.max_coord and 
                self.min_coord <= y <= self.max_coord)
    
    def get_size(self):
        return self.size
    
    def get_min_coord(self):
        return self.min_coord
    
    def get_max_coord(self):
        return self.max_coord