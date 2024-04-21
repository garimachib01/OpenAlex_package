
# OpenAlex package - keyword search and citation trends 

This package would provide a function that looks for keyword matches in titles, abstracts, and fulltext in the OpenAlex database.
This would be a Python package to use in notebooks, where the user provides keywords, and the output would be a pandas dataframe 
with the titles of top 20 works associated with that keyword, along with other fields like OpenAlex ID, citation count, and relevance score. 
The entries would be sorted by the relevance score, which is provided by OpenAlex as a measure of text similarity to search. 
If the number of works associated with the keywords is less than 20, the output would be the complete list of works matching
the keywords. An additional feature provided by the package would be citation trends by year for a given work,
where the user inputs a OpenAlex id and the output would be a list of dictionaries, where each dictionary represents a year and 
its corresponding citation count.
