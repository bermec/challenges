import os
import unittest

def analyze_text(filename):
    pass

class TextAnalysisTests(unittest, TestCase):
    ''' tests for the "analyze_text()" function'''


    def setUp(self):
        ''' Fixture that creates a file for the text methods to use.'''
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation.\n'
                    'or any nation so conceived and so dedicated\n'
                    'can long endure.')


    def tearDown(self):
        ''' Fixture that deletes the file used by the test method. '''
        try:
            os.remove(self.filename)
        except:
            pass



    def test_function_runs(self):
        ''' Basic smoke test: does the function run.'''
        analyze_text(self.filename)


    def test_line_count(self):
        ''' Check that the line count is correct. '''
        self.assertEqual(analyze_text(self.filename), 4)


if name == '__main__':
    unittest.main()