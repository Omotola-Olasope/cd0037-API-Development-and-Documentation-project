import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
CATEGORIES_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def paginate_categories(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * CATEGORIES_PER_PAGE
    end = start + CATEGORIES_PER_PAGE

    categories = [category.format() for category in selection]
    current_categories = categories[start:end]

    return current_categories

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/categories')
    def get_categories(): 
        selection = Category.query.order_by(Category.id).all()
        current_categories = paginate_categories(request, selection)

        if len(current_categories) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'categories': current_categories
        })

    @app.route('/questions')
    def get_questions(): 
        selection = Question.query.order_by(Question.id).all()
        current_question = paginate_questions(request, selection)

        if len(current_question) == 0:
            abort(404)
        
        return jsonify({
            'success': True,
            'questions': current_question,
            'total_questions': len(Question.query.all())
        })

    @app.route('/categories/<int:category_id>')
    def get_specific_category(category_id):
        category = Category.query.filter(Category.id == category_id).one_or_none()

        if category is None:
            abort(404)
        
        else:
            return jsonify({
                'success': True,
                'category': category.format()
            })

#    @app.route('/categories/${id}/questions')
#    def get_questions_by_category(id):
#        selection = Question.query.filter(Question.id == id).all()
#        current_question = paginate_questions(request, selection)
#
#        if len(current_question) == 0:
#            abort(404)
#                
#        return jsonify({
#            'success': True,
#            'questions': current_question,
#            'total_questions': len(Question.query.filter(Question.id == id).all()),
#            'current_category': id})

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            
            return jsonify({"success": True, "id": question.id})

        except:
            abort(422)
    
#    @app.route('/quizzes', methods=['POST'])
#    def next_quiz():
#        body = request.get_json()
#
#        previous_questions = body.get.getlist('previousQuestions', None)
#        quiz_category = body.get('current_category', None)
#        
#        try:
#            quiz = Question(title=new_title, author=new_author, rating=new_rating)
#            book.insert()
#
#            selection = Book.query.order_by(Book.id).all()
#            current_books = paginate_books(request, selection)
#
#            return jsonify(
#                {
#                    "success": True,
#                    "created": book.id,
#                    "books": current_books,
#                    "total_books": len(Book.query.all()),
#                }
#            )
#
#        except:
#            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()

        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_difficulty = body.get("difficulty", None)
        new_category = body.get("category", None)

        try:
            question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
            question.insert()

            return jsonify(
                {
                    "success": True,                    
                })

        except:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def search_question():
        body = request.get_json()

        searchTerm = body.get('searchTerm', None)
        question_search = "%{}%".format(searchTerm)
        searchResults = Question.query.filter(Question.question.ilike(question_search)).all()

        try:
            questionResult={
                'data': [],
                'totalQuestions': len(searchResults)                
            }
            for question in searchResults:
                questionResult['data'].append({
                'id': question.id,
                'question': question.question,
                'answer': question.answer,
                'difficulty': question.difficulty,
                'category': question.category                
                })
                    
            return jsonify(
                {
                    'success': True,
                    'questions': questionResult,
                    'currentCategory': question.category                  
                })

        except:
            abort(422)


    @app.errorhandler(400)
    def bad_request(error):
        return (
            jsonify({"success": False, "error": 400, "message": "bad request"}), 400
        )

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}), 404
        )

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}), 405
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}), 422
        )

    @app.errorhandler(500)
    def internal_server(error):
        return (
            jsonify({"success": False, "error": 500, "message": "internal server error"}), 500
        )

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """


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

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

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

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

