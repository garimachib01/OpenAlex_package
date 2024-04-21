"""Define utility functions for our package."""
import requests
from collections.abc import Iterable
import pandas as pd


def search_works(query):
    """Define function to search for top 20 works based on keyword."""
    if isinstance(query, str):
        query = "+".join(query.split())
    elif isinstance(query, Iterable):
        query = "+".join(query)

    endpoint = f"https://api.openalex.org/works?search={query}"
    response = requests.get(endpoint)
    results = response.json()

    # Extract relevant information from the results
    work_data = []
    for result in results.get("results", []):
        title = result["title"]
        citation_count = result["cited_by_count"]
        open_alex_id = result["id"]
        relevance_score = result["relevance_score"]

        work_data.append(
            {
                "Title": title,
                "Citation Count": citation_count,
                "ID": open_alex_id,
                "Relevance Score": relevance_score,
            }
        )

    # Create a DataFrame from the extracted information
    df = pd.DataFrame(work_data)

    # Sort DataFrame based on relevance score in descending order
    df_sorted = df.sort_values(by="Relevance Score", ascending=False)

    # Output top 20 works
    top_20_works = df_sorted.head(20)
    return top_20_works


def get_citation_trends(open_alex_id):
    """Define function to get citation counts by year using OpenAlex ID."""
    endpoint = f"https://api.openalex.org/works/{open_alex_id}"
    response = requests.get(endpoint)
    results = response.json()

    # Extract citation trends data
    citation_trends = results["counts_by_year"]
    return citation_trends
