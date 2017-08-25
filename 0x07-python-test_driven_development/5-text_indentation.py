"""Text Indentation Module

This module prints text with 2 new lines after each of these
characters: ., ? and : . Otherwise raise a TypeError.

"""


def text_indentation(text):
    """
     Args:
         text (string): String to be split.

     Returns:
         string: Split text by delimeter. TypeError otherwise.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] != '.' and text[i] != '?' and text[i] != ':':
            if text[i] == ' ' and text[i - 1] >= 'a' and text[i - 1] <= 'z':
                print(text[i], end="")
            else:
                continue
        else:
            print(text[i], end="\n")
            print()
