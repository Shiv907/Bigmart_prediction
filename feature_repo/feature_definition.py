from datetime import timedelta

import pandas as pd

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource,
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int64

# Define an entity for the driver. You can think of an entity as a primary key used to
# fetch features.
from feast import ValueType

items = Entity(
    name="item_id",
    value_type=ValueType.INT64,
    description="ID of the patient",
)

## Predictors Feature View
file_source = FileSource(path = r"data/predictors_df.parquet",
                         event_timestamp_column = "event_timestamp",)

df1_fv = FeatureView(
    name="predictors_df_feature_view",
    ttl=timedelta(seconds=86400*2),
    entities=[items],
    schema=[
        Field(name="Item_Weight", dtype=Int64),
        Field(name="Item_Visibility", dtype=Int64),
        Field(name="Item_MRP", dtype=Int64),
        Field(name="Outlet_Years", dtype=Int64),
        Field(name="Item_Visibility_MeanRatio", dtype=Int64),
        Field(name="Item_Fat_Content_0", dtype=Float64),
        Field(name="Item_Fat_Content_1", dtype=Float64),
        Field(name="Item_Fat_Content_2", dtype=Int64),
        Field(name="Outlet_Size_0", dtype=Int64),
        Field(name="Outlet_Size_1", dtype=Int64),
        Field(name="Outlet_Size_2", dtype=Int64),
        Field(name="Outlet_Years", dtype=Int64),
        Field(name="Outlet_Location_Type_0", dtype=Int64),
        Field(name="Outlet_Location_Type_1", dtype=Float64),
        Field(name="Outlet_Location_Type_2", dtype=Float64),
        Field(name="Outlet_Type_0", dtype=Int64),
        Field(name="Outlet_Type_1", dtype=Int64),
        Field(name="Outlet_Type_2", dtype=Int64),
        Field(name="Outlet_Type_3", dtype=Int64),
        Field(name="Item_Type_Combined_0", dtype=Int64),
        Field(name="Item_Type_Combined_1", dtype=Int64),
        Field(name="Item_Type_Combined_2", dtype=Int64),        
        
    ],
    source=file_source,
    online=True,
    tags={},
)

target_source = FileSource(path = r"data/target_df.parquet",
                         event_timestamp_column = "event_timestamp",)

target_fv = FeatureView(
    name="target_df_feature_view",
    ttl=timedelta(seconds=86400*2),
    entities=[items],
    schema=[
        Field(name="Item_Outlet_Sales", dtype=Int64),
    ],
    source=target_source,
    online=True,
    tags={},
)