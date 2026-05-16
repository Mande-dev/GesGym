param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$TestArgs
)

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    Write-Error "Python introuvable: $python"
    exit 1
}

& $python manage.py test --settings=smartclub.settings_test --noinput @TestArgs
exit $LASTEXITCODE
