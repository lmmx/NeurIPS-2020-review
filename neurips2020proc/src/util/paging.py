from pydoc import pager
from pandas import option_context

__all__ = ["listpager", "dfpager"]

def listpager(a_list):
    pager("\n".join([i if type(i) is str else repr(i) for i in a_list]))

def dfpager(dataframe):
    with option_context('display.max_rows', None, 'display.max_columns', None):
        listpager([dataframe.to_string()])
