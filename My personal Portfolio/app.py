from flask import Flask, send_from_directory
import subprocess
import os

app = Flask(__name__, static_folder='.', template_folder='.')

# Route to serve the HTML file
@app.route('/')
def home():
    return send_from_directory('.', 'Project.html')  # Serve the main HTML file

# Route to run the calculator when the image is clicked
@app.route('/run-calculator')
def run_calculator():
    calculator_script = os.path.join(os.getcwd(), "calculator.py")
    try:
        # Run the calculator script using subprocess
        subprocess.Popen(["python", calculator_script], shell=True)
        return """
            <h1>Calculator is Running!</h1>
            <p>The calculator application has been opened on your system. You can interact with it now.</p>
            <a href="/">Go Back to Projects</a>
        """
    except Exception as e:
        return f"<h1>Error:</h1><p>{str(e)}</p>"

# Route to serve static files (CSS, images, etc.)
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(debug=True)
