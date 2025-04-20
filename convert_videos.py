import os
import subprocess
from pathlib import Path

def convert_video_to_hls(input_video, output_dir):
    """
    Convert a video file to HLS format with continuous streaming support.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Output m3u8 and segment path
    output_m3u8 = os.path.join(output_dir, f"{Path(input_video).stem}.m3u8")
    segment_pattern = os.path.join(output_dir, f"{Path(input_video).stem}_%03d.ts")
    
    # FFmpeg command for HLS conversion
    cmd = [
        'ffmpeg',
        '-i', input_video,
        '-c:v', 'libx264',  # Video codec
        '-preset', 'veryfast',  # Encoding speed preset
        '-crf', '23',  # Constant Rate Factor (quality)
        '-c:a', 'aac',  # Audio codec
        '-ar', '48000',  # Audio sample rate
        '-b:a', '128k',  # Audio bitrate
        '-f', 'hls',  # HLS format
        '-hls_time', '2',  # Segment duration
        '-hls_list_size', '0',  # Include all segments (VOD style)
        '-hls_flags', 'independent_segments',  # Make segments independent
        '-hls_segment_type', 'mpegts',  # Segment type
        '-hls_segment_filename', segment_pattern,  # Segment naming pattern
        output_m3u8  # Output m3u8 file
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully converted {input_video} to HLS format")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_video}: {e}")
        return False

def process_videos():
    """
    Process all videos in the configuration
    """
    from configuration import STREAMS
    
    for stream in STREAMS:
        # Extract video ID
        video_id = stream['id']
        
        # Define input video path (assuming MP4 format)
        input_video = f"source_videos/{video_id}.mp4"
        
        # Define output directory
        output_dir = f"public/{video_id}"
        
        if os.path.exists(input_video):
            print(f"Processing {video_id}...")
            convert_video_to_hls(input_video, output_dir)
        else:
            print(f"Source video not found: {input_video}")

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs("source_videos", exist_ok=True)
    os.makedirs("public", exist_ok=True)
    
    process_videos() 