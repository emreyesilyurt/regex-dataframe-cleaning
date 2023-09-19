import pandas as pd
import time
from cleanco import basename

class column_cleaning_using_regex:
    def __init__(self) -> None:
        super().__init__()


    def elapsed_time_decorator(self, function):
        def wrapper(self, df, col):  
            start = time.time()
            func = function(self, df, col)  
            end = time.time()
            ep = end - start
            return (ep, func)

        return wrapper


    @elapsed_time_decorator
    def clean_numeric_chars(self, df, column):
        self.df = df
        self.column = column


        # pattern='[0-9]|[-]'
        pattern = ' |[0-9]|[-]'
        changeto = ''

        affected_count = df[column].str.contains(pattern).dropna().sum()
        df.replace({column: pattern}, {column: changeto}, regex=True, inplace=True)


        return affected_count

#        elapsed_time_decorator = self.elapsed_time_decorator(Clean_numeric_chars)


#    @elapsed_time_decorator
    def clean_unknown_information_indicator_related_strings(self, df, column):
        self.df = df
        self.column = column

        L = ['unknown', 'unspecified', 'no info', 'na']

        df1 = df[df[column].isin(L)]
        df.replace({column: L}, {column: ''}, regex=True, inplace=True)

        return len(df1)

#        elapsed_time_decorator = self.elapsed_time_decorator(Clean_unknown_information_indicator_related_strings)


    def clean_after_slash(self, df, column):
        self.df = df
        self.column = column

        pattern = ' /(?!.*/).*'
        changeto = ''

        affected_count = df[column].str.contains(pattern).dropna().sum()
        df.replace({column: pattern}, {column: changeto}, regex=True, inplace=True)

        return affected_count



    def clean_suffix_variation(self,df, column):
        self.df = df
        self.column = column

        column = df[column]
        cnt = 0
        for i in range(len(column)):

            if basename(str(column[i])) != column[i]:
                column[i] = basename(str(column[i]))
                cnt += 1

        return cnt

    def clean_extra_special_characters(self, df, column):

        self.df = df
        self.column = column
        # pandas contains

        # pattern='^.*[一-龥]'
        # pattern='[一-龠]+|[(?!/)(?!/\*)]'
        pattern = '[一-龠]+|[(?/\)]'

        changeto = ''

        affected_count = df[column].str.contains(pattern).dropna().sum()
        df.replace({column: pattern}, {column: changeto}, regex=True, inplace=True)

        return affected_count

    def clean_html(self, df, column):
        self.df = df
        self.column = column

        pattern = '<[^>]*>'
        changeto = ''

        affected_count = df[column].str.contains(pattern).dropna().sum()
        df.replace({column: pattern}, {column: changeto}, regex=True, inplace=True)

        return affected_count

    def clean_website_related_suffixes(self, df, column):
        self.df = df
        self.column = column

        start = time.time()

        # pattern="(https?:\/\/)?(www\.)?[a-z0-9-]+\.(com|org)(\.[a-z]{2,3})?"
        pattern = ".(com|org|net)"
        changeto = ''

        affected_count = df[column].str.contains(pattern).dropna().sum()
        df.replace({column: pattern}, {column: changeto}, regex=True, inplace=True)

        return affected_count


    def clean_extra_quotation_marks(self, df, column):
        self.df = df
        self.column = column

        # pattern = r'"(.*?)"'
        # pattern = '"(.*?)"(?=\s*(?:[a-z]+=|]))/'
        pattern = '\'|"'
        changeto = ''

        affected_count = df[column].str.contains(pattern).dropna().sum()
        df.replace({column: pattern}, {column: changeto}, regex=True, inplace=True)

        return affected_count
