# tbdf
Transform tensorboard file into dataframe library


```python
import tbdf

fpath = "data/2022-05-16 16_53_27.205090_0/events.out.tfevents.1652687609.ymdlab00.23384.0"
data_df = tbdf.load_as_dataframe(fpath)

```