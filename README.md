# Q Business Google Search Plugin (Python)

This plugin integrates Google Search functionality into AWS Q Business, allowing users to search the internet directly from Q Business.

## Overview

This plugin leverages the Google Custom Search JSON API to perform web searches and return results to Q Business users. The plugin is built using the AWS Q Business plugin framework with Python and follows AWS best practices for security and performance.

## Prerequisites

- AWS Q Business access and permissions to create/deploy plugins
- Google Cloud Platform account
- Google Custom Search API key
- AWS account with appropriate permissions

## Setup Instructions

1. Configure Google API credentials
2. Deploy the plugin to AWS Q Business
3. Configure the plugin in Q Business

## Project Structure

```
q-business-google-search-plugin/
├── README.md
├── src/
│   ├── lambda_function.py  # Main plugin handler
│   ├── google_search.py    # Google API integration
│   └── utils.py            # Helper functions
├── config/
│   └── config.json         # Plugin configuration
├── requirements.txt        # Python dependencies
└── tests/
    └── test_plugin.py      # Unit tests
```