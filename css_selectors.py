# CSS Selectors
CSS_FULLSCREEN_PARENT = "div[class*='LiveviewControls__ButtonGroup']"
# Newer Protect: button is a direct child of the ButtonGroup; older: wrapped in a div
CSS_FULLSCREEN_BUTTON = ":scope > button, :nth-child(2) > button"
CSS_LOADING_DOTS = "div[class*='TimedDotsLoader']"
CSS_LIVEVIEW_WRAPPER = "div[class*='liveView__LiveViewWrapper']"
CSS_CLOSE_BUTTON = "button[class*='closeButton']"