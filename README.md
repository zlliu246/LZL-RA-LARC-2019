# LZL-RA-LARC-2019
repo for research assistant role for LARC sep-nov 2019

# Query part
1) pip install flask flask_restplus flask_cors bs4 requests google nltk
32) py app.py

    * Serving Flask app "app" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 162-640-274
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    should appear

3) go to chrome and type "localhost:5000"
4) a Swagger UI should appear 
5) enter 1) query and 2) number of results and a json should be returned


# ML: classifying if query is relationship-related or not

training_data contains a bunch of training datasets (max size 120000 lines)
    - each containing half relationship-related, half non-related questions
    - related questions are labelled 1, while non-realted ones are labelled 0


TO TEST DATA:

    *** cd into ml folder on command line ***

    you will use 1) test.py and 2) test.csv 3) saved folder

    test.csv:
        - write your own questions and label it as relationship related or not (0 or 1)

    test.py
        pickle loads a trained model + tfidf Vectorizer from sklearn
        uses pre-trained model to predict your inputs

        run test.py (py test.py in the ml directory) and a table will be shown


