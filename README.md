# Random Quote Generator

A small Python script that prints a random inspirational quote each time it runs. It was built as an exercise in setting up and using a Python virtual environment.

## Example output

```
$ python main.py

It always seems impossible until it's done. - Nelson Mandela
```

## Requirements

- Python 3 (developed with Python 3.15)

## Setup

1. Clone the repository and move into the project folder:

   ```bash
   git clone <repository-url>
   cd venv-exercise
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate it:

   ```bash
   # macOS / Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

With the virtual environment active, run:

```bash
python main.py
```

Each run picks one of 10 quotes at random and prints it as `Quote - Author`.

When you're done, leave the virtual environment with:

```bash
deactivate
```

## Project structure

```
venv-exercise/
├── main.py            # The quote generator
├── requirements.txt   # Pinned dependencies for the virtual environment
├── .gitignore         # Keeps venv/, caches and .env out of git
└── README.md
```

## Notes

- The `venv/` folder is not committed to the repository. Each person creates their own from `requirements.txt` using the setup steps above.
- `main.py` only uses Python's built-in `random` module. The packages in `requirements.txt` (`requests` and its dependencies) were installed as part of the virtual environment exercise and aren't needed to run the script.
