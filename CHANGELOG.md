# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
