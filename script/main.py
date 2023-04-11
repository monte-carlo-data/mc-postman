import json
import os
from datetime import datetime
import sys

def get_date():
    return datetime.today().strftime('%Y-%m-%d_%H:%M:%S')

def replace_keys(id, key):
    with open('new.json', 'r') as f:
        data = f.read()
        data = data.replace(id, "{{x-mcd-id}}")
        data = data.replace(key, "{{x-mcd-token}}")

    with open('new.json', 'w') as f:
        f.write(data)

def main(id, key):
    replace_keys(id, key)

    with open('mc_postman_collection.json', 'r') as f1:
        f1_data = json.load(f1)

    with open('new.json', 'r') as f2:
        f2_data = json.load(f2)

    if f1_data == f2_data:
        os.remove('new.json')
    else:
        os.rename('mc_postman_collection.json', f'archive/mc_postman_collection_{get_date()}.json')
        os.rename('new.json', 'mc_postman_collection.json')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])