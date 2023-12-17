This project aims to verify the hypothesis that a newly discovered human settlement, referred to as 'A', 
utilizes an indigenous herb to significantly boost the heights of its inhabitants. To test this hypothesis, 
several statistical analyses are conducted on various samples from settlement 'A' and a nearby tribe 'B',
which does not have access to the herb. The following tasks outline the methodology and statistical tests used in this study:

Task Descriptions

(a) Single Population Z-test
Objective: Compare the mean heights of 200 women from tribe 'B' with the women of settlement 'A'.
Data: Heights from height_female.csv (settlement 'A') and height_female_200.csv (tribe 'B').
Test Applied: Single population Z-test.
Variance: Use 121 for the sample of 200 women.
Alpha: 0.05.
Null and Alternative Hypotheses:
Null Hypothesis (H0): The mean height of women in tribe 'B' is equal to that of women in settlement 'A'.
Alternative Hypothesis (H1): The mean height of women in tribe 'B' is different from that of women in settlement 'A'.

(b) Z-test for 2 Independent Populations
Objective: Test if the first 50 males and 50 females from settlement 'A' have the same mean height.
Data: First 50 heights from height_male.csv and height_female.csv.
Test Applied: Z-test for two independent populations.
Variance: 110 for males, 121 for females.
Alpha: 0.05.
Null and Alternative Hypotheses:
Null Hypothesis (H0): The mean height of males is equal to that of females in settlement 'A'.
Alternative Hypothesis (H1): The mean height of males is different from that of females in settlement 'A'.

(c) Single Population T-test
Objective: Compare the mean height of men from tribe 'B' with men of settlement 'A'.
Data: Heights from height_male.csv (settlement 'A'); sample heights for tribe 'B': [157.74, 155.98, ...].
Test Applied: Single population T-test.
Alpha: 0.05, degrees of freedom = 9, threshold value = 2.2622.
Null and Alternative Hypotheses:
Null Hypothesis (H0): The mean height of men in tribe 'B' is equal to that of men in settlement 'A'.
Alternative Hypothesis (H1): The mean height of men in tribe 'B' is different from that of men in settlement 'A'.

(d) Paired T-test
Objective: Determine if the herb had an effect on the heights of 10 males from settlement 'A' over one year.
Data: Heights measured now and after one year.
Test Applied: Paired T-test.
Alpha: 0.05, degrees of freedom = 9, threshold value = 2.2622.
Null and Alternative Hypotheses:
Null Hypothesis (H0): There is no significant difference in heights before and after the use of the herb.
Alternative Hypothesis (H1): There is a significant difference in heights due to the use of the herb.

(e) Unpaired T-test for 2 Independent Populations
Objective: Compare the mean heights of 10 people each from settlement 'A' and tribe 'B'.
Data: Heights of 10 people each from both groups.
Test Applied: Unpaired T-test for two independent populations.
Critical Value: 2.1.
Alpha: Assumed as per standard practice, usually 0.05.
Null and Alternative Hypotheses:
Null Hypothesis (H0): The mean height of people in settlement 'A' is equal to that of people in tribe 'B'.
Alternative Hypothesis (H1): The mean height of people in settlement 'A' is different from that of people in tribe 'B'.


******Instructions for Running the Analysis******

Rename your Python script to a5_q5.py.
Ensure that all data files (height_female.csv, height_female_200.csv, height_male.csv) are in the same directory as the script.
Run the script to perform the analyses and generate the outputs for each task.
Expected Outcomes

The script will output the results of each statistical test, including the test statistic and p-value.
Interpretation of the results based on the null hypotheses and the predetermined alpha levels.
