def get_ratings(file):
    """Restaurant rating lister."""
    rating = open(file)
    restaurant_rating = {}

    for line in rating:
	    line = line.rstrip()
	    restaurants, score = line.split(":")
	    restaurant_rating[restaurants] = int(score)

    
    for key, value in sorted(restaurant_rating.items()):
        print(f"{key} is rated at {value}")

    return restaurant_rating

get_ratings("scores.txt")


# # put your code here
