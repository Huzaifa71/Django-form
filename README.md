# Django User Authentication Project

This is a simple Django project demonstrating user authentication features, including sign up, sign in, and sign out functionalities.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you set up the project locally for development and testing purposes.

### Prerequisites

Make sure you have the following software installed on your system:

- Python (version 3.9)
- Django (version 4.2.11)

### Installation

1. Clone the repository:

    ```bash 
    git clone https://github.com/Huzaifa71/Django-form.git
    ```

2. Change directory to the project folder:

    ```bash
    cd cd Django-form
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Visit [http://127.0.0.1:8000/signup/](http://127.0.0.1:8000/signup/) to register a new user.
- Access [http://127.0.0.1:8000/signin/](http://127.0.0.1:8000/signin/) to log in with your registered credentials.
- Navigate to [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/) for the home page (protected, requires authentication).
- To log out, visit [http://127.0.0.1:8000/logout/](http://127.0.0.1:8000/logout/).

## Contributing

If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new pull request

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.
