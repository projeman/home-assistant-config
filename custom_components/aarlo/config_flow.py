"""Config flow for Aarlo"""

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

from .const import CONF_TFA_HOST, CONF_TFA_PASSWORD, CONF_TFA_USERNAME, DOMAIN


class AarloFlowHandler(ConfigFlow, domain=DOMAIN):
    """Aarlo config flow."""

    VERSION = 1

    def __init__(self):
        """Initialize the config flow."""
        self.username = None
        self.password = None
        self.tfaUsername = None
        self.tfaPassword = None
        self.tfaHost = None

    async def async_step_user(self, info: dict = None):
        """Handle user initiated flow."""
        errors = {}

        if info is not None:
            # TODO need to add error handling for blank fields / bad data
            # process the information
            if (
                not info[CONF_USERNAME]
                or not info[CONF_PASSWORD]
                or not info[CONF_TFA_USERNAME]
                or not info[CONF_TFA_PASSWORD]
                or not info[CONF_TFA_HOST]
            ):
                errors["base"] = "missing_field"
            elif "imap" not in info[CONF_TFA_HOST]:
                errors["base"] = "tfa_no_imap"
            else:
                return self.async_create_entry(
                    title=f"${DOMAIN} - ${self.email}", data=info
                )

        data_schema = {
            vol.Required(CONF_USERNAME, default=self.username): str,
            vol.Required(CONF_PASSWORD, default=self.password): str,
            vol.Required(CONF_TFA_USERNAME, default=self.tfaUsername): str,
            vol.Required(CONF_TFA_PASSWORD, default=self.tfaPassword): str,
            vol.Required(CONF_TFA_HOST, default=self.tfaHost): str,
        }

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(data_schema), errors=errors
        )
