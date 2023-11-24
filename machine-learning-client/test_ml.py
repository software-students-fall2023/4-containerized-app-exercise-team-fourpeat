import pytest
import speech_recognition as sr
from unittest import mock
from unittest.mock import Mock, patch, mock_open
from unittest.mock import MagicMock
from io import StringIO

from ml import (
    capture_voice_input,
    convert_voice_to_text,
    process_voice_command,
    sr as real_sr,
)

recognizer = sr.Recognizer()

import speech_recognition as sr

recognizer = sr.Recognizer()
