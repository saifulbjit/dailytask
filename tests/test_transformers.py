import unittest
from snapreq.utils.transformers import convert_arguement_to_dict

class TestTransformer(unittest.TestCase):
    def test_convert_arguement_to_dict(self):
        self.assertEqual(convert_arguement_to_dict("key1=value1&key2=value2"), {"key1": "value1", "key2": "value2"})
        self.assertEqual(convert_arguement_to_dict("key1=value1&key2=value2&key3=value3"), {"key1": "value1", "key2": "value2", "key3": "value3"})
        self.assertEqual(convert_arguement_to_dict("key1 = value1"), {"key1": "value1"})
        self.assertEqual(convert_arguement_to_dict("key1=value1& key2=value2&key3=value3&key4=value4"), {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"})
        self.assertEqual(convert_arguement_to_dict("key1=value1&key2=value2&key3=value3&key4=value4&key5=value5"), {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5"})
        self.assertEqual(convert_arguement_to_dict("key1=value1&key2=value2&key3=value3&key4=value4&key5=value5&key6=value6"), {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5", "key6": "value6"})
        self.assertEqual(convert_arguement_to_dict("key1=value1&key2=value2&key3=value3&key4=value4&key5=value5&key6=value6&key7=value7"), {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5", "key6": "value6", "key7": "value7"})


if __name__ == "__main__":
    unittest.main()