#!/usr/bin/env python3
import unittest
import subprocess
import echo


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()

    def make_namespaces(self, flags, word):
        res = []
        for flag in flags:
            res.append(self.parser.parse_args(
                [flag, word]))
        return res

    def get_stdouts(self, flags, word):
        res = []
        for flag in flags:
            args = (["python", "./echo.py", flag])
            if word:
                args.append(word)
            process = subprocess.Popen(args,
                                       stdout=subprocess.PIPE)
            stdout, _ = process.communicate()
            res.append(stdout)
        return res

    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_uppper(self):
        tags = ['-u', '--upper']
        original_word = 'hello'
        formatted_word = 'HELLO'
        namespaces = self.make_namespaces(tags, original_word)
        stdouts = self.get_stdouts(tags, original_word)

        for n in namespaces:
            self.assertTrue(n.upper)
        for s in stdouts:
            s = s.strip()
            self.assertEqual(s, formatted_word)

    def test_lower(self):
        tags = ['-l', '--lower']
        original_word = 'HELLO'
        formatted_word = 'hello'
        namespaces = self.make_namespaces(tags, original_word)
        stdouts = self.get_stdouts(tags, original_word)

        for n in namespaces:
            self.assertTrue(n.lower)
        for s in stdouts:
            s = s.strip()
            self.assertEqual(s, formatted_word)

    def test_title(self):
        tags = ['-t', '--title']
        original_word = 'hello'
        formatted_word = 'Hello'
        namespaces = self.make_namespaces(tags, original_word)
        stdouts = self.get_stdouts(tags, original_word)
        for n in namespaces:
            self.assertTrue(n.title)
        for s in stdouts:
            s = s.strip()
            self.assertEqual(s, formatted_word)

    def test_all_flags(self):
        original_word = 'heLLo!'
        formatted_word = 'Hello!'
        args = ["python", "./echo.py", '-u', '-l', '-t', original_word]
        process = subprocess.Popen(args,
                                   stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEqual(stdout.strip(), formatted_word)

    def test_no_flags(self):
        words = ['heLLo!', 'HELLO', 'hEllO!', 'hello']
        outs = []
        for word in words:
            args = ["python", "./echo.py", word]
            process = subprocess.Popen(args,
                                       stdout=subprocess.PIPE)
            stdout, _ = process.communicate()
            outs.append(stdout)
        for i, out in enumerate(outs):
            self.assertEqual(out.strip(), words[i])


if __name__ == '__main__':
    unittest.main()
