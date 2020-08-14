from get_csr import create_app
from os import environ
from dotenv import load_dotenv


load_dotenv()
app = application = create_app(environ.get('CONFIG_MODE', 'development'))


if __name__ == '__main__':
    app.run()
