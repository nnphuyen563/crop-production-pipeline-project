import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_api(download_info_product, *args, **kwargs) -> pd.DataFrame:

    file_name = download_info_product['file_name']
    df_name = download_info_product['df_name']
    metadata = [
        {
            "file_name": file_name,
            "df_name": df_name,
        }
    ]

    url = download_info_product['url']

    df = pd.read_csv(url, encoding='latin1')

    return [df, metadata]

