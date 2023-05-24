import os
from flask import Flask, request, make_response
from dotenv import load_dotenv
from core import Pythogram, EventListener
from core.domains import Webhook
from core.events import *

load_dotenv('default.env')
events = EventListener()
app = Flask(__name__)


@app.route('/telega', methods=['GET', 'POST'])
def telega():
    if request.method == 'POST':
        post = request.json.get('message', dict())
        message = Pythogram.parse_message(post)
        events.call(message=message)
    return make_response({'ok': True})


if __name__ == '__main__':
    t = Pythogram(token=os.environ.get('telegram_token'))
    t.webhook.set(Webhook(url=os.environ.get('telegram_webhook_url')+'/telega'))
    events.subscribe(ActionFortune(sender=t))
    events.subscribe(ActionRussia(sender=t))
    events.subscribe(ActionPhoto(sender=t))
    events.subscribe(ActionLocation(sender=t))
    events.subscribe(ActionVideo(sender=t))
    app.run(host='0.0.0.0')

