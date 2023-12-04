"""Unit tests of functions in ml.py"""
from unittest.mock import Mock, patch
import speech_recognition as sr
import pytest

from ml import (
    convert_voice_to_text,
    process_voice_command,
)

recognizer = sr.Recognizer()


def test_convert_voice_to_text():
    """Test to convert recognized voice to text"""
    mock_audio = Mock()
    mock_audio.text = "Recognized text"

    with patch.object(
        sr.Recognizer, "recognize_google", return_value="Recognized text"
    ):
        result = convert_voice_to_text(mock_audio)

        assert result == "Recognized text"


def test_convert_voice_to_text_unknown_value_error():
    """Test to convert voice to text with unknown value error"""
    mock_audio = Mock()

    with patch.object(sr.Recognizer, "recognize_google") as recognize_google_mock:
        recognize_google_mock.side_effect = sr.UnknownValueError("UnknownValueError")

        result = convert_voice_to_text(mock_audio)

        assert result == ""


def test_convert_voice_to_text_request_error():
    """Test to convert voice to text with request error"""
    mock_audio = Mock()

    with patch.object(sr.Recognizer, "recognize_google") as recognize_google_mock:
        recognize_google_mock.side_effect = sr.RequestError("RequestError")

        result = convert_voice_to_text(mock_audio)

        assert result == ""





if __name__ == "__main__":
    pytest.main()
