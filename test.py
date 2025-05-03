import unittest
from LA import User, ClassBooking, TrainerBooking  # Replace 'your_module_name' with the actual module name

class TestDetails(unittest.TestCase):
    # Test case 1: ClassBooking details
    def test_class_booking_details(self):
        print('Test Case 1: Class Booking Details')
        p1 = ClassBooking('lkpham1', 'password123', 'Linh', 'Pham', '6006003000', ['Yoga', 'Pilates'])  # Provide 'password123' and 'selected_classes'
        self.assertEqual(p1.username, 'lkpham1')
        self.assertEqual(p1.firstname, 'Linh')
        self.assertEqual(p1.lastname, 'Pham')
        self.assertEqual(p1.phone, '6006003000')
        self.assertListEqual(p1.selected_classes, ['Yoga', 'Pilates'])

    # Test case 2: TrainerBooking details
    def test_trainer_booking_details(self):
        print('Test Case 2: Trainer Booking Details')
        p2 = TrainerBooking('trainer1', 'password456', 'Trainer', 'One', '1234567890', 'Yoga Trainer')  # Provide 'password456' and 'selected_trainer_name'
        self.assertEqual(p2.username, 'trainer1')
        self.assertEqual(p2.firstname, 'Trainer')
        self.assertEqual(p2.lastname, 'One')
        self.assertEqual(p2.phone, '1234567890')
        self.assertEqual(p2.selected_trainer_name, 'Yoga Trainer')

    # Test case 3: User details
    def test_user_details(self):
        print('Test Case 3: User Details')
        p3 = User('user1', 'password123', 'John', 'Doe', '9876543210')
        self.assertEqual(p3.username, 'user1')
        self.assertEqual(p3.firstname, 'John')
        self.assertEqual(p3.lastname, 'Doe')
        self.assertEqual(p3.phone, '9876543210')
        self.assertEqual(p3.password, 'password123')


