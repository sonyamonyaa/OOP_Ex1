class Call:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        if dest > src:
            self.type = 1
        else:
            self.type = -1

    def is_legit(self, low, top):
        flag = self.src >= low and self.dest >= low
        flag = flag and self.src <= top and self.dest <= top
        return flag

