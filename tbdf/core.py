import logging
import pandas as pd
import tensorflow as tf

logger = logging.getLogger("tbdf")


def load_as_dataframe(file_path: str) -> pd.DataFrame:
    """Load tensorboard file as pandas.DataFrame."""
    metric_columns = set()
    step_set = set()

    # create metric column set
    logger.info("Initializing...")
    for event in tf.compat.v1.train.summary_iterator(file_path):
        step = event.step
        step_set.add(step)

        for summary_value in event.summary.value:
            tag = summary_value.tag
            metric_columns.add(tag)

    df_rows = {
        step: {key: None} for key in metric_columns
        for step in step_set
    }
    
    logger.info("Transforming...")
    for event in tf.compat.v1.train.summary_iterator(file_path):
        step = event.step
        
        for summary_value in event.summary.value:
            metric = summary_value.tag
            value = summary_value.simple_value
            df_rows[step][metric] = value
    
    logger.info("Complete transforming!!")
    df = pd.DataFrame.from_dict(df_rows, orient="index")
    return df
