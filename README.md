# Team 1 MIST4610 Group Project 2

### Team Name
Team 1

### Team Members
Noah Leon [@noahnbleon](https://github.com/noahnbleon)\
Lenny Keenan [@leonardkeenan](https://github.com/LeonardKeenan)\
Katie Gelderman [@katiegelderman](https://github.com/Katiegelderman)\
Tyson Colette [@tysoncolette](https://github.com/tysoncolette)

### Description of dataset
Our dataset, sourced from [https://catalog.data.gov/dataset/real-estate-sales-2001-2018](https://catalog.data.gov/dataset/real-estate-sales-2001-2018), comprises a detailed compilation of real estate listings. With 997,213 rows, we have access to an overview of aspects for each listing, including its Address, Assessor Remarks, List Year, Location, Non Use Code, OPM Remarks, Property Type, Residential Type, Serial Number, Town, Assessed Values, Sale Amount, and Sales Ratio.

### Question 1
Is there a monthly trend in the Sale Amounts of real estate listings in Connecticut?

### Importance

We seek to find if there are specific months of the year when the properties listed for sale in any given month have had on average higher or lower Sale Amounts compared to other months. We believe that in our pursuit to answer this question, the data we find could offer insight into when the real estate market in Connecticut is most and least affordable, and if there is a seasonality within this market.

It could also correlate to how seasonality affects the housing market in other states besides Connecticut. More analysis incorporating datasets from other states would need to be conducted to determine if patterns similar to Connecticut’s are present, but this data could provide us with the foundation needed to understand a broader range of markets.

We believe that our analysis could provide important information regarding real estate market habits and strategies in Connecticut; however, we acknowledge that there are many factors outside of our dataset that could play a role in manipulating our data, and that seasonality is likely not a standalone factor.

![Average   Median Sale Amounts Based on Month (2001-2020)](https://github.com/noahnbleon/project2/assets/148257298/08615c83-7ce7-45fc-80d8-f09668899af6)

In our Tableau graph, we see a very flat, somewhat cyclic pattern represented by our blue Median Sale Amount line. Further, our graph shows that the Median Sale Amounts are ranging between approximately $200,000 (February, trough) and $250,000 (July, peak). Our assessment is that Sale Amounts at the median of our dataset are fairly stable.

In contrast, our orange Average Sale Amount line shows a more volatile transition from month to month, indicating that our dataset may contain outliers swaying the averages accordingly. In addition, the range of our Average Sale Amounts is between approximately $350,000 (February, trough) and $450,000 (December, peak). We see that the averages within the dataset spike most dramatically out of line with the cyclic nature of our medians in August and December; whether this trend is representative of the sellers or their anticipation of who may be buying, we are uncertain. The month in which our averages most deviate from any potential trend is December; otherwise predicted to be a “flat” and “middle-range” month per our median, December represents a peak in Average Sale Amounts that rivals August.

Additionally this graph shows a difference between the median and average sales that ranges from $150,000 to $250,000. We believe this is caused by outliers in the dataset that are pulling on the average. For this reason we deduce that the median line shows a more accurate pattern, meaning the housing market in Connecticut is relatively stable with a peak over the summer months.

Perhaps due to our bias as college students, we felt the spikes in Average Sale Amounts could potentially be related to Property Type, in that the prices of apartment complexes being listed on the market during August, December, and to some extent January could be representative of apartment complex owners listing their property on the market. If one treats Connecticut like a microcosm of the greater economy it is within, this could make sense due to the cyclic nature of college students migrating apartments after their lease ends. (However, as previously stated, Connecticut is likely not plausible to view as a microcosm due to the various other factors impacting our dataset that are unaccounted for.)

### Question 2

Is there a relationship between Location and Median Sale Amount?

### Importance

We want to find if the Location of properties sold in Connecticut between 2001 and 2020 has an effect on its Median Sale Amount. Our goal is to use the dataset to uncover if Median Sale Amounts by Town in Connecticut contain variability. If they do not, we imagine we will see Median Sale Amounts by Town that are relatively the same as one another. If there is variability strong enough that these data are considered outliers, we intend to examine these outliers more closely.

### Our process

The Location data stored in the dataset as coordinates proved useful for our goal; with the assistance of Python, we were able to use these coordinates to connect our data points to a map in Tableau and display their counts () and Median Sales Amounts by Town 

Understanding the geographical distribution of property sale values, along with potential factors associated with these patterns, offers valuable insights across various industries. Real estate developers can use this information to identify potential areas for investments based on demand and affordability. Financial institutions may (for better or worse) assess credit risks and tailor loan products based on property values in specific locations. Insurance companies can use this data to set premiums and manage risk profiles in different regions. Additionally, policymakers can leverage this information to evaluate the effectiveness of economic development initiatives and allocate resources more efficiently. It is important to note that these are just some potential inferences, and further analysis is needed to draw more definitive conclusions, such as household income levels, employment statistics, and population demographics.

![Highest 8 Median Sale Amounts by Town](https://github.com/noahnbleon/project2/assets/148257298/0762b710-67a5-411c-a383-817ef4798f97)
This chart is filtered to show the first eight highest Median Sale Amounts by Town in Connecticut. There are clear differences in Median Sale Amount depending on which Town the sale occurred in. We speculate that the differences in the medians translates to a difference in overall Sale Amounts by Town.

We can conclude that there appears to be a relationship between certain towns and median sale amounts.

### Map of Connecticut
![Map of Connecticut Median Sale Amounts](https://github.com/noahnbleon/project2/assets/148257298/3387b61d-52e9-4692-aa90-6285373628ab)
From this map we can see that there is an increase in Sale Amounts in the southwestern region.

![Map of Connecticut Median Sale Amounts Near the NY Border](https://github.com/noahnbleon/project2/assets/148257298/0b6a1964-07c9-4906-b3b0-ec115a17caf4)
The observed increase in average sale amounts in the southwestern region of Connecticut, particularly in Greenwich, Darien, and New Canaan, aligns with several key factors specific to this region.

### Proximity to New York City:
These towns are within commuting distance of New York City, a major financial and business center. We believe that this proximity could impact our dataset, as it could correlate with a higher frequency in individuals and families employed in high-paying jobs, driving demand for upscale housing options and leading to higher listing amounts. New York City's notoriously expensive housing market can push potential buyers to seek more affordable options nearby. This spillover effect further increases demand for properties in southwestern Connecticut.

### Economic Demographics:
Greenwich, Darien, and New Canaan boast a significant concentration of affluent residents with high disposable incomes. This economic prosperity translates into a willingness and ability to pay premium prices for desirable properties. These towns offer a plethora of high-end amenities, including world-class golf courses, private clubs, and exclusive shops and restaurants. The presence of these amenities increases the overall desirability of the area, contributing to higher property values.

In conclusion, the combination of proximity to New York City, affluent demographics, a limited housing supply, and a focus on luxury living all contribute to the observed increase in average sale amounts in southwestern Connecticut, particularly in Greenwich, Darien, and New Canaan.

### Manipulations applied to the data set for analysis:

We did not have to manipulate any data. For our first visual in question 2 we restricted the chart to the top 8 towns in the dataset, this was to make the chart more readable and easier to digest as there are simply too many towns to display effectively. For the map visusual we had to augment the data in order to be used and the information on how we did this is available within the repository.

### Tableau packaged workbook:

The packaged workbook containing the visualizations shown above is attached to this repository.



