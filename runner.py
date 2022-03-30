from app import create_app

# https://flask.palletsprojects.com/en/2.0.x/config/
app_runner = create_app('config.DevConfiguration')

if __name__ == '__main__':
    app_runner.run(debug=True)
