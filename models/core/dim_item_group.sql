select 
    {{dbt.safe_cast(("item_code"), api.Column.translate_type("integer")) }} as item_code,
    item_group
from {{ ref("itemgroup") }}
