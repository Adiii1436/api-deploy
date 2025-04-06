import pandas as pd

def load_data()->pd.DataFrame:
    df = pd.read_csv('final.csv')  

    df['combined_text'] = df['name_idx'] + ' ' + df['test_type_mapped']

    return df