#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

arecord -D hw:1,0 -f cd -c1 -r 16000 --duration=5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav

