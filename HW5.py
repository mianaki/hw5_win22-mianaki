# Your name: Michaela Ianaki
# Your student id: 39084442
# Your email: mianaki@umich.edu
# List who you have worked with on this homework:

import re, os, unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines

def find_movie_titles(string_list):
    """
    This function returns a dictionary with the keys being numbers, (1 - 8)
    and the values being the names of movies.
    """
def find_movie_titles(string_list):
    movie_titles = {}
    reg_ex = '^[Tt]itle:\s'
    for line in string_list:
        movie = re.findall(reg_ex, line)
    for i in range(len(movie)): 
        movie_titles[movie] = i
    return movie_titles

def find_and_phrases(string_list):
    for line in string_list:
        and_phrases = re.findall('\w*\s[Aa]nd\s\w*', line)
    return and_phrases

def find_urls(string_list):
    for line in string_list:
        urls = re.findall("^http(s)?:\/+www.\S*.com.*", line)
    return urls

def find_valid_release_dates(string_list):
    """
    This function returns a list of valid release dates.
    Sample format:
        mm/dd/yyyy
        mm/dd/yy
        mm-dd-yyyy
        mm-dd-yy
    Please refer to the instructions and be careful about invalid dates!
    """
def find_valid_release_dates(string_list):
    for line in string_list:
        valid_dates = re.findall('(\d+|\/\d+\/|-\/d+)', line)

    return valid_dates

## Extra credit
def count_mid_str(string_list, string):
    """
    This function returns a count of the number of times a specified string appears
    in the text. The matched string should be in the middle of a word (ie: Not at 
    the start of end of a word).
    """
    pass

#Implement your own tests
class TestAllMethod(unittest.TestCase):

    def test_find_movie_titles(self):
        text = read_file('best_picture.txt')
        self.assertEqual(find_movie_titles(text), {'Belfast': 1,
                                                            'CODA': 2,
                                                            'Don\'t Look Up': 3, 
                                                            'Drive My Car': 4,
                                                            'King Richard': 5, 
                                                            'Licorice Pizza': 6, 
                                                            'The Power of the Dog': 7, 
                                                            'West Side Story': 8})

        movies = find_movie_titles(text)
        self.assertIn('Belfast', movies)
        self.assertEqual(movies['Drive My Car'], 4), 
        self.assertNotEqual(movies['King Richard', 1])

    def test_find_valid_release_dates(self):
        text = read_file('best_picture.txt')
        self.assertEqual(find_valid_release_dates(text), ['08-13-2021', '12/05/2021', '11/24/21', 
        '11 19 21', '11/17/2021', '12-10-2021'])


    def test_find_and_phrases(self):
        text = read_file('best_picture.txt')

        self.assertEqual(find_and_phrases(text), ['boy and his', 'Music and her', 'actor and director', 'Venus and Serena', 
        'Kane and Gary', 'around and going', 'fear and awe', 'wife and her', 'love and the', 'Jets and the'])

        self.assertIn('boy and his', )

    def test_find_urls(self):
        text = read_file('best_picture.txt')
        self.assertEqual(find_urls(text), ['https://www.focusfeatures.com/belfast/watch/', 'https://www.imdb.com/title/tt10366460/', 'https://www.netflix.com/title/81252357', 'https://www.imdb.com/title/tt14039582/', 
        'https://www.kingrichardfilm.com/', 'https://en.wikipedia.org/wiki/Licorice_Pizza', 'https://www.rottentomatoes.com/m/the_power_of_the_dog', 'https://www.imdb.com/title/tt3581652/'])
        

    #Uncomment if working on Extra Credit
    #def test_count_mid_str(self):
    #    pass


def main():
    #Feel free run your functions here as well!
    pass

if __name__ == '__main__':
    main()
    print()
    unittest.main(verbosity=2)