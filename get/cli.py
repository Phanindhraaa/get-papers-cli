import argparse
import logging
from get.pubmed_client import fetch_papers_by_query
from get.parser import parse_pubmed_response
from get.utils import write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech author affiliations.")
    parser.add_argument("query", help="Search query for PubMed.")
    parser.add_argument("-f", "--file", help="CSV filename to save results. If not provided, output is printed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging.")
    
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    logging.info(f"Searching PubMed for: {args.query}")
    xml_data = fetch_papers_by_query(args.query)
    papers = parse_pubmed_response(xml_data)

    if args.file:
        write_to_csv(papers, args.file)
        logging.info(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()

