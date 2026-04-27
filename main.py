import json


# First step is Load data from JSON file

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)



# Second step is Clean the dataset

def clean_data(data):
    # Here we have Remove users with empty names
    data["users"] = [u for u in data["users"] if u["name"].strip()]

    # Also here Remove duplicate friends for each user
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # Here we have Remove inactive users (no friends and no liked pages)
    data["users"] = [u for u in data["users"] if u["friends"] or u["liked_pages"]]

    # Remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page

    data["pages"] = list(unique_pages.values())

    return data



# Here we Get user name from ID

def get_user_name(user_id, data):
    for user in data["users"]:
        if user["id"] == user_id:
            return user["name"]
    return "Unknown"



# Here we Get page name from ID

def get_page_name(page_id, data):
    for page in data["pages"]:
        if page["id"] == page_id:
            return page["name"]
    return "Unknown"



# Here we Find "People You May Know"

def find_people_you_may_know(user_id, data):
    
    user_friends = {u["id"]: set(u["friends"]) for u in data["users"]}

    if user_id not in user_friends:
        return {}

    direct = user_friends[user_id]
    suggestions = {}

    # Check friends of friends
    for friend in direct:
        for mutual in user_friends.get(friend, []):
           
            if mutual != user_id and mutual not in direct:
                if mutual not in suggestions:
                    suggestions[mutual] = {
                        "count": 0,
                        "mutual_friends": []
                    }

                
                suggestions[mutual]["count"] += 1
                suggestions[mutual]["mutual_friends"].append(friend)

    return suggestions



# Find Pages You Might Like

def find_pages_you_might_like(user_id, data):
    user_pages = {u["id"]: set(u["liked_pages"]) for u in data["users"]}

    if user_id not in user_pages:
        return []

    liked = user_pages[user_id]
    suggestions = {}

    # Compare with other users
    for other, pages in user_pages.items():
        if other != user_id:
            common = liked.intersection(pages)

            for page in pages:
                if page not in liked:
                    suggestions[page] = suggestions.get(page, 0) + len(common)

    return sorted(suggestions, key=suggestions.get, reverse=True)



# MAIN PROGRAM

data = load_data("codebook_data.json")

# Clean the data
cleaned = clean_data(data)

# Save cleaned data into a new file
with open("cleaned_codebook_data.json", "w") as f:
    json.dump(cleaned, f, indent=4)

print("Cleaned Data Saved!")

# Take user input
user_id = int(input("Enter user id: "))


psuggestions = find_people_you_may_know(user_id, cleaned)

print(f"\nPeople You May Know for {get_user_name(user_id, cleaned)}:")

if not psuggestions:
    print("No suggestions found.")
else:
    for uid, info in psuggestions.items():
        mutual_names = [get_user_name(fid, cleaned) for fid in info["mutual_friends"]]

        print(f"- {get_user_name(uid, cleaned)} "
              f"(Mutual Friends: {mutual_names}, Count: {info['count']})")


page_ids = find_pages_you_might_like(user_id, cleaned)

page_names = [get_page_name(pid, cleaned) for pid in page_ids]

print("\nPages You Might Like:", page_names)
