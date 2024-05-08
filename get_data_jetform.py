from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class JotFormWebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the length of the incoming request body
        content_length = int(self.headers['Content-Length'])
        # Read the request body
        post_data = self.rfile.read(content_length)
        # Parse form data from the request body
        form_data = json.loads(post_data.decode('utf-8'))

        # Process the form data
        user_data = {
            'first_name': form_data['first_name'],
            'last_name': form_data['last_name'],
            'email': form_data['email'],
            'phone_number': form_data['phone_number'],
            # Add more fields as needed
        }

        # Add the user data to user_data.json
        with open('user_data.json', 'r') as file:
            all_users_data = json.load(file)
            all_users_data.append(user_data)

        with open('user_data.json', 'w') as file:
            json.dump(all_users_data, file, indent=4)

        # Send a response back to JotForm
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'message': 'User data added successfully'}).encode())

def run_server():
    server_address = ('', 8000)  # Use port 8000, adjust as needed
    httpd = HTTPServer(server_address, JotFormWebhookHandler)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
