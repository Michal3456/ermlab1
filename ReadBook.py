# encoding: utf-8
# module ReadBook
# from /home/michu/PycharmProjects/cout-words/couting/ReadBook.py
# by written 1.00
# no doc
# no Variables
# no import

# from couting.RemovePolishSymbols import RemovePolishSymbols


# class

class ReadBook:
    """
    read_book() -> str
    read_book() loading (read) book next remove Polish characters and insert in latin
    script characters.
    """

    # function

    @staticmethod
    def read_book(path_relative_to_book: str) -> str:  # real signature unknown; loaded from data/test_book
        """ open_file_count_word() -> str.
        Load all lines from path_relative_to_book, nest remove Polish
        charatcter and post _mystring_with_files.

        Parameters
        -----------
        path_relative_to_book:
            absolute path to book wherebout

        Returns
        -------
        return:
            string with no accents

        """
        try:
            with open(path_relative_to_book, 'r') as __files:
                _mystring_with_files = __files.read()
            return _mystring_with_files

        except Exception as e:
            print("Error in loading book: %s" % e)
            _mystring_with_files = 'error'
            return _mystring_with_files
