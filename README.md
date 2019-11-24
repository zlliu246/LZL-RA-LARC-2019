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
