# Django Example Project

A modern Django web application built with Docker, PostgreSQL, and Poetry for dependency management.

## 🚀 Features

- **Django 5.2+** - Latest Django framework
- **PostgreSQL** - Robust database backend
- **Docker & Docker Compose** - Containerized development environment
- **Poetry** - Modern Python dependency management
- **Environment-based configuration** - Secure configuration management
- **Russian localization** - Configured for Russian language and timezone

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started) and Docker Compose
- [Poetry](https://python-poetry.org/docs/#installation) (for local development)
- Python 3.11+ (for local development)

## 🛠️ Installation

### Using Docker (Recommended)

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd django-example
   ```

2. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

3. **Start the services**

   ```bash
   # Start database and storage services
   make storages

   # Start the full application
   make app
   ```

4. **Run database migrations**

   ```bash
   make migrate
   ```

5. **Create a superuser (optional)**

   ```bash
   make superuser
   ```

6. **Collect static files**
   ```bash
   make collectstatic
   ```

### Local Development

1. **Install dependencies**

   ```bash
   poetry install
   ```

2. **Activate virtual environment**

   ```bash
   poetry shell
   ```

3. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

## 🐳 Docker Commands

The project includes a comprehensive Makefile for easy Docker management:

### Database Management

```bash
make storages          # Start PostgreSQL database
make storages-down     # Stop database services
make storages-logs     # View database logs
make postgres          # Connect to PostgreSQL shell
```

### Application Management

```bash
make app               # Start full application stack
make app-down          # Stop application stack
make app-logs          # View application logs
```

### Django Management

```bash
make migrate           # Run database migrations
make migrations        # Create new migrations
make superuser         # Create Django superuser
make collectstatic     # Collect static files
```

## 📁 Project Structure

```
django-example/
├── core/                          # Main Django project
│   ├── apps/                      # Django applications
│   │   └── products/              # Products app
│   └── project/                   # Project configuration
│       ├── settings/              # Settings modules
│       │   ├── main.py           # Main settings
│       │   └── local.py          # Local development settings
│       ├── urls.py               # URL configuration
│       ├── wsgi.py               # WSGI configuration
│       └── asgi.py               # ASGI configuration
├── docker_compose/                # Docker Compose configurations
│   ├── app.yaml                  # Application services
│   └── storages.yaml             # Database services
├── static/                       # Static files
├── Dockerfile                    # Docker image configuration
├── entrypoint.sh                 # Container entrypoint script
├── Makefile                      # Development commands
├── manage.py                     # Django management script
├── pyproject.toml                # Poetry configuration
└── .env                          # Environment variables
```

## ⚙️ Configuration

### Environment Variables

The application uses environment variables for configuration. Key variables include:

- `DJANGO_KEY` - Django secret key
- `POSTGRES_DB` - Database name
- `POSTGRES_USER` - Database user
- `POSTGRES_PASSWORD` - Database password
- `POSTGRES_HOST` - Database host
- `POSTGRES_PORT` - Database port
- `DJANGO_PORT` - Django application port

### Settings

The project uses a modular settings structure:

- `main.py` - Base settings for all environments
- `local.py` - Local development overrides

## 🗄️ Database

The project uses PostgreSQL as the primary database. The database configuration is handled through environment variables and supports:

- Connection pooling
- Environment-specific configurations
- Docker-based development setup

## 🌐 Localization

The application is configured for Russian localization:

- Language: Russian (`ru`)
- Timezone: Europe/Moscow
- Internationalization enabled

## 🚀 Deployment

### Production Considerations

1. **Security**

   - Change the default secret key
   - Set `DEBUG = False`
   - Configure proper `ALLOWED_HOSTS`
   - Use environment-specific database credentials

2. **Static Files**

   - Run `make collectstatic` to collect static files
   - Configure static file serving for production

3. **Database**
   - Use production-grade PostgreSQL configuration
   - Set up proper backup strategies

## 🧪 Development

### Adding New Apps

1. Create a new Django app:

   ```bash
   make migrations  # If you have a running container
   # or
   python manage.py startapp <app_name>
   ```

2. Add the app to `INSTALLED_APPS` in settings

3. Create and run migrations:
   ```bash
   make migrations
   make migrate
   ```

### Code Style

The project follows Django best practices and PEP 8 guidelines.

## 📝 API Documentation

Currently, the project includes:

- Django Admin interface (accessible at `/admin/`)
- Basic Django models structure
- REST API endpoints (to be implemented)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Review the Docker logs: `make app-logs`
3. Check database connectivity: `make postgres`

## 🔄 Updates

To update the project:

1. Pull the latest changes
2. Update dependencies: `poetry update`
3. Run migrations: `make migrate`
4. Restart services: `make app-down && make app`

---

**Happy coding!** 🎉
