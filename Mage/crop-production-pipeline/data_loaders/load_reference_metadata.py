import pandas as pd
from typing import Dict, List

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_api(*args, **kwargs) -> List[List[Dict]]:

    download_info = []
    data = ['elements', 'flags', 'items', 'units']

    for i in data:

        url = f'url_{i}'
        df_name = "df_" + i

        if url == "url_elements":
            url = "https://query.data.world/s/3xxorrcjf2mpvoszwky5cszn6ag5uk?dws=00000"
        elif url == "url_flags":
            url = "https://query.data.world/s/epzeijuc7nxtxfmhzdaz5k6ragyruz?dws=00000"
        elif url == "url_items":
            url = "https://query.data.world/s/grel4mw5pt35yls433tgxuuspoxkiu?dws=00000"
        else:
            url = "https://query.data.world/s/ts2xvzrphahavtb5xsjdrdl7degxxn?dws=00000"
        
        download_info.append(dict(file_name = i, df_name = df_name, url = url))


    return [download_info]