# Light Intensity Detection API

A web-based application that monitors ambient light levels in real-time using your device's camera, providing immediate feedback on lighting conditions through a Flask backend API and browser-based frontend.

## Features
- Real-time light level detection through web browser
- Flask-based API for light analysis
- Browser-based video capture and monitoring
- Simple user interface with status feedback
- Cross-Origin Resource Sharing (CORS) enabled

## Components
1. **Backend (Flask API)**
   - Processes image data
   - Analyzes light levels
   - Returns binary light status (sufficient/insufficient)

2. **Frontend (HTML/JavaScript)**
   - Captures video from user's camera
   - Sends frames to backend for analysis
   - Displays real-time lighting status

## Requirements
- Python 3.6 or higher
- Flask
- OpenCV (cv2)
- NumPy
- Flask-CORS
- Web browser with camera access
- Compatible webcam or camera device

## Installation
1. Clone this repository:
```bash
git clone https://github.com/SakibAhmedShuva/Light-Intensity-Detection-API.git
cd Light-Intensity-Detection-API
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the Flask backend:
```bash
python app.py
```

2. Open the frontend HTML file in a web browser

3. Allow camera access when prompted

4. Click "Start Recording" to begin light level monitoring

### How it Works
1. The frontend captures frames from your camera
2. Frames are sent to the Flask backend
3. Backend analyzes light levels using OpenCV
4. Results are displayed in real-time on the webpage

## Technical Implementation
The system uses two main components:

1. **Backend (app.py)**
   - `/check_light` endpoint processes POST requests
   - Converts base64 image data to OpenCV format
   - Analyzes HSV color space for brightness
   - Returns JSON response with light status

2. **Frontend (HTML/JavaScript)**
   - Manages camera access and video display
   - Captures and sends frames to backend
   - Updates UI based on API response

## Customization
Adjustable parameters:
- Light sensitivity threshold in backend: `avg_brightness < 100`
- Frame capture interval in frontend (currently 1 second)

## Screenshot

![image](https://github.com/user-attachments/assets/250ead00-3fc4-4fa4-a186-d21990218584)


## Example Notebook
This repository includes a Jupyter notebook demonstrating the core concepts and development process.

## Contributing

Contributions are welcome! Feel free to:
- Fork the repository
- Create feature branches
- Submit pull requests
- Open issues for bugs or feature enhancements

## License
This project is distributed under the MIT License - see the [LICENSE](LICENSE) file for details.
