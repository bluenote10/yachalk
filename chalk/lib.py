class Generator:
    def __init__(self, on, off):
        self.on = on
        self.off = off

    def __call__(self, s: str) -> str:
        all_on = "".join(self.on)
        all_off = "".join(self.off)
        return all_on + s + all_off


class Chalk:
    @property
    def blue(self) -> Generator:
        return Generator("bon", "boff")


def create_chalk():
    return Chalk()


chalk = create_chalk()
