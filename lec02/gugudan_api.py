from flask import Flask, request
from markupsafe import escape
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r'*': {'origins': '*'}})

@app.route("/")
def hello():
    html_str = """
<!DOCTYPE html>
<html lang="kr">
<head>
<meta charset="UTF-8">
<title>Flask Home Page</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
</head>
<body>
<form id="form_id" action="javascript:post_query()">
<h2>구구단 출력하기</h2>
<label>단 :
<input type="text" name="dan">
</label>
<button type="submit">출력</button>
</form>
<div id="results"></div>
<script>

function post_query() {
$.ajax({
type: "GET",
url: "http://localhost:5000/gugudan/",
data: $("#form_id").serialize(),
success: update_result,
dataType: "html"
});
}
function update_result(data) {
$("#results").html(data);
}
</script>
</body>
</html>   
    
    """

    return html_str

@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요. {escape(name)}님."

@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str = ""
    for i in range(1, 10):
        html_str += f"{dan} X {i} = {int(dan)*i}<br>"
    return html_str


@app.route("/gugudan/")
def gugudan_arg_html():
    dan = request.args.get("dan", "2")
    html_str = ""
    for i in range(1, 10):
        html_str += f"{dan} X {i} = <strong>{int(dan)*i}</strong><br>"
    return html_str

app.run(debug=True)