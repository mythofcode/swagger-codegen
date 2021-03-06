# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\ 

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Order(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Order - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'pet_id': 'int',
            'quantity': 'int',
            'ship_date': 'datetime',
            'status': 'str',
            'complete': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'pet_id': 'petId',
            'quantity': 'quantity',
            'ship_date': 'shipDate',
            'status': 'status',
            'complete': 'complete'
        }

        self._id = None
        self._pet_id = None
        self._quantity = None
        self._ship_date = None
        self._status = None
        self._complete = False

    @property
    def id(self):
        """
        Gets the id of this Order.


        :return: The id of this Order.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Order.


        :param id: The id of this Order.
        :type: int
        """
        
        self._id = id

    @property
    def pet_id(self):
        """
        Gets the pet_id of this Order.


        :return: The pet_id of this Order.
        :rtype: int
        """
        return self._pet_id

    @pet_id.setter
    def pet_id(self, pet_id):
        """
        Sets the pet_id of this Order.


        :param pet_id: The pet_id of this Order.
        :type: int
        """
        
        self._pet_id = pet_id

    @property
    def quantity(self):
        """
        Gets the quantity of this Order.


        :return: The quantity of this Order.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Order.


        :param quantity: The quantity of this Order.
        :type: int
        """
        
        self._quantity = quantity

    @property
    def ship_date(self):
        """
        Gets the ship_date of this Order.


        :return: The ship_date of this Order.
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """
        Sets the ship_date of this Order.


        :param ship_date: The ship_date of this Order.
        :type: datetime
        """
        
        self._ship_date = ship_date

    @property
    def status(self):
        """
        Gets the status of this Order.
        Order Status

        :return: The status of this Order.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Order.
        Order Status

        :param status: The status of this Order.
        :type: str
        """
        allowed_values = ["placed", "approved", "delivered"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )

        self._status = status

    @property
    def complete(self):
        """
        Gets the complete of this Order.


        :return: The complete of this Order.
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """
        Sets the complete of this Order.


        :param complete: The complete of this Order.
        :type: bool
        """
        
        self._complete = complete

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

