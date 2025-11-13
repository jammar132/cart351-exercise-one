from flask import Flask, render_template_string
import io
import contextlib
import runpy
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>CART 351 – Exercise 1 AQI</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background: #f5f5f5;
      }
      h1 {
        text-align: center;
      }
      pre {
        background: #111;
        color: #0f0;
        padding: 15px;
        border-radius: 8px;
        overflow-x: auto;
        font-size: 14px;
      }
      .error {
        color: red;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <h1>CART 351 – Exercise 1 Output</h1>
    {% if error %}
      <p class="error">{{ error }}</p>
    {% else %}
      <pre>{{ output }}</pre>
    {% endif %}
  </body>
</html>
"""

@app.route("/")
def index():
    """
    Runs the original ex-one.py script and captures whatever it prints.
    ex-one.py stays untouched; we just execute it as a script.
    """
    script_path = os.path.join(os.path.dirname(__file__), "ex-one.py")

    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            # run the original script as __main__, no modification needed
            runpy.run_path(script_path, run_name="__main__")
        output = buffer.getvalue()
        if not output.strip():
            output = "Script ran successfully but did not print anything."
        return render_template_string(HTML_TEMPLATE, output=output, error=None)
    except Exception as e:
        # if your script errors, we show that instead of breaking the server
        return render_template_string(
            HTML_TEMPLATE,
            output="",
            error=f"Error while running ex-one.py: {e}"
        )

if __name__ == "__main__":
    app.run(debug=True)
