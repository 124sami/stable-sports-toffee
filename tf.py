import requests

SOURCE_URL = "https://raw.githubusercontent.com/abusaeeidx/Toffee-playlist/refs/heads/main/ott_navigator.m3u"
OUTPUT_FILE = "toffee.m3u"

CUSTOM_CHANNELS = [
    {
        "extinf": '#EXTINF:-1 group-title="Sports Channels" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/ljE2lZ0BNnOkwJLW9lrg/posters/b4bee75a-b8a3-4594-b562-6e3910d71625.png",Bangladesh VS Pakistan',
        "url": "https://your-stream-link.m3u8"
    }
]


def update_playlist():
    r = requests.get(SOURCE_URL)
    r.raise_for_status()

    lines = r.text.splitlines()

    channels = []
    current = None

    for line in lines:
        if line.startswith("#EXTINF"):
            if current:
                channels.append(current)
            current = [line]
        elif current is not None:
            current.append(line)

    if current:
        channels.append(current)

    # আসল প্রথম channel remove
    if len(channels) > 0:
        channels.pop(0)

    output = ["#EXTM3U"]

    for ch in channels:
        output.extend(ch)

    # নিজের channel শেষে add
    for c in CUSTOM_CHANNELS:
        output.append(c["extinf"])
        output.append(c["url"])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    update_playlist()
