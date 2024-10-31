from data import Point, Rectangle, Duration, Song
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: Point, point2: Point )-> Rectangle:
    if point1.x > point2.x:
        left_x, right_x = point2.x, point1.x
    else:
        left_x, right_x = point1.x, point2.x

    if point1.y > point2.y:
        top_y, bottom_y = point1.y, point2.y
    else:
        top_y, bottom_y = point2.y, point1.y

    top_left = Point(left_x, top_y)
    bottom_right = Point(right_x, bottom_y)

    return Rectangle(top_left, bottom_right)

#The purpose of this function is to return a Rectangle object using by finding the top-left and bottom-right corners of two points with the greatest y-values.
#The input for this function is two points of the Point class and the output is a Rectangle object with top-left and bottom-point points.
#def create_rectangle(point1: Point, point2: Point )-> Rectangle:
#Refer to hw2_tests.py for tests

# Part 2
def shorter_duration_than(piece1: Duration, piece2: Duration)->bool:
    piece1total = piece1.minutes*60 + piece1.seconds
    piece2total = piece2.minutes*60 + piece2.seconds

    if piece1total < piece2total:
        return True
    else:
        return False
#The purpose of this function is to return True if the first song is shorter than the second passed into the function.
#The input is two pieces/songs of the class Duration and the output is a boolean that returns True if the second piece is longer in duration than the first.
#def shorter_duration_than(piece1: Duration, piece2: Duration)->bool:
#Refer to hw2_tests.py for tests


# Part 3
def song_shorter_than(music: list[Song], length: Duration)-> list:
    return [song for song in music if shorter_duration_than(song.duration, length)]

#The purpose of the function is to return the songs in the list, music, that is less than the length, a Duration passed into the function.
#The input is a list of songs of the Song class and a length of the Duration class. The output is a list.
#def song_shorter_than(music: list[Song], length: Duration)-> list:
#Refer to hw2_tests.py for tests


# Part 4
def running_time(music: list[Song], nums: list[int])->Duration:
    seconds = 0
    for i in nums:
        if 0 <= i < len(music):
            song_duration = music[i].duration
            seconds += song_duration.minutes * 60 + song_duration.seconds

    minutes = seconds // 60
    seconds = seconds % 60
    return Duration(minutes, seconds)

#The purpose of this function is to return the duration of a list of songs given a list of indices corresponding to song durations in the inputted list.
#The input is a list of songs of class Song and a list of integers that contain the desired indices. The output is a object of the Duration class, containing minutes and seconds.
#running_time(music: list[Song], nums: list[int])->Duration:
#Refer to hw2_tests.py for tests

# Part 5
def validate_route(city_links:list[list[str]], cities: list[str])->bool:
    if len(cities) <= 1:
        return True

    for i in range(len(cities)-1):
        if [cities[i], cities[i+1]] not in city_links and [cities[i+1], cities[i]] not in city_links:
            return False
    return True

#The purpose of this function is to return a boolean that evaluates if there's a direct route between values in a list.
#The input a list of cities and a list of the desired cities that need to be checked for a direct route. The output is a boolean, True or False.
#validate_route(city_links:list[list[str]], cities: list[str])->bool:
#Refer to hw2_tests.py for tests



# Part 6
def longest_repetition(nums: list[int])-> Optional[int]:
    if not nums:
        return None
    count = 1
    longest = 1
    idx = 0

    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]:
            count+=1
            if count > longest:
                idx = (i + 2) - count
                longest = count
        else:
            count = 1

    return idx
#The purpose of this function is to take in a list of numbers and find the index of teh first occurrence of the longest repetition of a certain number.
#The input of this function is a list of numbers or integers and the output is a int representing an index value for the inputted list.
#def longest_repetition(nums: list[int])-> Optional[int]:
##Refer to hw2_tests.py for tests