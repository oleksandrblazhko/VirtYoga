# Глосарій термінів опису функціональних та нефункціональних вимог до програми

1) бібліотека Mediapipe - https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker?hl=en
2) скелетон тіла користувача - це 33 суглоби тіла людини
3) типи суглобів тіла людини <номер суглобу>-<назва суглобу>:
  0-nose, 1-left eye, 2-left eye, 3-left eye, 4-right eye, 5-right eye, 6-right eye, 7-left ear, 8-right ear, 9-mouth (left), 10-mouth (right), 11-left shoulder, 
  12-right shoulder, 13-left elbow, 14-right elbow, 15-left wrist, 16-right wrist, 17-left pinky, 18-right pinky, 19-left index, 20-right index, 21-left thumb, 
  22-right thumb, 23-left hip, 24-right hip, 25-left knee, 26-right knee, 27-left ankle, 28-right ankle, 29-left heel, 30-right heel, 31-left foot index, 
  32-right foot index;
4) анатомічні зв'язки між суглобами скелетону (номери):
  0-4,4-5,5-6,6-8,0-1,1-2,2-3,3-7,10-9,18-20,18-16,20-16,22-16,16-14,14-12,19-17,15-19,15-17,21-15,13-21,
  11-13,12-11,24-23,12-24,24-26,26-28,28-32,28-30,32-30,11-23,23-25,25-27,27-31,27-29,29-31;
5) розташування суглоба - координата (x,y,z)