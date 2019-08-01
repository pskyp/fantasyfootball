import datetime
import logging
import requests

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    resp = requests.get(url)
    print(resp.json())
