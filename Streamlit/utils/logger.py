import logging
from colorlog import ColoredFormatter
import traceback


# Formato colorido
formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "INFO":     "green",
        "WARNING":  "yellow",
        "ERROR":    "red",
    }
)

# Configura console handler com o formatter colorido
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Configura logger raiz
logging.basicConfig(
    level=logging.INFO,
    handlers=[console_handler]
)

def log_message(level: str, message: str, details: dict = None, exc: Exception = None) -> str:
    level = level.upper()
    valid_levels = {"INF", "WR", "ERR"}

    if level not in valid_levels:
        level = "INF"

    formatted_message = message

    if details:
        details_str = " | ".join(f"{key}: {value}" for key, value in details.items())
        formatted_message += f" | {details_str}"

    if exc:
        tb = traceback.extract_tb(exc.__traceback__)[-1] 
        file_info = f"{tb.filename}, line {tb.lineno}, in {tb.name}"
        formatted_message += f" | location: {file_info}"

    log_func = {
        "INF": logging.info,
        "WR": logging.warning,
        "ERR": logging.error
    }.get(level, logging.info)

    log_func(formatted_message)
    return formatted_message