# exception/file_upload_exception.py

class FileUploadException(Exception):
    def __init__(self, message="Error uploading file."):
        self.message = message
        super().__init__(self.message)

class FileNotFoundError(FileUploadException):
    def __init__(self, message="File not found. Please check the file path."):
        super().__init__(message)

class FileSizeExceededException(FileUploadException):
    def __init__(self, message="File size exceeds the allowed limit."):
        super().__init__(message)

class UnsupportedFileFormatException(FileUploadException):
    def __init__(self, message="Unsupported file format. Please upload a valid file type."):
        super().__init__(message)
