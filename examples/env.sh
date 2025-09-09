#!/bin/bash

# Test environment variables for envsh library
# Demonstrating variable interpolation - the main advantage over .env files

# Base configuration
export BASE_PORT=8000
export HOST="localhost"
export DB_NAME="myapp"
export DB_USER="admin"
export DB_PASSWORD="secret123"

# Database configuration profile
declare -A DB_CONFIG=(
    [HOST]="$HOST"
    [PORT]="5432"
    [NAME]="$DB_NAME"
    [USER]="$DB_USER"
    [PASSWORD]="$DB_PASSWORD"
    [SSL_MODE]="prefer"
    [POOL_SIZE]="10"
    [TIMEOUT]="30"
)
export_array_as_json DB_CONFIG 2>/dev/null || true

# MQTT configuration profile
declare -A MQTT_CONFIG=(
    [HOST]="$HOST"
    [PORT]="1883"
    [USERNAME]="mqtt_user"
    [PASSWORD]="mqtt_pass"
    [TOPIC_PREFIX]="$APP_NAME"
    [QOS]="1"
    [KEEP_ALIVE]="60"
)
export_array_as_json MQTT_CONFIG 2>/dev/null || true

# Redis configuration profile
declare -A REDIS_CONFIG=(
    [HOST]="$HOST"
    [PORT]="6379"
    [PASSWORD]=""
    [DATABASE]="0"
    [POOL_SIZE]="5"
)
export_array_as_json REDIS_CONFIG 2>/dev/null || true

# Variable interpolation - this is what makes envsh special!
export DATABASE_URL="postgresql://${DB_CONFIG[USER]}:${DB_CONFIG[PASSWORD]}@${DB_CONFIG[HOST]}:${DB_CONFIG[PORT]}/${DB_CONFIG[NAME]}"
export REDIS_URL="redis://${REDIS_CONFIG[HOST]}:${REDIS_CONFIG[PORT]}/${REDIS_CONFIG[DATABASE]}"
export MQTT_URL="mqtt://${MQTT_CONFIG[USERNAME]}:${MQTT_CONFIG[PASSWORD]}@${MQTT_CONFIG[HOST]}:${MQTT_CONFIG[PORT]}"

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
