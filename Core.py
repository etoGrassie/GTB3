import Exceptions as TCExceptions
import regex as re


class Proceed:
    def __init__(self):
        pass

    def defaultProceed(self, single_task: str):
        re.match('(?<=^//\s*)')
