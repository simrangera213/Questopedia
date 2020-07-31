# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os
import pandas as pd
import time
from ast import literal_eval

from cdqa.utils.converters import pdf_converter
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model

download_model(model='bert-squad_1.1', dir='./models')
df = pdf_converter(directory_path='./dataset')
cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib', max_df=1.0)

# Fit Retriever to documents
cdqa_pipeline.fit_retriever(df=df)

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


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
        
        dispatcher.utter_message(prediction[0])
        print('query: {}'.format(query))
        print('answer: {}'.format(prediction[0]))
        print('title: {}'.format(prediction[1]))
        print('paragraph: {}'.format(prediction[2]))
        et=time.time()
        print(et-st)
        return []
