"""Unit tests of functions in ml.py"""
from unittest.mock import Mock, patch
import speech_recognition as sr
import pytest

from ml import (
    capture_voice_input,
    convert_voice_to_text,
    process_voice_command,
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


@patch("ml.save_to_database")
def test_process_voice_command(mock_save_to_db):
    """Test for different strings"""
    texts = [
        "Hello, human!",
        "meow",
        "Dog barks loudly",
        "cow says moo",
        "No match",
        "Goodbye!",
    ]

    # Call the method for each text
    for text in texts:
        process_voice_command(text)

    # Assertions
    assert mock_save_to_db.call_count == len(
        texts
    )  # Check if save_to_database is called same times as texts


@patch("ml.save_to_database")
def test_process_voice_command_human(mock_save_to_db):
    """Test for different strings"""
    texts = "Hello, human!"

    # Call the method for each text

    process_voice_command(texts)

    # Assertions
    assert (
        mock_save_to_db.call_count == 1
    )  # Check if save_to_database is called same times as texts


@patch("ml.save_to_database")
def test_process_voice_command_cat(mock_save_to_db):
    """Test for different strings"""
    texts = "cat"

    # Call the method for each text

    process_voice_command(texts)

    # Assertions
    assert (
        mock_save_to_db.call_count == 1
    )  # Check if save_to_database is called same times as texts


@patch("ml.save_to_database")
def test_process_voice_command_dog(mock_save_to_db):
    """Test for different strings"""
    texts = "dog"

    # Call the method for each text

    process_voice_command(texts)

    # Assertions
    assert (
        mock_save_to_db.call_count == 1
    )  # Check if save_to_database is called same times as texts


if __name__ == "__main__":
    pytest.main()
