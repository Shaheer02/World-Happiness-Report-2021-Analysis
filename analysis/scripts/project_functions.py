import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(url_or_path_to_csv_file):
  """
  Load and process the given data.
  rename column headings that are necessary and insert columns desired.

  Parameters
  ----------
  url_or_path_to_csv_file : str
      The path to the file.csv.
      
  Returns
  -------
  <class 'pandas.core.frame.DataFrame'>
      The dataFrame containing the cleaned data. 
      
  Examples
  --------
  >>> make_palindrome('../../data/raw/world-happiness-report-2021.csv')
  <class 'pandas.core.frame.DataFrame'>
  """
    
  # supporting file
  data_2020 = pd.read_csv('../../data/raw/world-happiness-report-2020.csv')

  # Method Chain 1 (Load data and deal with missing data)

  # no missing values and the head are self-explanatory except "ladder score"
  data_2021 = (
      pd.read_csv(url_or_path_to_csv_file)
      .rename(columns={'Ladder score': 'Ladder score 2021'})
    )
  print(type(data_2021))
  data_2020 = (
      pd.read_csv('../../data/raw/world-happiness-report-2020.csv')
      .rename(columns={'Ladder score': 'Ladder score 2020'})
  )

  # Method Chain 2 (Create new columns, drop others, and do processing)

  # add column 'Ladder score 2020' and 'Score difference' using pd.dataFrame.insert()
  data_2021.insert(3, 'Ladder score 2020', data_2020['Ladder score 2020'])
  data_2021.insert(4, 'Score difference', data_2021['Ladder score 2021'] - data_2020['Ladder score 2020'])

  # Make sure to return the latest dataframe

  return data_2021

---

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