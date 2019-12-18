## Data preparation
 You need download Wikipedia's new dataset at [viwiki](https://dumps.wikimedia.org/viwiki/)
<br> Then install [wikiextractor](https://github.com/attardi/wikiextractor) to get data from Wikipedia.
<br> Running **WikiExtractor.py**:
```php
python WikiExtractor.py -o viwiki viwiki-20191201-pages-articles-multistream.xml.bz2
```
## Data processing
Running  **process_data.py** obtain to get file ***datatrain.txt***
