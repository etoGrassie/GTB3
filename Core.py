import Exceptions as TCExceptions
import regex as re
from Regex import Regex as rep


class TCCore:
    """
    This is a class used to proceed tasks.
    """
    def __init__(self):
        pass

    def ProceedTasks(self, tasks):
        for task in tasks:
            re.sub(rep.annotation_regex, '', task)
            if re.search(rep.print_regex, task):
                if re.search(rep.print_regex, task).group('arg1'):
                    print(re.search(rep.print_regex, task).group('arg1'))
                else:
                    print()
            else:
                raise TCExceptions.NoTaskException()
