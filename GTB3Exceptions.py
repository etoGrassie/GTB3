class GTBIOError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class GTBFunctionError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class GTBArgumentError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
