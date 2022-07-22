using Microsoft.Azure.Cosmos;
using Newtonsoft.Json;
using System;

string COSMOS_ENDPOINT = "https://cosmos-db-test1-serverless.documents.azure.com:443/";
string COSMOS_KEY = "LLmkBIfqsclH5vEta5ouBXn03HibZhw77HRqaMFk3STfNzrEcFHb4EAA3lP7mk2CLluSvulyZ9DvFZbfnqxNvQ==";
string JSON_PATH = "gen.json";

try{
    if (args[0] != null){
    COSMOS_ENDPOINT = args[0];
    }

    if (args[1] != null){
        COSMOS_KEY = args[1];
    }

    if (args[2] != null){
        JSON_PATH = args[2];
    }
}
catch(Exception e){
    Console.WriteLine($"Argument not defined!{e}");
}

CosmosClientOptions options = new(){
    AllowBulkExecution = true,
    RequestTimeout = new TimeSpan(0, 0, 90),
    OpenTcpConnectionTimeout = new TimeSpan(0, 0, 90)
};

CosmosClient client = new(COSMOS_ENDPOINT, COSMOS_KEY, options);

// Container container = client.GetContainer("cosmos-db", "Container1");

Database database = await client.CreateDatabaseIfNotExistsAsync(
    id: "cosmos-db"
);

// Container reference with creation if it does not alredy exist
Container container = await database.CreateContainerIfNotExistsAsync(
    id: "products",
    partitionKeyPath: "/PostCode"
);

Console.WriteLine($"New container:\t{container.Id}");


// Data Loading from Json File


List<Item> items = new List<Item>();

using (StreamReader r = new StreamReader(JSON_PATH))
{
    string json = r.ReadToEnd();
    items = JsonConvert.DeserializeObject<List<Item>>(json);
}

// Bulk_Building

List<Task> concurrentTasks = new List<Task>();
foreach(Item item in items){
    // Console.WriteLine(item.Abn);
    concurrentTasks.Add(
        container.CreateItemAsync(
            item,
            new PartitionKey(item.PostCode)
        )
    );
}

Console.WriteLine("Bulk creation done!");

// Send it when it is ready
await Task.WhenAll(concurrentTasks);
