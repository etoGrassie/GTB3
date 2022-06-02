class NoCommandException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class InvalidCommandException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class NoTaskException:
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg