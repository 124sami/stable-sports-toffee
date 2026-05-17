import requests

SOURCE_URL = "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u"
OUTPUT_FILE = "toffee.m3u"

CUSTOM_CHANNEL = """#EXTINF:-1 tvg-id="mychannel" group-title="Custom",My Channel
https://your-stream-link.m3u8
"""

def update_playlist():
    r = requests.get(SOURCE_URL)
    lines = r.text.splitlines()

    channels = []
    current = []

    for line in lines:
        if line.startswith("#EXTINF"):
            if current:
                channels.append(current)
            current = [line]
        else:
            current.append(line)

    if current:
        channels.append(current)

    channels = channels[1:]

    output = ["#EXTM3U"]

    for ch in channels:
        output.extend(ch)

    output.extend(CUSTOM_CHANNEL.splitlines())

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output))

update_playlist()
