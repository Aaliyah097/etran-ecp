import time
from pydantic import BaseModel
from typing import TypeVar
from typing import Any
import requests
import xmltodict
import json
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from settings import settings


T = TypeVar('T', bound=BaseModel)


@contextmanager
def client_session() -> requests.Session:
    with requests.Session() as session:
        yield session


class EtranClient:
    XML_CONTAINER = """<?xml version="1.0" encoding="UTF-8"?>
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/">
        <SOAP-ENV:Body SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
        <NS1:GetBlock xmlns:NS1="SysEtranInt">
            <Login>%s</Login>
            <Password>%s</Password>
            <Text>
                %s
            </Text>
        </NS1:GetBlock>
        </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>"""

    def clean_dict(self, data):
        if isinstance(data, dict):
            if set(data.keys()) == {'@value'}:
                return data['@value']
            return {key: self.clean_dict(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.clean_dict(item) for item in data]
        else:
            return data

    def parse_response(self, response: str, reply_key: str) -> dict:
        root = ET.fromstring(response)
        response = (
            xmltodict.parse(
                root.findall('.//Text')[0].text
            )
        )
        if 'error' in response:
            with open(f'{reply_key}_error.xml', 'w', encoding='utf-8') as error_file:
                error_file.write(str(response))
            raise Exception(response)

        response = response[reply_key]

        return self.clean_dict(response)

    def request(self, session: requests.Session, scheme: str, reply_key: str, response_cls: T) -> T:
        request = (
            self.XML_CONTAINER % (
                settings.ETRAN_USERNAME,
                settings.ETRAN_PASSWORD,
                scheme
            )
        )

        with open(f'{reply_key}_request.xml', 'w', encoding='utf-8') as request_file:
            request_file.write(str(request))

        response = self.parse_response(
            session.post(
                url=settings.ETRAN_URL,
                data=request.encode('utf-8')
            ).text,
            reply_key
        )

        with open(f'{reply_key}_response.xml', 'w', encoding='utf-8') as response_file:
            response_file.write(str(response))

        return response_cls(**response)
