# meep-backend

## Setup

### Unix
  1. Install python
     ```
     sudo apt-get install python3
     ```
  2. clone the master branch
  3. create a virtual environment in the project root directory
  4. activate the virtual environment ```source venv/bin/activate```
  5. pip install requiremnets ```pip install -r requirements.txt```
  6. create a sqlite database ```touch dev.db```
  7. set dev database environment variable ```export DEV_DATABASE_URL=sqlite:///dev.db```
  8. create and populate tables ```python db_operations.py reset```  
  9. set flask environment variable to development
    ```
    export FLASK_ENV=development
    ```
  10. run the app
    ```
    flask run
    ```
  11. test to see if it worked: in a browser, type 
  
  
  

### Windows
  1. Install python
  2. Install pip
  3. Install virtualenv
  4. clone the master branch
  5. create a virtual environment in the project root directory
  6. activate the virtual environment ```venv\Scripts\activate```
  7. pip install requirements ```pip install -r requirements.txt```
  8. In mysql, create a new database named 'meep_dev'.
  9. Add a user called 'meep' to this database. 
  10. Create a password 'meep' for the user 'meep'.
  