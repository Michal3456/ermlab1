# encoding: utf-8
# module CoutingWords
# from /home/michu/PycharmProjects/cout-words/couting/CoutingWords.py
# by written 1.00
# no doc

# imports
import os
import nltk.corpus
from nltk.text import Text
from nltk import FreqDist
from nltk.tokenize import word_tokenize

from couting.ReadBook import ReadBook

# Variable with simple values

_ERR = 0


# class


class CoutingWords:
    """
    open_file_count_word() write key,value dictionary.
    open_file_count_word() load path_relative_to_book next split elements
    in __mystring_with_files, next create dictionary (key=word,value=number of
    words) and write it.
    """

    # function

    @staticmethod
    def open_file_count_word(path_to_book):  # real signature unknown; loaded from data/test_book
        """ open_file_count_word() -> None.  Write all items from __dist.

        Parameters
        -----------
        path_to_book:
            absolute path to book wherebout

        Returns
        -------
        return:
            None
        """
        try:
            print("***************start:********************")
            path_to_book = os.path.abspath(path_to_book)
            mystring_with_files = ReadBook.read_book(path_to_book)
            mystring_with_files = word_tokenize(mystring_with_files, 'polish')
            dist = FreqDist(mystring_with_files)
            __vocablary = list(dist.keys())
            moby = Text(nltk.corpus.gutenberg.words('/home/michu/PycharmProjects/cout-words/data/test_book'))
            moby.dispersion_plot(__vocablary[1:100])
            for d, v in sorted(dist.items()):
                print("%r %r" % (d, v))
            print("Cout words:%d" % len(__vocablary))
            print("***************the end*******************")
        except Exception as e:
            print("Error in general metod: %e" % e)
        finally:
            print("Process finished with exit code %d" % _ERR)


if __name__ == '__main__':
    CoutingWords.open_file_count_word('/home/michu/PycharmProjects/cout-words/data/test_book')
