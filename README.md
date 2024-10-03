![](./polarpandas_github_repo_qr.png)
URL: https://github.com/octaflop/polarpandas

# Get started:

After cloning, and with python 3.12 installed, run this

```bash
python3.12 -m venv venv &&
source venv/bin/activate &&
pip install -r requirements.txt &&
jupyter lab
```

You should be presented with a jupyter lab. Run this in the first cell
to use the slide snippets.

```python
import io
import pandas as pd
import polars as pl
import numpy as np
from time import time
from rich.console import Console
from rich.table import Table
from rich.progress import track
import plotext as plt

console = Console()
```

Open `slides/presentation.md` by right-clicking and selecting `Open with > Marp Preview`.

## Demos

- `polarpandas.py` is a basic dataframes demo

## Tools

- `qrslide.py` is used to generate a QR code for the presentation url.
