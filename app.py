import os
from redisearch import Client, TextField, IndexDefinition

# Creating a client with a given index name
client = Client("index-document")

# IndexDefinition is avaliable for RediSearch 2.0+
definition = IndexDefinition(prefix='doc:')

# Creating the index definition and schema
try:
    client.create_index((TextField("title"), TextField("body")), definition=definition)
except:
    pass

folder = "/home/simran/projects/redisearch/documents/"

for file in os.listdir(folder):    
    filepath = os.path.join(folder, file)
    f = open(filepath, 'r')
    client.redis.hset('doc:'+file,
                mapping={
                    'title': file,
                    'body': f.read()
                })

    f.close()

# Simple search
res = client.search("document")

# the result has the total number of results, and a list of documents
print(res.total) 
print(res.docs) 
