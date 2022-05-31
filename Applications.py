import regex as re
from PyQt5.QtCore import QThread


class ProceedTasks(object):
    Tasks = []
    Output = []
    Feedback = []

    def __init__(self):
        super(ProceedTasks, self).__init__()

    def aa(self):
        if not self.Tasks:
            return
        for task in self.Tasks:
            if (not task) or (task.startswith('//')):
                continue
            func = re.search(r'(?<=gtb\s+)(prt|print|random|randint|randobj).*(?>=;', task, re.IGNORECASE)
            print(func)
            if not (re.search(r'(?<=gtb\s+)(prt|print|random|randint|randobj).*;', task, re.IGNORECASE)):
                self.Feedback.append(task)
                continue
            print('suc', re.search(r'(?<=gtb\s+)(prt|print|random|randint|randobj).*;', task, re.IGNORECASE).group())


if __name__ == '__main__':
    a = ProceedTasks()
    a.Tasks = ['//Hello', 'gtb prt;']
    a.aa()
    print(a.Feedback)