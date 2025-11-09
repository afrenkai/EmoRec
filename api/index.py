"""
Vercel serverless function entrypoint.
This file exports the FastAPI app for Vercel's Python runtime.
"""
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

# Vercel expects the ASGI app to be named 'app'
# This is already defined in backend.main, so we just re-export it
__all__ = ['app']
