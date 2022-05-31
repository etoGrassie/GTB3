import Exceptions as TCExceptions
import regex as re


class UnsupportedCommand:
    pass


class Proceed:
    """
    This class is used to proceed the input task.
    defaultProceed is used to proceed the input task with a normal way.
    """
    unsupported = UnsupportedCommand()

    # Regex of notes
    regex_notes = re.compile(r'(?<=^//).*')
    # Regex of commands
    available_commands = ['print', 'web', 'random', 'randint', 'randobj', 'exit|quit']
    temp_commands_raw_regex = r'^({}\s+)'.format('|'.join(available_commands))
    print(temp_commands_raw_regex)
    regex_available_commands = re.compile(temp_commands_raw_regex)
    del temp_commands_raw_regex

    # Regex of arguments
    arg_regex_print = re.compile(r'(?<=^print\s+).*(?=;$)')
    arg_regex_web = re.compile(r'(?<=^web\s+).*(?=;$)')
    arg_regex_random = re.compile(r'(?<=^random\s+).*(?=;$)')
    arg_regex_randint = re.compile(r'(?<=^randint\s+).*(?=;$)')
    arg_regex_randobj = re.compile(r'(?<=^randobj\s+).*(?=;$)')

    # Regex of repeat arguments
    rep_regex_times = re.compile(r'(?<=::\s*)\w(?=;$)')
    rep_regex_random_min = re.compile(r'(?<=^random\s+int\s+)\d')

    def defaultProceed(self, single_task: str):
        # Check if the task is a note
        temp = re.search(self.regex_notes, single_task)
        if temp:
            return temp.group(0)  # Return the note (directly print as output)

        # Check if the task is an available command
        temp = re.search(self.regex_available_commands, single_task)
        if temp:
            command = temp.group(0).strip()

            if command == 'print':
                # Check if the task is a print command
                temp = re.search(self.arg_regex_print, single_task)
                if temp:
                    return temp.group(0)
                else:
                    raise TCExceptions.InvalidCommandException

            elif command == 'web':
                return self.unsupported

            elif command == 'random':
                times = re.search(self.rep_regex_times, single_task)
                if times:
                    try:
                        times = int(times.group(0))
                    except ValueError:
                        raise TCExceptions.InvalidCommandException
                    else:
                        random_list = list(re.search())
                        for i in range(times):



if __name__ == "__main__":
    core = Proceed()
    print(core.defaultProceed("// hello"))
