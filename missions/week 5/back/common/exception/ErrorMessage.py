from enum import Enum


class ErrorMessage(Enum):
    PRODUCT_NOT_FOUND = ("PRODUCT_001",  "Product Not Found")
    PRODUCT_VALIDATION_ERROR = ("PRODUCT_002", "Product Post Invalid Error")

    MARKET_NOT_FOUND = ('MARKET_001', 'Market Not Found')
    MARKET_ID_NOT_CORRECT = ("MARKET_002", 'Market Id Is Not Correct')
    MARKET_VALIDATION_ERROR = ("MARKET_003", "Market Post Invalid Error")
    MARKET_COMPANY_NAME_DUPLICATE = ("MARKET_004", "Company Name Duplicate")
    MARKET_COMPANY_NUMBER_DUPLICATE = ("MARKET_005", "Company Number Duplicate")
    MARKET_ALREADY_EXIST_MAPPING_USER = ('MARKET_006', 'Market User Already Mapping')

    PRODUCT_CATEGORY_NOT_FOUND = ("PRODUCT_CATEGORY_001", "Product Category Not Found")
    PRODUCT_CATEGORY_INVALID = ("PRODUCT_CATEGORY_002", "Product Category Invalid")

    PRODUCT_OPTION_DUPLICATE = ("PRODUCT_OPTION_001", "Product Option Duplicate")

    USER_NOT_FOUND = ("USER_001", "User Not Found")



    def __init__(self, code, message):
        self.code = code
        self.message = message
