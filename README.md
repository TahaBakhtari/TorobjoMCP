# Torobjo MCP Server

A powerful MCP (Model Context Protocol) server implementation for product search and Instagram analysis.

## 🚀 Key Features

- **MCP Protocol Implementation**: Full support for Model Context Protocol
- **Dual Functionality**:
  - Torob product search API integration
  - Instagram caption extraction and analysis
- **Claude Integration**: Designed to work seamlessly with Claude Sonnet

## Technical Architecture

- **FastMCP Core**: High-performance MCP server implementation
- **Modular Tools**: Each functionality exposed as separate MCP tools
- **Standardized Interface**: Consistent JSON input/output format

## Tools Overview

### `search_torob`
- Searches products on Torob.com
- Returns price, title and URL
- Supports Persian language queries

### `get_instagram_caption`
- Extracts captions from Instagram posts
- Handles various post formats
- Error-resistant design
