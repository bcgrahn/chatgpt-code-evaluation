import unittest

class Test(unittest.TestCase):

    def test_read_TXT(self):
        try:
            with open('./public/prompts.txt', 'r') as file:
                file.read()
        except IOError:
            self.fail('Unable to read file')

    
    def test_file_writing(self):
        # open a test file in write mode
        file = open("./public/ResponseFiles/responseTest.txt", "w")
        # write some text to the file
        file.write("This is a test.")
        # close the file
        file.close()
        
        # open the file again in read mode to check if the text was written successfully
        file = open("./public/ResponseFiles/responseTest.txt", "r")
        content = file.read()
        file.close()

         # erase content
        file = open("./public/ResponseFiles/responseTest.txt", "w")
        file.write("")
        file.close()
        
        # assert that the text we wrote is the same as the text we read
        self.assertEqual(content, "This is a test.")

if __name__ == '__main__':
    unittest.main()

