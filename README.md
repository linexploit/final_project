

# Dark Market Analysis & Phishing Detection

![darkweb](https://github.com/linexploit/final_project/blob/main/resources/darkweb.jpg?raw=true)

## Project Description
This project aims to understand what information and products are sold on dark web markets. By understanding what kind of data criminals are able to buy from hackers on the Dark Web, we can determine what kinds of threats we're up against, and what data we need to secure. This knowledge can be used by governments, companies and all cyber professionals to conduct countermeasures, to protect themselves and to detect phishing emails, which is often the first vector of attacks.

The data used in this project comes from dark market transactions between 2014 and 2015. An attempt was made to scrape more recent data from Tor, but due to the complexity of the task, limited time and resources, this was not completed. 


## Development of Analysis Questions/Objectives
The project was initiated with a set of guiding questions focusing on the activities, products, and users of dark web markets. The objectives include understanding the prevalence of certain types of information and products, assessing the potential risks associated with their use, and predicting future threats.

## Pre-Selection of Datasets
The project involved a careful pre-selection of datasets relevant to the analysis objectives. Criteria for dataset selection included comprehensiveness, reliability, and relevance to the theme of Dark Markets.

- **MAIN DATASETS:** 
 - [Dark Market 2014-2015](https://www.kaggle.com/datasets/philipjames11/dark-net-marketplace-drug-data-agora-20142015)
 - [Phishing Email](https://www.kaggle.com/datasets/subhajournal/phishingemails)
- **SECONDARY DATASETS:**
  - [Dark Market 2023](https://www.privacyaffairs.com/dark-web-price-index-2023/) 
  - [Dark Market 2022](https://www.privacyaffairs.com/dark-web-price-index-2022/)
  - [Dark Market 2021](https://www.privacyaffairs.com/dark-web-price-index-2021/)
  - [Dark Market 2020](https://www.privacyaffairs.com/dark-web-price-index-2020/)


## Development of Cleaning Functions
Cleaning functions were developed to handle specific inconsistencies and issues in the datasets. I focused on ensuring data quality and relevance for the analysis. The datasets underwent thorough cleaning. This process included standardizing data formats, handling missing values, and removing irrelevant entries.

## Data Cleaning and Preprocessing
Detailed steps were taken to clean and preprocess the data. Specific attention was given to the normalization and transformation of data for analysis readiness. I used the `CLEANING_FUNCTION.py` file (HOMEMADE) to clean this dataset and others.

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis was conducted to provide initial insights into the data. It included statistical summaries and visualizations. (check notebooks)

## Machine Learning Models
In this project, we utilized two primary machine learning models for predicting phishing emails: Logistic Regression and Naive Bayes. Both models were chosen for their simplicity, interpretability, and effectiveness in text classification tasks. However, it's worth noting that neither model achieved perfect accuracy, likely due to the inherent complexity and variability of phishing attempts. (check notebooks)

## Limitations and Further Research
The data used in this project primarily comes from transactions conducted between 2014 and 2015. While this provides valuable insights into the state of dark web markets during that period, it may not fully represent the current landscape. Therefore, further research could involve collecting more recent data, possibly through more complex methods such as web scraping from Tor.
Another limitation is the computational resources available for training the machine learning models. The models used in this project, while effective, are not perfect due to these constraints. Future work could explore more advanced models or techniques to improve prediction accuracy.
Finally, while the project focuses on phishing detection, it does not cover all aspects of cybersecurity threats. Expanding the scope to include other forms of malicious activity could enhance the utility of the project.

## Recommended Actions
- Ensure regular updates to your systems to benefit from the latest security patches.
- Be mindful of what information you share publicly to avoid potential exposure.
- Only work on company-provided hardware and environments to ensure secure operations.
- Consult with a cybersecurity expert if you encounter any uncertainty or unfamiliar situations.

You can also check if your data are leaked on these websites:
- [haveibeenpwned](https://haveibeenpwned.com/)  
- [Google One](https://one.google.com/dwr/dashboard) 


## Technologies Used
The project is built using Python, with libraries such as Pandas and Scikit-Leark for data manipulation and machine learning respectively. Natural Language Processing (NLP) techniques were also employed.