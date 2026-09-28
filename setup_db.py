import os
import sys

def main():
    print("--- CodSoft Task 1: Database Setup Utility ---")
    
    # Check if .env exists
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    env_vars = {}
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env_vars[k.strip()] = v.strip().strip("'").strip('"')

    use_mysql = env_vars.get('USE_MYSQL', 'true').lower() in ('true', '1', 'yes')

    if use_mysql:
        db_name = env_vars.get('DB_NAME', 'todo_db')
        db_user = env_vars.get('DB_USER', 'root')
        db_password = env_vars.get('DB_PASSWORD', '')
        db_host = env_vars.get('DB_HOST', 'localhost')
        db_port = int(env_vars.get('DB_PORT', '3306'))

        print(f"Connecting to MySQL server at {db_host}:{db_port} as user '{db_user}'...")

        try:
            import MySQLdb
            conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, port=db_port)
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            print(f"[SUCCESS] MySQL database '{db_name}' ensured successfully!")
            conn.close()
        except Exception as e:
            print(f"[WARNING] Could not connect to MySQL server with current credentials ({e}).")
            print("Switching fallback mode: Django will run on SQLite3 so you can use the app immediately.")
            print("To connect to MySQL, update your DB_PASSWORD in '.env' and set USE_MYSQL=true.")
            
            # Update .env to fallback to SQLite
            new_lines = []
            if os.path.exists(env_file):
                with open(env_file, 'r') as f:
                    for line in f:
                        if line.startswith('USE_MYSQL='):
                            new_lines.append('USE_MYSQL=false\n')
                        else:
                            new_lines.append(line)
            with open(env_file, 'w') as f:
                f.writelines(new_lines)
    else:
        print("Using SQLite3 database backend.")

if __name__ == '__main__':
    main()
