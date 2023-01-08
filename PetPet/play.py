from nonebot_plugin_imageutils import BuildImage
from typing import List
from PIL.Image import Image as IMG
from io import BytesIO
import random,os

def save_gif(frames: List[IMG], duration: float) -> BytesIO:
    output = BytesIO()
    frames[0].save(
        output,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=duration * 1000,
        loop=0,
        disposal=2,
        optimize=False,
    )
    nbytes = output.getbuffer().nbytes
    return output

def load_image(path: str) -> BuildImage:
    return BuildImage.open(f"{os.path.dirname(__file__)}\\resources\\images\\{path}").convert("RGBA")

def petpet(path:str):
    img = BuildImage.open(path).convert("RGBA").square()
    frames: List[IMG] = []
    locs = [
        (14, 20, 98, 98),
        (12, 33, 101, 85),
        (8, 40, 110, 76),
        (10, 33, 102, 84),
        (12, 20, 98, 98),
    ]
    for i in range(5):
        hand = load_image(f"petpet\\{i}.png")
        frame = BuildImage.new("RGBA", hand.size, (255, 255, 255, 0))
        x, y, w, h = locs[i]
        frame.paste(img.resize((w, h)), (x, y), alpha=True)
        frame.paste(hand, alpha=True)
        frames.append(frame.image)
    return save_gif(frames, 0.06)

def blood_pressure(path:str):
    img = BuildImage.open(path)
    frame = load_image("blood_pressure\\0.png")
    def make(img: BuildImage) -> BuildImage:
        return frame.copy().paste(
            img.resize((414, 450), keep_ratio=True), (16, 17), below=True
        )
    return make(img).save_jpg()

def addition(path:str):
    img = BuildImage.open(path)
    frame = load_image("addiction\\0.png")
    def make(img: BuildImage) -> BuildImage:
        return frame.copy().paste(img.resize((70, 70), keep_ratio=True), (0, 0))
    return make(img).save_jpg()

def anti_kidnap(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").circle().resize((450, 450))
    bg = load_image("anti_kidnap\\0.png")
    frame = BuildImage.new("RGBA", bg.size, "white")
    frame.paste(img, (30, 78))
    frame.paste(bg, alpha=True)
    return frame.save_jpg()

def china_flag(path:str):
    frame = load_image("china_flag\\0.png")
    img = BuildImage.open(path)
    frame.paste(img.convert("RGBA").resize(frame.size, keep_ratio=True), below=True)
    return frame.save_jpg()

def cover_face(path:str):
    img = BuildImage.open(path)
    frame = load_image("china_flag\\0.png")
    points = ((15, 15), (448, 0), (445, 456), (0, 465))
    img = img.convert("RGBA").square().resize((450, 450)).perspective(points)
    frame = load_image("cover_face\\0.png")
    frame.paste(img, (120, 150), below=True)
    return frame.save_jpg()

def crawl(path:str):
    img = BuildImage.open(path)
    frame = load_image("china_flag\\0.png")
    num = 0
    total_num = 92
    num = random.randint(1, total_num)
    img = img.convert("RGBA").circle().resize((100, 100))
    frame = load_image(f"crawl\\{num:02d}.jpg")
    frame.paste(img, (0, 400), alpha=True)
    return frame.save_jpg()

def decent_kiss(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").resize((589, 340), keep_ratio=True)
    frame = load_image("decent_kiss\\0.png")
    frame.paste(img, (0, 91), below=True)
    return frame.save_jpg()

def dont_touch(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").square().resize((170, 170))
    frame = load_image("dont_touch\\0.png")
    frame.paste(img, (23, 231), alpha=True)
    return frame.save_jpg()

def marriage(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").resize_height(1080)
    img_w, img_h = img.size
    if img_w > 1500:
        img_w = 1500
    elif img_w < 800:
        img_h = int(img_h * img_w / 800)
    frame = img.resize_canvas((img_w, img_h)).resize_height(1080)
    left = load_image("marriage\\0.png")
    right = load_image("marriage\\1.png")
    frame.paste(left, alpha=True).paste(
        right, (frame.width - right.width, 0), alpha=True
    )
    return frame.save_jpg()

def mywife(path:str):
    img = BuildImage.open(path).convert("RGBA").resize_width(400)
    img_w, img_h = img.size
    frame = BuildImage.new("RGBA", (650, img_h + 500), "white")
    frame.paste(img, (int(325 - img_w / 2), 105), alpha=True)

    img_point = load_image("mywife\\1.png").resize_width(200)
    frame.paste(img_point, (421, img_h + 270))
    return frame.save_jpg()

def need(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").square().resize((115, 115))
    frame = load_image("need\\0.png")
    frame.paste(img, (327, 232), below=True)
    return frame.save_jpg()

def no_response(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").resize((1050, 783), keep_ratio=True)
    frame = load_image("no_response\\0.png")
    frame.paste(img, (0, 581), below=True)
    return frame.save_jpg()

def painter(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").resize((240, 345), keep_ratio=True, direction="north")
    frame = load_image("painter\\0.png")
    frame.paste(img, (125, 91), below=True)
    return frame.save_jpg()

def pat(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").square()
    locs = [(11, 73, 106, 100), (8, 79, 112, 96)]
    img_frames: List[IMG] = []
    for i in range(10):
        frame = load_image(f"pat\\{i}.png")
        x, y, w, h = locs[1] if i == 2 else locs[0]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        img_frames.append(frame.image)
    # fmt: off
    seq = [0, 1, 2, 3, 1, 2, 3, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 0, 0, 0, 4, 5, 5, 5, 6, 7, 8, 9]
    # fmt: on
    frames = [img_frames[n] for n in seq]
    return save_gif(frames, 0.085)

def play(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").square()
    # fmt: off
    locs = [
        (180, 60, 100, 100), (184, 75, 100, 100), (183, 98, 100, 100),
        (179, 118, 110, 100), (156, 194, 150, 48), (178, 136, 122, 69),
        (175, 66, 122, 85), (170, 42, 130, 96), (175, 34, 118, 95),
        (179, 35, 110, 93), (180, 54, 102, 93), (183, 58, 97, 92),
        (174, 35, 120, 94), (179, 35, 109, 93), (181, 54, 101, 92),
        (182, 59, 98, 92), (183, 71, 90, 96), (180, 131, 92, 101)
    ]
    # fmt: on
    raw_frames: List[BuildImage] = [load_image(f"play\\{i}.png") for i in range(38)]
    img_frames: List[BuildImage] = []
    for i in range(len(locs)):
        frame = raw_frames[i]
        x, y, w, h = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        img_frames.append(frame)
    frames = (
        img_frames[0:12]
        + img_frames[0:12]
        + img_frames[0:8]
        + img_frames[12:18]
        + raw_frames[18:38]
    )
    frames = [frame.image for frame in frames]
    return save_gif(frames, 0.06)

def play_game(path):
    img = BuildImage.open(path)
    frame = load_image("play_game\\0.png")
    def make(img: BuildImage) -> BuildImage:
        points = ((0, 5), (227, 0), (216, 150), (0, 165))
        screen = img.resize((220, 160), keep_ratio=True).perspective(points)
        return frame.copy().paste(screen.rotate(9, expand=True), (161, 117), below=True)

    return make(img).save_jpg()

def police(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").square().resize((245, 245))
    frame = load_image("police\\0.png")
    frame.paste(img, (224, 46), below=True)
    return frame.save_jpg()

def pound(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").square()
    # fmt: off
    locs = [
        (135, 240, 138, 47), (135, 240, 138, 47), (150, 190, 105, 95), (150, 190, 105, 95),
        (148, 188, 106, 98), (146, 196, 110, 88), (145, 223, 112, 61), (145, 223, 112, 61)
    ]
    # fmt: on
    frames: List[IMG] = []
    for i in range(8):
        frame = load_image(f"pound\\{i}.png")
        x, y, w, h = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        frames.append(frame.image)
    return save_gif(frames, 0.05)

def prpr(path:str):
    img = BuildImage.open(path)
    frame = load_image("prpr\\0.png")
    def make(img: BuildImage) -> BuildImage:
        points = ((0, 19), (236, 0), (287, 264), (66, 351))
        screen = img.resize((330, 330), keep_ratio=True).perspective(points)
        return frame.copy().paste(screen, (56, 284), below=True)
    return make(img).save_jpg()

def punch(path:str):
    img = BuildImage.open(path)
    img = img.convert("RGBA").square().resize((260, 260))
    frames: List[IMG] = []
    # fmt: off
    locs = [
        (-50, 20), (-40, 10), (-30, 0), (-20, -10), (-10, -10), (0, 0),
        (10, 10), (20, 20), (10, 10), (0, 0), (-10, -10), (10, 0), (-30, 10)
    ]
    # fmt: on
    for i in range(13):
        fist = load_image(f"punch\\{i}.png")
        frame = BuildImage.new("RGBA", fist.size, "white")
        x, y = locs[i]
        frame.paste(img, (x, y - 15), alpha=True).paste(fist, alpha=True)
        frames.append(frame.image)
    return save_gif(frames, 0.03)
path = f'{os.path.dirname(__file__)}\\test.jpg'
fun = {0:petpet(path),1:blood_pressure(path),2:addition(path),3:anti_kidnap(path),4:china_flag(path),5:cover_face(path),
       6:crawl(path),7:marriage(path),8:mywife(path),9:decent_kiss(path),10:dont_touch(path),11:need(path),12:no_response(path),
       13:painter(path),14:pat(path),15:play(path),16:play_game(path),16:police(path),17:pound(path),18:prpr(path),19:punch(path),20:pound(path)}
for i in range(0,21):
    print(i)
    with open(f'{os.path.dirname(__file__)}\\ret{i}.jpg',mode = 'wb+') as file:
        file.write(fun[i].getvalue())


