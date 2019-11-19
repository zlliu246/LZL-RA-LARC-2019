# LZL-RA-LARC-2019
repo for research assistantship for LARC Sep-Nov 2019

## Setting up the application
```
pip install -r requirements.txt
py app.py
```
- 3) go to chrome and type "localhost:5000"

## Query Api
- endpoint: /api/query
- parameters:
    - query (question to be asked)
    - num_results (number of results to return - default=3)

- sample input:
```
localhost:5000/api/query?query=test question here&num_results=5
```

- sample output:
```
{
  "query": "testing question", 
  "results": [
    {
      "response": "sample response 1", 
      "score": 2.738019, 
      "time taken": 5.390608310699463, 
      "url": "https://random-url.com/"
    }, 
    {
      "response": "sample response 2", 
      "score": 1.9605274661184546, 
      "time taken": 2.8204832077026367, 
      "url": "https://random-url2.com"
    }, 
    {
      "response": "sample response 3", 
      "score": 1.8652154963606848, 
      "time taken": 4.174862861633301, 
      "url": "https://random-url3.com"
    }
  ]
}
```

## Text classification Api: identifying if query is relationship-related or not

- endpoint: /api/classify
- parameters:
    - query (question to be classified)

- sample input:
```
localhost:5000/api/classify?query=random question
```

- sample output:
```
{
  "query": "random question", 
  "relationship-related": "no"
}
```

## Understanding the machine learning portion - ml folder

### training_data directory
- this directory contains 7 .csv files used for training the models
- each row contains {question}{1 or 0: 1 if it is relationship-related else 0}
- they are randomly selected from the master dataset of 2 million questions
- each dataset has equal numbers of relationship-related and non-relationship-related questions
- the dataset size increases progressively from 1 (20k rows) to 7 (1.2 million rows)

### saved directory
- this directory contains many .sav files
- they are ready-trained and saved models that can be reused, as well as the corresponding vectorizers
```
import pickle

vectorizer, model = pickle.load(open("saved/filename.sav","rb))
```
- each .sav file has a model class name and a number 
- eg. BernoulliNB_3 means that a sklearn BernoulliNB model was trained on training_data/train3.csv

## Testing ml models
- cd into the ml folder on command line
- edit the test.csv folder
- set your own questions in the following format: {question};{0 or 1}
- edit test.py and set your desired model name to "MODEL_NAME" 
- run:
```
py test.py
```

