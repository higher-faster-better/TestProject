import os
import re

def update_file(filepath, pattern, replacement):
    """Update the given file by replacing the specified pattern."""
    temp_filepath = f"{filepath}.tmp"

    with open(filepath, "r") as file, open(temp_filepath, "w") as temp_file:
        for line in file:
            temp_file.write(re.sub(pattern, replacement, line))

    os.replace(temp_filepath, filepath)

def update_version_numbers():
    """Update build version numbers in SConstruct and VERSION files."""
    source_path = os.environ.get("SourcePath", "")
    build_num = os.environ.get("BuildNum", "")

    if not source_path or not build_num.isdigit():
        raise ValueError("Invalid environment variables: SourcePath or BuildNum.")

    files = {
        "SConstruct": (r"point=\d+", f"point={build_num}"),
        "VERSION": (r"ADLMSDK_VERSION_POINT=\d+", f"ADLMSDK_VERSION_POINT={build_num}")
    }

    for filename, (pattern, replacement) in files.items():
        filepath = os.path.join(source_path, "develop", "global", "src", filename)

        if os.path.exists(filepath):
            os.chmod(filepath, 0o755)
            update_file(filepath, pattern, replacement)
        else:
            print(f"Warning: {filepath} not found!")

if __name__ == "__main__":
    update_version_numbers()
