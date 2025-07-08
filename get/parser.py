from lxml import etree
from typing import List, Dict
from get.utils import is_academic, is_company_affiliated

def parse_pubmed_response(xml_data: str) -> List[Dict[str, str]]:
    if not xml_data:
        return []

    root = etree.fromstring(xml_data.encode("utf-8"))
    papers = []

    for article in root.xpath("//PubmedArticle"):
        try:
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            pub_date = (
                article.findtext(".//PubDate/Year") or
                article.findtext(".//PubDate/MedlineDate") or
                "Unknown"
            )

            authors = article.findall(".//Author")
            non_academic_authors = []
            company_affiliations = []
            corresponding_email = None

            for author in authors:
                affiliation_info = author.findtext("AffiliationInfo/Affiliation")
                email = extract_email(affiliation_info)

                if affiliation_info:
                    # Only include authors whose affiliation is NOT academic
                    if not is_academic(affiliation_info):
                        non_academic_authors.append(get_author_name(author))
                    if is_company_affiliated(affiliation_info):
                        company_affiliations.append(affiliation_info)

                if not corresponding_email and email:
                    corresponding_email = email

            # Only keep papers with at least one company affiliation
            if company_affiliations:
                papers.append({
                    "PubmedID": pmid,
                    "Title": title,
                    "Publication Date": pub_date,
                    "Non-academic Author(s)": "; ".join(non_academic_authors),
                    "Company Affiliation(s)": "; ".join(set(company_affiliations)),
                    "Corresponding Author Email": corresponding_email or "N/A"
                })

        except Exception as e:
            print(f"Error parsing article: {e}")
            continue

    return papers

def get_author_name(author) -> str:
    last = author.findtext("LastName") or ""
    first = author.findtext("ForeName") or ""
    return f"{first} {last}".strip()

def extract_email(affiliation: str | None) -> str | None:
    if affiliation and "@" in affiliation:
        words = affiliation.split()
        for word in words:
            if "@" in word:
                return word.strip(".,;()[]{}<>")
    return None
