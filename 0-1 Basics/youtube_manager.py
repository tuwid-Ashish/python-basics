import json
file_name = "youtube.text"

def load_data():
    try:
        with open(file_name, "r") as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(video):
    with open(file_name,"w") as file:
        json.dump(video,file)

def list_videos(videos):
   for index,video in  enumerate(videos,start=1):
       print(f"{index}. {video["video"]} and has duration {video["time"]}")

def add_videos(videos):
    video = input("Enter video name : ")
    time = input("Enter video duration : ")
    videos.append({"name": video, "time": time})
    save_data(videos)

def update_videos(videos):
    list_videos(videos)
    index = int(input("Enter the index of video: "))
    if 1<= index <= len(videos):
        video = input("Enter video name : ")
        time = input("Enter video duration : ")
        videos[index-1] = {"name": video, "time": time}
        save_data(videos)

def delete_videos(videos):
    list_videos(videos)
    index = int(input("Enter the index of video: "))
    if 1<= index <= len(videos):
        del videos[index-1]

        save_data(videos) 


def main():
    videos = load_data()
    while True:
        print("\n Yputube Manager | choose a option")
        print("1. List all youtube videos")
        print("2. Add a  youtube videos")
        print("3. update a  youtube videos")
        print("4. delete a  youtube videos")
        print("5. Exist the app")
        choice = input("Enter your choice")
        match choice:
            case "1" :   list_videos(videos)
            case "2" :    add_videos(videos)
            case "3" : update_videos(videos)
            case "4" : delete_videos(videos)
            case "5": break
            case _: print("Invalid entry")

if __name__ == "__main__":
    main()