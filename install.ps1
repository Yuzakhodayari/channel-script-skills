# Installs the four channel skills for Claude Code, Antigravity/Gemini and Codex (Windows PowerShell).
# Usage: .\install.ps1            (global)
#        .\install.ps1 -Project   (into .\.claude\skills, .\.agent\skills and .\.cursor\skills)
param([switch]$Project)
$ErrorActionPreference = 'Stop'
$Src = Join-Path $PSScriptRoot 'skills'
if ($Project) {
  # Project-local: preferred for channel work (portable, higher precedence)
  $Targets = @("$PWD\.claude\skills", "$PWD\.agent\skills", "$PWD\.agents\skills", "$PWD\.cursor\skills")
} else {
  # Global: Antigravity discovers ~/.gemini/config/skills\  (NOT ~/.gemini\antigravity\skills)
  $Targets = @("$HOME\.claude\skills", "$HOME\.gemini\config\skills", "$HOME\.codex\skills")
}
foreach ($t in $Targets) {
  New-Item -ItemType Directory -Force -Path $t | Out-Null
  Get-ChildItem -Directory $Src | ForEach-Object {
    $dest = Join-Path $t $_.Name
    if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
    Copy-Item -Recurse $_.FullName $dest
    Write-Host "installed $($_.Name) -> $dest"
  }
}
