import pandas as pd 
import numpy as np

def read_income():
    # Read in income data 
    df = pd.read_csv('income.csv') 

    # Only keep the row where income["Label (Grouping)"] = "Mean income (dollars)"
    filtered_rows = df[df['Label (Grouping)'] == 'Mean income (dollars)']

    # For columns - assuming you want columns where the name matches a certain pattern
    column_names = []
    for i in range(4, 125):
        column_names.append(f"Census Tract {str(i)}, Hamilton County, Tennessee!!Households!!Estimate")
    filtered_columns = [col for col in df.columns if col in column_names]
    filtered_data = filtered_rows[filtered_columns]

    # write out filtered_data to csv 
    filtered_data.to_csv('income_data_by_tract.csv', index=False)

def read_vehicle():
    df = pd.read_csv('private_vehicle.csv')
    filtered_rows = df[df['Label (Grouping)'] == '    Private vehicle occupancy']
        # For columns - assuming you want columns where the name matches a certain pattern
    column_names = []
    for i in range(4, 125):
        column_names.append(f"Census Tract {str(i)}, Hamilton County, Tennessee!!Total!!Estimate")
    filtered_columns = [col for col in df.columns if col in column_names]
    filtered_data = filtered_rows[filtered_columns]
    # write out filtered_data to csv 
    filtered_data.to_csv('vehicle_data_by_tract.csv', index=False)

def make_heuristic():
    # Read in the saved data 
    income_df = pd.read_csv('income_data_by_tract.csv')
    vehicle_df = pd.read_csv('vehicle_data_by_tract.csv')
    tract_column = income_df.columns

    # verify that the data is the same shape
    assert income_df.shape == vehicle_df.shape

    # convert the data to 1d arrays
    income_data = income_df.values.flatten()
    vehicle_data = vehicle_df.values.flatten()

    # convert income data to integers 
    income_data = [int(i.replace(",", "")) for i in income_data]
    vehicle_data = [float(i.replace("%", "")) for i in vehicle_data]

    # noramlize the data 
    income_data = np.array(income_data)
    income_data = income_data / np.linalg.norm(income_data)
    vehicle_data = np.array(vehicle_data)
    vehicle_data = vehicle_data / np.linalg.norm(vehicle_data)

    # Invert the normalized values
    income_data_inverted = 1 - income_data
    vehicle_data_inverted = 1 - vehicle_data

    # Create a new array that takes a linear combination of the two inverted arrays
    heuristic = 0.5 * income_data_inverted + 0.5 * vehicle_data_inverted

    # write priority score out to csv by track
    heuristic_df = pd.DataFrame({'tract': tract_column, 'heuristic': heuristic})
    heuristic_df.to_csv('heuristic_by_tract.csv', index=False)

    print(heuristic)

read_income()
read_vehicle()
make_heuristic()