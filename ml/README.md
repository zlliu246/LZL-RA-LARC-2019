ML portion of relationship chatbot

training_data contains a bunch of training datasets (max size 120000 lines)
    - each containing half relationship-related, half non-related questions
    - related questions are labelled 1, while non-realted ones are labelled 0


TO TEST DATA:
    you will use 1) test.py and 2) test.csv 3) saved folder

    test.csv:
        - write your own questions and label it as relationship related or not (0 or 1)

    test.py
        pickle loads a trained model + tfidf Vectorizer from sklearn
        uses pre-trained model to predict your inputs

        run test.py (py test.py in the ml directory) and a table will be shown


