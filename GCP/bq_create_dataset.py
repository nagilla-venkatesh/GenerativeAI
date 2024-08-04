from google.cloud import bigquery

client = bigquery.Client()

datasets_names = ['raw_bikesharing', 'dwh_bikesharing', 'dm_bikesharing']

location = 'US'

def create_bigquery_dataset(dataset_name):
    dataset_id = f'{client.project}.{dataset_name}'
    
    try:
        client.get_dataset(dataset_id)
        print(f'Dataset {dataset_id} already exists.')
    except Exception as e:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(dataset, timeout=30)
        print(f'Dataset {dataset_id} created with {client.project}.')

for name in datasets_names:
    create_bigquery_dataset(name)
    