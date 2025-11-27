import pandas

df = pandas.read_csv("data/daily_sales_data_0.csv")

pink_morsels_df = df[df['product'] == 'pink morsel'].copy()

s_clean = (
    pink_morsels_df["price"]
        .str.replace("$", "", regex=False)
)

s_int = s_clean.astype(float)

pink_morsels_df["price"] = s_int

pink_morsels_df['sales'] = pink_morsels_df['price'] * pink_morsels_df['quantity']

pink_morsels_df = pink_morsels_df[['sales', 'date', 'region']]

print(pink_morsels_df)