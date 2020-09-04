# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
<<<<<<< HEAD
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset


import os
import pandas as pd
import time
import re

from ast import literal_eval

from cdqa.utils.converters import pdf_converter
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model
from writeToExcel import writeToExcel


# To download the pretrained BERT SQUAD Model.

download_model(model='bert-squad_1.1', dir='./models')
df = pdf_converter(directory_path='./dataset')
cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)

# Fit Retriever to documents
cdqa_pipeline.fit_retriever(df=df)
=======
import os
import pandas as pd
import time
from ast import literal_eval
>>>>>>> 525fc9dae07534041de4526cb6c9fddca75cc78f

from cdqa.utils.converters import pdf_converter
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model

download_model(model='bert-squad_1.1', dir='./models')
df = pdf_converter(directory_path='./dataset')
cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)

# Fit Retriever to documents
cdqa_pipeline.fit_retriever(df=df)

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://images.unsplash.com/photo-1533745848184-3db07256e163?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1189&q=80")

        dispatcher.utter_message(text="Hey! 👋")
        dispatcher.utter_message(text = "Welcome to the Questopedia Bot. \n I am there to answer all your queries related to the Science Topics.")
        return[]



class ActionQuestionAsk(Action) :
    def name(self) -> Text:
        return "action_question_ask"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        st=time.time()
        
        print("entered")
        
        query=tracker.latest_message['text']
        
        prediction = cdqa_pipeline.predict(query)
       

        dispatcher.utter_message("The Answer is : " + prediction[0])
        
        print('query: {}'.format(query))
        print('answer: {}'.format(prediction[0]))
        print('title: {}'.format(prediction[1]))
        print('paragraph: {}'.format(prediction[2]))
         
        # print('PREDICTION : {}'.format(prediction))

        
        et=time.time()
        
        print(et-st)

        writeToExcel(prediction , query , et-st )

        return []




# For taking feedbacks from students





class FormGetRating(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_rating"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["rating"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "rating": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class FormGetInfluence(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_influence"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        # decide if the rating is low and ask for influence
        rating = int(tracker.get_slot("rating"))

        if rating < 3:
            return ["influence"]
        else:
            return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "influence": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # decide if the rating is low and send according finish message
        rating = int(tracker.get_slot("rating"))

        if rating < 3:
            dispatcher.utter_template("utter_influence_done", tracker)
        else:
            dispatcher.utter_template("utter_awesome", tracker)
            
        return []

class FormGetSupportFeedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_support_feedback"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["support_feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "support_feedback": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class FormGetRatingQuick(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_rating_quick"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["rating_quick"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "rating_quick": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []


class FormGetEmail(FormAction):

    def name(self) -> Text:
        return "form_get_email"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["email_address"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "email_address": [
                self.from_text(),
            ],
        }

    def submit( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        dispatcher.utter_message("your email must be like that example marysmith90@gmail.com")

        email= ((tracker.latest_message)['text'])
        regex_email =r"([A-Za-z0-9]+)@\S+"

        email_matched = re.findall(regex_email,email)

        if  email_matched is not None :
            dispatcher.utter_message("your email has been accepted:{}".format(email_matched))
        
        else :
            dispatcher.utter_message("your email has been not accepted")
            
        return []



# This actions is for resetting all the slots.

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]
