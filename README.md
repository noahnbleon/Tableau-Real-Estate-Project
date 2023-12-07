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

The Location data stored in the dataset as coordinates proved useful for our goal; with the assistance of Python, we were able to use these coordinates to connect our data points to a map in Tableau and display their counts (through bubble size) and Median Sales Amounts (through color intensity) by Town.

Understanding the geographical distribution of property sale values, along with potential factors associated with these patterns, offers valuable insights across various industries. Real estate developers may be interested in using this information to identify potential areas for investments based on demand and affordability. Financial institutions may (for better or worse) assess credit risks and tailor loan products based on property values in specific locations, and insurance companies may use data similar to ours to set premiums and manage risk profiles in different regions. Additionally, policymakers may leverage information similar to this in evaluating the effectiveness of economic development initiatives and allocate resources more efficiently. It is important to note that these are just some potential inferences, and further analysis is needed to draw more definitive conclusions.

### Map of Connecticut
![Map of Connecticut Median Sale Amounts (final revision)](https://github.com/noahnbleon/project2/assets/124447378/2e0225cf-d226-4d6f-ac1e-6d050cebc6c1)
From this map we can see that there is a drastic increase in Sale Amounts in the southwestern region near the state's border with New York. Counts of Sale Amounts by Town seem primarily stratified in the central area of the state surrounding Hartford (the state's capital city), continuing towards the southwest corner of the state and also occurring sporadically in each major city (Danbury, Torrington, Norwich, New London).

![Detected Outliers in our Map of Connecticut Median Sale Amounts](https://github.com/noahnbleon/project2/assets/124447378/c9cf8786-359c-45d7-bd2b-07affd6498f9)\
In the Data Guide panel of the map we created in Tableau, these outliers were detected.

![Outlier Median Sale Amounts by Town](https://github.com/noahnbleon/project2/assets/124447378/b5efe4cb-a705-4791-9a74-cee6ce1558d4)
To show how the outliers compare to one another, this chart is filtered to show these Outlier Median Sale Amounts by Town.

### Highlighting the outliers on a map
Aside from having the highest Median Sale Amounts of all the points in the dataset, we believe these Towns may tell us something about Sale Amount and Location. Our hypothesis is that their proximity to New York and their economic demograph may influence the Sale Amounts in this area.

![Map of Connecticut Median Sale Amounts Near the NY Border (final revision)](https://github.com/noahnbleon/project2/assets/124447378/1f741d46-a171-4b73-997f-0d5614d61757)
In this map, we focus on only our five outliers and add a Background Layer that accounts for data gathered regarding percentage of Blue Collar and Farm Occupation as according to the Census Tract in 2018. The observed increase in Median Sale Amounts in specifically the southwestern region of Connecticut near the New York border and outside of blue collar and rural areas (excluding the southwestern-most city of Greenwich) aligns with our hypothesis. We believe that Greenwich's heightened proximity to New York compared to the other outliers may override the presence of a large, primarily blue collar and rural area nearby.

#### Proximity to New York City:
These 5 towns are within commuting distance of New York City, a major financial and business center. We believe that this proximity could impact our dataset, as it could correlate with a higher frequency in individuals and families employed in high-paying jobs, driving demand for upscale housing options and leading to higher listing amounts. New York City's notoriously expensive housing market can push potential buyers to seek more affordable options nearby. This spillover effect further increases demand for properties, possibly in southwestern Connecticut.

#### Economic Demographics:
After some research using external sources ([Greenwich Household Income](https://statisticalatlas.com/place/Connecticut/Greenwich/Household-Income), [New Canaan Household Income](https://statisticalatlas.com/county-subdivision/Connecticut/Fairfield-County/Town-of-New-Canaan/Household-Income), [Darien Household Income](https://statisticalatlas.com/place/Connecticut/Darien/Household-Income), ([Westport Household Income](https://statisticalatlas.com/place/Connecticut/Westport/Household-Income), [Weston Household Income](https://statisticalatlas.com/county-subdivision/Connecticut/Fairfield-County/Town-of-Weston/Household-Income)), we see that our outlier towns are largely composed of affluent residents with incomes of $250,000 a year or greater. This economic prosperity translates into a willingness and ability to pay higher prices for desirable properties. Further, towns with richer residents tend to have greater access to high-end amenities. The presence of these amenities increases the overall desirability of the area, contributing to higher property values.

We believe that the combination of greater proximity to New York City and the affluence of residents contributes to the observed increase in average Sale Amount in southwestern Connecticut.

### Manipulations applied to the data set for analysis
For the map visual, we augmented the Location data in order to be useful for Python so that we could create our maps in Tableau. The information on how this was done is available within the repository (Project 2 > src > dataAugmentation.md). Also available are the town coordinates after they were coded to function with Tableau (Project 2 > data > Output > town_coordinates.json).

### Tableau workbook
The packaged workbook containing the visualizations shown above is NOT attached to this repository (we're sorry, GitHub wouldn't let us attach it; but you can find all images used above in Project2 > Charts).

## Made with love, Tableau, Python, and Gnu Image Manipulation Program (to put legends on the empty space in our maps!)
