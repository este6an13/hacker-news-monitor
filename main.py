import requests
import time

THRESHOLD = 50
KEYWORDS = ['python', 'techcrunch']

def fetch_stories():
    urls = [ "https://hacker-news.firebaseio.com/v0/beststories.json",
             "https://hacker-news.firebaseio.com/v0/topstories.json",
             "https://hacker-news.firebaseio.com/v0/newstories.json" ]
    result = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            result += response.json()
        else:
            print("Failed to fetch new stories. Status code:", response.status_code)
    return list(set(result))

def check_keywords_in_text(keywords, text):
    for keyword in keywords:
        if keyword.lower() in text.lower():
            return True
    return False

def fetch_story_details(story_id, threshold, keywords):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        story_data = response.json()
        if story_data.get("type") == "story" and "url" in story_data:
            text = story_data.get("title") + ' ' + story_data.get("url")
            if story_data.get("score") > threshold or check_keywords_in_text(keywords, text):
                return story_data
    return None

def print_story_details(story_data):
    if story_data:
        title = story_data.get("title")
        url = story_data.get("url")
        score = story_data.get("score")
        print(f"Title: {title}\nURL: {url}\nScore: {score}\n")

def write_ids_to_file(ids, filename):
    with open(filename, "w") as f:
        for item_id in ids:
            f.write(str(item_id) + "\n")

def read_ids_from_file(filename):
    try:
        with open(filename, "r") as f:
            return set(int(line.strip()) for line in f)
    except FileNotFoundError:
        return set()

if __name__ == "__main__":
    existing_ids_filename = "ids.txt"

    existing_ids = read_ids_from_file(existing_ids_filename)
    new_ids = set()

    while True:
        try:

            new_stories = fetch_stories()

            new_ids = set(new_stories) - set(existing_ids)

            fetched_ids = []
            # Fetch details for new IDs and print story details
            for story_id in new_ids:
                story_data = fetch_story_details(story_id, THRESHOLD, KEYWORDS)
                if story_data:
                    # equivalent to sending notification
                    print_story_details(story_data)
                    fetched_ids.append(story_id)

            existing_ids = existing_ids.union(set(fetched_ids))

            # Old items that didn't come in new_stories are removed here
            existing_ids.intersection_update(new_stories)

            # Write the updated existing_ids to the file
            write_ids_to_file(existing_ids, existing_ids_filename)

        except Exception as e:
            print("Error occurred:", e)

        # print('Waiting...\n')

        # Wait for 1 minute before the next check
        time.sleep(60)
        