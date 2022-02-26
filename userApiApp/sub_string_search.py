from unittest import result
from fuzzywuzzy import process


def get_string(query, choices_data, limit=3):
    
    results = process.extract(query, choices_data, limit=limit)
    return results
