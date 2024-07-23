import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
        id  INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in  cursor.fetchall():
              print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (? ,? )", (name,time))
    conn.commit()
    
def  update_videos(video,video_id,time):
    cursor.execute("UPDATE videos SET name = ? , time = ? , WHERE id = ?",(video,video_id,time))
    conn.commit()

def delete_videos(video_id):
     cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
     conn.commit()

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
                  time = input("Enter video duration : ")
                  add_videos(video,time)

            case "3" :
                video_id = int(input("Enter the video ID : "))
                video = input("Enter video name : ")
                time = input("Enter video duration : ")
                update_videos(video,video_id,time)

            case "4" :
                video_id = int(input("Enter the video ID : "))
                delete_videos(video_id)

            case "5": break

            case _: print("Invalid entry")

    conn.close()
if __name__ == "__main__":
    main()