"""
Scrape wikipedia for the most populated US cities & write to a csv.

This is a one off so it's not optimized for reuse.
"""
import pandas as pd

# init url
url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

#get tables from url
read = pd.read_html(url)
#select the correct table
city_df = read[2]

#City, ST, 2022 estimate, Location columns
keep_cols = [0, 1, 2, 9]
#subset df on keep_cols
city_df = city_df.iloc[:, keep_cols]
#keep the first column name
city_df.columns = city_df.columns.droplevel(level=1)

#set save path
path = r'C:\Users\user\PycharmProjects\placesscraper\city_pop'
#save as csv
city_df.to_csv(path, index=False)