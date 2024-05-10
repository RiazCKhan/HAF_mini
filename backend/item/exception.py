from rest_framework.exceptions import APIException


class InventoryException(APIException):
    status_code = 400
    default_detail = "Unable to create inventory. Stock already exists"
