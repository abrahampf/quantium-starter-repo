import pandas

def cleanPrice(df):
    s_clean = (
        df["price"]
            .str.replace("$", "", regex=False)
    )

    s_int = s_clean.astype(float)

    df["price"] = s_int
    return 
    
def main():
    files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]
    first = True

    for file in files:
        df = pandas.read_csv(file)
        df = df[df['product'] == 'pink morsel'].copy()
        cleanPrice(df)
        df['sales'] = df['price'] * df['quantity']
        df = df[['sales', 'date', 'region']]
        if first:
            df.to_csv("pink_m_sales.csv")
            first = False
        else:
            df.to_csv(
                "pink_m_sales.csv",
                mode="a",
                index=False,
                header=False)


main()
