# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

GET '\categories'

Fetches a dictionary of categories
Request Arguments: None
Example response:
{
  "categories": [
    {
      "id": 1, 
      "type": "History"
    }, 
    {
      "id": 2, 
      "type": "Science"
    }, 
    {
      "id": 3, 
      "type": "Computer"
    }, 
    {
      "id": 4, 
      "type": "Geography"
    }, 
    {
      "id": 5, 
      "type": "Sports"
    }, 
    {
      "id": 6, 
      "type": "Entertainment"
    }
  ], 
  "success": true, 
  "total_categories": 6
}

GET '\questions?page=<page_number>'

Fetches a dictionary of questions in all categories
Request Arguments(optional): page:int
Example response:
 {
  "all_categories": [
    {
      "type": "History"
    }, 
    {
      "type": "Science"
    }, 
    {
      "type": "Computer"
    }, 
    {
      "type": "Geography"
    }, 
    {
      "type": "Sports"
    }, 
    {
      "type": "Entertainment"
    }
  ], 
  "question_category": [
    {
      "category": "Science", 
      "question": "What is the chemical formula for water?"
    }, 
    {
      "category": "History", 
      "question": "Who is the PM of INDIA?"
    }, 
    {
      "category": "Science", 
      "question": "How many bones are in the human body?"
    }, 
    {
      "category": "Science", 
      "question": "e concept of gravity was discovered by which famous physicist?"
    }, 
    {
      "category": "Science", 
      "question": "What is the hardest natural substance on Earth?"
    }, 
    {
      "category": "Science", 
      "question": "What modern-day country was Marie Curie born in?"
    }, 
    {
      "category": "Science", 
      "question": "How many teeth does an adult human have?"
    }, 
    {
      "category": "Science", 
      "question": "What is the biggest planet in our solar system?"
    }, 
    {
      "category": "Science", 
      "question": "What is the most abundant gas in the Earths atmosphere?"
    }, 
    {
      "category": "Sports", 
      "question": "What is the national game of China?"
    }
  ], 
  "success": true, 
  "total_number_of_questions": 70
}

DELETE '\questions\<question_id>'

Removes existing questions from the repository
Request Arguments: question_id:int
Example response:
"deleted": "28",
"success": true
POST '\questions'

Adds questions to the repository
Request Arguments: {question:string, answer:string, difficulty:int, category:string}
Example response:
"created": "87",
"success": true

POST '\questions\search'

Fetches all questions matching a substring in a search term
Request Arguments: {searchTerm:string}
Example response:
{ 
  "questions": [
   {
    "answer": "H2O",
    "category": "Science",
    "difficulty": 5,
    "id": 5,
    "question": "What is the chemical formula of water?"
},  
"success": true, 
"total_questions": 1
}
GET '\categories\<int:category_id>\questions'

Fetches all questions within a specific category
Request Arguments: category_id:int
Example response:
{
  "category": "History", 
  "questions": [
    {
      "answer": "Modiji", 
      "category": "History", 
      "difficulty": 1, 
      "id": 1, 
      "question": "Who is the PM of INDIA?"
    }, 
    {
      "answer": "1853", 
      "category": "History", 
      "difficulty": 5, 
      "id": 22, 
      "question": "The system of competitive examination for civil service was accepted in principle in the year?"
    }, 
    {
      "answer": "Mahanayakacharya", 
      "category": "History", 
      "difficulty": 4, 
      "id": 23, 
      "question": "\t\nThrough which one of the following, the king exercised his control over villages in the Vijayanagar Empire?"
    }, 
    {
      "answer": "Telugu", 
      "category": "History", 
      "difficulty": 2, 
      "id": 24, 
      "question": "The Vijayanagara ruler, Kirshnadev Rayas work Amuktamalyada, was in?"
    }, 
    {
      "answer": "1757", 
      "category": "History", 
      "difficulty": 1, 
      "id": 25, 
      "question": "\t\nThe Battle of Plassey was fought in?"
    }, 
    {
      "answer": "military affairs", 
      "category": "History", 
      "difficulty": 1, 
      "id": 26, 
      "question": "Under Akbar, the Mir Bakshi was required to look after?"
    }
  ], 
  "success": true, 
  "total_questions": 6
}

POST '\quizzes'

Fetches a random question within a specific category, excluding those previously asked
Request Arguments: {previous_questions: arr, quiz_category: {id:int, type:string}}
Example response:
{
  "question": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
  ], 
  "success": true
}

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
