"""Upload to the Materials Cloud QE Input Generator tool"""
import tempfile
from typing import Union
import warnings

import ipywidgets as ipw
from optimade.adapters import Structure
from optimade_client.exceptions import OptimadeClientError
from optimade_client.logger import LOGGER
from optimade_client.utils import ButtonStyle, DEVELOPMENT_MODE
from optimade_client.warnings import OptimadeClientWarning
from traitlets import traitlets


class QEInputButton(ipw.HTML):
    """QE Input Generator upload button

    Arguments:
        button_style: The style for the button.
        kwargs: Any extra keywords (not including `value`) are passed on to the `ipywidgets.HTML`
            initiator.

    """

    structure = traitlets.Instance(Structure, allow_none=True)

    _button_format = """<button
    class="p-Widget jupyter-widgets jupyter-button widget-button mod-{button_style}"
    title="Use the chosen structure in the QE Input Generator Tool" style="width:auto;" {disabled}
    onclick="var file_data = new Blob([{data!r}], {{type: 'charset=utf-8'}});

const XHR = new XMLHttpRequest();
const FD = new FormData();

FD.append('fileformat', 'xsf-ase');
FD.append('structurefile', file_data);

XHR.onreadystatechange = function() {{
    if (XHR.readyState === 4) {{
        var response = JSON.parse(XHR.responseText);
        var link = document.createElement('a');
        link.href = response.redirect;
        link.target = '_blank';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }}
}}

XHR.open('POST', 'https://{subdomain}.materialscloud.org/qeinputgenerator/compute/upload_structure/')
XHR.send(FD);">Use in QE Input Generator</button>
"""

    def __init__(self, button_style: Union[ButtonStyle, str] = None, **kwargs) -> None:
        if button_style:
            if isinstance(button_style, str):
                self._button_style = ButtonStyle[button_style.upper()]
            elif isinstance(button_style, ButtonStyle):
                self._button_style = button_style
            else:
                raise TypeError(
                    "button_style should be either a string or a ButtonStyle Enum. "
                    f"You passed type {type(button_style)!r}."
                )
        else:
            self._button_style = ButtonStyle.DEFAULT

        self._default_subdomain = "dev-tools" if DEVELOPMENT_MODE else "tools"

        kwargs.pop("value", None)
        super().__init__(
            value=self._format_button(disabled="disabled", data=""), **kwargs
        )

    @property
    def style(self) -> ButtonStyle:
        """Get the style format used for the button"""
        return self._button_style

    def _format_button(self, **kwargs) -> str:
        """Utility method to format button.

        Returns:
            The formatted string.

        """
        return self._button_format.format(
            button_style=self.style.value,
            data=kwargs.get("data", ""),
            disabled=kwargs.get("disabled", "disabled"),
            subdomain=kwargs.get("subdomain", self._default_subdomain),
        )

    def format_button(self, disabled: bool = True, data: str = None) -> None:
        """Set the button's HTML value

        Parameters:
            disabled: Whether or not the widget should be disabled (clickable).
            data: The data as a string of binary data.

        """
        self.value = self._format_button(
            disabled="disabled" if disabled else "",
            data=data if data is not None else "",
        )

    @traitlets.observe("structure")
    def _on_change_structure(self, change: dict) -> None:
        """Update button HTML according to a possible new structure"""
        LOGGER.debug(
            "Updating the QE Input Generator button with the structure: %s",
            self.structure,
        )
        if not self.structure or self.structure is None:
            LOGGER.debug("structure is not defined.")
            self.reset()
            return
        if not all(
            getattr(self.structure.attributes, field, None) is not None
            for field in (
                "structure_features",
                "species",
                "nsites",
                "lattice_vectors",
                "dimension_types",
                "cartesian_site_positions",
                "species_at_sites",
            )
        ):
            LOGGER.debug("Missing information when trying to convert to `ase.Atoms`")
            self.reset()
            return

        output = None
        with warnings.catch_warnings():
            warnings.filterwarnings("error")

            try:
                output = self.structure.as_ase
            except RuntimeWarning as warn:
                if "numpy.ufunc size changed" in str(warn):
                    # This is an issue that may occur if using pre-built binaries for numpy and
                    # scipy. It can be resolved by uninstalling scipy and reinstalling it with
                    # `--no-binary :all:` when using pip. This will recompile all related binaries
                    # using the currently installed numpy version.
                    # However, it shouldn't be critical, hence here the warning will be ignored.
                    warnings.filterwarnings("default")
                    output = self.structure.as_ase
                else:
                    self.reset()
                    warnings.warn(OptimadeClientWarning(warn))
            except Warning as warn:
                self.reset()
                warnings.warn(OptimadeClientWarning(warn))
            except Exception as exc:
                self.reset()
                if isinstance(exc, OptimadeClientError):
                    raise exc
                # Else wrap the exception to make sure to log it.
                raise OptimadeClientError(exc)

        with tempfile.NamedTemporaryFile(mode="w+b") as handle:
            output.write(handle.name, format="xsf")
            output = handle.read().decode("utf-8")

        self.format_button(disabled=False, data=output)

    def freeze(self) -> None:
        """Disable widget"""

    def unfreeze(self) -> None:
        """Activate widget"""

    def reset(self) -> None:
        """Reset widget"""
        self.format_button(disabled=True)
