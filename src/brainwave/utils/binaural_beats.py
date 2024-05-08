from typing import Optional

import numpy as np


def generate_binaural_beats(
    base_freq: int,
    beat_freq: int,
    duration: int,
    fs: Optional[int] = 44100,
) -> tuple[np.ndarray, int]:
    n_samples: int = int(fs * duration)
    t: np.ndarray = np.arange(n_samples) / fs
    left_ear: np.ndarray = np.sin(2 * np.pi * base_freq * t)
    right_ear: np.ndarray = np.sin(2 * np.pi * (base_freq + beat_freq) * t)
    stereo_sound: np.ndarray = np.vstack((left_ear, right_ear)).T
    stereo_normalized: np.ndarray = np.int16(
        (stereo_sound / np.max(np.abs(stereo_sound))) * 32767
    )
    return stereo_normalized, fs
