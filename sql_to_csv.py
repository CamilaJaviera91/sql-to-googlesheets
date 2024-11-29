import pandas as pd
from queries import amounts_quantity as aq

def sql_to_csv():
    df = pd.DataFrame(aq())
    folder = './/'
    output_file_path = folder+'vehicle_circulation_permit.csv'
    df.to_csv(output_file_path, index=False)
    print(".csv file successfully created")
    
    return df.to_csv(output_file_path, index=False)