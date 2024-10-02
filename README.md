# Low-Light-Detection-Model

An intelligent Python model that monitors ambient light levels during video capture, ensuring optimal recording conditions and providing real-time feedback for low-light situations.

## Features

- Real-time low light detection and monitoring
- Automated video recording with light-level awareness
- Console-based feedback system for lighting conditions
- Configurable light sensitivity and recording parameters
- Video output in AVI format with maintained quality

## Requirements

- Python 3.6 or higher
- OpenCV (cv2)
- Compatible webcam or camera device

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Low-Light-Detection-Model.git
cd Low-Light-Detection-Model
```

2. Install required dependencies:
```bash
pip install opencv-python
```

## Usage

Execute the model using Python:

```bash
python light_detection_model.py
```

The model will:
1. Initialize your camera device
2. Begin continuous light level monitoring
3. Automatically start recording when lighting is adequate
4. Terminate after 60 seconds or upon pressing 'q'

### Customization

Adjustable parameters within the model:
- Light sensitivity threshold: `avg_brightness < 100`
- Recording duration: `time.time() - start_time > 60`
- Output video resolution: `(640, 480)`
- Frame rate: `20.0` FPS

## Technical Implementation

The model utilizes two primary functions:

1. `check_light(frame)`:
   - Converts captured frames to HSV color space
   - Analyzes brightness levels
   - Returns a boolean indicator for lighting adequacy

2. `capture_video(cap, save_path)`:
   - Manages continuous frame capture
   - Implements real-time light monitoring
   - Controls video recording based on lighting conditions
   - Provides user feedback through console output

## Output

The model generates an 'output.avi' file containing only the footage captured under sufficient lighting conditions.

## Limitations

- Camera compatibility dependent on OpenCV support
- May require calibration for different camera sensors
- Currently limited to AVI format for video output

## Contributing

Contributions are welcome! Feel free to:
- Fork the repository
- Create feature branches
- Submit pull requests
- Open issues for bugs or feature enhancements

## License

This project is distributed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV community for comprehensive documentation
- Python community for valuable resources and support

