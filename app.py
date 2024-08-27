from flask import Flask, jsonify

# Define the merge sort function
def merge_sort(arr):
    """Perform merge sort on a list of strings.
    
    Args:
        arr (list of str): The list of video titles to be sorted.
        
    Returns:
        list of str: The sorted list of video titles.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Create a Flask application
app = Flask(__name__)

# List of video titles
video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

@app.route('/sort', methods=['GET'])
def sort_videos():
    """Handle sort requests and return the sorted list of video titles.
    
    Returns:
        JSON: The sorted list of video titles.
    """
    sorted_titles = merge_sort(video_titles[:])  # Sort a copy of the list to avoid modifying the original
    return jsonify({"sorted_titles": sorted_titles})

if __name__ == "__main__":
    app.run(debug=True)
