import base64
from io import BytesIO

import scipy.io.wavfile as wav
import streamlit as st

from brainwave.config.app import (
    BASE_FREQUENCY_DEFAULT,
    BASE_FREQUENCY_RANGE_MAX,
    BASE_FREQUENCY_RANGE_MIN,
    BASE_FREQUENCY_STEP,
    BEAT_FREQUENCY_RANGE_MAX,
    BEAT_FREQUENCY_RANGE_MIN,
    BRAIN_WAVES,
    DURATION_DEFAULT,
    DURATION_RANGE_MAX,
    DURATION_RANGE_MIN,
)
from brainwave.utils.binaural_beats import generate_binaural_beats


def app():
    st.title('Binaural Beats Generator')

    st.subheader('Brain Wave Selection')
    selected_wave: str = st.selectbox(
        'Select a type of brain wave:', list(BRAIN_WAVES.keys())
    )
    default_beat: int = BRAIN_WAVES[selected_wave]

    st.subheader('Base Frequency (Hz)')
    base_frequency: int = st.slider(
        'Base Frequency (Hz):',
        min_value=BASE_FREQUENCY_RANGE_MIN,
        max_value=BASE_FREQUENCY_RANGE_MAX,
        value=BASE_FREQUENCY_DEFAULT,
        step=BASE_FREQUENCY_STEP,
    )
    base_frequency_input: int = st.number_input(
        '...or enter the base frequency using the keyboard:',
        min_value=BASE_FREQUENCY_RANGE_MIN,
        max_value=BASE_FREQUENCY_RANGE_MAX,
        value=base_frequency,
        step=BASE_FREQUENCY_STEP,
    )

    st.subheader('Beat Frequency (Hz)')
    beat_frequency: int = st.slider(
        'Select the beat frequency using the slider:',
        min_value=BEAT_FREQUENCY_RANGE_MIN,
        max_value=BEAT_FREQUENCY_RANGE_MAX,
        value=default_beat,
    )
    beat_frequency_input: int = st.number_input(
        '...or enter the beat frequency using the keyboard:',
        min_value=BEAT_FREQUENCY_RANGE_MIN,
        max_value=BEAT_FREQUENCY_RANGE_MAX,
        value=beat_frequency,
    )

    st.subheader('Duration (seconds)')
    duration: int = st.slider(
        'Duration (seconds):',
        min_value=DURATION_RANGE_MIN,
        max_value=DURATION_RANGE_MAX,
        value=DURATION_DEFAULT,
    )
    duration_input: int = st.number_input(
        '...or enter the duration using the keyboard:',
        min_value=DURATION_RANGE_MIN,
        max_value=DURATION_RANGE_MAX,
        value=duration,
    )

    base_frequency = base_frequency_input
    beat_frequency = beat_frequency_input
    duration = duration_input

    if st.button('Generate Sound'):
        audio_data, sample_rate = generate_binaural_beats(
            base_frequency, beat_frequency, duration
        )
        wav_file: BytesIO = BytesIO()
        wav.write(wav_file, sample_rate, audio_data)
        wav_file.seek(0)

        b64: str = base64.b64encode(wav_file.read()).decode()
        audio_html: str = (
            f'<audio controls loop><source src="data:audio/wav;base64,{b64}" '
            f'type="audio/wav"></audio>'
        )
        st.markdown(audio_html, unsafe_allow_html=True)

        href: str = (
            f'<a href="data:file/wav;base64,{b64}" download="'
            f'binaural_beats_{selected_wave}.wav">Download '
            f'{selected_wave} Binaural Beat</a>'
        )
        st.markdown(href, unsafe_allow_html=True)


if __name__ == '__main__':
    app()
