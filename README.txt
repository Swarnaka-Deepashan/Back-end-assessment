# Project Setup Instructions

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python (version 3.x.x, as used in the project)
- pip (Python package manager)
- Virtual environment (optional but recommended)

## Installation

1. **Clone the repository**

   Start by cloning the project repository from GitHub to your local machine:

   git clone <URL_OF_THE_GITHUB_REPOSITORY>

    cd <REPOSITORY_NAME>


2. **Set up a virtual environment (Optional)**

It's recommended to create a virtual environment for your project dependencies. You can do this by running:python -m venv venv


Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

3. **Install project dependencies**

Install the required packages specified in the `requirements.txt` file:pip install -r requirements.txt



4. **Database Setup**

To fully run this project, you'll need the database file, which is too large to host directly on GitHub. You can download the database file from the following link:

[Download Database](https://drive.google.com/drive/folders/1JgfdGcfOWdTF7j42u-3DdZsA-T8GrlD5?usp=sharing)



5. **Running the Development Server**

Start the Django development server by running:python manage.py runserver

Access the application through your web browser at `http://127.0.0.1:8000/`.