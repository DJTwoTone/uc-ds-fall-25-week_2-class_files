"""Index and change by position."""


def demo() -> None:
    photos = ["img_001.jpg", "img_002.jpg", "img_003.jpg"]
    print("3rd photo:", photos[2])
    photos[1] = "img_002_edit.jpg"
    print("After change:", photos)


if __name__ == "__main__":
    demo()