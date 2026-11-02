"""Public fabricated DuoChat text/sequence contract; no chat messages from users."""
import unittest

def synthetic_chat_message(sender, sequence, body):
    if sender not in {"fixture-a", "fixture-b"}:
        raise ValueError("not synthetic sender")
    if not isinstance(sequence, int) or sequence < 0:
        raise ValueError("invalid sequence")
    if not isinstance(body, str) or len(body) > 100:
        raise ValueError("invalid body")
    return (sender, sequence, body)

class FakeChatContract(unittest.TestCase):
    def test_fixture_accepted(self):
        self.assertEqual(synthetic_chat_message("fixture-a", 1, "hello"), ("fixture-a", 1, "hello"))
    def test_unknown_sender_denied(self):
        with self.assertRaises(ValueError):
            synthetic_chat_message("real-user", 1, "hello")
    def test_negative_sequence_denied(self):
        with self.assertRaises(ValueError):
            synthetic_chat_message("fixture-a", -1, "hello")
    def test_long_body_denied(self):
        with self.assertRaises(ValueError):
            synthetic_chat_message("fixture-b", 2, "x"*101)
    def test_bad_type_denied(self):
        with self.assertRaises(ValueError):
            synthetic_chat_message("fixture-a", 0, None)

if __name__ == "__main__":
    unittest.main()
