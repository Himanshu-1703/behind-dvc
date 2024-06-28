import pandas as pd
from pathlib import Path


URL = 'https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv'


def read_data_from_url(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    return df


def select_numerical_only(df: pd.DataFrame) -> pd.DataFrame:
    df_selected = df.select_dtypes(include='number')
    return df_selected
    
    
def save_data(df: pd.DataFrame, save_path: Path) -> None:
    df.to_csv(save_path,index=False)
    
    
def filter_length_of_membership(df: pd.DataFrame, filter_value: int) -> pd.DataFrame:
    column_name = "Length of Membership"
    df_filtered = df.loc[df[column_name].ge(filter_value), :]
    return df_filtered
   
    
def main():
    root_path = Path(__file__).parent.parent
    data_save_path = root_path / 'data' / 'customer.csv'
    
    # read the data from url
    df = read_data_from_url(URL)
    # select only numerical columns
    df_numerical = select_numerical_only(df=df)
    # filter the data based on condition
    filter_value = 3
    df_final = filter_length_of_membership(df=df_numerical,
                                           filter_value=filter_value)
    # save the final dataframe to save location
    save_data(df=df_final,save_path=data_save_path)
    

if __name__ == "__main__":
    main()