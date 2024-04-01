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
    
    df.columns = (df.columns
        .str.replace(' ', '_')
        .str.lower()      
        )

    df['area_code'] = df['area_code'].astype(np.int64)
    df['item_code'] = df['item_code'].astype(np.int64)
    df['element_code'] = df['element_code'].astype(np.int64)

    return df
