import unittest
import os
import shutil
import tempfile
import logging
from trimFilenames import trim_files

# Configure logging for tests
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_trimFilenames.log'),
        logging.StreamHandler()
    ]
)

class TestTrimFilenames(unittest.TestCase):
    def setUp(self):
        logging.info("Setting up test environment")
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        logging.info(f"Created temporary directory: {self.test_dir}")
        
        # Create test files
        self.test_files = [
            "0100 - TestFile1.txt",
            "0100 - TestFile2.txt",
            "0100 - TestFile3.txt"
        ]
        for file in self.test_files:
            file_path = os.path.join(self.test_dir, file)
            with open(file_path, 'w') as f:
                f.write("test content")
            logging.info(f"Created test file: {file_path}")

    def tearDown(self):
        logging.info("Cleaning up test environment")
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)
        logging.info(f"Removed temporary directory: {self.test_dir}")

    def test_trim_files_dryrun(self):
        logging.info("Starting dry run test")
        # Test dry run mode
        trim_files(self.test_dir, 7, True)
        
        # Verify files still exist with original names
        for file in self.test_files:
            file_path = os.path.join(self.test_dir, file)
            self.assertTrue(os.path.exists(file_path))
            logging.info(f"Verified file exists: {file_path}")

    def test_trim_files_actual(self):
        logging.info("Starting actual rename test")
        # Test actual file renaming
        trim_files(self.test_dir, 7, False)
        
        # Verify files were renamed correctly
        expected_files = [f[7:] for f in self.test_files]
        for file in expected_files:
            file_path = os.path.join(self.test_dir, file)
            self.assertTrue(os.path.exists(file_path))
            logging.info(f"Verified renamed file exists: {file_path}")
        
        # Verify original files no longer exist
        for file in self.test_files:
            file_path = os.path.join(self.test_dir, file)
            self.assertFalse(os.path.exists(file_path))
            logging.info(f"Verified original file removed: {file_path}")

    def test_trim_files_different_length(self):
        logging.info("Starting different trim length test")
        # Test with different trim length
        trim_files(self.test_dir, 5, False)
        
        # Verify files were renamed with 5 characters removed
        expected_files = [f[5:] for f in self.test_files]
        for file in expected_files:
            file_path = os.path.join(self.test_dir, file)
            self.assertTrue(os.path.exists(file_path))
            logging.info(f"Verified file with different trim length exists: {file_path}")

    def test_empty_directory(self):
        logging.info("Starting empty directory test")
        # Test with empty directory
        empty_dir = tempfile.mkdtemp()
        try:
            logging.info(f"Created empty test directory: {empty_dir}")
            trim_files(empty_dir, 7, False)
            # No exception should be raised
            logging.info("Successfully processed empty directory")
        finally:
            shutil.rmtree(empty_dir)
            logging.info(f"Removed empty test directory: {empty_dir}")

if __name__ == '__main__':
    unittest.main() 