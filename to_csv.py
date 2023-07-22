import json
import csv
import os



for thn in [2020,2021,2022,2023]:
    path = f'dataset/{thn}/distribution_map'
    files =  os.listdir(path)
    for file in files:
        try:
            filename = os.path.splitext(file)[0]
            if file.endswith('.json'):
                with open(os.path.join(path, file)) as json_file:
                    json_data = json.load(json_file)


                with open(f'export/{thn}/distribution_map/{filename}.csv', 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(json_data[0].keys())
                    for row in json_data:
                        csv_writer.writerow(row.values())
        except:
            pass


