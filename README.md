# Social Media Website

This is a social media website built with Django and React. The backend is powered by Django, providing a robust and scalable API, while the frontend is developed with React for a dynamic and responsive user experience. The website features user authentication with JWT, enabling secure user interactions.

## Features

- User registration and login
- JWT-based authentication
- Create, update, and delete posts
- Like and comment on posts
- Share media content
- Responsive design

## Table of Contents

- [Installation](#installation)
- [Backend Setup (Django)](#backend-setup-django)
- [Frontend Setup (React)](#frontend-setup-react)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow the steps below to set up the project locally.

### Prerequisites

- Python 3.x
- Node.js and npm
- Django
- Django REST framework
- djangorestframework-simplejwt
- React

### Backend Setup (Django)

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/social-media-website.git
    cd social-media-website/backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

### Frontend Setup (React)

1. Navigate to the frontend directory:

    ```bash
    cd ../frontend
    ```

2. Install the required packages:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

## Usage

1. Open your web browser and go to `http://localhost:8000` to access the Django backend.
2. Open another tab and go to `http://localhost:3000` to access the React frontend.

## API Endpoints

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - User login and obtain JWT token
- `POST /api/auth/logout/` - User logout
- `GET /api/posts/` - Retrieve all posts
- `POST /api/posts/` - Create a new post
- `GET /api/posts/{id}/` - Retrieve a single post
- `PUT /api/posts/{id}/` - Update a post
- `DELETE /api/posts/{id}/` - Delete a post
- `POST /api/posts/{id}/like/` - Like a post
- `POST /api/posts/{id}/comment/` - Comment on a post

## Technologies Used

- **Backend:**
  - Django
  - Django REST framework
  - djangorestframework-simplejwt

- **Frontend:**
  - React
  - Axios (for API requests)
  - Redux (for state management)
  - Tailwind CSS (for styling)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding!
