import logging
import logging.handlers
import time

from faker import Faker

logger = logging.getLogger("elk_example_app")
logger.setLevel(logging.DEBUG)

formmatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler = logging.handlers.RotatingFileHandler(
    "/var/log/elk_example_app/app.log",
    maxBytes=1024 * 1024 * 10,
    backupCount=5,
)
handler.setFormatter(formmatter)

logger.addHandler(handler)


def main() -> None:
    fake = Faker()

    while True:
        level = fake.random_element(elements=[
            logging.CRITICAL,
            logging.ERROR,
            logging.WARNING,
            logging.INFO,
            logging.DEBUG,
        ])
        message = fake.text(max_nb_chars=80)

        logger.log(level, message)

        time.sleep(1.0)


if __name__ == "__main__":
    main()
