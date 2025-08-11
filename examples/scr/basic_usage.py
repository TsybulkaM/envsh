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
host = envsh.read_env('HOST', str)
db_name = envsh.read_env('DB_NAME', str)

print(f"BASE_PORT: {base_port}")
print(f"HOST: {host}")
print(f"DB_NAME: {db_name}")

print("\n=== Interpolated Variables ===")
# These values were created using shell variable interpolation
database_url = envsh.read_env('DATABASE_URL', str)
api_endpoint = envsh.read_env('API_ENDPOINT', str)

print(f"DATABASE_URL: {database_url}")
print("  -> Built from: postgresql://$HOST:5432/$DB_NAME")
print(f"API_ENDPOINT: {api_endpoint}")
print("  -> Built from: http://$HOST:$BASE_PORT/api")

print("\n=== Complex Interpolation ===")
cache_size = envsh.read_env('CACHE_SIZE', int)
max_workers = envsh.read_env('MAX_WORKERS', int)
full_app_id = envsh.read_env('FULL_APP_ID', str)

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

print("\n=== Why this matters ===")
print("❌ Standard .env files can't do this:")
print("   DATABASE_URL=postgresql://$HOST:5432/$DB_NAME  # Won't work!")
print("   WORKER_PORTS=$BASE_PORT,8001,8002              # Won't work!")

print("\n✅ Envsh with shell scripts can:")
print("   - Use variable interpolation: $VAR, ${VAR}")
print("   - Perform calculations: $(($VAR + 1))")
print("   - Execute commands: $(date), $(nproc)")
print("   - Create dynamic configurations")
print("   - Share common values between variables")

print("\n=== Use Cases ===")
print("🔧 Dynamic port allocation based on base port")
print("🔧 Environment-specific database URLs")
print("🔧 Configuration that adapts to system resources")
print("🔧 Build-time variable injection")
print("🔧 Complex service discovery URLs")

print("\n=== Demo completed successfully! ===")
