class call:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        if dest > src:
            self.type = 1
        else:
            self.type = -1
