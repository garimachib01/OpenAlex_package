import os
import pytest
import requests
from collections.abc import Iterable
from package import get_citation_trends


def test_get_citation_trends():
    """Test get_citation_trends function."""
    # Define a valid OpenAlex ID to query
    open_alex_id = "https://openalex.org/W2741809807"

    # Call the function under test with the OpenAlex ID
    results = get_citation_trends(open_alex_id)

    # Assert that the counts are retrieved successfully
    assert isinstance(results, list)
    assert len(results) > 0  # Ensure at least one count is returned
    assert all(isinstance(result["cited_by_count"], int) and 
               result["cited_by_count"] >= 0 for result in results) # Ensure all counts are non-negative integers
