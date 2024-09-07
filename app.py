from flask import Flask, request, render_template_string, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store the HTML code globally to be accessed by the /display route
html_code_global = ""

# Root route to provide instructions or redirect
@app.route('/')
def index():
    return "Navigate to /display to see the generated HTML and CSS."

# Route to display the generated HTML and CSS
@app.route('/display', methods=['GET', 'POST'])
def display_html_css():
    global html_code_global
    if request.method == 'POST':
        # Fetch the HTML and CSS code from the request
        html_code_global = request.form.get('html_code', '')
        return redirect(url_for('display_html_css'))
    else:
        # Display the stored HTML and CSS
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Generated HTML with Tailwind CSS</title>
            <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        </head>
        <body>
            {html_code_global}
        </body>
        </html>
        """
        return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)