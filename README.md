# Restaurant Finder Web Application

This web application allows users to find restaurants based on postcode using the Just Eat API.

## Installation

1. **Clone the repository:**

git clone https://github.com/denizgezerli/app_rest_data.git

2. **Navigate to the project directory:**

cd app_rest_data

3. **Create a virtual environment:**

python -m venv venv

4. **Activate the virtual environment:**
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. **Install the required dependencies:**

pip install -r requirements.txt

6. **Usage:**

To run the application, execute the following command: python app.py

Once the application is running, open your web browser and go to http://localhost:5000 to access the web interface. 
You can enter a postcode in the input box and click "Submit" to find restaurants in that area.

7. **Possible Improvements:**

Instead of parsing the restaurants data in HTML, it can be parsed in Python. That would be a nicer solution.
