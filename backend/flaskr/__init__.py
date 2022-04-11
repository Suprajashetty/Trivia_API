import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def pagination_question(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    current_question = [question.format() for question in selection]
    return current_question[start:end]

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app)
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
 # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS,PATCH"
        )
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def retrieve_categories():
        categories = Category.query.all()
        current_category = [category.format() for category in categories]
        return jsonify({
            "success" : True,
            "categories" : current_category,
            "total_categories" : len(categories)
        })


    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions')
    def retrieve_questions():
        #questions = Question.query.with_entities(Question.question, Question.category).all()
        questions = Question.query.all()
        categories = Category.query.with_entities(Category.type).all()
        current_category = [{"type" :category["type"] } for category in categories]
        if ((questions is None) or (categories is None)):
            abort(404)
        current_question = pagination_question(request, questions)
        #quest_cate=[]
        required_questions =[{ "question" : ques['question'], "category" : ques['category'] } for ques in current_question]
        
        #required_questions = required_questions.format()
       # required_categories =[ques['category'].format() for ques in current_question]
        if len(required_questions) == 0:
            abort(404)
        return jsonify({
            "success" : True,
            #"List_of_questions" : required_questions,
            "question_category" : required_questions,
            "all_categories" : current_category,
            "total_number_of_questions" : len(questions)
        })

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.
    
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()
            if question is None:
                abort(404)
            question.delete()
            questions = Question.query.all()
            
            return jsonify({
                "success" : True,
                "deleted" : question_id,
                "total_number_of_questions" : len(questions)
            })
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route("/questions", methods=["POST"])
    def create_questions():
        body = request.get_json()
        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_category = body.get("category", None)
        new_difficulty = body.get("difficulty", None)

        try:
            question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
            question.insert()

            selection = Question.query.order_by(Question.id).all()
            current_questions = pagination_question(request, selection)

            return jsonify(
                {
                    "success": True,
                    "created": question.id,
                    "questions": current_questions,
                    "total_questions": len(selection)
                }
            )
        except:
            abort(422)
    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        body = request.get_json()
        search = body.get("search", None)
        if search:
            selection = Question.query.order_by(Question.id).filter(Question.question.ilike("%{}%".format(search))).all()
            current_questions = pagination_question(request, selection)
            return jsonify(
                {
                    "success": True,
                    "questions": current_questions,
                    "total_questions": len(selection),
                }
            )
        abort(404)
    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:category_id>/questions')
    def retrive_category_question(category_id):
        categories = Category.query.filter(Category.id==category_id).one_or_none()
        questions = Question.query.filter(Question.category==categories.type).all()
        question = pagination_question(request, questions)

        return jsonify(
                {
                    "success": True,
                    "questions":question,
                    "category":categories.type,
                    "total_questions" : len(questions)
                })
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def questions_to_play_quiz():
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions')
            category = body.get('quiz_category')
            if not ('quiz_category' in body and 'previous_questions' in body):
                abort(422)
        
            required_questions = Question.query.filter_by(category=category['type']).filter(Question.id.notin_((previous_questions))).all()
            question = required_questions[random.randrange(0, len(required_questions))].format() if len(required_questions) > 0 else None
            return jsonify({
                'success': True, 
                'question': question
                })
        except:
            abort(422)
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )
    return app

