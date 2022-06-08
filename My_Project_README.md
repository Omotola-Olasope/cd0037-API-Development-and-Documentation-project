
# API Reference

## Endpoints 
###### GET /categories

Fetches all available categories
Request arguments: None
Returns all available categories and success value

Sample: 'curl http://127.0.0.1:5000/categories'

{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}

###### GET /questions

Fetches a list of questions and categories
Request arguments: Page
Returns paginated questions (10 questions/page), success value, number of total questions, categories and current category

Sample: 'curl http://127.0.0.1:5000/questions'
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "testAns1",
      "category": 3,
      "difficulty": 4,
      "id": 1,
      "question": "testQ1"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    }
  ],
  "success": true,
  "total_questions": 21
}

###### GET /categories/<int:category_id>/questions

Fetches a list of questions based on a category
Request arguments: category ID
Returns all questions in a given category, success value, number of total questions, and current category

Sample: curl http://127.0.0.1:5000/categories/4/questions

{
  "current_category": 4,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 4
}

###### DELETE /questions/<int:question_id>

Deletes a question using its question `ID`
Request arguments: question ID
Returns the ID of the deleted question and success value

Sample: curl -X DELETE http://127.0.0.1:5000/questions/1

{"deleted":1,"success":true}

###### POST /quizzes

Gets a question used to play a quiz. The endpoint takes a category and previous question parameters and returns a new question
Request arguments: The quiz category and question IDs of previous questions
Returns a random question within the given category, if provided, and if it is not one of the previous questions


###### POST /questions

Creates a new question that reflects in the database
Request arguments: question, answer, difficulty and category
Returns a success value, ID of the question created, paginated questions (10 questions/page) and total questions

Sample: curl -X POST -H "Content-Type: application/json" -d '{"question":"testQ", "answer":"testA", "difficulty":"5", "category":"4"}' http://127.0.0.1:5000/questions | jq '.'

{
  "created": 26,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 22
}

###### POST /questions/search
Search for a question using a search term
Request argument: a search term/phrase
Returns a success value, a list of questions, total questions in the search and current category

###### Errors
# Error 400
Returns an object with these keys: success, error and message.

{"success": false, "error": 400, "message": "bad request"}

# Error 404
Returns an object with these keys: success, error and message.

{"success": false, "error": 404, "message": "resource not found"}

# Error 405
Returns an object with these keys: success, error and message.

{"success": False, "error": 405, "message": "method not allowed"})

# Error 422
Returns an object with these keys: success, error and message.

{"success": false, "error": 422, "message": "unprocessable"}

# Error 500
Returns an object with these keys: success, error and message.

{"success": false, "error": 500, "message": "internal server error"}

###### Testing
To run the tests, run the script run_unit_tests.sh:

# Remember that the script needs execution permission
chmod +x run_unit_tests.sh

./run_unit_tests.sh