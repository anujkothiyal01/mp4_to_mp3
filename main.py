import os.path

import streamlit as st
from moviepy.editor import *

def convert_mp3_to_mp4(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path, codec='libmp3lame')
    video.close()

st.title('Video To Audio Converter')
uploaded_file = st.file_uploader('Upload MP4 Video', type=['mp4'])

if uploaded_file is not None:
    st.video(uploaded_file)

    video_path = os.path.join('temp', uploaded_file.name)
    if not os.path.exists('temp'):
        os.makedirs('temp')
    with open(video_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    audio_path = video_path.replace('.mp4', '.mp3')

    if st.button('Convert to MP3'):
        convert_mp3_to_mp4(video_path, audio_path)
        st.success('Conversion Successful')

        with open(audio_path, 'rb') as f:
            st.download_button('Download MP3', f, file_name=os.path.basename(audio_path))

        os.remove(video_path)
        os.remove(audio_path)