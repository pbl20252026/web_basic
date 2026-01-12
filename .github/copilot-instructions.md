# AI Coding Agent Instructions for Hand Drag & Drop

## Project Overview
This is a real-time hand gesture recognition application using computer vision. It detects hand landmarks via webcam and interprets grab gestures (thumb + index finger proximity) to simulate drag-and-drop interactions.

## Architecture & Key Concepts

### Core Pipeline
1. **Capture**: Frame from webcam via OpenCV (`cv2.VideoCapture(0)`)
2. **Process**: Hand detection using MediaPipe (`mp_hands.Hands()`)
3. **Analyze**: Extract landmark positions (thumb=4, index=8) and compute Euclidean distance
4. **Interpret**: Classify gesture state based on distance threshold
5. **Display**: Draw landmarks, circles, distance, and status text to video frame

### State Machine
The gesture state is determined by `GRAB_THRESHOLD` (40 pixels by default):
- **No Hand**: No hands detected
- **MOVE**: Hand detected, distance > threshold, not previously grabbing
- **GRAB/DRAG**: Distance < threshold (fingers close together)
- **DROP**: Transition from GRAB state to open hand

**Critical Pattern**: `is_grabbing` flag tracks the previous frame state to distinguish MOVE from DROP.

## MediaPipe Hand Landmarks Reference
- Landmark 4: Thumb tip
- Landmark 8: Index finger tip
- Full hand has 21 landmarks; only these two are used for grab detection
- Coordinates are normalized (0-1 range); multiply by frame dimensions for pixel positions

## Common Modifications & Patterns

### Adjusting Sensitivity
```python
GRAB_THRESHOLD = 40  # Reduce (30-35) for stricter grab, increase (45-50) for looser
```

### Adding New Gesture Detection
Use the same pattern: extract relevant landmarks, compute distance/angle, check against threshold:
```python
# Example: Detect peace sign (index and middle separated)
middle = handLms.landmark[12]
# Then: dist = distance(index_pos, middle_pos)
```

### Expanding to Multiple Hands
`result.multi_hand_landmarks` is already a list; current loop processes all detected hands. To track individual hands across frames, use MediaPipe's hand classification (left/right) via `result.multi_handedness`.

## Debugging & Testing
- **Visibility issues**: Check `min_detection_confidence` (currently 0.7) — lower to 0.5 for poor lighting
- **Distance values not changing**: Verify webcam is working (`cv2.VideoCapture(0)` — may need index 1+ on multi-camera systems)
- **Gesture misdetection**: Print landmark coordinates to console; common issue is hand too close/far from camera

## Development Workflow
1. Run: `python hand_drag_drop.py`
2. Press ESC to exit
3. No build or test infrastructure; modifications are live-tested via webcam

## Code Style & Conventions
- Comments in Vietnamese; maintain this for consistency if modifying
- Status text uses all-caps for key states: "GRAB / DRAG", "DROP", "MOVE"
- OpenCV drawing uses BGR color format (blue, green, red)
- Math operations via `math.hypot()` for distance; use this pattern for consistency
