# test_signalhound.py
"""
Tests for SignalHound module.
"""

import unittest
from signalhound import SignalHound

class TestSignalHound(unittest.TestCase):
    """Test cases for SignalHound class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SignalHound()
        self.assertIsInstance(instance, SignalHound)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SignalHound()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
