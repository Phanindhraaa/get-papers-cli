import csv
import logging
from typing import List, Dict

# Keywords that indicate academic institutions
ACADEMIC_KEYWORDS = [
    "University", "College", "Institute", "School", "Hospital",
    ".edu", ".ac", ".gov", "Department of", "Faculty of", "Center for",
    "Division of", "Research Center", "Graduate School", "National Institute"
]

# Keywords that suggest industry/company affiliations
COMPANY_KEYWORDS = [
    "Inc", "Ltd", "LLC", "Corp", "Corporation",
    "Pharmaceutical", "Biotech", "Therapeutics",
    "Diagnostics", "Research Labs", "Biosciences", "GmbH", "S.A.", "Pvt"
]

def is_academic(affiliation: str) -> bool:
    """Return True if the affiliation seems academic."""
    return any(keyword.lower() in affiliation.lower() for keyword in ACADEMIC_KEYWORDS)

def is_company_affiliated(affiliation: str) -> bool:
    """Return True if the affiliation suggests a company or industry."""
    return any(keyword.lower() in affiliation.lower() for keyword in COMPANY_KEYWORDS)

def write_to_csv(data: List[Dict[str, str]], filename: str):
    """Write a list of dictionaries to a CSV file."""
    if not data:
        logging.warning("No data to write.")
        return

    fieldnames = [
        "PubmedID", "Title", "Publication Date",
        "Non-academic Author(s)", "Company Affiliation(s)",
        "Corresponding Author Email"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
