from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:

    metadata = [
        {"file_name": kwargs["file_name"]}
    ]

    df.columns = (df.columns
            .str.replace(" ", "_")
            .str.lower()
    )

    return [df, metadata]
