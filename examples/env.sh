#!/bin/bash

# Test environment variables for envsh library
# Demonstrating variable interpolation - the main advantage over .env files

export BASE_PORT=8000
export HOST="localhost"
export DB_NAME="myapp"

# Variable interpolation - this is what makes envsh special!
export DATABASE_URL="postgresql://$HOST:5432/$DB_NAME"
export API_ENDPOINT="http://$HOST:$BASE_PORT/api"
export WORKER_PORTS="$BASE_PORT,$(($BASE_PORT + 1)),$(($BASE_PORT + 2))"

# Complex interpolation with calculations
export CACHE_SIZE=$((1024 * 1024))  # 1MB in bytes
export MAX_WORKERS=$(nproc)         # Number of CPU cores

# Array with interpolated values
export SERVICE_URLS="http://$HOST:$BASE_PORT,https://$HOST:8443,ws://$HOST:9000"
export PORT_RANGE="$BASE_PORT,$(($BASE_PORT + 100)),$(($BASE_PORT + 200))"

# Environment-specific configurations
export LOG_LEVEL="DEBUG"
export APP_NAME="envsh-demo"
export FULL_APP_ID="$APP_NAME-$(date +%Y%m%d)"
