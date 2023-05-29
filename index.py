from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('se+c4fyxVOmqGgpakT0mohWLHAYNqGvzLewZ4oay2GVr6w40X1X0HZcQ2Hfx91QEVBwWyNLDF6Y8VvDlnkZ/0Gfkwlhx0gp4/I4QAgz5gqrnHiui0pHFlXzBZ3P6V4iUpYZO+LcyJ89ObBnCOSppxAdB04t89/1O/w1cDnyilFU=')
handler1 = WebhookHandler('4254f56563e22f457b02aa6ec296d72a 4254f56563e22f457b02aa6ec296d72a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
