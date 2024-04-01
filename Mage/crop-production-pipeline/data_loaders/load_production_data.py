import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader



@data_loader
def load_data_from_api(*args, **kwargs):

    continents = ['Africa', 'Americas', 'Asia', 'Europe', 'Ocenia']

    df = pd.DataFrame()
    df['Continents'] = ''


    for i in continents:
        url = "url_" + i.lower()

        if url == "url_africa":
            url = 'https://query.data.world/s/t72nj3qfb2r3cwhkyx32cranhh6k4i?dws=00000'
        elif url == "url_americas":
            url = 'https://query.data.world/s/nk5o7hk2rsh54mspyziuvimkyxpjy6?dws=00000'
        elif url == "url_asia":
            url = 'https://query.data.world/s/wq4zi64ru46vj3aybvtqp6d5rq6567?dws=00000'
        elif url == "url_europe":
            url = 'https://query.data.world/s/z45ad6ewwr6rsf3bf3wo4p4j23vozp?dws=00000'
        else:
            url = 'https://query.data.world/s/rdnnojyh23fzkzpkaplpurypiokdw2?dws=00000'

        df_temp = pd.read_csv(url, encoding = "latin-1")
        df_temp['Continents'] = i
        df = pd.concat([df, df_temp], ignore_index = True)

    return df
