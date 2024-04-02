{{
    config(
        materialized='view'
    )
}}
with 

source as (

    select * from {{ source('staging', 'product_europe') }}

),

renamed as (

    select
        area_code,
        area,
        item_code,
        item,
        element_code,
        element,
        unit,
        y1961,
        y1961f,
        y1962,
        y1962f,
        y1963,
        y1963f,
        y1964,
        y1964f,
        y1965,
        y1965f,
        y1966,
        y1966f,
        y1967,
        y1967f,
        y1968,
        y1968f,
        y1969,
        y1969f,
        y1970,
        y1970f,
        y1971,
        y1971f,
        y1972,
        y1972f,
        y1973,
        y1973f,
        y1974,
        y1974f,
        y1975,
        y1975f,
        y1976,
        y1976f,
        y1977,
        y1977f,
        y1978,
        y1978f,
        y1979,
        y1979f,
        y1980,
        y1980f,
        y1981,
        y1981f,
        y1982,
        y1982f,
        y1983,
        y1983f,
        y1984,
        y1984f,
        y1985,
        y1985f,
        y1986,
        y1986f,
        y1987,
        y1987f,
        y1988,
        y1988f,
        y1989,
        y1989f,
        y1990,
        y1990f,
        y1991,
        y1991f,
        y1992,
        y1992f,
        y1993,
        y1993f,
        y1994,
        y1994f,
        y1995,
        y1995f,
        y1996,
        y1996f,
        y1997,
        y1997f,
        y1998,
        y1998f,
        y1999,
        y1999f,
        y2000,
        y2000f,
        y2001,
        y2001f,
        y2002,
        y2002f,
        y2003,
        y2003f,
        y2004,
        y2004f,
        y2005,
        y2005f,
        y2006,
        y2006f,
        y2007,
        y2007f,
        y2008,
        y2008f,
        y2009,
        y2009f,
        y2010,
        y2010f,
        y2011,
        y2011f,
        y2012,
        y2012f,
        y2013,
        y2013f,
        y2014,
        y2014f,
        y2015,
        y2015f,
        y2016,
        y2016f,
        y2017,
        y2017f,
        y2018,
        y2018f,
        y2019,
        y2019f

    from source

)

select * from renamed
