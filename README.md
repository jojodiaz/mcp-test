# MCP Server for local development context

## Description
This project is designed to facilitate the usage of MCP-compliant clients such as Claude Code, Claude Desktop, Google Gemini, etc.  
By having this local MCP server running and configured with an MCP client, you essentially allow the client access the the *tools* and *resources* that server.py exposes.  
This allows, for example, your MCP client to be able to run certain git commands on your computer, and receive the output so that it can gain context.  
There are ambitious plans to expand this project to analyze code significantly, including plans to expose the python dis module so that the client can view bytecode generated from different code segments and replace it to increase different metrics.

## Prerequisites

- Python 3.10 or higher.
- `uv` (recommended for dependency management) or `pip`.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp_test
   ```

2. Install dependencies:
   ```bash
   # Using Python 3.10 or higher with pyenv
   pyenv install 3.10.0 
   pyenv local 3.10.0
   
   # Using uv
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt

   # OR using pip
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

Allow MCP client to run the server using Python:
TODO: UPDATE WITH CLAUDE CODE & GOOGLE ANTIGRAVITY SPECIFIC INSTRUCTIONS
```

The server listens on `stdio` by default. It assumes an MCP-compliant client will start it and communicate via standard input/output.
```

## Commit Pattern

According to Google, there are *11* types of commits (listed below).  

Please mark the beginning of your commit with an identifier string indicating what type of commit it is.    
This helps keep track of the development cadence and is also useful for extracting relevant information  
from commit history. I also realize I am talking to myself here lol.  

Example: ```git commit -m "docs: Adding documentation because I am a responsible engineer"```

**feat**: Introduces a new feature.  
**fix**: Patches a bug in the code.  
**docs**: Changes to documentation only (README, comments).  
**style**: Formatting, whitespace, missing semicolons; no code change in meaning.  
**refactor**: Restructures code without changing functionality (neither a feature nor a fix).  
**perf**: Improves performance.  
**test**: Adds or corrects tests.  
**build**: Changes affecting the build system or external dependencies (npm, webpack).  
**ci**: Changes to CI configuration files and scripts (GitHub Actions, Jenkins).  
**chore**: Maintenance tasks, updating dependencies, build process changes that don't touch src or test files.  
**revert**: Reverts a previous commit.  

