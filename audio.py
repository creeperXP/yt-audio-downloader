# will improve later by adding folders

import yt_dlp

# select only audio for download
ydl_aspects = {
    'format': 'bestaudio/best',  # get the best audio quality possible
}

# download function with given url
def download(video_url):
    with yt_dlp.YoutubeDL(ydl_aspects) as ydl: # resource cleaned up/ydl object creation from YoutubeDL class
        ydl.download([video_url])  # Download the audio

# continue downloading user's audio until they say 0 
tracker = 1
while tracker == 1:
    link = input("Enter YouTube URL to download: ")
    url = link.strip()
    
    # Check if the link is a playlist and download if necessary
    if 'playlist' in url:  
        with yt_dlp.YoutubeDL(ydl_aspects) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            playlist_title = info_dict.get('title', 'Playlist')
            
    # Download the audio 
    download(url)  
    channel = int(input("Enter '1' to download more videos\nEnter 0 if not: "))
