import pandas as pd

def extraction2excel(dataset, extraction_name):
    if dataset:
        df = pd.DataFrame(dataset)
        # print(df)
        
        df['buying_rate'].ffill(inplace=True)

        # Save to Excel
        df.to_excel(extraction_name+'_EUR-TRY.xlsx', index=False)
