"""
Utility functions for the Q Business Google Search plugin
"""

from typing import Dict, Any, List

def format_search_results(search_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Formats Google search results for Q Business
    
    Args:
        search_data: Raw search results from Google API
        
    Returns:
        List of formatted search results
    """
    formatted_results = []
    
    if 'items' not in search_data:
        return formatted_results
    
    for item in search_data['items']:
        result = {
            'title': item.get('title', ''),
            'link': item.get('link', ''),
            'snippet': item.get('snippet', ''),
            'source': 'Google Search'
        }
        
        # Add thumbnail if available
        if 'pagemap' in item and 'cse_thumbnail' in item['pagemap']:
            thumbnails = item['pagemap']['cse_thumbnail']
            if thumbnails and len(thumbnails) > 0:
                result['thumbnail'] = thumbnails[0].get('src', '')
        
        formatted_results.append(result)
    
    return formatted_results

def extract_query_from_event(event: Dict[str, Any]) -> str:
    """
    Extracts the search query from the Q Business event
    
    Args:
        event: The event from Q Business
        
    Returns:
        The extracted search query or empty string if not found
    """
    if 'query' in event:
        return event['query']
    
    if 'parameters' in event and 'query' in event['parameters']:
        return event['parameters']['query']
    
    return ''