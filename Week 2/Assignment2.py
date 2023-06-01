# rian-kh, 06/01/23
# Coursera: Introduction to Data Science in Python (University of Michigan)
# Week 2: Assignment 2

# Question 1
# Write a function called proportion_of_education which returns the proportion of children
# in the dataset who had a mother with the education levels equal to less than high school (<12),
# high school (12), more than high school but not a college graduate (>12) and college degree.
# This function should return a dictionary in the form of (use the correct numbers, do not round numbers):
#     {"less than high school":0.2,
#     "high school":0.4,
#     "more than high school but not college":0.2,
#     "college":0.2}

import pandas as pd


def proportion_of_education():

    # Your code here
    df = pd.read_csv('assets/NISPUF17.csv', na_filter=True)

    # Get the number of children by finding the last value of the first column
    numChildren = df.T.iloc[0, -1]

    # Find the number of less than/equal to/more than high school education,
    # and number of college education
    numLess = len(df['EDUC1'].where(df['EDUC1'] == 1).dropna())
    numEq = len(df['EDUC1'].where(df['EDUC1'] == 2).dropna())
    numMore = len(df['EDUC1'].where(df['EDUC1'] == 3).dropna())
    numColl = len(df['EDUC1'].where(df['EDUC1'] == 4).dropna())

    # Return dictionary of the respective ratioes compared to the total number of children
    return {"less than high school": numLess / numChildren,
            "high school": numEq / numChildren,
            "more than high school but not college": numMore / numChildren,
            "college": numColl / numChildren}



# Question 2
# Let's explore the relationship between being fed breastmilk as a child and
# getting a seasonal influenza vaccine from a healthcare provider.
# Return a tuple of the average number of influenza vaccines for those children
# we know received breastmilk as a child and those who know did not.
# This function should return a tuple in the form (use the correct numbers:
#   (2.5, 0.1)

def average_influenza_doses():

    # Your code here
    df = pd.read_csv('assets/NISPUF17.csv', na_filter=True)

    # Create sub-dataframes if the child was/wasn't breastfed,
    # and include only the number of shots as the other column
    milkTrue = df[['CBF_01', 'P_NUMFLU']][df['CBF_01'] == 1].dropna()
    milkFalse = df[['CBF_01', 'P_NUMFLU']][df['CBF_01'] == 2].dropna()

    # Return a tuple of the ratio of total shots to number of children
    # in the respective categories
    return (milkTrue['P_NUMFLU'].sum() / len(milkTrue), milkFalse['P_NUMFLU'].sum() / len(milkFalse))



# Question 3
# It would be interesting to see if there is any evidence of a link between vaccine effectiveness
# and sex of the child. Calculate the ratio of the number of children who contracted chickenpox
# but were vaccinated against it (at least one varicella dose) versus those who were vaccinated
# but did not contract chicken pox. Return results by sex.
# This function should return a dictionary in the form of (use the correct numbers):
#     {"male":0.2,
#     "female":0.4}

def chickenpox_by_sex():

    # Your code here
    df = pd.read_csv('assets/NISPUF17.csv', na_filter=True)
    # Only include the sex, vaccine and had chickepox columns
    df = df[['SEX', 'P_NUMVRC', 'HAD_CPOX']]

    # Create sub-dataframes of males and females, where
    # they both have at least one vaccine.
    males = df[(df['SEX'] == 1) & (df['P_NUMVRC'] >= 1)]
    females = df[(df['SEX'] == 2) & (df['P_NUMVRC'] >= 1)]

    # Return dictionary of the ratio for each gender of
    # if they had or didn't have chickenpox, and they all have
    # had at least one vaccine
    return {"male": len(males[males['HAD_CPOX'] == 1]) / len(males[males['HAD_CPOX'] == 2]),
            "female": len(females[females['HAD_CPOX'] == 1]) / len(females[females['HAD_CPOX'] == 2])}



# Question 4
# A correlation is a statistical relationship between two variables.
# If we wanted to know if vaccines work, we might look at the correlation between
# the use of the vaccine and whether it results in prevention of the infection or disease [1].
# In this question, you are to see if there is a correlation between having had the chicken pox
# and the number of chickenpox vaccine doses given (varicella).

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    # Your code here
    df = pd.read_csv('assets/NISPUF17.csv', na_filter=True)
    # Only include the vaccine and had chickenpox columns
    df = df[['P_NUMVRC', 'HAD_CPOX']].dropna()

    # Only include children that have a confirmed Yes/No for chickenpox
    # (Values 3-5 are unsure)
    df = df[df['HAD_CPOX'] < 3]

    # GIVEN CODE: here is some stub code to actually run the correlation
    corr, pval = stats.pearsonr(df['P_NUMVRC'], df['HAD_CPOX'])

    # just return the correlation
    return corr


