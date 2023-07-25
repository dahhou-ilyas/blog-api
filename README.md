# blog-api
a blog API , can create create, delete and put blog with authentication

## Installation

To install the project and its dependencies using `pipenv`, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies with pipenv:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
## Usage

1. create superuser:
   ```bash
   python manage.py createsuperuser
   ```
2. Run the development server:
   ```bash
   python manage.py runserver
   ```

## endpoint
1. admin/
2. blog/
4. blog/<str:pk>/
5. addBlog/
6. users/
7. users/<int:pk>/
8. api-auth/ login/ [name='login']
9. api-auth/ logout/ [name='logout']

