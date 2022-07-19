from azure.cosmos import exceptions, PartitionKey, CosmosClient
from azure.cosmos.aio import CosmosClient as CosmosClientAio
import data
import asyncio
import json
import config
import uuid
import time
import random 

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

async def create_item(loop):
    async with CosmosClientAio(HOST, credential=MASTER_KEY) as client:
        database = client.get_database_client(DATABASE_ID)
        container = await database.create_container_if_not_exists(
                                                            id=CONTAINER_ID, 
                                                            partition_key=PartitionKey(path="/lastName"),
                                                            offer_throughput=1000
                                                        )
        # Add items to the container
        # <create_item>
        start_time = time.time()
        for i in range(0, 2*10**7):
            await container.create_item(body={
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
                # "id": "bf855ce3-b694-4c26-9e3a-2bec97261308",
                # "type": "AbrIndex",
                # "PartitionKey": "6169",
                # "_rid": "epxIAMDtU-QBAAAAAAAAAA==",
                # "_self": "dbs/epxIAA==/colls/epxIAMDtU-Q=/docs/epxIAMDtU-QBAAAAAAAAAA==/",
                # "_etag": "\"0700deb5-0000-1c00-0000-62bec41b0000\"",
                # "_attachments": "attachments/",
                # "_ts": 1656669211
            })
        request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
        print('Create items. Operation consumed {0} request units'.format((request_charge)))
        # </create_item>
        print("Total Time to insert 20 million data: {}".format(str(time.time()-start_time)))

async def read_item(loop):
    async with CosmosClientAio(HOST, credential=MASTER_KEY) as client:
        database = client.get_database_client(DATABASE_ID)
        container = await database.create_container_if_not_exists(
                                                            id=CONTAINER_ID, 
                                                            partition_key=PartitionKey(path="/lastName"),
                                                            offer_throughput=400
        )

        # Query these items using the SQL query syntax. 
        # Specifying the partition key value in the query allows Cosmos DB to retrieve data only from the relevant partitions, which improves performance
        # <query_items>
        query = "SELECT * FROM c WHERE c.lastName IN ('Wakefield', 'Andersen')"
        items = container.query_items(
            query=query,
            enable_cross_partition_query=True
        )
        request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
        print('Query returned items. Operation consumed {1} request units'.format(request_charge))

        async for item in items:
            print(json.dumps(item, indent=True))

def get_item_count():
    
    client = CosmosClient(HOST, credential=MASTER_KEY)
    database = client.get_database_client(DATABASE_ID)
    container = database.get_container_client(CONTAINER_ID)
    query = "SELECT VALUE COUNT(1) FROM c"

    items = list(container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
    for item in items:
        print(item)

    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

    print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))

# METHOD CALL
def run_sample():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_item(loop))
    loop.close()   
    get_item_count()

    # loop = asyncio.get_event_loop()
    # # Blocking call which returns when the create_item() coroutine is done
    # loop.run_until_complete(read_item(loop))
    # loop.close()   


if __name__ == '__main__':
    run_sample()