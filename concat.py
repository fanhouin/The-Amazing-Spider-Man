import os
for i in range(1, 26):
    os.system(f"(for %i in (video/{i}/*.ts) do @echo file '%i') > video/{i}/mylist.txt")
    os.system(f"ffmpeg.exe -f concat -i video/{i}/mylist.txt -c copy video/{i}.ts")
    os.system(f"ffmpeg.exe -i video/{i}.ts -c copy video/{i}.mp4")
    os.remove(f"video/{i}.ts")
