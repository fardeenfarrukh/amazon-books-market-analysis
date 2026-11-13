# BUSINESS INSIGHTS REPORT
## Book Catalog Market Analysis

**Data Source:** Books to Scrape
**Project:** Amazon Books Market Analysis - Demonstration Dataset
**Records Analyzed:** 163 books
**Prepared by:** Syed Fardeen
**Report Date:** November 13, 2026
**Version:** 1.0

## 1. Introduction

The purpose of this analysis is to collect book listing information and explore what could be learned from it through data analysis. Rather than looking at indiviual listings seperately, I wanted to organize the information and identify patterns in pricing, ratings, stock availability, and category distribution.

The data was collected from Book to Scrape, an educational website intended for web scraping practice. Python was used to collect and clean the information, while Pandas and Matplotlib were used for the analysis and visualizations.

The final dataset contains 163 book listings across five categories. Although this is relatively small sample, it provides enough information to perform some basic comparisons and identify areas that could be investigated further.

## 2. Dataset Overview

The collected dataset contains several pieces of information for each book, including:

- Book title and category
- Price excluding and including tax
- Tax amount
- Availability and stock quantity
- Book rating
- Number of reviews
- Product URL

After cleaning, the dataset contained **163 records and 13 columns**. 

During the initial checks, I found that only one book was missing a description. I decided to retain that record rather than exclude the entire book, since the missing description did not affect the other information available for analysis.

No duplicate product URLs were identified. Overall, the dataset was complete enough for the pricing, rating, category, and stock comparisons planned for this project.

## 3. Category Distribution

The collected books were divided into five categories. However, the distribution was not particularly balanced.

| Category | Number of Books |
|---|---:|
| Sequential Art | 75 |
| Mystery | 32 |
| Historical Fiction | 26 |
| Classics | 19 |
| Travel | 11 |
| **Total** | **163** |

Sequention Art accounts for approximately 46% of the entire dataset, making it consierable larger than the other categories. Travel, on the other hand, contains only 11 books.

This difference is worth keeping in mind throughout the analysis. For example, a category with 75 books has a much larger influence on the overall dataset than one with only 11. The category comparisons are still useful, but the results should not be treated as though every category has equal representation.

## 4. Pricing Analysis

The average listed price across all 163 books was **£34.45**, excluding tax.