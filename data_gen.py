# import data
import random
import time
import uuid
import json
import sys
import data

def generate_data(no_of_rows, filename):
    objs = []
    random.seed(time.time())
    for i in range(no_of_rows):
        objs.append({
                    'id': str(uuid.uuid4()),
                    "AbrId": "606dda32-b75e-4cf9-a7fd-d726e4f76749",
                    "Abn": str(data.get_ABN_numbers()),
                    "EntityType": "Discretionary Trading Trust",
                    "ASICNumber": 0,
                    "Acn": "",
                    "PostCode": str(data.get_post_code()),
                    "EntityName": data.get_people_name(),
                    "BusinessName": data.get_business_name(),
                    "TradingName": data.get_trading_name(),
                    "State": "WA",
                    "TradingCount": 0,
                    "BusinessCount": 0,
                    "Active": True,
                    "AbnStatus": False,
                    "AcnStatus": False,
                    "LastUpdateDate": "2016-10-10T00:00:00",
                })
        print("Done for file No: {}".format(i+1))

    with open(filename, "w") as f:
        f.write(json.dumps(objs, indent=4))

if __name__ == "__main__":
    no_of_rows = sys.argv[1]
    filname = sys.argv[2]

    generate_data(int(no_of_rows), filname)