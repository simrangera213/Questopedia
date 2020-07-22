## happy path
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
  - utter_did_that_help

## sad path 1
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
  - utter_did_that_help
* affirm
  - utter_happy

## happy path 3
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
* question
  - utter_wait
  - action_question_ask
* question
  - utter_wait
  - action_question_ask
  - utter_did_that_help
* deny
  - utter_regret

## say goodbye
* question
  - utter_wait
  - action_question_ask
* goodbye
  - utter_goodbye


## bot challenge
* bot_challenge
  - utter_iamabot
