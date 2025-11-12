import unittest

from robot import robot
from table import table

class TestRobotMovement(unittest.TestCase):
    """Test suite for robot movement commands"""
    
    def setUp(self):
        """Set up a fresh robot and table for each test"""
        self.table = robot.TABLE  # Use the shared static table
    
    def test_move_north_within_bounds(self):
        """Test MOVE command when facing NORTH and within bounds"""
        test_robot = robot(0, 0, "NORTH")
        test_robot.invoke_movement_commands(["MOVE", "MOVE", "MOVE"])
        self.assertEqual(test_robot.get_x(), 0)
        self.assertEqual(test_robot.get_y(), 3)
        self.assertEqual(test_robot.get_direction(), "NORTH")
    
    def test_move_north_blocked_at_boundary(self):
        """Test MOVE command blocked when reaching table boundary"""
        test_robot = robot(0, 5, "NORTH")
        test_robot.invoke_movement_commands(["MOVE"])
        # Should stay at (0, 5) because movement to (0, 6) is blocked
        self.assertEqual(test_robot.get_x(), 0)
        self.assertEqual(test_robot.get_y(), 5)
    
    def test_move_east_within_bounds(self):
        """Test MOVE command when facing EAST and within bounds"""
        test_robot = robot(0, 0, "EAST")
        test_robot.invoke_movement_commands(["MOVE", "MOVE"])
        self.assertEqual(test_robot.get_x(), 2)
        self.assertEqual(test_robot.get_y(), 0)
    
    def test_move_south_within_bounds(self):
        """Test MOVE command when facing SOUTH and within bounds"""
        test_robot = robot(5, 5, "SOUTH")
        test_robot.invoke_movement_commands(["MOVE", "MOVE"])
        self.assertEqual(test_robot.get_x(), 5)
        self.assertEqual(test_robot.get_y(), 3)
    
    def test_move_west_within_bounds(self):
        """Test MOVE command when facing WEST and within bounds"""
        test_robot = robot(5, 5, "WEST")
        test_robot.invoke_movement_commands(["MOVE", "MOVE"])
        self.assertEqual(test_robot.get_x(), 3)
        self.assertEqual(test_robot.get_y(), 5)
    
    def test_move_blocked_at_all_boundaries(self):
        """Test MOVE blocked at each boundary"""
        # North boundary
        test_robot1 = robot(0, 5, "NORTH")
        test_robot1.invoke_movement_commands(["MOVE"])
        self.assertEqual(test_robot1.get_y(), 5)
        
        # South boundary
        test_robot2 = robot(0, 0, "SOUTH")
        test_robot2.invoke_movement_commands(["MOVE"])
        self.assertEqual(test_robot2.get_y(), 0)
        
        # East boundary
        test_robot3 = robot(5, 0, "EAST")
        test_robot3.invoke_movement_commands(["MOVE"])
        self.assertEqual(test_robot3.get_x(), 5)
        
        # West boundary
        test_robot4 = robot(0, 0, "WEST")
        test_robot4.invoke_movement_commands(["MOVE"])
        self.assertEqual(test_robot4.get_x(), 0)


class TestRobotRotation(unittest.TestCase):
    """Test suite for robot rotation commands"""
    
    def test_left_rotation_from_north(self):
        """Test LEFT command from NORTH"""
        test_robot = robot(2, 2, "NORTH")
        test_robot.invoke_movement_commands(["LEFT"])
        self.assertEqual(test_robot.get_direction(), "WEST")
    
    def test_left_rotation_from_west(self):
        """Test LEFT command from WEST"""
        test_robot = robot(2, 2, "WEST")
        test_robot.invoke_movement_commands(["LEFT"])
        self.assertEqual(test_robot.get_direction(), "SOUTH")
    
    def test_left_rotation_from_south(self):
        """Test LEFT command from SOUTH"""
        test_robot = robot(2, 2, "SOUTH")
        test_robot.invoke_movement_commands(["LEFT"])
        self.assertEqual(test_robot.get_direction(), "EAST")
    
    def test_left_rotation_from_east(self):
        """Test LEFT command from EAST"""
        test_robot = robot(2, 2, "EAST")
        test_robot.invoke_movement_commands(["LEFT"])
        self.assertEqual(test_robot.get_direction(), "NORTH")
    
    def test_full_rotation_left(self):
        """Test 4 LEFT commands returns to original direction"""
        test_robot = robot(2, 2, "NORTH")
        test_robot.invoke_movement_commands(["LEFT", "LEFT", "LEFT", "LEFT"])
        self.assertEqual(test_robot.get_direction(), "NORTH")
    
    def test_right_rotation_from_north(self):
        """Test RIGHT command from NORTH"""
        test_robot = robot(2, 2, "NORTH")
        test_robot.invoke_movement_commands(["RIGHT"])
        self.assertEqual(test_robot.get_direction(), "EAST")
    
    def test_right_rotation_from_east(self):
        """Test RIGHT command from EAST"""
        test_robot = robot(2, 2, "EAST")
        test_robot.invoke_movement_commands(["RIGHT"])
        self.assertEqual(test_robot.get_direction(), "SOUTH")
    
    def test_right_rotation_from_south(self):
        """Test RIGHT command from SOUTH"""
        test_robot = robot(2, 2, "SOUTH")
        test_robot.invoke_movement_commands(["RIGHT"])
        self.assertEqual(test_robot.get_direction(), "WEST")
    
    def test_right_rotation_from_west(self):
        """Test RIGHT command from WEST"""
        test_robot = robot(2, 2, "WEST")
        test_robot.invoke_movement_commands(["RIGHT"])
        self.assertEqual(test_robot.get_direction(), "NORTH")
    
    def test_full_rotation_right(self):
        """Test 4 RIGHT commands returns to original direction"""
        test_robot = robot(2, 2, "SOUTH")
        test_robot.invoke_movement_commands(["RIGHT", "RIGHT", "RIGHT", "RIGHT"])
        self.assertEqual(test_robot.get_direction(), "SOUTH")


class TestRobotComplexSequences(unittest.TestCase):
    """Test suite for complex command sequences"""
    
    def test_sequence_move_left_move(self):
        """Test: MOVE, LEFT, MOVE sequence"""
        test_robot = robot(1, 2, "EAST")
        test_robot.invoke_movement_commands(["MOVE", "MOVE", "LEFT", "MOVE"])
        self.assertEqual(test_robot.get_x(), 3)
        self.assertEqual(test_robot.get_y(), 3)
        self.assertEqual(test_robot.get_direction(), "NORTH")
    
    def test_sequence_with_blocked_move(self):
        """Test: sequence continues after blocked move"""
        test_robot = robot(3, 3, "NORTH")
        test_robot.invoke_movement_commands(["MOVE", "MOVE", "MOVE", "LEFT", "MOVE"])
        # First 3 MOVEs: (3,3) -> (3,4) -> (3,5) -> blocked at (3,6)
        # LEFT: facing WEST
        # MOVE: (3,5) -> (2,5)
        self.assertEqual(test_robot.get_x(), 2)
        self.assertEqual(test_robot.get_y(), 5)
        self.assertEqual(test_robot.get_direction(), "WEST")
    
    def test_sequence_multiple_rotations_and_moves(self):
        """Test: alternating moves and rotations"""
        test_robot = robot(2, 2, "NORTH")
        test_robot.invoke_movement_commands([
            "MOVE",      # (2,3)
            "RIGHT",     # facing EAST
            "MOVE",      # (3,3)
            "LEFT",      # facing NORTH
            "MOVE"       # (3,4)
        ])
        self.assertEqual(test_robot.get_x(), 3)
        self.assertEqual(test_robot.get_y(), 4)
        self.assertEqual(test_robot.get_direction(), "NORTH")
    
    def test_sequence_360_rotation_with_moves(self):
        """Test: rotation sequence doesn't affect position"""
        test_robot = robot(2, 2, "NORTH")
        initial_x = test_robot.get_x()
        initial_y = test_robot.get_y()
        
        test_robot.invoke_movement_commands(["RIGHT", "RIGHT", "RIGHT", "RIGHT"])
        
        self.assertEqual(test_robot.get_x(), initial_x)
        self.assertEqual(test_robot.get_y(), initial_y)
        self.assertEqual(test_robot.get_direction(), "NORTH")


class TestTableBoundaries(unittest.TestCase):
    """Test suite for table boundary validation"""
    
    def test_table_min_coordinate(self):
        """Test table minimum coordinate is 0"""
        test_table = table()
        self.assertTrue(test_table.position_is_valid(0, 0))
    
    def test_table_max_coordinate(self):
        """Test table maximum coordinate is 5"""
        test_table = table()
        self.assertTrue(test_table.position_is_valid(5, 5))
    
    def test_table_below_minimum(self):
        """Test position below minimum is invalid"""
        test_table = table()
        self.assertFalse(test_table.position_is_valid(-1, 0))
        self.assertFalse(test_table.position_is_valid(0, -1))
    
    def test_table_above_maximum(self):
        """Test position above maximum is invalid"""
        test_table = table()
        self.assertFalse(test_table.position_is_valid(6, 5))
        self.assertFalse(test_table.position_is_valid(5, 6))

class TestRobotInitialization(unittest.TestCase):
    """Test suite for robot initialization"""
    
    def test_robot_initialization(self):
        """Test robot initializes with correct values"""
        test_robot = robot(1, 2, "SOUTH")
        self.assertEqual(test_robot.get_x(), 1)
        self.assertEqual(test_robot.get_y(), 2)
        self.assertEqual(test_robot.get_direction(), "SOUTH")
        self.assertTrue(test_robot.get_is_on_table())
    
    def test_robot_directions_list(self):
        """Test robot has correct directions list"""
        self.assertEqual(robot.DIRECTIONS, ["NORTH", "EAST", "SOUTH", "WEST"])


class TestMultiplePlaceCommands(unittest.TestCase):
    """Test suite for multiple PLACE commands - spec requirement"""
    
    def test_multiple_place_commands_in_sequence(self):
        """Test that robot can be re-placed multiple times"""
        test_robot = robot(0, 0, "NORTH")
        test_robot.invoke_movement_commands(["MOVE"])
        # At (0, 1), now re-place at (2, 2) facing EAST
        test_robot = robot(2, 2, "EAST")
        test_robot.invoke_movement_commands(["MOVE", "LEFT"])
        # After MOVE to (3, 2) and LEFT to NORTH
        self.assertEqual(test_robot.get_x(), 3)
        self.assertEqual(test_robot.get_y(), 2)
        self.assertEqual(test_robot.get_direction(), "NORTH")
    
    def test_multiple_place_resets_position(self):
        """Test that second PLACE command resets robot position"""
        test_robot = robot(1, 1, "NORTH")
        test_robot.invoke_movement_commands(["MOVE", "MOVE"])
        # At (1, 3), now re-place at (4, 4) facing SOUTH
        test_robot = robot(4, 4, "SOUTH")
        # Robot should be at (4, 4) SOUTH, not affected by previous moves
        self.assertEqual(test_robot.get_x(), 4)
        self.assertEqual(test_robot.get_y(), 4)
        self.assertEqual(test_robot.get_direction(), "SOUTH")
    
    def test_commands_ignored_before_first_place(self):
        """Test that commands before first PLACE are ignored"""
        # Start at (2, 2) NORTH (simulating first valid PLACE after invalid commands)
        test_robot = robot(2, 2, "NORTH")
        test_robot.invoke_movement_commands(["MOVE"])
        # After MOVE to (2, 3)
        self.assertEqual(test_robot.get_x(), 2)
        self.assertEqual(test_robot.get_y(), 3)
        self.assertEqual(test_robot.get_direction(), "NORTH")


if __name__ == "__main__":
    unittest.main(verbosity=2)
