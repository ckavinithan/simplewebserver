from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <tittle>
            
        </tittle>
    </head>
    <body>
        <h1  >Device spefication ( Kavinithan - 25011970)</h1>
        <table border="10" cellpadding="10">
            <tr>
                <td bgcolor="pink">S.no</td>
                <td bgcolor="pink">Device name</td>
                <td bgcolor="pink">RAM</td>
                <td bgcolor="pink">Device ID</td>
                <td bgcolor="pink">Product ID</td>
            </tr>
            <tr>
                <td>1</td>
                <td>TMP215-75-G2</td>
                <td>16.0 GB </td>
                <td>8ADCC6A1-2205-442F-A722-1D58E3978823</td>
                <td>00342-42784-66156-AAOEM</td>
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