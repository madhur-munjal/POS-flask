# import cv2
# from pyzbar import pyzbar.de
# from pyzbar.pyzbar import decode
# from pydub import AudioSegment
# from pydub.playback import play
#
# cap = cv2.VideoCapture(0)

# song = AudioSegment.from_wav("beep-02.wav")

# while cap.isOpened():
#     success,frame = cap.read()
#     frame = cv2.flip(frame,1)
#     detectedBarcode = decode(frame)
#     if not detectedBarcode:
#         print("No barcode detected")
#     else:
#         for barcode in detectedBarcode:
#             if barcode.data != "":
#                 cv2.putText(frame, str(barcode.data),(50,50),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,255),2)
#                 # play(song)
#                 cv2.imwrite("code.png",frame)
