"""Unit tests of functions in ml.py"""
from unittest.mock import Mock, MagicMock, patch
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


def test_process_voice_command_snake():
    """Test with recognized command of snake"""
    result = process_voice_command("snake")
    assert result is False


def test_process_voice_command_goodbye():
    """Test with recognized command of goodbye"""
    result = process_voice_command("goodbye")
    assert result is True


if __name__ == "__main__":
    pytest.main()
