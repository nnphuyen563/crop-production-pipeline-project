from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    metadata = [
        {"file_name": kwargs["file_name"]}
    ]

    df.columns = (df.columns
        .str.replace(' ', '_')
        .str.lower()      
        )

    df['area_code'] = df['area_code'].astype(np.int64)
    df['item_code'] = df['item_code'].astype(np.int64)
    df['element_code'] = df['element_code'].astype(np.int64)

    del_index = set()

    for record in range(len(df)):
        for i in range(1961, 2020, 1):
            col_name = f"y{i}f"
            if df.iloc[record]["y2019f"] == "M":
                del_index.add(record)
            elif df.iloc[record][col_name] == "M":
                continue
            else:
                break
    df.drop(df.index[list(del_index)], inplace=True)

    return [df, metadata]
