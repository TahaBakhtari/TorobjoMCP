# Watch the tutorial video on how to create an MCP server from [here](https://youtu.be/FedhNynmm8g?si=M4QbluZEKyuVJM1p).

# ویدیو آموزش ساخت سرور MCP را از [اینجا](https://youtu.be/FedhNynmm8g?si=M4QbluZEKyuVJM1p) ببینید.

# Torobjo MCP Server

A production-grade MCP (Model Context Protocol) server implementation that combines Torob product search with Instagram content analysis capabilities. Built on FastMCP for high-performance model communication and data processing.

## Key Technical Features

- **Full MCP Protocol Support**: Implements all core Model Context Protocol specifications
- **Dual-Mode Operation**:
  - Direct Torob.com API integration for Persian product search
  - Instagram content processing pipeline
- **Claude-Optimized**: Designed specifically for Claude Sonnet integration
- **Enterprise-Grade Reliability**:
  - Automatic retry mechanisms
  - Comprehensive error handling
  - Rate limiting protection

## Architecture Highlights

- **FastMCP Core**: Leverages the high-performance FastMCP implementation
- **Modular Tool Design**: Each service exposed as independent MCP endpoints
- **Unified Interface**: Consistent JSON API for all operations
- **Scalable**: Built to handle high-volume requests

## Core Endpoints

### Product Search (`search_torob`)
- Full Torob.com API coverage
- Persian language optimized
- Pagination support
- Price filtering

### Instagram Processing (`get_instagram_caption`)
- Robust caption extraction
- Multiple fallback selectors
- Headless browser automation
- Error recovery


![1](https://github.com/user-attachments/assets/49155d39-311c-4b57-8eda-df2390dc631b)
