from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys
sys.path.append('.')  # Add current directory to path

from src.model_training import BasicClassifier
from src.entity_extraction import EntityExtractor

class SalesCallAnalysisHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.classifier = BasicClassifier()
        self.entity_extractor = EntityExtractor()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == '/analyze':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            text = request_data.get('text', '')
            labels = self.classifier.predict_labels(text)
            entities = self.entity_extractor.extract_entities(text)
            
            response = {
                'text': text,
                'labels': labels,
                'entities': entities,
                'summary': f"Analysis of text with {len(labels)} labels"
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404)

    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy"}).encode('utf-8'))
        else:
            self.send_error(404)

def run_server(port=5000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SalesCallAnalysisHandler)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()