# Database Setup Guide

## MySQL Setup

### Option 1: Local MySQL Installation

1. **Install MySQL Community Edition:**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - Or use Docker: `docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=your_password mysql:8.0`

2. **Start MySQL Service:**
   ```bash
   # Windows
   net start MySQL80
   
   # Linux/Mac
   sudo systemctl start mysql
   ```

3. **Create .env file:**
   ```bash
   # Copy database_config.py content to .env file
   DB_NAME=genaimech_db
   DB_USER=root
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

### Option 2: MySQL Cloud (AWS RDS, Google Cloud SQL, etc.)

1. **Create MySQL Cloud Instance:**
   - AWS RDS: https://aws.amazon.com/rds/mysql/
   - Google Cloud SQL: https://cloud.google.com/sql/docs/mysql
   - Or any other cloud provider

2. **Get Connection Details:**
   - Note down the host, port, username, and password
   - Ensure the instance is publicly accessible or configure VPC

3. **Update .env file:**
   ```bash
   DB_NAME=genaimech_db
   DB_USER=your_cloud_username
   DB_PASSWORD=your_cloud_password
   DB_HOST=your_cloud_host.amazonaws.com
   DB_PORT=3306
   ```

### Option 3: SQLite (Alternative)

If you prefer SQLite instead of MySQL:

1. **Update settings.py:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

2. **Remove MySQL dependencies:**
   - Remove `mysqlclient` from requirements.txt
   - Remove `django-environ` if not needed

## Database Migration

After setting up the database:

```bash
# Navigate to backend directory
cd Gen-AI-Hackathon/backend/genaimechbackend

# Install dependencies
pip install -r requirements.txt

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## Testing Database Connection

```bash
# Test Django shell
python manage.py shell

# In Django shell:
from django.db import connection
connection.ensure_connection()
print("Database connected successfully!")
```

## Troubleshooting

### Common Issues:

1. **MySQL not running:**
   - Check if MySQL service is started
   - Verify port 3306 is not blocked

2. **Authentication failed:**
   - Check username/password in .env file
   - Ensure user has proper permissions
   - Try connecting with MySQL client: `mysql -u root -p`

3. **Connection timeout:**
   - Check network connectivity
   - Verify MySQL host and port
   - Check firewall settings

4. **MySQL client compatibility:**
   - Ensure Django and mysqlclient versions are compatible
   - Current setup: Django 4.1.13 + mysqlclient 2.2.4

5. **Database not exists:**
   - Create database manually: `CREATE DATABASE genaimech_db;`
   - Or let Django create it during migration
