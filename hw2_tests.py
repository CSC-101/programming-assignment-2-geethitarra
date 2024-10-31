from data import Rectangle, Point, Duration, Song
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        point1 = Point(0,0)
        point2 = Point(10,10)
        expected = Rectangle(Point(0, 10), Point(10, 0))
        result = hw2.create_rectangle(point1,point2)
        self.assertEqual(expected, result)

    def test_create_rectangle2(self):
        point1 = Point(10,10)
        point2 = Point(10,10)
        expected = Rectangle(Point(10, 10), Point(10, 10))
        result = hw2.create_rectangle(point1,point2)
        self.assertEqual(expected, result)
    # Part 2
    def test_shorter_duration_than(self):
        piece1 = Duration(100,10)
        piece2 = Duration(0,10)
        expected = False
        result = hw2.shorter_duration_than(piece1,piece2)
        self.assertEqual(expected, result)

    def test_shorter_duration_than2(self):
        piece1 = Duration(0, 0)
        piece2 = Duration(0, 0)
        expected = False
        result = hw2.shorter_duration_than(piece1, piece2)
        self.assertEqual(expected, result)

    def test_shorter_duration_than3(self):
        piece1 = Duration(9, 48)
        piece2 = Duration(10000, 9)
        expected = True
        result = hw2.shorter_duration_than(piece1, piece2)
        self.assertEqual(expected, result)

    # Part 3
    def test_song_shorter_than(self):
        duration1 = Duration(600, 30)  # 2 minutes, 30 seconds
        duration2 = Duration(56, 10)  # 3 minutes
        duration3 = Duration(1, 0)  # 1 minute, 45 seconds

        song1 = Song("Taylor Swift", "Blank Space", duration1)
        song2 = Song("Katy Perry", "Firework", duration2)
        song3 = Song("Beyonce", "Girls", duration3)


        songs = [song1, song2, song3]
        length = Duration(2, 0)  # 2 minutes

        expected = [song3]
        result = hw2.song_shorter_than(songs, length)
        self.assertEqual(expected, result)

    def test_song_shorter_than2(self):
        duration1 = Duration(100, 0)  # 2 minutes, 30 seconds
        duration2 = Duration(9000, 10)  # 3 minutes
        duration3 = Duration(1, 0)  # 1 minute, 45 seconds

        song1 = Song("Taylor Swift", "Blank Space", duration1)
        song2 = Song("Katy Perry", "Firework", duration2)
        song3 = Song("Beyonce", "Girls", duration3)


        songs = [song1, song2, song3]
        length = Duration(0, 0)  # 2 minutes

        expected = []
        result = hw2.song_shorter_than(songs, length)
        self.assertEqual(expected, result)
    # Part 4
    def test_running_time(self):
        duration1 = Duration (4, 6)
        duration2 = Duration(10, 0)
        duration3 = Duration(2, 0)

        song1 = Song("The Weeknd", "The Hills", duration1)
        song2 = Song("Ariana Grande", "The Way", duration2)
        song3 = Song("Kali Uchis", "Tyrant", duration3)

        music = [song1, song2, song3]
        playlist = [0, 2, 1, 0]
        result = hw2.running_time(music, playlist)

        expected = Duration(20, 12)
        self.assertEqual(result, expected)

    def test_running_time2(self):
        duration1 = Duration (4, 6)
        duration2 = Duration(10, 0)
        duration3 = Duration(2, 0)

        song1 = Song("The Weeknd", "The Hills", duration1)
        song2 = Song("Ariana Grande", "The Way", duration2)
        song3 = Song("Kali Uchis", "Tyrant", duration3)

        music = [song1, song2, song3]
        playlist = [0, 2, 1]
        result = hw2.running_time(music, playlist)

        expected = Duration(16, 6)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        cities = ['san luis obispo']
        expected = True
        result = hw2.validate_route(city_links, cities)
        self.assertEqual(result, expected)

    def test_validate_route2(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],['atascadero', 'santa margarita'],['atascadero', 'creston']]
        cities = ['san luis obispo','pismo beach', 'atascadero']
        expected = False
        result = hw2.validate_route(city_links, cities)
        self.assertEqual(result, expected)
    # Part 6
    def test_longest_repetition(self):
        nums = [3, 6, 6, 6, 1, 1]
        expected = 1
        result = hw2.longest_repetition(nums)
        self.assertEqual(result, expected)

    def test_longest_repetition2(self):
        nums = []
        expected = None
        result = hw2.longest_repetition(nums)
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
