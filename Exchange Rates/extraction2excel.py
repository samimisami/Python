import pandas as pd

def extraction2excel(dataset, extraction_name):
    if dataset:
        df = pd.DataFrame(dataset)
        
        # Filling Empty Values of buying_rate
        df['buying_rate'] = df['buying_rate'].ffill()

        # Save to Excel
        df.to_excel('output_'+extraction_name+'_EUR-TRY.xlsx', index=False)
