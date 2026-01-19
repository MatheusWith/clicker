from app.config.setup import configure
from app.config.config import settings


def main():
    configure(settings=settings)


if __name__ == "__main__":
    main()
