from typing import Union, Tuple, Callable, Optional

from customtkinter import CTkTabview
from customtkinter import CTkFrame


class TabFrames(CTkTabview):
	"""
	TabFrames is a CTkTabview without the default buttons to change tabs
	For detailed information check out the documentation of CTkTabview.
	"""

	def __init__(self,
				 master: any,
				 width: int = 300,
				 height: int = 250,
				 corner_radius: Optional[int] = None,
				 border_width: Optional[int] = None,

				 bg_color: Union[str, Tuple[str, str]] = "transparent",
				 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
				 border_color: Optional[Union[str, Tuple[str, str]]] = None,

				 segmented_button_fg_color: Optional[Union[str, Tuple[str, str]]] = None,
				 segmented_button_selected_color: Optional[Union[str, Tuple[str, str]]] = None,
				 segmented_button_selected_hover_color: Optional[Union[str, Tuple[str, str]]] = None,
				 segmented_button_unselected_color: Optional[Union[str, Tuple[str, str]]] = None,
				 segmented_button_unselected_hover_color: Optional[Union[str, Tuple[str, str]]] = None,

				 text_color: Optional[Union[str, Tuple[str, str]]] = None,
				 text_color_disabled: Optional[Union[str, Tuple[str, str]]] = None,

				 command: Union[Callable, None] = None,
				 state: str = "normal",
				 **kwargs):
				 
		super().__init__(
			master = master,
			width = width,
			height = height,
			corner_radius = corner_radius,
			border_width = border_width,
			bg_color = bg_color,
			fg_color = fg_color,
			border_color = border_color,
			segmented_button_fg_color = segmented_button_fg_color,
			segmented_button_selected_color = segmented_button_selected_color,
			segmented_button_selected_hover_color = segmented_button_selected_hover_color,
			segmented_button_unselected_color = segmented_button_unselected_color,
			segmented_button_unselected_hover_color = segmented_button_unselected_hover_color,
			text_color = text_color,
			text_color_disabled = text_color_disabled,
			command = command,
			state = state,
			**kwargs
		)
		del self._segmented_button


	def _configure_segmented_button_background_corners(self):
		""" Do nothing ! """
		pass

	def _set_grid_segmented_button(self):
		""" Do nothing ! """
		pass

	def set(self, name: str):
		""" select tab by name : avoid using self._segmented_button.set """

		if name in self._tab_dict:
			self._current_name = name
			self._grid_forget_all_tabs()
			self._set_grid_tab_by_name(name)
		else:
			raise ValueError(f"CTkTabview has no tab named '{name}'")

	def insert(self, index: int, name: str) -> CTkFrame:
		""" creates new tab with given name at position index : avoid using segmented_button """

		if name not in self._tab_dict:

			self._name_list.insert(index, name)
			self._tab_dict[name] = self._create_tab()
			self._configure_tab_background_corners_by_name(name)

			# if created tab is only tab select this tab
			if len(self._tab_dict) == 1:
				self._current_name = name
				self._grid_forget_all_tabs()
				self._set_grid_tab_by_name(self._current_name)

			return self._tab_dict[name]
		else:
			raise ValueError(f"CTkTabview already has tab named '{name}'")

