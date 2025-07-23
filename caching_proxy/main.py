import argparse
import sys
from .proxy_server import run_proxy_server, clear_cache

def main():
    parser = argparse.ArgumentParser(description="Start caching proxy server or clear cache.")
    parser.add_argument("--port", type=int, help="Port to run proxy server on.")
    parser.add_argument("--origin", type=str, help="Origin server URL (e.g. https://dummyjson.com)")
    parser.add_argument("--clear-cache", action="store_true", help="Clear the cached responses and exit.")

    args = parser.parse_args()

    if args.clear_cache:
        clear_cache()
        print("✅ Cache cleared successfully.")
        sys.exit(0)

    if not args.port or not args.origin:
        parser.error("--port and --origin are required unless using --clear-cache")

    run_proxy_server(port=args.port, origin=args.origin)
