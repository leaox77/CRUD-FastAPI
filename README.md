# FastAPI CRUD Project

This is a basic CRUD application using FastAPI, Bootstrap, and Axios to handle form submissions and dynamic content rendering.

## Requirements

- Python 3.11
- Conda

## Setup

### 1. Install Conda

If Conda is not installed, download and install it from [here](https://docs.conda.io/en/latest/miniconda.html).

### 2. Create a Conda Environment

Run the following command to create a new environment with Python 3.11:

```bash
conda create --name fastapi_env python=3.11
```

### 3. Activate the enviroment.

```bash
conda activate fastapi_env
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
uvicorn main:app --reload
```