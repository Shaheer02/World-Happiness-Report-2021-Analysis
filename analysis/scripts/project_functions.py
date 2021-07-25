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
    >>> load_and_process(path_2021='../../data/raw/world-happiness-report-2021.csv', path_2020='../../data/raw/world-happiness-report-2020.csv')
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
    )
    
    return df