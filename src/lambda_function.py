"""
Q Business Google Search Plugin - Main Lambda Handler

This module serves as the entry point for the AWS Q Business plugin,
handling requests and returning search results.
"""

import json
import logging
from typing import Dict, Any

from google_search import perform_google_search
from utils import format_search_results

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Main handler for the Q Business plugin
    
    Args:
        event: The event from Q Business
        context: The Lambda context object
        
    Returns:
        Dict containing the response to send back to Q Business
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        # Extract search query from the event
        query = None
        if 'query' in event:
            query = event['query']
        elif 'parameters' in event and 'query' in event['parameters']:
            query = event['parameters']['query']
        
        if not query:
            logger.error("No search query provided in the request")
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Search query is required'
                })
            }
        
        # Perform Google search
        search_results = perform_google_search(query)
        
        # Format results for Q Business
        formatted_results = format_search_results(search_results)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'results': formatted_results
            })
        }
    
    except Exception as e:
        logger.error(f"Error in plugin execution: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred while processing the search request',
                'error': str(e)
            })
        }