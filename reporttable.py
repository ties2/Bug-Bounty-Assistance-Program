from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the table data
table_data = [
    ["WSTG-INFO-01", "Conduct Search Engine Discovery Reconnaissance for Information Leakage", "", ""],
    ["WSTG -INFO-02", "Fingerprint Web Server", "-", ""],
    ["WSTG -INFO-03", "Review Webserver Metafiles for Information Leakage", "-", ""],
    ["WSTG-INFO-04", "Enumerate Applications on Webserver", "-", ""],
    ["WSTG-INFO-05", "Review Web Page Content for Information Leakage", "-", ""],
    ["WSTG-INFO-06", "Identify Application Entry Points", "-", ""],
    ["WSTG-INFO-07", "Map Execution Paths Through Application", "-", ""],
    ["WSTG-INFO-08", "Fingerprint Web Application Framework", "-", ""],
    ["WSTG-INFO-09", "Fingerprint Web Application (Merged into WSTG-INFO-08)", "-", ""],
    ["WSTG-INFO-10", "Map Application Architecture", "-", ""],
    ["WSTG", "Information Gathering", "Description", ""]
]

@app.route('/')
def index():
    return render_template('index.html', table_data=table_data)

@app.route('/update', methods=['POST'])
def update_table():
    # Process the form data to update the table
    # For simplicity, this example does not persist the changes
    # You would typically save these changes to a database or another persistent storage
    for i, row in enumerate(request.form.getlist('row')):
        for j, cell in enumerate(row):
            if j == 3:  # Assuming the last column is the "Result" column
                table_data[i][j] = cell
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
