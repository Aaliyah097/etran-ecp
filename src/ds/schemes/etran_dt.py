from datetime import datetime


class etrandatetime(datetime):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value, values, config, field):
        if isinstance(value, datetime):
            return value
        try:
            return datetime.strptime(value, "%d.%m.%Y %H:%M:%S")
        except ValueError:
            raise ValueError("Datetime must be in format DD.MM.YYYY HH:MM:SS")

    def __str__(self):
        return self.strftime("%d.%m.%Y %H:%M:%S")
