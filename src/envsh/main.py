import subprocess
import inspect
import os
from pathlib import Path
from typing import List, Optional, Type, Union, overload

def _apply_shell_environment(script_path: Path) -> None:
    """Applies environment variables from shell script to current process."""
    command = f"source {script_path.resolve()} > /dev/null && printenv -0"
    try:
        result = subprocess.run(
            command,
            shell=True,
            executable='/bin/bash',
            capture_output=True,
            check=True,
            text=False
        )
        env_vars = result.stdout.strip(b'\0').split(b'\0')
        for var_line_bytes in env_vars:
            if not var_line_bytes:
                continue
            var_line = var_line_bytes.decode('utf-8')
            if '=' in var_line:
                key, value = var_line.split('=', 1)
                os.environ[key] = value
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise RuntimeError(f"Failed to load environment from {script_path}: {e}")

def load(search_paths: Optional[List[str]] = None, verbose: bool = False) -> bool:
    """Loads environment variables from .sh files in specified directories."""
    frame = inspect.currentframe()
    caller_frame = frame.f_back if frame else None
    caller_file = caller_frame.f_globals.get('__file__') if caller_frame else None
    caller_dir = Path(caller_file).parent.resolve() if caller_file else Path('.').resolve()

    if search_paths is None:
        search_paths = [str(caller_dir)]
    else:
        search_paths = [
            str((caller_dir / p).resolve()) if not Path(p).is_absolute() else str(Path(p).resolve())
            for p in search_paths
        ]

    if verbose:
        print(f"\nSearch paths: {search_paths}")

    found_files = set()
    for path_str in search_paths:
        path_obj = Path(path_str)
        if not path_obj.exists():
            continue
        for sh_file in path_obj.glob('*.sh'):
            found_files.add(sh_file.resolve())

    if not found_files:
        if verbose:
            print("No .sh files found in search paths")
        return False

    sorted_files = sorted(list(found_files))

    if verbose:
        print(f"Found {len(sorted_files)} .sh file(s):")
        for file_path in sorted_files:
            print(f"  -> {file_path}")

    for file_path in sorted_files:
        try:
            _apply_shell_environment(file_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load environment from {file_path}: {e}")

    return True

# Type overloads for proper typing
@overload
def read_env(name: str, return_type: Type[int]) -> int: ...

@overload
def read_env(name: str, return_type: Type[float]) -> float: ...

@overload
def read_env(name: str, return_type: Type[str]) -> str: ...

@overload
def read_env(name: str, return_type: Type[List[int]]) -> List[int]: ...

@overload
def read_env(name: str, return_type: Type[List[str]]) -> List[str]: ...


def read_env(name: str, return_type: Type[Union[int, str, List[int], List[str], float]]) -> Union[int, str, List[int], List[str], float]:
    """Reads environment variable with specified return type."""
    value = os.getenv(name)
    if value is None:
        raise EnvironmentError(f"The environment variable '{name}' is not set.")

    if return_type is int:
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"The environment variable '{name}' contains non-integer value: '{value}'")
        
    elif return_type is float:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"The environment variable '{name}' contains non-float value: '{value}'")

    elif return_type is str:
        return str(value)

    elif return_type is List[int]:
        if not value.strip():
            return []
        try:
            return [int(item.strip()) for item in value.split(',') if item.strip()]
        except ValueError:
            raise ValueError(f"The environment variable '{name}' contains non-integer values: '{value}'")

    elif return_type is List[str]:
        if not value.strip():
            return []
        return [item.strip() for item in value.split(',') if item.strip()]

    else:
        raise TypeError(f"Unsupported return type: {return_type}")

