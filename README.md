# Django Template

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)


## Configuration

Before running the project, you need to configure certain settings. Follow the instructions below:

1. Rename the `.env.example` file to `.env`:

   ```shell
   mv .env.example .env
   
2. #### Open the .env file in a text editor and provide the necessary values for the environment variables:
    SECRET_KEY=your_secret_key

    DEBUG=True

    DATABASE_URL=your_database_url


## Installation

You can choose either of the following methods to install and set up the project:

### Docker Installation

1. Make sure you have Docker installed on your system. Refer to the [Docker documentation](https://docs.docker.com/get-docker/) for installation instructions.


2. Clone the repository:
    ```
    git clone https://github.com/nurbol0tt/restaurant.git
    ```
   2.1 Build the Docker image and start the container:
   ```
    cd RestaurantPlatForm
   ```
   ```
    docker-compose up --build
   ```

3. Access the application at http://0.0.0.0:8000/.
___


### Manual Installation

1. Clone the repository:
    ```
    git clone https://github.com/nurbol0tt/restaurant.git
    ```

2. Create a virtual environment:
    ```
    cd RestaurantPlatForm
    python -m venv env
    ```

3. Activate the virtual environment:
   * For Windows:
      ```
      .\env\Scripts\activate
      ```
   * For Unix/macOS:
      ```
      source env/bin/activate
      ```
     

4. Install the dependencies:
    ```
    pip install requirements.txt
    ```

5. Perform database migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:

   ``` 
   python manage.py runserver
   ```
   
7. Access the application at http://0.0.0.0:8000.


8. URL Address http://0.0.0.0:8000/api/swagger
## License

This project is licensed under the [MIT License](LICENSE).
