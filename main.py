import os
from pathlib import Path

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

access_token_path = Path.home() / ".config" / "feedly" / "access.token"


app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command("/update-token")
def write_token(ack, respond, command):
    ack()

    try:
        access_token_path.parent.mkdir(exist_ok=True, parents=True)
        access_token_path.write_text(command["text"])
    except BaseException as e:
        respond(str(e))
    else:
        respond(f"Token updated: {command['text']}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
