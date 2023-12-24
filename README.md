# API_ECG

## Requirements
Python 3.10 is required.

## Execution 
Create virtual environment
```bash
sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run app (only run locally, no configuration for a production environment available)
```bash
python main.py
```
The app run on http://localhost:8000

Run tests
```bash
pytest
```

## Notes
I didn't want to use more time than required, the development of the code took me about 4 hours. Besides, I used 5-6 hours to learn about FastAPI since I didn't know the technology and I thought it was interesting to take advantage of the technical test to learn.

Improvements to be made:
- Use the Dockerfile and implement the services in containers to be able to use it independently from the system and be able to add scalability.

- The tests are unfinished, I have lacked more time.
- There is no database to store the information, everything is in RAM memory. It would be interesting to implement one.
- Currently there is little code and everything is unified in a single module, as it grows it would be interesting to divide the logic by different modules, for example the authentication and ECG, also add the tests in each module and not have them in a global 'test' folder.