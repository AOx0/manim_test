rf:
    just render manim.cfg 2160p60

rl:
    just render manim_low.cfg 720p30

rvl:
    just render manim_very_low.cfg 360p15

render config quality:
    sshpass -p "1234" ssh parallels@192.168.0.15 \
        "\
            cd ~/Desktop/Parallels\ Shared\ Folders/Home/manim_test \
            && /home/parallels/.local/bin/manim \
                --format mp4 \
                -c cfg/{{config}} \
                main.py\
        "
    qil QuickTime
    sleep 1
    just openr {{quality}}

openr quality:
    open /Users/alejandro/manim_test/media/videos/main/{{quality}}/DefaultTemplate.mp4 -a "QuickTime PLayer"
