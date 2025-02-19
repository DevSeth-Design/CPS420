# Porject Overview
- This is a FastApi project that allows users to create squares (for now... Circles comming soon! ) and get the area and perimeter.

## Getting Started
### 1. Clone from the repository
``` bash
git clone https://github.com/DevSeth-Design/CPS420.git
cd HW2/src
```
### 2. Create a virtual enviornment
#### Windows (PowerShell):
``` bash
    python -m venv mypy
    mypy\Scripts\Activate
```
#### Linux (Terminal):
``` bash
    python3 -m venv mypy
    mypy\Scripts\activate
```
### 3. Install dependencies
#### requirements.txt comming soon!
## Using this in the browser
### 1. Run the main class
``` bash
python -m main
```
### 2. select the http://127.0.0.1:8000 and it should load in the browser
### 3. In the browser's address bar add /docs and press enter. 
### 4. This should bring you to the FastApi docs page were you can test all the methods. 

## Testing
This project also has a test file to test the sqaures if you don't want to mannually imput them. 
### 1. Ensure you are in the root dir and run: 
``` bash
pytest
```
#### or if you want details: 
``` bash 
pytest -v
```
#### If you want to run only one of the test suites:
``` bash
pytest src\test\web
```
#### If you want to run an individual test module:
``` bash
pytest src\test\web\test_square.py
```
#### If you want to run an individual test module:
``` bash
pytest src\test\web\test_square.py -k test_case
```
#### This should test adding and getting squares [(8,15), (4.7, 1.1), (3, 1.4)] then testing the area and circumference
### NOTE: doing individual test cases may yeild poor results.    

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
