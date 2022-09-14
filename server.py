from Flask_app import app
from Flask_app.controllers import users_controller
from Flask_app.controllers import products_controller

if __name__=="__main__":
    app.run(debug=True)