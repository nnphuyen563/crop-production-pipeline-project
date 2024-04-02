{{
    config(
        materialized='table'
    )
}}
with africa as (
    select *,
        "Africa" as continent
    from {{ ref("stg_product_africa") }}
),
americas as (
    select *,
        "America" as continent
    from {{ ref("stg_product_americas") }}
),
asia as (
    select *,
        "Asia" as continent
    from {{ ref("stg_product_asia") }}
),
europe as (
    select *,
        "Europe" as continent
    from {{ ref("stg_product_europe") }}
),
oceania as (
    select *,
        "Oceania" as continent
    from {{ ref("stg_product_oceania") }}
),
product_unioned as (
    select * from africa
    union all
    select * from americas
    union all
    select * from asia
    union all
    select * from europe
    union all
    select * from oceania
)
select
    product_unioned.continent,
    product_unioned.area_code,
    product_unioned.area,
    product_unioned.item_code,
    product_unioned.item,
    product_unioned.element_code,
    product_unioned.element,
    product_unioned.unit,
    product_unioned.y1961,
    product_unioned.y1962,
    product_unioned.y1963,
    product_unioned.y1964,
    product_unioned.y1965,
    product_unioned.y1966,
    product_unioned.y1967,
    product_unioned.y1968,
    product_unioned.y1969,
    product_unioned.y1970,
    product_unioned.y1971,
    product_unioned.y1972,
    product_unioned.y1973,
    product_unioned.y1974,
    product_unioned.y1975,
    product_unioned.y1976,
    product_unioned.y1977,
    product_unioned.y1978,
    product_unioned.y1979,
    product_unioned.y1980,
    product_unioned.y1981,
    product_unioned.y1982,
    product_unioned.y1983,
    product_unioned.y1984,
    product_unioned.y1985,
    product_unioned.y1986,
    product_unioned.y1987,
    product_unioned.y1988,
    product_unioned.y1989,
    product_unioned.y1990,
    product_unioned.y1991,
    product_unioned.y1992,
    product_unioned.y1993,
    product_unioned.y1994,
    product_unioned.y1995,
    product_unioned.y1996,
    product_unioned.y1997,
    product_unioned.y1998,
    product_unioned.y1999,
    product_unioned.y2000,
    product_unioned.y2001,
    product_unioned.y2002,
    product_unioned.y2003,
    product_unioned.y2004,
    product_unioned.y2005,
    product_unioned.y2006,
    product_unioned.y2007,
    product_unioned.y2008,
    product_unioned.y2009,
    product_unioned.y2010,
    product_unioned.y2011,
    product_unioned.y2012,
    product_unioned.y2013,
    product_unioned.y2014,
    product_unioned.y2015,
    product_unioned.y2016,
    product_unioned.y2017,
    product_unioned.y2018,
    product_unioned.y2019
from product_unioned