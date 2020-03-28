# DFA Final Project
## Industrial Problem
#### Clincal Trial Records are valuable documents containing enormous information, which could potentially help in a large range of fields like new clinical trial designing, pharmaceutical analysis and regulation analysis.
#### Clinicaltrials.gov is an offical open database for clincal trial records. A law has enforced all clinical trial sponsors to release their data in this website since 2007. So it's important to know how well is this data disclosure process practiced.
#### We would like to know how the completeness of these changes over time, this is the key industrial question for this project.
## Data Problem
#### How the completeness changed as a function of time(year-submitted) from 1999-2020(the dataset has no data before 1999)
## Data Answer
### Initial Data Analysis Conclusion:
- Most records have only less than 50% completeness.Some datafields has less than 50% completemness.
- The completeness of data changed following a trend of going up first and going down with a turning point at 2007
- The upgoing part and the downgoing part both fit well into a linear regression model
### Data Result Reasoning
#### Question:
What caused this turing point at year 2007, which seemingly is the opposite of what should happen after 2007 data disclosure bill?
#### Hypothesis:
- 1.More records were put into the datset with law enforce, which "diluted" the data completeness
- 2.As clinical trial takes a long time the data may be missing due to on-going trials
#### Data Analysis to test this two hypothesis:
- Analyze the trend of number of Records over time
- Analyze the %of ongoing cases over time
#### Data Results:
- Though since 2004 the number of records is growing consistently,NO signicificant change of number of records submitted near the time point 2007.
- Due to a chaotic value-set(a lot of missing or ambiguous data), no analysis is conducted w.r.t. trial status distribution over time
#### Conclusion:
- Hypothesis 1 disconfirmed.
- Hypothesis 2 Unknown
## Industrial Answer
#### The record completeness follows a linear trend of going upfirst from 1999-2008 and then going down from 2008-2020
#### It seems the 2007 FDA data disclosure bill is not working as intended
#### The reason of this is still unknown. Further research on this is need for a better policy in the future.


## Data Source
(https://www.clinicaltrials.gov)

### Original data are in .xml format 
