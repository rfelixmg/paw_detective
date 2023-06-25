import pkg_resources
from numpy.random import shuffle

file_path = pkg_resources.resource_filename(__name__, "src/words.txt")

with open(file_path) as fp:
    words = [line.split("\n")[0] for line in fp.readlines()]


def name_generator(n: int = 2) -> str:
    """
    Name generator: it generates a string with n funny words
    :return:
    """
    shuffle(words)
    return "_".join([words[i] for i in range(n)])
