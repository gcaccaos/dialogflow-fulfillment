"""Unit tests module for RichResponse classes"""
import unittest

from dialogflow_fulfillment import Card, Image, Payload, QuickReplies, Text


class TextTests(unittest.TestCase):
    def setUp(self):
        self.text = Text('text')

    def test_has_text(self):
        self.assertTrue(hasattr(self.text, 'text'))

    def test_no_arg(self):
        self.assertRaises(TypeError, Text)

    def test_non_string_arg(self):
        self.assertRaises(TypeError, Text, ['list'])

    def test_get_response_object(self):
        self.assertEqual({'text': {'text': [self.text.text]}},
                         self.text._get_response_object())


class QuickRepliesTests(unittest.TestCase):
    def setUp(self):
        self.quick_replies = QuickReplies(['first reply', 'second reply'])

    def test_has_quick_replies(self):
        self.assertTrue(hasattr(self.quick_replies, 'quick_replies'))

    def test_no_arg(self):
        self.assertRaises(TypeError, QuickReplies)

    def test_non_sequence(self):
        self.assertRaises(TypeError, QuickReplies, 'text')

    def test_get_response_object(self):
        self.assertEqual({'quickReplies': {'quickReplies': self.quick_replies.quick_replies}},
                         self.quick_replies._get_response_object())


class PayloadTests(unittest.TestCase):
    def setUp(self):
        self.payload = Payload({'pay': 'load'})

    def test_has_payload(self):
        self.assertTrue(hasattr(self.payload, 'payload'))

    def test_has_set_payload(self):
        self.assertTrue(hasattr(self.payload, 'set_payload'))

    def test_no_arg(self):
        self.assertRaises(TypeError, Payload)

    def test_non_dictionary(self):
        self.assertRaises(TypeError, Payload, 'text')

    def test_get_response_object(self):
        self.assertEqual({'payload': self.payload.payload},
                         self.payload._get_response_object())


class ImageTests(unittest.TestCase):
    def setUp(self):
        self.image = Image('https://picsum.photos/128')

    def test_has_image_url(self):
        self.assertTrue(hasattr(self.image, 'image_url'))

    def test_has_set_image(self):
        self.assertTrue(hasattr(self.image, 'set_image'))

    def test_no_arg(self):
        self.assertRaises(TypeError, Image)

    def test_get_response_object(self):
        self.assertEqual({'image': {'imageUri': self.image.image_url}},
                         self.image._get_response_object())


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card('card title')

    def test_has_title(self):
        self.assertTrue(hasattr(self.card, 'title'))

    def test_has_set_title(self):
        self.assertTrue(hasattr(self.card, 'set_title'))

    def test_no_arg(self):
        self.assertRaises(TypeError, Card)

    def test_get_response_object(self):
        self.assertEqual({'card': {'title': self.card.title}},
                         self.card._get_response_object())


if __name__ == '__main__':
    unittest.main()
