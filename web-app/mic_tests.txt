"""Unit tests of functions in app.py"""
from unittest.mock import MagicMock, patch
import speech_recognition as sr

from app import (
  capture_voice_input,
)

recognizer = sr.Recognizer()

def test_capture_voice_input_timeout():
    """Test of timeout in voice input capture"""

    def listen_mock(*args, **kwargs):
        """Simulating wait timeout error"""
        raise sr.WaitTimeoutError()

    with patch.object(sr.Recognizer, "listen", side_effect=listen_mock):
        result = capture_voice_input(timeout=0.01)
        assert result is None


def test_capture_voice_input():
    """Test to mock voice input capture"""

    mock_audio_data = sr.AudioData(b"fake_audio_data", 16000, 2)

    mock_recognizer_instance = MagicMock()
    mock_listen = MagicMock(return_value=mock_audio_data)
    setattr(mock_recognizer_instance, "listen", mock_listen)

    with patch("ml.sr.Recognizer", return_value=mock_recognizer_instance):
        result = capture_voice_input()

        assert isinstance(result, type(mock_audio_data))
