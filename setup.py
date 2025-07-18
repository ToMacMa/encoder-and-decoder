from cx_Freeze import setup

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
}

setup(
    name="Encdecoder",
    version="1.0",
    description="An app for decoding and encoding text.",
    options={"build_exe": build_exe_options},
    executables=[{"script": "gui.py", "base": "gui"}],
)