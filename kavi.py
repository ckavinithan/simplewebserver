from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <tittle>
            
        </tittle>
    </head>
    <body>
        <h1  >Device spefication ( Kavinithan )</h1>
        <table border="10" cellpadding="10">
            <tr>
                <td bgcolor="pink">S.no</td>
                <td bgcolor="pink">Device specification</td>
                <td bgcolor="pink">type</td>
            </tr>
            <tr>
                <td>1</td>
                <td>Kavin</td>
                <td>left</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Santhosh</td>
                <td>Right</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Sachin</td>
                <td>Right</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Ajay</td>
                <td>left</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Kervin</td>
                <td>Right</td>
            </tr>    
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()