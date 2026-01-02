# Test MCP Server

Test MCP Server

## Description


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
