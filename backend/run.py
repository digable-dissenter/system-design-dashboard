from app import main

app = main.app

# Check if the run.py file has executed directly and not imported
# Statement starts the Flask server on your local machine
if __name__ == "__main__":
    app.run(debug=True)

from app import indices , sectors, shares, quarters, dataframes