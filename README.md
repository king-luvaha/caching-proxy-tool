# ⚡ Caching Proxy CLI Tool

A lightweight Python CLI tool to start a caching proxy server that forwards `GET` requests to an origin server, caches responses, and serves cached content on repeat requests. Built for developers and API testers.

---

## 🚀 Features

- 🔁 Forwards `GET` requests to an origin server
- ⚡ In-memory response caching
- 📦 Adds `X-Cache: HIT` or `MISS` response headers
- 🧹 Clear cache via CLI (`--clear-cache`)
- 🧪 Testable via Postman or cURL
- 🛠️ Minimal dependencies, fast and easy to use

---

## 📦 Installation

### ✅ 1. Clone the repository

```bash
git clone https://github.com/your-username/caching_proxy.git
cd caching_proxy
````

### ✅ 2. Create and activate a virtual environment

```bash
# Create venv
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (macOS/Linux)
source venv/bin/activate
```

### ✅ 3. Install required dependencies

```bash
pip install requests
```

### ✅ 4. Install the tool in editable (dev) mode

```bash
pip install --editable .
```

This registers the CLI tool globally in your environment as:

```
caching-proxy
```

---

## 🧑‍💻 Usage

### ✅ Start the proxy server

```bash
caching-proxy --port 3000 --origin https://dummyjson.com
```

This starts the proxy at `http://localhost:3000` and forwards requests to `https://dummyjson.com`.

---

### 🔁 Example Request

Send a `GET` request to:

```
http://localhost:3000/products/1
```

| Request # | Behavior          | Header          |
| --------- | ----------------- | --------------- |
| First     | Fetch from origin | `X-Cache: MISS` |
| Second+   | Serve from cache  | `X-Cache: HIT`  |

✅ Cached responses are returned instantly.

---

### ♻️ Clear the cache

To manually clear all cached responses:

```bash
caching-proxy --clear-cache
```

Output:

```
✅ Cache cleared successfully.
```

---

## 🧪 Testing with Postman

1. Open [Postman](https://www.postman.com/)
2. Create a `GET` request to:

```
http://localhost:3000/products/1
```

3. Click **Send** and inspect the **Headers** tab in the response.
4. Look for `X-Cache: HIT` or `MISS`.

---

## 📁 Project Structure

```
caching_proxy/
├── caching_proxy/
│   ├── __init__.py
│   ├── main.py             # CLI entry point
│   └── proxy_server.py     # Proxy server logic
├── pyproject.toml          # Tool configuration and CLI script
```

---

## ⚙️ How It Works

* Builds a local HTTP server that listens on your specified port.
* Forwards incoming `GET` requests to a remote origin server.
* Caches the full response in memory (URL → content).
* Adds an `X-Cache` header to identify source (cache or origin).
* Supports manual cache clearing via `--clear-cache`.

---

## 🔒 Notes

* Only `GET` requests are supported.
* Cache is stored in memory — it's reset on restart.
* Avoids chunked transfer encoding for Postman compatibility.

---

## 🧠 Roadmap Ideas

* [ ] Cache TTL (expiration timer)
* [ ] Redis or disk-based persistent cache
* [ ] `--cache-stats` command for debugging
* [ ] Support for POST/PUT methods (optional)
* [ ] Caching rules (e.g. path whitelist/blacklist)
* [ ] Publish to PyPI for global installation

---

## 📜 License

[MIT License](LICENSE) © 2025

---

## 🤝 Contributions

Feel free to fork, submit issues, or open pull requests. Let's make this tool even better!

---

Roadmap Project URL: https://roadmap.sh/projects/caching-server
