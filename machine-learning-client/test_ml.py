"""Module providing a function printing python version."""
from unittest.mock import MagicMock, patch
import speech_recognition as sr
import pytest

from ml import (
    capture_voice_input,
    process_voice_command,
)

recognizer = sr.Recognizer()


def test_capture_voice_input_timeout():
    """Mocking the listen function to simulate a WaitTimeoutError"""

    def listen_mock(*args, **kwargs):
        """Simulating Wait time out Error"""
        raise sr.WaitTimeoutError()

    with patch.object(sr.Recognizer, "listen", side_effect=listen_mock):
        result = capture_voice_input(timeout=0.01)
        assert result is None


def test_capture_voice_input():
    """Test with mock voice input capture"""

    mock_audio_data = sr.AudioData(b"fake_audio_data", 16000, 2)

    mock_recognizer_instance = MagicMock()
    mock_listen = MagicMock(return_value=mock_audio_data)
    setattr(mock_recognizer_instance, "listen", mock_listen)

    with patch("ml.sr.Recognizer", return_value=mock_recognizer_instance):
        result = capture_voice_input()

        assert isinstance(result, type(mock_audio_data))


def test_process_voice_command_human():
    """Test with recognized command of human"""
    result = process_voice_command("human")
    assert result is False


def test_process_voice_command_cat():
    """Test with recognized command of cat"""
    result = process_voice_command("cat")
    assert result is False


def test_process_voice_command_dog():
    """Test with recognized command of dog"""
    result = process_voice_command("dog")
    assert result is False


def test_process_voice_command_cow():
    """Test with recognized command of cow"""
    result = process_voice_command("cow")
    assert result is False


def test_process_voice_command_bird():
    """Test with recognized command of bird"""
    result = process_voice_command("bird")
    assert result is False


def test_process_voice_command_frog():
    """Test with recognized command of frog"""
    result = process_voice_command("frog")
    assert result is False


if __name__ == "__main__":
    pytest.main()
