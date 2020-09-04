<!-- ## happy path
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
  - utter_did_that_help -->
  
## sad path 1
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
  - utter_menu
* short_feedback
  - utter_no_feedback

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
  - utter_menu
* long_feedback
  - action_reset_all_slots
  - utter_thanks
  - form_get_rating
  - form{"name": "form_get_rating"}
  - form{"name": null}
  - form_get_influence
  - form{"name": "form_get_influence"}
  - form{"name": null}
  - form_get_support_feedback
  - form{"name": "form_get_support_feedback"}
  - form{"name": null}
  - form{"name" : "form_get_email"}
  - form{"name": null}
  - utter_pre_finish
  - utter_finish


## say goodbye
* question
  - utter_wait
  - action_question_ask
* goodbye
  - utter_goodbye


## bot challenge
* bot_challenge
  - utter_iamabot
