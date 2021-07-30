import pandas as pd

def load_and_process(path_2021, path_2020):
    """
    Load and process the given data.
    rename column headings that are necessary and insert columns desired.

    Parameters
    ----------
    path_2021 : str
      The path to world-happiness-report-2021.csv
    path_2020 : str
      The path to world-happiness-report-2020.csv

    Returns
    -------
    <class 'pandas.core.frame.DataFrame'>
      The dataFrame containing the cleaned data. 

    Examples
    --------
    >>> load_and_process_karel(path_2021='../../data/raw/world-happiness-report-2021.csv', path_2020='../../data/raw/world-happiness-report-2020.csv')
    <class 'pandas.core.frame.DataFrame'>
    """
    # read supporting file
    data_2021 = pd.read_csv(path_2021)
    data_2020 = pd.read_csv(path_2020)
    
    # no need for cleaning since data has no missing value and sorted decendingly by ladder score
    # method chain for data wrangling
    df = (
        data_2021.assign(Ladder_score_2020 = data_2020['Ladder score'],
                         Score_difference = data_2021['Ladder score'] - data_2020['Ladder score'])
        .rename(columns={'Ladder score': 'Ladder score 2021',
                         'Ladder_score_2020': 'Ladder score 2020',
                         'Score_difference': 'Score difference'})
        .dropna()
        .reset_index()
        .drop(columns=['index', 'Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                       'Explained by: Log GDP per capita', 'Explained by: Social support',
                       'Explained by: Healthy life expectancy', 'Explained by: Freedom to make life choices',
                       'Explained by: Generosity', 'Explained by: Perceptions of corruption',
                       'Dystopia + residual'])
    )
    
    return df

def load_and_process_kaitlyn():    
    # Method Chain 1
    # No Missing Data 
    happiness2020 = pd.read_csv("/Users/kaitlynpeverley/Desktop/COSC301/Labs/project-group10-project/data/raw/world-happiness2020.csv")
    happiness2021 = pd.read_csv("/Users/kaitlynpeverley/Desktop/COSC301/Labs/project-group10-project/data/raw/world-happiness-report-2021.csv")

    # Method Chain 2 
    happinessdata1 = (happiness2021
                     .rename(columns={'Country name': 'Country Name', 
                                      'Regional indicator': 'Regional Indicator', 
                                      'Ladder score': 'Ladder Score', 
                                      'Standard error of ladder score': 'Standard Error of Ladder Score', 
                                      'upperwhisker': 'Upper Whisker', 
                                      'lowerwhisker': 'Lower Whisker', 
                                      'Logged GDP per capita': 'Logged GDP Per Capita', 
                                      'Social support': 'Social Support',
                                      'Healthy life expectancy': 'Healthy Life Expectancy',
                                      'Freedom to make life choices': 'Freedom to Make Life Choices',
                                      'Perceptions of corruption': 'Perceptions of Corruption',
                                      'Ladder score in Dystopia': 'Ladder Score in Dystopia',
                                      'Explained by: Log GDP per capita': 'Explained by: Log GDP per Capita',
                                      'Explained by: Perceptions of corruption': 'Explained by: Perceptions of Corruption',
                                      'Explained by: Social support': 'Explained by: Social Support',
                                      'Explained by: Healthy life expectancy': 'Explained by: Healthy Life Expectancy',
                                      'Explained by: Freedom to make life choices': 'Explained by: Freedom to make Life Choices',
                                      'Dystopia + residual': 'Dystopia and Residual',
                                      'Ladder score': 'Ladder score 2021'})
                   .insert(3, 'Ladder Score Percent Change From Previous Year', ((happiness2021['Ladder score'] - happiness2020['Ladder  score'])/happiness2020['Ladder score'])*100))

    return happinessdata1

def load_and_process_shaheer(urlOrPathCSV1, urlOrPathCSV2):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = pd.read_csv(urlOrPathCSV1).dropna(axis='rows',how='any')
          

    # Method Chain 2 (drop columns, rename columns and do processing)

    df1 = df1.loc[:,'Country name':'Perceptions of corruption'].drop(['upperwhisker','lowerwhisker'], axis='columns').rename(columns={'Ladder score':'Ladder score 2021'})


    # Method Chain 3 (Add new columns and reorder)
    df2 = pd.read_csv(urlOrPathCSV2)
    df1.insert(3,'Ladder score 2020',df2['Ladder score'])
    df1.insert(4,'Ladder score difference (2021 subtracted by 2020)',df1['Ladder score 2021'] - df1['Ladder score 2020'])
    temp = df1['Standard error of ladder score']
    df1 = df1.drop('Standard error of ladder score',axis='columns')
    df1.insert(3,'Standard error of ladder score 2021',temp)
    df1.insert(5,'Standard error of ladder score 2020',df2['Standard error of ladder score'])
    
    return df1
