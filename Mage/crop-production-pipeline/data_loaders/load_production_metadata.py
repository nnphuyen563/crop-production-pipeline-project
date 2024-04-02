import pandas as pd
from typing import Dict, List

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_api(*args, **kwargs) -> List[List[Dict]]:

    download_info_product = []
    continents = ['americas', 'africa', 'asia', 'europe', 'oceania']

    for i in continents:

        url = f'url_{i}'
        df_name = "df_production_" + i

        if url == "url_americas":
            url = "https://query.data.world/s/yw4p5llqlrf7kyextlbrdl2jldpv3j?dws=00000"
        elif url == "url_africa":
            url = "https://query.data.world/s/qvrzgjzy2l3lpptngpx7mnoussk5h7?dws=00000"
        elif url == "url_asia":
            url = "https://query.data.world/s/t5tg3jxm6cesrilrswg6ctxzfedags?dws=00000"
        elif url == "url_europe":
            url = "https://query.data.world/s/xctyjpwtzuwo7igw74walvrvc7f53k?dws=00000"
        else:
            url = "https://query.data.world/s/jvdyudbmvhuydialwujlcyqerxstze?dws=00000"
            
        download_info_product.append(dict(file_name = i, df_name = df_name, url = url))


    return [download_info_product]