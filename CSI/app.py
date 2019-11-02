from flask import Flask
import datetime, os

app = Flask(__name__)

# The app will work with a "log.txt" sitting on a directory "data"
mylog = os.path.join("data", "log.txt")

@app.route("/")
def hello():
    if os.path.isdir("data"):
        f = open(mylog,'a+')
        visits = len(f.readlines())
        f.write('New access at: {}\r\n'.format(datetime.datetime.now()))
        f.close()
        html = """<h3>Hello World!</h3><br>
        The IaC workshop in New York is AWESSOOOOME!!<br><br>
        <b>Visits:</b> {}<br><br>
        <a href="/dump">Click here</a> to see the log
        """.format(visits)
        return html
    else:
        return "<h3>Log file could not be found</h3>"


@app.route("/dump")
def dump():
    f = open(mylog,'a+')
    entries = f.readlines()
    f.close()

    html = "<h3>This is a dump of the log</h3><br>"
    for each_entry in entries:
        html += each_entry + "<br>"
        
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
