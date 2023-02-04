"""
Post a new review in the database
HTTP Method : POST
"""

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator("jIgFW3QzX8e_k8aAWhYA4SaeDfXQ62Jy0szogP5-eVJa")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://apikey-v2-rg5tzn3w5twkdi5w3oiiwrc8i3qlbhhmy8miw6ptjtx:11749eab45d913ef5e98f4276a578e76@148477bd-c1eb-4521-a003-97beae46f41d-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }
        