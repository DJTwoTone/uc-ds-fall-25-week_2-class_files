"""Add to end, read first, skip first (slow front)."""


def next_song(playlist: list[str]) -> str | None:
    return playlist[0] if playlist else None


def add_song(playlist: list[str], title: str) -> None:
    playlist.append(title)


def skip_song(playlist: list[str]) -> None:
    if playlist:
        playlist.pop(0)  # slow for long lists


if __name__ == "__main__":
    pl = ["Song A", "Song B"]
    print("Now playing:", next_song(pl))
    add_song(pl, "Song C")
    print("Queue:", pl)
    skip_song(pl)
    print("After skip:", pl)