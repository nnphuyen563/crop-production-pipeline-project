CREATE OR REPLACE TABLE `crop-production-project.crop_production_dataset._cluster`
CLUSTER BY area AS (
    SELECT * FROM {{ df_1 }}
)