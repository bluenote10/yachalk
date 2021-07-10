from .chalk_factory import ChalkFactory


def create_chalk() -> ChalkFactory:
    return ChalkFactory()


chalk = create_chalk()
