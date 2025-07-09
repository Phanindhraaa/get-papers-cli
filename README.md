# get-papers

A Python CLI tool to **fetch PubMed papers** related to a search query, and **filter out papers that only have academic authors**. 
It saves the results (with industry authors only) to a CSV file for further analysis.

# Features

-  Search PubMed using a keyword
-  Parse XML metadata for papers
-  Filter out academic-only affiliations (like universities, hospitals)
-  Only include papers with at least **one author from a pharma/biotech/company**
-  Save results to a CSV file or print to terminal
-  Modular and testable code structure

# Installation (using Poetry)
Make sure Python 3.12+ is installed.
       bash:
      -git clone https://github.com/Phanindhraaa/get-papers-cli.git
      -cd get-papers
      -poetry init (select all defaults)
      -poetry add requests lxml
 
# To Run
      bash:
     -poetry run get-papers-list QUERY [-f results.csv] [-d]
         
QUERY Your PubMed search keyword (e.g. cancer, brain), -f filename.csv (Optional) Save results to CSV instead of printing, -d(Optional) Enable debug logging
         
        

# Example
bash:
 -poetry run get-papers-list cancer -f results.csv -d

          1.Searches PubMed for "cancer"
          2.Filters only industry-affiliated authors
          3.Saves results to results.csv
          4.Shows debug logs in the terminal
          
Behind the Scenes The CLI tool:

          1.Calls PubMed's E-Utilities API to search and fetch paper metadata
          2.Parses the XML using lxml
          3.Uses keyword matching to detect: Academic affiliations: University, Hospital, .edu, etc.
                                             Company affiliations: Inc, Pharmaceutical, Biotech, etc.
          4.Only includes papers with at least one non-academic, company-affiliated author   



Phanindhra Sura
Email: suraphanindhra@gmail.com
GitHub: https://github.com/Phanindhraaa


                                           
          
         



