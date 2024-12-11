import os
from typing import Literal

OPENAI_KEY = os.getenv("openai_key")
SUPPORTED_LANG=Literal["Hungarian","Spanish", "French", "German", "Japanese", "Arabic", "Hindi", "Portuguese"]
LOG_FOLDER='logs/'