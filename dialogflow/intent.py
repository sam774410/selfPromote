# encoding: utf-8

import apiai
import json
import sys
# add search range
sys.path.append('..')
from util.config import DIALOGFLOW_CLIENT_ACCESS_TOKEN


class Intent:

    def __init__(self):
        pass
    
    def get_user_intent(self, msg):

        ai = apiai.ApiAI(DIALOGFLOW_CLIENT_ACCESS_TOKEN)
        request = ai.text_request()
        request.lang = 'zh-TW'
        request.query = msg
        response = request.getresponse()

        try:
            # alias python="python3" make share in python3 env 
            result = json.loads(str(response.read(), encoding = "utf-8")) 
            print(result)

            # about me
            if 'get_user_intent' in result['result']['parameters']:
                
                response = dict()
                response["isOk"] = True
                response["response"] = result['result']['fulfillment']['speech']
                response["intent"] = result['result']['parameters']['get_user_intent']
                return response

            # help
            elif 'help' in result['result']['parameters']:
                
                response = dict()
                response["isOk"] = True
                response["response"] = result['result']['fulfillment']['speech']
                response["intent"] = result['result']['parameters']['help']
                return response

            # fallback
            else:
                
                response = dict()
                response["isOk"] = False
                response["response"] = result['result']['fulfillment']['speech']
                response["intent"] = "None"
                return response

        except Exception as e:
            print('get user intent exception: '+ str(e))




if __name__ == "__main__":
    
   intent = Intent()
   print(intent.get_user_intent('做過什麼project?'))
    