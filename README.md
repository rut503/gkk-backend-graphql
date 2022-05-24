# GKK Backend (Graphql Server)

## Install Requirements 
- Python v3.10.1
- pipenv v2022.3.28

## Commands

1. Install pipenv
    - `pip3 install pipenv`
2. Start python virtual environment (gkk-backend)
    - Be inside of directory (../gkk-backend-graphql/)
    - `pipenv shell`
3. Run server
    - `pipenv run uvicorn app.main:app --reload`

=========================================================
To run tests,
- Be inside of a virtual environment.
- Be in root dir, `gkk-backend-graphql`
- Package, Build and Install code by
    - `pipenv install -e .`
- Run `pytest`