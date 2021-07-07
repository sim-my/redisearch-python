# RediSearch-Python Client
Python Client for performing Redisearch feeding multiple files from a folder

## Steps to run this repository

#### Step 1: Clone this repository
`git clone git@github.com:sim-my/redisearch-python.git` 

#### Step 2: Create a virtual environment
`python3 -m venv venv`

#### Step 3: Install requirements
`pip install -r requirement.txt`

#### Step 4: Install RediSearch with docker image
`docker run -p 6379:6379 redislabs/redisearch:latest`

#### Step 5: Run app.py file
`python3 ./app.py`
