

class RTResult:
    def __init__(self):
        self.value = None
        self.error= None

    def registger(self, res):
        if res.error: self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self


class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()
    
    def set_pos(self):
        pass

    def set_context(self):
        pass


