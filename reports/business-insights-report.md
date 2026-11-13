# BUSINESS INSIGHTS REPORT
## Book Catalog Market Analysis

**Data Source:** Books to Scrape
**Project:** Amazon Books Market Analysis - Demonstration Dataset
**Records Analyzed:** 163 books
**Prepared by:** Syed Fardeen
**Report Date:** November 13, 2026
**Version:** 1.0

## 1. Introduction

The purpose of this analysis is to collect book listing information and explore what we can learned from it through data analysis. Rather than looking at the indiviual listings seperately, I wanted to organize the information and identify the patterns in pricing, ratings, stock availability, and category distribution.

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

| Pricing Metric | Result |
|---|---:|
| Average Price | £34.45 |
| Lowest Price | £10.16 |
| Highest Price | £59.48 |

### Average Price by Category

| Category | Average Price |
|---|---:|
| Travel | £39.79 |
| Classics | £36.55 |
| Sequential Art | £34.57 |
| Historical Fiction | £33.64 |
| Mystery | £31.72 |

Travel has the highest average price at approximately £39.79, while Mystery had the lowest at £31.72.

The difference between these categories is noticable, although it would be difficult to explain the reason using the available data alone. We do not have information about book length, publishing costs, editions, or other factors that might influence the listed prices.

What the results do show is that pricing is inconsistent across the five categories. This could be explored further with larger sets of data.

## 5. Book Rating Analysis

The average rating arcross the whole dataset was approximately **2.93 out of 5 stars**.

### Average Rating by Categpry

| Category | Number of Books |
|---|---:|
| Historical Fiction | 3.23 |
| Sequential Art | 2.97 |
| Mystery | 2.94 |
| Travel | 2.73 |
| Classics | 2.47 |

The highest average rating was recorded by Historical Fiction, While the lowest average rating was recorded by Classics

One interesting thing i found was that the category with the highest average price was not the category with the highest average rating. The most expensive category on average was Travel, but Historical Fiction recieved the highest average rating.

Do not take this to mean that Historical Fiction is more prefered by the readers or that its a better value compared to other category books. It just shows ratings are only one measure, and the dataset does not provide enough information to explain why these differences exist. Even then, the comparison still shows how looking at the price alone cannot tell you the whole story.

## 6. Stock Availability Analysis

The average stock quantity was approximately **8 books per listing**. Across all 163 listings, the recorded stock total was 1,314 copies.

| Category | Number of Books |
|---|---:|
| Sequential Art | 686 |
| Mystery | 290 |
| Historical Fiction | 194 |
| Travel | 89 |
| Classics | 55 |

Sequential Art had the highest total stock, with 686 copies recorded. At first glance this might suggest that the category has a much larger supply than the other. However, it seems to also contain the most amount of book listings, so the total is partly explain by its larger size.

If you want a fairer comparison, Stock per listing would also be worth looking at. Total stock by themselves could give a misleading impression when category sizes are so different.

Please note that these quantities relect the availability displayed when the pages were scraped. they should not be treated as permanent inventory figures.

## 7. Highest and Lowest Priced Books

To get a closer look at the individual listings, i decided to examine the five most expensive and least expensive books in the dataset.

### Five Most Expensive Listings

| Category | Number of Books |
|---|---|---:|
| Boar Island (Anna Pigeon #19) | Mystery | £59.48
| Candide | Classics | £58.63 |
| The No. 1 Ladies' Detective Agency | Mystery | £57.70 |
| El Deafo | Sequential Art | £57.70 |
| Animal Farm | Classics | £57.22 |

### Five Least Expensive Listings

| Category | Number of Books |
|---|---|---:|
| Paitence | Sequential Art | £10.16
| The Complete Maus | Sequential Art | £10.64 |
| Tastes Like Fear | Mystery | £10.69 |
| Adulthood Is a Myth | Sequential Art | £10.90 |
| Fruits Basket, Vol.2 | Sequential Art | £11.64 |

There are a couple of interesting details here. Mystery and Classics both appear twice among the five most expensive, while Sequential Art appears almost 4 times out of the five least expensive.

Fruits Basket, Vol.2, which is priced at £11.64 has a five-star rating. This is useful because it tells us that a lower listed price is not automatically corresponding to a lower rating.

These are still just the highest and lowest listings in this particular sample. These findings should not be used to make general claims about the pricing of the entire book categories.

## 8. Key Business Observations

After reviewing the results, I identified several observations that stood out:

1. **Category representation:** Almost 46% of the collected books are from Sequential Art. This is a significant portion of the data and should be considered when interpreting the overall averages.

2. **Pricing differences:** The highest average listed price is from Travel, while Mystery has the lowest. There is no available information here that explains what causes this difference.

3. **Ratings:** The highest average rating is from Historical Fiction, at 3.23 stars. Classics has the lowest, at 2.47 stars.

4. **Stock availability:** The highest total recorded stock is also from Sequential Art. However since Sequential Art does hold a majority of the data these findings alone are not enough to compare inventory levels fairly.

5. **Price and ratings:** Some lower-priced books have higher ratings than some of the most expensive listings. There does not seem to be a straightforward relationship between price and rating based on these findings.

6. **Review data limitation:** There are zero reviews on each listing. This means the review count column does not provide any useful information or comparisons of the customer engagement in this dataset.

The Observations provided are a starting point for understanding the catalogue, although some of them would benefit from additional data before being used to support business decisions.

## 9. Recommendations

Based on the results, here are some areas that could be explored in the future:

- **Expand the dataset:** Having more books and categories would increase the sample size and category comparisons more useful.
- **Improve inventory comparisons:** Consider average stock per listing instead of total stock, this could help get a better understanding of the stock availability across categories.
- **Collect meaningful review data:**
- **Examine pricing in more detail:**
- **Collect data over time:**

These are some of the possible areas for future analysis. The current data does not have enough sample size to allow for firm recommendations about sales performance, market demand or puchasing behaviour.

## 10. Limitations

## 11. Conclusion