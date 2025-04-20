# Continuous HLS Stream Demo

This project demonstrates continuous HLS video streaming using FFmpeg for conversion and HLS.js for playback.

## Prerequisites

- FFmpeg installed on your system
- Python 3.x
- Source videos in MP4 format

## Project Structure

```
.
├── source_videos/       # Place your source MP4 files here
│   ├── demo_crash1.mp4
│   ├── demo_crash2.mp4
│   ├── demo_crash3.mp4
│   └── demo_crash4.mp4
├── public/             # Generated HLS streams and web player
│   ├── index.html
│   ├── demo_crash1/
│   ├── demo_crash2/
│   ├── demo_crash3/
│   └── demo_crash4/
├── configuration.py    # Stream configuration
├── convert_videos.py   # Video conversion script
└── README.md
```

## Setup Instructions

1. Install FFmpeg if not already installed:
   ```bash
   # macOS (using Homebrew)
   brew install ffmpeg

   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install ffmpeg
   ```

2. Place your source MP4 videos in the `source_videos` directory with the following names:
   - demo_crash1.mp4
   - demo_crash2.mp4
   - demo_crash3.mp4
   - demo_crash4.mp4

3. Run the conversion script:
   ```bash
   python convert_videos.py
   ```

4. Deploy the `public` directory to Vercel:
   ```bash
   vercel deploy
   ```

## Features

- Automatic video conversion to HLS format
- Continuous looping playback
- Error recovery and handling
- Support for multiple simultaneous streams
- Mobile-friendly responsive design
- Safari compatibility

## Configuration

The stream configuration is managed in `configuration.py`. Each stream entry contains:
- `id`: Unique identifier for the stream
- `url`: URL path to the HLS manifest
- `location`: Display name for the stream
- `analysis_fps`: Frame rate for analysis (if applicable)

## Deployment

The project is designed to be deployed on Vercel. The `public` directory contains all the necessary files for deployment.

## Troubleshooting

1. If videos don't play:
   - Check that FFmpeg conversion completed successfully
   - Verify that .m3u8 and .ts files are present in the public directory
   - Check browser console for errors

2. If looping doesn't work:
   - Ensure videos are properly encoded with FFmpeg
   - Check that HLS.js is properly initialized
   - Verify that the ended event listener is working

3. If streams don't load:
   - Verify that the URLs in configuration.py match your deployment
   - Check network tab for 404 errors
   - Ensure proper CORS headers are set on your deployment

## License

MIT