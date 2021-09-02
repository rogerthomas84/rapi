import io
import os
import pathlib

__version__ = "0.0.1"
__author_name__ = "Roger Thomas"
__author_email__ = "rogere84@gmail.com"
__author__ = "%s <%s>" % (__author_name__, __author_email__)
__package_url__ = "https://github.com/rogerthomas84/rapi"


class RaPi:
    """A helper to identify if a device is a Raspberry Pi.

    Example:
        inst = RaPi()
        print(inst.is_raspberry_pi())
        print(inst.get_model())
        print(inst.get_chip())
    """

    def __init__(self):
        self.__is_pi = False
        self.__chip = None
        self.__model = None

        self.__read_model()
        if self.__is_pi is True:
            self.__read_chip()
        pass

    def is_pi(self):
        """Is this device a Raspberry Pi?

        :returns: A boolean value, indicating whether this device is a Raspberry Pi
        :rtype: bool
        """
        return self.__is_pi

    def model(self):
        """Get the model string of the device if it's a Raspberry Pi. Example "Raspberry Pi 4 Model B Rev 1.4"

        :returns: A string value if the device is a Raspberry Pi, otherwise it returns None
        :rtype: str|None
        """
        return self.__model

    def chip(self):
        """Get the chipset of the device if it's a Raspberry Pi.

        :returns: A string value if the device is a Raspberry Pi, otherwise it returns None
        :rtype: str|None
        """
        return self.__chip

    # noinspection SpellCheckingInspection
    def __read_model(self):
        """Read whether this device is a Raspberry Pi
        """
        existing_is = os.getenv('RAPI_CHECK_IS')
        existing_model = os.getenv('RAPI_CHECK_MODEL')
        if existing_is is not None and existing_model is not None:
            self.__is_pi = bool(int(existing_is))
            self.__model = existing_model
            return

        if pathlib.Path('/sys/firmware/devicetree/base/model').exists() is False:
            os.putenv('RAPI_CHECK_IS', '0')
            os.putenv('RAPI_CHECK_MODEL', '')
            return
        try:
            with io.open('/sys/firmware/devicetree/base/model', 'r') as base_model:
                line = base_model.read()
                if 'raspberry pi' in line.lower():
                    os.putenv('RAPI_CHECK_IS', '1')
                    os.putenv('RAPI_CHECK_MODEL', line)
                    self.__is_pi = True
                    self.__model = line
                    return
        except Exception:
            pass

    # noinspection SpellCheckingInspection
    def __read_chip(self):
        chips = [
            'BCM2708',
            'BCM2709',
            'BCM2710',
            'BCM2711',
            'BCM2835',
            'BCM2836',
            'BCM2837'
        ]
        if pathlib.Path('/proc/cpuinfo').exists() is False:
            return

        with io.open('/proc/cpuinfo', 'r') as proc_cpu_info:
            for line in proc_cpu_info:
                if line.startswith('Hardware') and ':' in line:
                    _, value = line.strip().split(':', 1)
                    value = value.strip()
                    if value in chips:
                        self.__chip = value
                        return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inst = RaPi()
    print(inst.is_pi())
    print(inst.model())
    print(inst.chip())
