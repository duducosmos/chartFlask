from flask import Flask, Response, render_template, stream_with_context
import time


app = Flask(__name__)


def genData():
    x = 0
    y = 0
    while(True):
        time.sleep(1)
        y = x * x
        yield "id:{0}\nevent:{1}\ndata:{2},{3}\n\n".format(x,
                                                           "in-progress",
                                                           x,
                                                           y)
        x += 1

@app.route("/mychart")
def mychart():
    return Response(stream_with_context(genData()), mimetype="text/event-stream")


@app.route("/")
def home():
    return render_template("home.html")


if(__name__ == "__main__"):
    app.run(debug=True)
