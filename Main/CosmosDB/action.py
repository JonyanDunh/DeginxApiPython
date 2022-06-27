import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import os
from Main.CosmosDB.model import default_creat_user_model
from Main.Action import encrypt
import json
settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://deginx-cosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'IXIGApp6sASfyToiEQpdAHDH9IkcUqpihjKIFcv6MpucQkESFiWxxjc7Qfjc49xdnpbyCTZrteADuUcxg7foPg=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'user'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'user'),
    'tenant_id': os.environ.get('TENANT_ID', '[YOUR TENANT ID]'),
    'client_id': os.environ.get('CLIENT_ID', '[YOUR CLIENT ID]'),
    'client_secret': os.environ.get('CLIENT_SECRET', '[YOUR CLIENT SECRET]'),
}

HOST = settings['host']
MASTER_KEY = settings['master_key']
DATABASE_ID = settings['database_id']
CONTAINER_ID = settings['container_id']

client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )
db = client.create_database_if_not_exists(id=DATABASE_ID)
container = db.create_container_if_not_exists(id=CONTAINER_ID, partition_key=PartitionKey(path='/username', kind='Hash'))

def create_user(user):
    user_information = default_creat_user_model(user)
    container.create_item(body= user_information)

def get_user_uuid(user):
    user_json=''
    users=container.query_items(query='SELECT * FROM mycontainer r WHERE r.username="'+user["username"]+'"',enable_cross_partition_query=True)
    for user in users:
        user_json=user
    return user_json["id"]

def get_user(user):
    # Note that Reads require a partition key to be spcified.
    response = container.read_item(item=get_user_uuid(user), partition_key=user["username"])
    user_information={'id' : response["id"],
            'username':response["username"],
            'email' : response["email"]
            }
    return user_information
    #return  json.dumps(user_information, indent=True)
    


def get_all_user():
    item_list = list(container.read_all_items(max_item_count=10))

    print('Found {0} items'.format(item_list.__len__()))

    for doc in item_list:
        print('Item Id: {0}'.format(doc.get('id')))


def query_users(user):
    print('\n1.4 Querying for an  Item by Id\n')

    # enable_cross_partition_query should be set to True as the container is partitioned
    items = list(container.query_items(
        query="SELECT * FROM r WHERE r.id=@id",
        parameters=[
            { "name":"@id", "value": encrypt.md5_hash(user["email"]) }
        ],
        enable_cross_partition_query=True
    ))

    print('Item queried by Id {0}'.format(items[0].get("id")))


def replace_item(container, doc_id):
    print('\n1.5 Replace an Item\n')

    read_item = container.read_item(item=doc_id, partition_key=doc_id)
    read_item['subtotal'] = read_item['subtotal'] + 1
    response = container.replace_item(item=read_item, body=read_item)

    print('Replaced Item\'s Id is {0}, new subtotal={1}'.format(response['id'], response['subtotal']))


def upsert_item(container, doc_id):
    print('\n1.6 Upserting an item\n')

    read_item = container.read_item(item=doc_id, partition_key=doc_id)
    read_item['subtotal'] = read_item['subtotal'] + 1
    response = container.upsert_item(body=read_item)

    print('Upserted Item\'s Id is {0}, new subtotal={1}'.format(response['id'], response['subtotal']))


def delete_item(container, doc_id):
    print('\n1.7 Deleting Item by Id\n')

    response = container.delete_item(item=doc_id, partition_key=doc_id)

    print('Deleted item\'s Id is {0}'.format(doc_id))