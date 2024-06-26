"""Registration for PyData."""
from discord.ext import commands

from cogs.registration import (
    Registration,
    RegistrationButton,
    RegistrationForm,
    RegistrationView,
)

# from configuration import Config
# from error import AlreadyRegisteredError, NotFoundError
# from helpers.channel_logging import log_to_channel
# from helpers.tito_connector import TitoOrder


# config = Config()
# order_ins = TitoOrder()

# CHANGE_NICKNAME = False

EMOJI_POINT = "\N{WHITE LEFT POINTING BACKHAND INDEX}"

# _logger = logging.getLogger(f"bot.{__name__}")


class RegistrationButtonPyData(RegistrationButton):
    def __init__(
        self,
        registration_form: RegistrationForm,
    ):
        super().__init__(registration_form=RegistrationFormPyData)


class RegistrationFormPyData(RegistrationForm):
    def __init__(self):
        super().__init__(title="PyConDE/PyData Berlin 2024 Registration")


class RegistrationViewPyData(RegistrationView):
    def __init__(self):
        super().__init__(
            registration_button=RegistrationButtonPyData, registration_form=RegistrationFormPyData
        )


class RegistrationPyData(Registration, commands.Cog):
    def __init__(self, bot):
        super().__init__(bot, registration_view=RegistrationViewPyData)
        self._title = "Welcome to PyConDE / PyData Berlin 2024 on Discord! 🎉🐍"
        # TODO(dan): update text
        self._desc = (
            "Follow these steps to complete your registration:\n\n"
            f'1️⃣ Click on the green "Register Here {EMOJI_POINT}" button.\n\n'
            '2️⃣ Fill in the "Order/Reference Number" in the format "XXXX-X" or "XXXX-XX") and '
            'your "Full Name" (first and last name as printed on your ticket/badge under ticket '
            "holder). "
            "You can find the information also in your confirmation email from "
            'support@tito.io with the subject: "Your PyCon.DE & PyData Berlin 2024 Ticket".\n\n'
            '3️⃣ Click "Submit". We\'ll verify your ticket and give you your role(s) based on '
            "your ticket type.\n\n"
            "Experiencing trouble? Ask for help in the registration-help channel or from a "
            "volunteer (purple shirts) at the conference.\n\n"
            "See you on the server! 🐍💻🎉"
        )
