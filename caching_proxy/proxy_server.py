from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import threading

# In-memory cache
cache = {}
cache_lock = threading.Lock()

class CachingProxyHandler(BaseHTTPRequestHandler):
    origin = None

    def do_GET(self):
        target_url = f"{self.origin}{self.path}"

        with cache_lock:
            if target_url in cache:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(cache[target_url])))
                self.send_header("X-Cache", "HIT")
                self.end_headers()
                self.wfile.write(cache[target_url])
                print(f"Cache HIT: {target_url}")
                return

        try:
            response = requests.get(target_url, stream=True)
            content = response.content

            self.send_response(response.status_code)
            self.send_header("Content-Type", response.headers.get("Content-Type", "application/json"))
            self.send_header("Content-Length", str(len(content)))
            self.send_header("X-Cache", "MISS")
            self.end_headers()

            self.wfile.write(content)

            # Cache the content
            with cache_lock:
                cache[target_url] = content

            print(f"Cache MISS: {target_url}")
        except requests.RequestException as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(b"Bad Gateway: Could not reach origin server.")


def run_proxy_server(port, origin):
    CachingProxyHandler.origin = origin.rstrip("/")  # Remove trailing slash
    server = HTTPServer(("", port), CachingProxyHandler)
    print(f"Proxy server running on port {port}, forwarding to {origin}")
    server.serve_forever()

def clear_cache():
    with cache_lock:
        cache.clear()
