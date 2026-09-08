# ============================================================
# TARGET-LEARN Folder Structure
# ============================================================

$Root = "D:\TARGET-LEARN"

# Create root directory
New-Item -ItemType Directory -Path $Root -Force | Out-Null


# ============================================================
# CODE
# ============================================================

$CodeFolders = @(
    "code\python\basics",
    "code\python\advanced",
    "code\python\oop",
    "code\python\modules",
    "code\python\file_handling",
    "code\python\exceptions",
    "code\python\decorators",
    "code\python\generators",
    "code\python\practice",

    "code\dsa\arrays",
    "code\dsa\strings",
    "code\dsa\hashing",
    "code\dsa\two_pointers",
    "code\dsa\sliding_window",
    "code\dsa\prefix_suffix",
    "code\dsa\binary_search",
    "code\dsa\stack",
    "code\dsa\queue",
    "code\dsa\linked_list",
    "code\dsa\heap",
    "code\dsa\intervals",
    "code\dsa\trees",
    "code\dsa\graphs",
    "code\dsa\greedy",
    "code\dsa\backtracking",
    "code\dsa\dynamic_programming",

    "code\sql\basics",
    "code\sql\joins",
    "code\sql\subqueries",
    "code\sql\window_functions",
    "code\sql\indexes",
    "code\sql\optimization",

    "code\backend\fastapi",
    "code\backend\rest_api",
    "code\backend\authentication",
    "code\backend\sqlalchemy",
    "code\backend\postgresql",
    "code\backend\redis",
    "code\backend\testing",

    "code\kafka\producers",
    "code\kafka\consumers",
    "code\kafka\partitions",
    "code\kafka\projects",

    "code\aws\iam",
    "code\aws\ec2",
    "code\aws\s3",
    "code\aws\lambda",
    "code\aws\ecr",
    "code\aws\eks",
    "code\aws\cloudwatch",

    "code\docker",
    "code\kubernetes",
    "code\terraform",
    "code\linux",
    "code\networking"
)


# ============================================================
# DOCUMENTS
# ============================================================

$DocumentFolders = @(
    "documents\plan",

    "documents\dsa\patterns",
    "documents\dsa\concepts",
    "documents\dsa\interview_questions",
    "documents\dsa\mistakes",

    "documents\python\concepts",
    "documents\python\interview_questions",
    "documents\python\notes",

    "documents\sql\concepts",
    "documents\sql\interview_questions",
    "documents\sql\queries",

    "documents\backend\fastapi",
    "documents\backend\rest_api",
    "documents\backend\authentication",
    "documents\backend\databases",
    "documents\backend\testing",

    "documents\system_design\lld",
    "documents\system_design\hld",
    "documents\system_design\architecture",
    "documents\system_design\case_studies",

    "documents\cloud\aws",
    "documents\cloud\azure",
    "documents\cloud\devops",

    "documents\interview\dsa",
    "documents\interview\python",
    "documents\interview\sql",
    "documents\interview\backend",
    "documents\interview\system_design",
    "documents\interview\behavioral"
)


# ============================================================
# PROJECTS
# ============================================================

$ProjectFolders = @(
    "projects\budgetflow",
    "projects\realtime_chat",
    "projects\fastapi_microservice",
    "projects\cloud_cicd"
)


# ============================================================
# INTERVIEW
# ============================================================

$InterviewFolders = @(
    "interview\company_questions",
    "interview\mock_interviews",
    "interview\mistakes",
    "interview\revision"
)


# ============================================================
# CERTIFICATIONS
# ============================================================

$CertificationFolders = @(
    "certifications\aws",
    "certifications\azure",
    "certifications\other"
)


# ============================================================
# RESUME
# ============================================================

$ResumeFolders = @(
    "resume\master",
    "resume\python_backend",
    "resume\ats",
    "resume\old_versions"
)


# ============================================================
# CREATE ALL FOLDERS
# ============================================================

$AllFolders = @(
    $CodeFolders +
    $DocumentFolders +
    $ProjectFolders +
    $InterviewFolders +
    $CertificationFolders +
    $ResumeFolders
)

foreach ($Folder in $AllFolders) {

    $FullPath = Join-Path $Root $Folder

    # Create folder
    New-Item `
        -ItemType Directory `
        -Path $FullPath `
        -Force | Out-Null

    # Create .gitkeep
    $GitKeepPath = Join-Path $FullPath ".gitkeep"

    if (-not (Test-Path $GitKeepPath)) {
        New-Item `
            -ItemType File `
            -Path $GitKeepPath `
            -Force | Out-Null
    }
}


# ============================================================
# CREATE IMPORTANT DOCUMENT FILES
# ============================================================

$Files = @(
    "README.md",

    "documents\plan\90_day_plan.md",
    "documents\plan\weekly_plan.md",
    "documents\plan\daily_plan.md",
    "documents\plan\career_plan.md"
)

foreach ($File in $Files) {

    $FullPath = Join-Path $Root $File

    if (-not (Test-Path $FullPath)) {

        New-Item `
            -ItemType File `
            -Path $FullPath `
            -Force | Out-Null
    }
}


# ============================================================
# CREATE .gitignore
# ============================================================

$GitIgnorePath = Join-Path $Root ".gitignore"

if (-not (Test-Path $GitIgnorePath)) {

    @"
# ============================================================
# Python
# ============================================================

__pycache__/
*.py[cod]
*.pyo

# Virtual environments
venv/
.venv/
env/

# Environment variables
.env
.env.*
!.env.example


# ============================================================
# IDE
# ============================================================

.vscode/
.idea/


# ============================================================
# Jupyter
# ============================================================

.ipynb_checkpoints/


# ============================================================
# Operating System
# ============================================================

.DS_Store
Thumbs.db


# ============================================================
# Logs
# ============================================================

*.log


# ============================================================
# Databases
# ============================================================

*.db
*.sqlite
*.sqlite3


# ============================================================
# Python Build
# ============================================================

build/
dist/
*.egg-info/


# ============================================================
# Secrets
# ============================================================

*.pem
*.key
credentials.json


# ============================================================
# Terraform
# ============================================================

.terraform/
*.tfstate
*.tfstate.*
*.tfvars


# ============================================================
# Node.js
# ============================================================

node_modules/


# ============================================================
# Temporary Files
# ============================================================

*.tmp
*.temp
"@ | Set-Content -Path $GitIgnorePath -Encoding UTF8
}


# ============================================================
# COMPLETED
# ============================================================

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host " TARGET-LEARN STRUCTURE CREATED SUCCESSFULLY" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""

Write-Host "Location: $Root" -ForegroundColor Cyan
Write-Host ""

Write-Host "GitHub support:" -ForegroundColor Yellow
Write-Host " .gitkeep files created in all folders" -ForegroundColor Green
Write-Host " .gitignore created" -ForegroundColor Green
Write-Host " README.md created" -ForegroundColor Green
Write-Host ""

# Display structure
tree $Root /F