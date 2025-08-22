# Database Configuration
# Copy this file to .env or set these as environment variables

# MySQL Configuration
DB_NAME = "genaimech_db"           # Database name
DB_USER = "root"                   # MySQL username
DB_PASSWORD = ""                    # MySQL password
DB_HOST = "localhost"              # MySQL host
DB_PORT = "3306"                   # MySQL port

# Alternative: If you want to use MongoDB instead
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'genaimech_db',
#         'CLIENT': {
#             'host': 'mongodb://localhost:27017',
#             'username': 'your_username',
#             'password': 'your_password',
#         }
#     }
# }

# Alternative: If you want to use SQLite instead
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
