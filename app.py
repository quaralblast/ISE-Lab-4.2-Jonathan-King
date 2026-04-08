import os

from flaskr import create_app

app = create_app()

# https://8080-cs-73483424128-default.cs-us-east1-vpcf.cloudshell.dev/
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')