import regex as re


class Regex:
    """
    This is a class used to recall regex
    """

    # Regex for types:
    string_regex = re.compile(r'(?<=(\'|\")).+(?=\1)')  # String
    int_regex = re.compile(r'\d+')  # Integer
    float_regex = re.compile(r'\d+\.\d+')  # Float
    bool_regex = re.compile(r'(True|False)')  # Boolean
    list_regex = re.compile(r'\[.*\]')  # List

    # Regex for annotation
    annotation_regex = re.compile(r'(?<=//\s)(?P<annotation>.*)')

    # Regex for function - print
    print_regex = re.compile(r'(?<=print\s)(?P<arg1>.*)')


if __name__ == '__main__':
    test = Regex()
    print(re.search(test.annotation_regex, '// This is a test.').group('annotation'))
