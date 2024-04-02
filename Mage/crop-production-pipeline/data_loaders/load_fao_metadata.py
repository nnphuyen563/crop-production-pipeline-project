import io
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader



@data_loader
def load_data_from_api(*args, **kwargs):
    
    url = 'https://query.data.world/s/phdyb4iyxhtw7p444jl74br44ydvht?dws=00000'
    df_fao = pd.read_csv(url, sep = ',')

    return df_fao

