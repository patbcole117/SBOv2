from app import app
from app.utils.conf_parse import get_config

if __name__=='__main__':
    c = get_config()
    app.run(debug=False, host=c['SBO_HOST'], port=c['SBO_PORT'])

