from website import create_app
from flask_restful import Resource, Api

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)