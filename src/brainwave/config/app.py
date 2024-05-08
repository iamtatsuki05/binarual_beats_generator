from typing import Final

BRAIN_WAVES: Final[dict[str, int]] = {
    'Alpha Waves': 10,  # Typically 8-13 Hz
    'Beta Waves': 20,  # Typically 14-30 Hz
    'Theta Waves': 6,  # Typically 4-7 Hz
    'Delta Waves': 2,  # Typically 0.5-3 Hz
    'Gamma Waves': 40,  # Typically 30-100 Hz
}

BASE_FREQUENCY_RANGE_MIN: Final[int] = 1
BASE_FREQUENCY_RANGE_MAX: Final[int] = 500
BASE_FREQUENCY_DEFAULT: Final[int] = 200
BASE_FREQUENCY_STEP: Final[int] = 10

BEAT_FREQUENCY_RANGE_MIN: Final[int] = 1
BEAT_FREQUENCY_RANGE_MAX: Final[int] = 100

DURATION_RANGE_MIN: Final[int] = 1
DURATION_RANGE_MAX: Final[int] = 300
DURATION_DEFAULT: Final[int] = 30
