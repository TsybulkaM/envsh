# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2025-10-01

### Added

- Support for `list[float]` type

## [0.1.3] - 2025-09-28

### Added

- Type overloads for the `read_env` function with `default` argument support for all types.
- Explicit warning when using a default value for missing environment variables.
- Updated documentation and examples for structured configuration usage.

## [0.1.2] - 2025-09-09

### Added
- Bash associative arrays support via `envsh-utils.sh`
- `export_array_as_json` function for converting associative arrays to JSON
- Support for reading dictionary structures with `read_env(..., dict)` 
- Variable interpolation within associative array values
- Complex configuration profiles using structured data
- Enhanced shell utilities for better configuration management
- Examples demonstrating structured configuration usage

### Enhanced
- Shell environment loading now includes utility functions
- Improved documentation with structured configuration examples

## [0.1.1] - 2025-08-27

### Added
- Windows support using Git Bash and MSYS2
- Automatic detection of Windows vs Unix systems

## [0.1.0] - 2025-08-11

### Added
- Initial release of envsh library
- `load()` function to load environment variables from .sh files
- `read_env()` function with type-safe reading capabilities
- Support for int, float, str, list[int], and list[str] types
- Automatic type conversion and validation
- Array parsing from comma-separated values
- Comprehensive error handling
- Full type hints and py.typed marker file
- Unit tests with 100% coverage
- Documentation and examples

### Features
- Search multiple directories for shell scripts
- Automatic whitespace trimming in arrays
- Empty element filtering in arrays
- Verbose logging option
- Clean error messages for debugging
