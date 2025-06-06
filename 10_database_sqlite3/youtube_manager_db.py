import sqlite3

# Establish a connection to the database
# This will create 'youtube_videos.db' if it doesn't exist
con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

# Create the 'videos' table if it doesn't already exist.
# IMPORTANT: We've renamed 'video' to 'video_time' to avoid confusion and use a more descriptive name.
cursor.execute('''CREATE TABLE IF NOT EXISTS videos (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    video_time TEXT NOT NULL -- Changed 'video' to 'video_time' for clarity
                )''')

def list_videos():
    """Fetches and prints all videos from the database."""
    cursor.execute("SELECT * FROM videos")
    print("\n--- Your Videos ---")
    # Fetch all results and iterate through them
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")
    print("-------------------\n")

def add_video(name, time):
    """Adds a new video record to the database."""
    # Ensure you're inserting into the correct column name ('video_time')
    cursor.execute('INSERT INTO videos (name, video_time) VALUES (?, ?)',
                   (name, time))
    con.commit() # Commit the transaction to save changes to the database
    print("Video added successfully!")

def update_video(video_id, new_name, new_time):
    """Updates an existing video record in the database."""
    # Corrected 'vidoes' to 'videos' and 'time' to 'video_time'
    cursor.execute('UPDATE videos SET name = ?, video_time = ? WHERE id = ?',
                   (new_name, new_time, video_id))
    con.commit() # Commit the transaction
    print("Video updated successfully!")

def delete_video(video_id):
    """Deletes a video record from the database."""
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit() # Commit the transaction
    print("Video deleted successfully!")

def main():
    """Main function to run the YouTube Manager application."""
    while True:
        print("\n--- YouTube Manager App with DB ---")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('Enter the video name: ')
            time = input('Enter the video time (e.g., "10:30"): ')
            add_video(name, time)
        elif choice == '3':
            video_id = input('Enter video ID to update: ')
            # Input validation: Ensure video_id is a number
            if not video_id.isdigit():
                print("Invalid ID. Please enter a number.")
                continue
            name = input('Enter the new video name: ')
            time = input('Enter the new video time: ')
            update_video(int(video_id), name, time) # Convert video_id to int
        elif choice == '4':
            video_id = input('Enter video ID to delete: ')
            # Input validation: Ensure video_id is a number
            if not video_id.isdigit():
                print("Invalid ID. Please enter a number.")
                continue
            delete_video(int(video_id)) # Convert video_id to int
        elif choice == '5':
            print("Exiting YouTube Manager. Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a number from 1 to 5.")
    
    # Close the database connection when the app exits
    con.close() 

if __name__ == "__main__":
    main()