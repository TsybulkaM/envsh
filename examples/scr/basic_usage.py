import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
# Example usage of envsh library - demonstrating variable interpolation advantage

import envsh

print("=== Envsh: Shell Variable Interpolation Demo ===")
print("The main advantage over .env files: full shell variable interpolation!\n")

# Load environment variables with interpolation
# Path is interpreted relative to the caller's directory,
#   so we use the parent directory in this case
envsh.load(['..'])

print("\n=== Basic Variables ===")
base_port = envsh.read_env('BASE_PORT', int)
host = envsh.read_env('HOST')
db_name = envsh.read_env('DB_NAME')
# DEBUG_MODE will use default value as it's not set in env.sh, for reducing boilerplate 
DEBUG_MODE = envsh.read_env('DEBUG_MODE', int, default=0)

print(f"BASE_PORT: {base_port}")
print(f"HOST: {host}")
print(f"DB_NAME: {db_name}")
print(f"DEBUG_MODE: {DEBUG_MODE}")

print("\n=== Configuration Structures (JSON from Bash Associative Arrays) ===")
# Read configuration structures exported as JSON
db_config = envsh.read_env('DB_CONFIG_JSON', dict)
mqtt_config = envsh.read_env('MQTT_CONFIG_JSON', dict)
redis_config = envsh.read_env('REDIS_CONFIG_JSON', dict)

print(f"DB_CONFIG: {db_config}")
print("  -> Host:", db_config['HOST'])
print("  -> Port:", db_config['PORT'])
print("  -> Database:", db_config['NAME'])
print("  -> Pool Size:", db_config['POOL_SIZE'])

print(f"\nMQTT_CONFIG: {mqtt_config}")
print("  -> Host:", mqtt_config['HOST'])
print("  -> Port:", mqtt_config['PORT'])
print("  -> Username:", mqtt_config['USERNAME'])
print("  -> Topic Prefix:", mqtt_config.get('TOPIC_PREFIX', 'N/A'))

print(f"\nREDIS_CONFIG: {redis_config}")
print("  -> Host:", redis_config['HOST'])
print("  -> Port:", redis_config['PORT'])
print("  -> Database:", redis_config['DATABASE'])
print("  -> Pool Size:", redis_config['POOL_SIZE'])

print("\n=== Using Configuration Structures ===")
# Demonstrate practical usage of configuration structures
def create_database_connection_string(config: dict) -> str:
    """Create database connection string from config structure."""
    return f"postgresql://{config['USER']}:{config['PASSWORD']}@{config['HOST']}:{config['PORT']}/{config['NAME']}?sslmode={config['SSL_MODE']}"

def create_redis_connection_string(config: dict) -> str:
    """Create Redis connection string from config structure."""
    password_part = f":{config['PASSWORD']}@" if config['PASSWORD'] else ""
    return f"redis://{password_part}{config['HOST']}:{config['PORT']}/{config['DATABASE']}"

def create_mqtt_connection_string(config: dict) -> str:
    """Create MQTT connection string from config structure."""
    return f"mqtt://{config['USERNAME']}:{config['PASSWORD']}@{config['HOST']}:{config['PORT']}"

db_conn_str = create_database_connection_string(db_config)
redis_conn_str = create_redis_connection_string(redis_config)
mqtt_conn_str = create_mqtt_connection_string(mqtt_config)

print(f"Database Connection: {db_conn_str}")
print(f"Redis Connection: {redis_conn_str}")
print(f"MQTT Connection: {mqtt_conn_str}")

print("\n=== Interpolated Variables ===")
# These values were created using shell variable interpolation
database_url = envsh.read_env('DATABASE_URL')
redis_url = envsh.read_env('REDIS_URL')
mqtt_url = envsh.read_env('MQTT_URL')
api_endpoint = envsh.read_env('API_ENDPOINT')

print(f"DATABASE_URL: {database_url}")
print("  -> Built from: postgresql://${DB_CONFIG[USER]}:${DB_CONFIG[PASSWORD]}@${DB_CONFIG[HOST]}:${DB_CONFIG[PORT]}/${DB_CONFIG[NAME]}")
print(f"REDIS_URL: {redis_url}")
print("  -> Built from: redis://${REDIS_CONFIG[HOST]}:${REDIS_CONFIG[PORT]}/${REDIS_CONFIG[DATABASE]}")
print(f"MQTT_URL: {mqtt_url}")
print("  -> Built from: mqtt://${MQTT_CONFIG[USERNAME]}:${MQTT_CONFIG[PASSWORD]}@${MQTT_CONFIG[HOST]}:${MQTT_CONFIG[PORT]}")
print(f"API_ENDPOINT: {api_endpoint}")
print("  -> Built from: http://$HOST:$BASE_PORT/api")

print("\n=== Complex Interpolation ===")
cache_size = envsh.read_env('CACHE_SIZE', int)
max_workers = envsh.read_env('MAX_WORKERS', int)
full_app_id = envsh.read_env('FULL_APP_ID')

print(f"CACHE_SIZE: {cache_size} bytes")
print("  -> Calculated with: $((1024 * 1024))")
print(f"MAX_WORKERS: {max_workers}")
print("  -> Set to CPU cores with: $(nproc)")
print(f"FULL_APP_ID: {full_app_id}")
print("  -> Built with date command: $APP_NAME-$(date +%Y%m%d)")

print("\n=== Interpolated Arrays ===")
worker_ports = envsh.read_env('WORKER_PORTS', list[int])
service_urls = envsh.read_env('SERVICE_URLS', list[str])
port_range = envsh.read_env('PORT_RANGE', list[int])

print(f"WORKER_PORTS: {worker_ports}")
print("  -> Calculated ports: $BASE_PORT,$(($BASE_PORT + 1)),$(($BASE_PORT + 2))")
print(f"SERVICE_URLS: {service_urls}")
print("  -> Mixed interpolation with different protocols")
print(f"PORT_RANGE: {port_range}")
print("  -> Port calculations: $BASE_PORT,$(($BASE_PORT + 100)),$(($BASE_PORT + 200))")

print("\n=== Configuration Management Examples ===")
# Demonstrate how to use structures for configuration management
print("🔧 Database Configuration Management:")
print(f"  - Connection Pool: {db_config['POOL_SIZE']} connections")
print(f"  - Connection Timeout: {db_config['TIMEOUT']} seconds")
print(f"  - SSL Mode: {db_config['SSL_MODE']}")

print("\n🔧 MQTT Configuration Management:")
print(f"  - Quality of Service: {mqtt_config['QOS']}")
print(f"  - Keep Alive: {mqtt_config['KEEP_ALIVE']} seconds")
print(f"  - Topic Prefix: {mqtt_config.get('TOPIC_PREFIX', 'Not set')}")

print("\n🔧 Redis Configuration Management:")
print(f"  - Connection Pool: {redis_config['POOL_SIZE']} connections")
print(f"  - Database Index: {redis_config['DATABASE']}")
print(f"  - Password Protected: {'Yes' if redis_config['PASSWORD'] else 'No'}")

print("\n=== Why Configuration Structures Matter ===")
print("❌ Standard .env files:")
print("   DB_HOST=localhost")
print("   DB_PORT=5432")
print("   DB_USER=admin")
print("   # Flat structure, no organization")

print("\n✅ Envsh with Bash associative arrays:")
print("   declare -A DB_CONFIG=(")
print("       [HOST]='localhost'")
print("       [PORT]='5432'")
print("       [USER]='admin'")
print("   )")
print("   export_array_as_json DB_CONFIG")
print("   # Structured configuration, easy to manage!")

print("\n=== Advanced Use Cases ===")
print("🔧 Multi-environment configuration profiles")
print("🔧 Service discovery with structured endpoints")
print("🔧 Connection pool management")
print("🔧 Feature flags and service configurations")
print("🔧 Microservices configuration templates")

print("\n=== Demo completed successfully! ===")