## Prerequisites
1. Create python virtual environment
2. Activate the virtual environment:
    - On macOS/Linux: `source venv/bin/activate`
    - On Windows: `.\venv\Scripts\activate`
3. Install dependencies:
    - `pip install -r requirements.txt`

## Steps to build and run

- `docker build --tag kbs-02 . `
- `docker run -it kbs-02`
- `python app.py`
