import os
import sys
from pathlib import Path
from unittest.mock import patch

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from auth.auth_service import get_secret, get_supabase_config


def test_get_supabase_config_handles_missing_secrets():
    with patch.object(st, "secrets", {}, create=True):
        assert get_supabase_config() == (None, None)


def test_get_supabase_config_uses_environment_fallback():
    with patch.dict(os.environ, {"SUPABASE_URL": "https://example.supabase.co", "SUPABASE_KEY": "demo-key"}, clear=True):
        with patch.object(st, "secrets", {}, create=True):
            assert get_supabase_config() == ("https://example.supabase.co", "demo-key")


def test_get_secret_returns_env_value_when_streamlit_secret_missing():
    with patch.dict(os.environ, {"GROQ_API_KEY": "env-groq-key"}, clear=True):
        with patch.object(st, "secrets", {}, create=True):
            assert get_secret("GROQ_API_KEY") == "env-groq-key"
