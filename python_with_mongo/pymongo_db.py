from pymongo import MongoClient
from bson import ObjectId
client =  MongoClient("mongodb+srv://freeapi:Y1MbQRGBlO7Qq6Jb@clusterfa.zji7qge.mongodb.net",port=4000)
# not a good approch
db = client["ytmanager"]
video_collection = db["videos"]


def list_videos():
    for video in video_collection.find():
        print(f"ID:{video["_id"]} has data , {video['name']} and the duration = {video["time"]}")
    

def add_videos(name,time):
    video_collection.insert_one({
           "name": name ,
           "time": time
    })
    
def  update_videos(video,video_id,time):
    video_collection.find_one_and_update({'_id': ObjectId(video_id)},{ "$set" :{"name": video , "time":time}},)
    #   video_collection.update_one({'_id': video_id},{ "$set" :{"name": video , "time":time}})  
def delete_videos(video_id):
     video_collection.delete_one({"_id":ObjectId(video_id)}) 

def main():
    while True:
        print("\n Yputube Manager with DB | choose a option")
        print("1. List all youtube videos")
        print("2. Add a  youtube videos")
        print("3. update a  youtube videos")
        print("4. delete a  youtube videos")
        print("5. Exist the app")
        choice = input("Enter your choice")

        match choice:
            case "1" :   list_videos()

            case "2" :
                  video = input("Enter video name : ")
                  time  = input("Enter video duration : ")
                  add_videos(video,time)

            case "3" :
                video_id = input("Enter the video ID : ")
                video = input("Enter video name : ")
                time = input("Enter video duration : ")
                update_videos(video,video_id,time)

            case "4" :
                video_id = input("Enter the video ID : ")
                delete_videos(video_id)

            case "5": break

            case _: print("Invalid entry")

if __name__ == "__main__":
    main()