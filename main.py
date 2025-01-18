import gemini_settings
import random
import time

import mesop as me
import mesop.labs as mel

from data_model import State

def on_load(e: me.LoadEvent):
  me.set_theme_mode("system")

@me.content_component
def dialog(is_open: bool):
  """Renders a dialog component.
  Args:
    is_open: Whether the dialog is visible or not.
  """
  with me.box(
    style=me.Style(
      display="block" if is_open else "none",
      margin=me.Margin.symmetric(horizontal=500, vertical=76),
      height="100%",
      position="fixed",
      width="100%",
    )
  ):
    with me.box(
      style=me.Style(
        place_items="center",
        display="grid",
        height="90vh",
      )
    ):
      with me.box(
        style=me.Style(
          background=me.theme_var("surface-container-lowest"),
          border_radius=20,
          box_sizing="content-box",
          box_shadow=(
            "0 3px 1px -2px #0003, 0 2px 2px #00000024, 0 1px 5px #0000001f"
          ),

          padding=me.Padding.all(20),
        )
      ):
        me.slot()

# Close api key dialog box
def on_click_close_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = False

# Open api key dialog box
def on_click_open_dialog(e: me.ClickEvent):
  state = me.state(State)
  state.is_open = True

# Set the api key using valur entered in dialog box
def set_gemini_api_key(e: me.InputBlurEvent):
    me.state(State).gemini_api_key = e.value

# Define the dialogue box for entering api key
def dialog_box():
  state = me.state(State)

  with dialog(state.is_open):
    with me.box(style=me.Style(display="flex", flex_direction="column")):
        me.input(
            label="Gemini API Key",
            value=state.gemini_api_key,
            on_blur=set_gemini_api_key,
        )
        me.button("Confirm", on_click=on_click_close_dialog)

@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io", "https://huggingface.co"]
  ),
  path="/chat",
  title="Mesop Test Output",
  on_load=on_load,
)
def page():
   state = me.state(State)
   dialog_box()
   with me.box(style=_STYLE_CONTAINER):
    # Main Header
    with me.box(style=me.Style(border=
                               me.Border.all(me.BorderSide(
                                 color=me.theme_var("outline-variant"), width=1, style="solid")),
                                 padding=me.Padding.all(15))):
      with me.box(style=me.Style(display="inline-block")):
        me.text(
          state.title,
          type="headline-6",
          style=me.Style(line_height="24px", margin=me.Margin(bottom=0)),
        )

    # Toolbar Header
    with me.box(style=me.Style(border=me.Border.all(
      me.BorderSide(color=me.theme_var("outline-variant"), width=1, style="solid")), padding=me.Padding.all(10))):
      me.button("API Key", type="stroked", color="primary", on_click=on_click_open_dialog)
    mel.chat(transform, title="Mesop Demo Chat", bot_user="Mesop Bot")
  
def transform(input: str, history: list[mel.ChatMessage]):
  for line in random.sample(LINES, random.randint(3, len(LINES) - 1)):
    time.sleep(0.3)
    yield line + " "


LINES = [
  "Mesop is a Python-based UI framework designed to simplify web UI development for engineers without frontend experience.",
  "It leverages the power of the Angular web framework and Angular Material components, allowing rapid construction of web demos and internal tools.",
  "With Mesop, developers can enjoy a fast build-edit-refresh loop thanks to its hot reload feature, making UI tweaks and component integration seamless.",
  "Deployment is straightforward, utilizing standard HTTP technologies.",
  "Mesop's component library aims for comprehensive Angular Material component coverage, enhancing UI flexibility and composability.",
  "It supports custom components for specific use cases, ensuring developers can extend its capabilities to fit their unique requirements.",
  "Mesop's roadmap includes expanding its component library and simplifying the onboarding processs.",
]

_STYLE_CONTAINER = me.Style(
  display="grid",
  grid_template_columns="5fr 2fr",
  grid_template_rows="auto 5fr",
  height="100vh",
)