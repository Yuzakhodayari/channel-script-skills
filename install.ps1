# Installs the four channel skills for Claude Code, Antigravity/Gemini and Codex (Windows PowerShell).
# Usage: .\install.ps1            (global)
#        .\install.ps1 -Project   (into .\.claude\skills, .\.agent\skills and .\.cursor\skills)
param([switch]$Project)
$ErrorActionPreference = 'Stop'
$Src = Join-Path $PSScriptRoot 'skills'
if ($Project) { $Targets = @("$PWD\.claude\skills", "$PWD\.agent\skills", "$PWD\.cursor\skills") }
else { $Targets = @("$HOME\.claude\skills", "$HOME\.gemini\antigravity\skills", "$HOME\.codex\skills") }
foreach ($t in $Targets) {
  New-Item -ItemType Directory -Force -Path $t | Out-Null
  Get-ChildItem -Directory $Src | ForEach-Object {
    $dest = Join-Path $t $_.Name
    if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
    Copy-Item -Recurse $_.FullName $dest
    Write-Host "installed $($_.Name) -> $dest"
  }
}
