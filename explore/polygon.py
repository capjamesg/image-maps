import json

with open('data.json') as f:
    data = json.load(f)

boxes = data['boxes']

link_registry = {
    "cmos": "https://jamesg.blog/category/fun-with-words/",
    "camera": "https://jamesg.blog/category/computer-vision/",
    "web": "https://jamesg.blog/indieweb/",
    "joy": "https://jamesg.blog/category/moments-of-joy",
    "mybook": "https://jamesg.blog/category/technical-writing/",
    "laptop": "https://jamesg.blog/category/coding/",
    "coffee": "https://jamesg.blog/coffee/",
}

image_map = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<script>
    function playMusic () {
        var music = document.getElementById('music');
        if (music.paused) {
            music.play();
        } else {
            music.pause();
        }
    }
</script>
<audio id="music" src="https://jamesg.blog/summer.mp3" preload="auto" style="display: none;"></audio>
<img src="books.jpeg" usemap="#image_map" height="960" width="1280" /><map name="image_map">"""
for box in boxes:
    if box['type'] == 'polygon':
        points = ''
        for point in box['points']:
            points += f'{point[0]},{point[1]} '
        points = points.strip()
        points = points[:-1]
        if box["label"] != "music":
            image_map += f'<area shape="poly" coords="{points}" href="#" alt="{box["label"]}" onclick="window.open(\'{link_registry[box["label"]]}\', \'_blank\');" />\n'
        else:
            image_map += f'<area shape="poly" coords="{points}" href="#" alt="{box["label"]}" onclick="playMusic()" />\n'
image_map += '</map></body></html>'

with open('image_map.html', 'w') as f:
    f.write(image_map)