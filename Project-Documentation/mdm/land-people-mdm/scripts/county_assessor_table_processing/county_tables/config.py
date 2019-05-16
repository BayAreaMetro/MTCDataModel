import os

step_1_output_dir = 'step_1_outputs'
csv_dir = os.path.join(step_1_output_dir, 'csv_data')
columns_dir = os.path.join(step_1_output_dir, 'data_features')
step_2_output_dir = 'step_2_outputs'
step_3_output_dir = 'step_3_outputs'

# Make into Redshift table?
fipco_mapping = {'Alameda': 'CA001',
                 'Contra_Costa': 'CA013',
                 'Marin': 'CA041',
                 'Napa': 'CA055',
                 'San_Francisco': 'CA075',
                 'San_Mateo': 'CA081',
                 'Santa_Clara': 'CA085',
                 'Solano': 'CA095',
                 'Sonoma': 'CA097'}