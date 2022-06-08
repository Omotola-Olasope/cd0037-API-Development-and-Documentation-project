
# API Reference

# Endpoints

## GET /categories

Fetches all available categories,

Request arguments: None,

Returns all available categories and success value

Sample: 'curl http://127.0.0.1:5000/categories'

## GET /questions

Fetches a list of questions and categories

Request arguments: Page

Returns paginated questions (10 questions/page), success value, number of total questions, categories and current category

Sample: 'curl http://127.0.0.1:5000/questions'

## GET /categories/<int:category_id>/questions

Fetches a list of questions based on a category

Request arguments: category ID

Returns all questions in a given category, success value, number of total questions, and current category

Sample: curl http://127.0.0.1:5000/categories/4/questions

## DELETE /questions/<int:question_id>

Deletes a question using its question `ID`

Request arguments: question ID

Returns the ID of the deleted question and success value

Sample: curl -X DELETE http://127.0.0.1:5000/questions/1

## POST /quizzes

Gets a question used to play a quiz. The endpoint takes a category and previous question parameters and returns a new question

Request arguments: The quiz category and question IDs of previous questions

Returns a random question within the given category, if provided, and if it is not one of the previous questions

## POST /questions

Creates a new question that reflects in the database

Request arguments: question, answer, difficulty and category

Returns a success value, ID of the question created, paginated questions (10 questions/page) and total questions

Sample: curl -X POST -H "Content-Type: application/json" -d '{"question":"testQ", "answer":"testA", "difficulty":"5", "category":"4"}' http://127.0.0.1:5000/questions | jq '.'

## POST /questions/search

Search for a question using a search term

Request argument: a search term/phrase

Returns a success value, a list of questions, total questions in the search and current category

# Errors

## Error 400

Returns an object with these keys: success, error and message.

{"success": false, "error": 400, "message": "bad request"}

## Error 404

Returns an object with these keys: success, error and message.

{"success": false, "error": 404, "message": "resource not found"}

## Error 405

Returns an object with these keys: success, error and message.

{"success": False, "error": 405, "message": "method not allowed"})

## Error 422

Returns an object with these keys: success, error and message.

{"success": false, "error": 422, "message": "unprocessable"}

## Error 500

Returns an object with these keys: success, error and message.

{"success": false, "error": 500, "message": "internal server error"}