"""
Google Search API integration for Q Business plugin
"""

import os
import logging
from typing import Dict, Any, Optional

import requests

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configuration constants
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
GOOGLE_SEARCH_ENGINE_ID = os.environ.get('GOOGLE_SEARCH_ENGINE_ID')
GOOGLE_SEARCH_API_URL = 'https://www.googleapis.com/customsearch/v1'

def perform_google_search(query: str, options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Performs a Google search using the Custom Search JSON API
    
    Args:
        query: The search query
        options: Additional search options
        
    Returns:
        Dict containing the search results
    
    Raises:
        ValueError: If API credentials are missing
        RuntimeError: If the Google API request fails
    """
    try:
        if not GOOGLE_API_KEY or not GOOGLE_SEARCH_ENGINE_ID:
            raise ValueError('Google API key or Search Engine ID not configured')

        if options is None:
            options = {}
            
        params = {
            'key': GOOGLE_API_KEY,
            'cx': GOOGLE_SEARCH_ENGINE_ID,
            'q': query,
            'num': options.get('results_count', 10),
            'start': options.get('start_index', 1)
        }

        # Add optional parameters if provided
        if 'safe_search' in options:
            params['safe'] = options['safe_search']
        if 'file_type' in options:
            params['fileType'] = options['file_type']
        if 'site_search' in options:
            params['siteSearch'] = options['site_search']

        logger.info(f"Performing Google search for query: {query}")
        
        response = requests.get(GOOGLE_SEARCH_API_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error performing Google search: {str(e)}")
        
        if hasattr(e, 'response') and e.response:
            logger.error(f"Google API response: {e.response.text}")
        
        raise RuntimeError(f"Google search failed: {str(e)}")
    
    except Exception as e:
        logger.error(f"Unexpected error in Google search: {str(e)}")
        raise