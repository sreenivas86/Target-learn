@'
{
    "include": [
        "CODE/**/*.py"
    ],
    "exclude": [
        "**/__pycache__",
        "**/.pytest_cache",
        "**/.venv",
        "**/venv",
        "**/env",
        "**/.git"
    ],
    "typeCheckingMode": "strict",
    "pythonVersion": "3.14",
    "reportMissingImports": "error",
    "reportMissingTypeStubs": "none",
    "reportUnusedImport": "warning",
    "reportUnusedVariable": "warning",
    "reportUndefinedVariable": "error",
    "reportUnboundVariable": "error",
    "reportArgumentType": "error",
    "reportAssignmentType": "error",
    "reportReturnType": "error"
}
'@ | Set-Content -Path "D:\TARGET-LEARN\pyrightconfig.json"