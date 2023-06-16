import json
import sys
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features,SentimentOptions
def main(dict):
    apikey = "RXqz8AZvDrtEmZkUawphBEZpM1sRvZVUMCbsEUN7Xr6P"
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/9933667d-202c-45b2-b744-b3d662390303"

    authenticator = IAMAuthenticator(apikey)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
    )
    natural_language_understanding.set_service_url(url)

    response = natural_language_understanding.analyze(text=dict['text'],features=Features(sentiment=SentimentOptions(targets=[dict['text']]))).get_result() 
    label = response['sentiment']['document']['label'] 
    result= {
        'headers': {'Content-Type':'application/json'}, 
        'body': {'label':label} 
        }    
    return result