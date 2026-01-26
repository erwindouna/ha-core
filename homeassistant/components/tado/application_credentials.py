"""Application credentials platform for Tado."""

from homeassistant.components.application_credentials import AuthorizationServer
from homeassistant.core import HomeAssistant


async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer:
    """Return authorization server."""
    return AuthorizationServer(
        authorize_url="https://login.tado.com/oauth2/device_authorize",
        token_url="https://login.tado.com/oauth2/token",
    )


# Works for now, let's see what Core members think
async def async_use_device_flow(hass: HomeAssistant) -> bool:
    """Use device flow for OAuth2."""
    return True
