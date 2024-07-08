

class Position:
    # idx = IndexError
    # ln = line number
    # col = col number
    # fn = file Name
    # ftxt = file text
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt
    
    # current_char = current character in stream
    def advance(self, current_char=None):
        self.idx += 1
        self.col += 1

        if current_char == "\n":
            self.ln += 1
            self.col = 0

        return self

    
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

