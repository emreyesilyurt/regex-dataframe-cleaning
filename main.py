import pandas as pd
from regex_dataset_cleaning import column_cleaning_using_regex

# Sample DataFrame 
data = {'column_name': ['123abc', '456-def', '789_ghi']} #you can put your data here
df = pd.DataFrame(data)

# Create an instance of the column_cleaning_using_regex class
cleaner = column_cleaning_using_regex()

# Clean numeric characters from a DataFrame column
ep, affected_count = cleaner.clean_numeric_chars(df, column_name)
print(f'Cleaned numeric characters in {affected_count} rows. Elapsed time: {ep} seconds')

# Clean unknown information indicator-related strings
ep, affected_count = cleaner.clean_unknown_information_indicator_related_strings(df, column_name)
print(f'Cleaned unknown information in {affected_count} rows. Elapsed time: {ep} seconds')

# Clean after slash
ep, affected_count = cleaner.clean_after_slash(df, column_name)
print(f'Cleaned after slash in {affected_count} rows. Elapsed time: {ep} seconds')

# Clean suffix variation
affected_count = cleaner.clean_suffix_variation(df, column_name)
print(f'Cleaned suffix variation in {affected_count} rows. Elapsed time: {ep} seconds')

# Clean extra special characters
ep, affected_count = cleaner.clean_extra_special_characters(df, column_name)
print(f'Cleaned extra special characters in {affected_count} rows. Elapsed time: {ep} seconds')

# Clean HTML tags
ep, affected_count = cleaner.clean_html(df, column_name)
print(f'Cleaned html tags in {affected_count} rows. Elapsed time: {ep} seconds')

# Clean website-related suffixes
ep, affected_count = cleaner.clean_website_related_suffixes(df, column_name)
print(f'Cleaned website related suffixes in {affected_count} rows. Elapsed time: {ep} seconds')

# Clean extra quotation marks
ep, affected_count = cleaner.clean_extra_quotation_marks(df, column_name)
print(f'Cleaned extra quotation marks in {affected_count} rows. Elapsed time: {ep} seconds')
