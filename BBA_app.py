from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Your Python code goes here
    return render_template_string('''
<html>
<head>
    <title>Hello</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 24px;
            text-align: center;
            padding-top: 100px;
        }
    </style>
</head>
<body>
    <h1>Hello</h1>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(debug=True)