import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        #getting  the payload 
        body = req.get_body()
        length = len(body)
    except Exception as ex :
        logging.error (f"Something went wrong while getting payload : {ex}")    

    logging.warn(f'All set! Got {length} bytes')
    return func.HttpResponse(f"All set! Got {length} bytes")
