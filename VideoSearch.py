from flask import Flask, request, jsonify

def binary_search(sorted_list, target):
    """Perform binary search on a sorted list to find the target item.
    
    Args:
        sorted_list (list of str): The sorted list of video titles.
        target (str): The title of the video to search for.
        
    Returns:
        str: The title of the video if found, else 'Not Found'.
    """
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return sorted_list[mid]
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return 'Not Found'

app = Flask(__name__)

# Sorted list of video titles
video_titles = [
    "Artificial Intelligence Revolution",
    "Cooking Masterclass: Italian Cuisine",
    "Digital Photography Essentials",
    "Exploring the Cosmos",
    "Financial Planning for Beginners",
    "Fitness Fundamentals: Strength Training",
    "History Uncovered: Ancient Civilizations",
    "Nature's Wonders: National Geographic",
    "The Art of Coding",
    "Travel Diaries: Discovering Europe"
]

@app.route('/search', methods=['GET'])
def search_video():
    """Handle search requests and return the result of the binary search.
    
    Query Parameters:
        title (str): The title of the video to search for.
        
    Returns:
        JSON: The search result, either the video title or 'Not Found'.
    """
    query = request.args.get('title', '')
    if not query:
        return jsonify({"error": "Query parameter 'title' is required."}), 400
    
    result = binary_search(video_titles, query)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
