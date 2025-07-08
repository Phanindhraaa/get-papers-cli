import requests
import logging

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
SEARCH_URL = BASE_URL + "esearch.fcgi"
FETCH_URL = BASE_URL + "efetch.fcgi"

def fetch_papers_by_query(query: str, max_results: int = 20) -> str:
    """
    Step 1: Search for PubMed IDs matching the query.
    Step 2: Fetch full details for those IDs.
    Returns: XML string with full paper details.
    """
    logging.debug("Sending query to PubMed: %s", query)
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    search_resp = requests.get(SEARCH_URL, params=search_params)
    search_resp.raise_for_status()

    ids = search_resp.json()["esearchresult"].get("idlist", [])
    logging.debug("Found PubMed IDs: %s", ids)

    if not ids:
        logging.warning("No results found for query: %s", query)
        return ""

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    fetch_resp = requests.get(FETCH_URL, params=fetch_params)
    fetch_resp.raise_for_status()

    logging.debug("Fetched XML data for %d papers", len(ids))
    return fetch_resp.text

