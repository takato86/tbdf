import tbdf
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("tbdf")


def test():
    df = tbdf.core.load_as_dataframe("data/2022-05-16 16_53_27.205090_0/events.out.tfevents.1652687609.ymdlab00.23384.0")
    df.to_csv("data/test_result.csv")


if __name__ == "__main__":
    test()
